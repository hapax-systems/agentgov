#!/usr/bin/env bash
# pii-guard.sh — Block writes that introduce PII patterns into tracked files.
# Checks for email addresses, phone numbers, SSNs, and configurable custom patterns.
# Respects .gitignore — untracked/ignored files are not scanned.
set -euo pipefail

input="$(cat)"
tool_name="$(printf '%s' "$input" | jq -r '.tool_name // empty')"

case "$tool_name" in
  Edit|Write|MultiEdit|NotebookEdit) ;;
  *) exit 0 ;;
esac

file_path="$(printf '%s' "$input" | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null || true)"
[ -n "$file_path" ] || exit 0

# Skip gitignored files
if git rev-parse --is-inside-work-tree &>/dev/null; then
  git check-ignore -q "$file_path" 2>/dev/null && exit 0
fi

# Skip binary files
case "$file_path" in
  *.png|*.jpg|*.jpeg|*.gif|*.ico|*.wav|*.mp3|*.mp4|*.db|*.sqlite|*.woff|*.woff2|*.ttf|*.eot) exit 0 ;;
esac

new_content="$(printf '%s' "$input" | jq -r '.tool_input.new_string // .tool_input.content // empty' 2>/dev/null || true)"
[ -n "$new_content" ] || exit 0

blocked=()

# Email addresses (high confidence: user@domain.tld, not package@version patterns)
if echo "$new_content" | grep -qP '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' 2>/dev/null; then
  # Exclude common false positives
  if ! echo "$new_content" | grep -qP '(noreply@|example\.com|test@|user@|nobody@|root@)'; then
    blocked+=("Email address detected")
  fi
fi

# US Social Security Numbers
if echo "$new_content" | grep -qP '\b\d{3}-\d{2}-\d{4}\b' 2>/dev/null; then
  blocked+=("Possible SSN detected")
fi

# Phone numbers (US format)
if echo "$new_content" | grep -qP '\b(\+1[-.]?)?\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b' 2>/dev/null; then
  blocked+=("Phone number detected")
fi

# Home directory paths (reveals username)
if echo "$new_content" | grep -qP '/home/[a-z][a-z0-9_-]+/' 2>/dev/null; then
  case "$file_path" in
    */.gitignore|*/CLAUDE.md|*/hooks/*|*/.claude/*|*/systemd/*|*/scripts/*) ;;
    *) blocked+=("Home directory path detected (reveals username)") ;;
  esac
fi

# Custom patterns from .agentgov.toml (future: read from config)

if [ ${#blocked[@]} -gt 0 ]; then
  echo "BLOCKED: PII detected in content being written to $file_path:" >&2
  for msg in "${blocked[@]}"; do
    echo "  - $msg" >&2
  done
  echo "If intentional (e.g., gitignored file), add to .gitignore first." >&2
  exit 2
fi
