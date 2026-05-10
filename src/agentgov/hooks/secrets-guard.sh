#!/usr/bin/env bash
# secrets-guard.sh — Block writes containing API keys, tokens, and secrets.
# Scans for common secret patterns in file mutations.
set -euo pipefail

input="$(cat)"
tool_name="$(printf '%s' "$input" | jq -r '.tool_name // empty')"

case "$tool_name" in
  Edit|Write|MultiEdit|NotebookEdit) ;;
  *) exit 0 ;;
esac

file_path="$(printf '%s' "$input" | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null || true)"
[ -n "$file_path" ] || exit 0

# Skip gitignored files (secrets in .env are expected)
if git rev-parse --is-inside-work-tree &>/dev/null; then
  git check-ignore -q "$file_path" 2>/dev/null && exit 0
fi

# Skip known secret-holding files
case "$file_path" in
  *.env|*.env.*|*/.envrc|*/credentials*|*secret*) exit 0 ;;
esac

new_content="$(printf '%s' "$input" | jq -r '.tool_input.new_string // .tool_input.content // empty' 2>/dev/null || true)"
[ -n "$new_content" ] || exit 0

blocked=()

# AWS keys
if echo "$new_content" | grep -qP 'AKIA[0-9A-Z]{16}' 2>/dev/null; then
  blocked+=("AWS Access Key ID detected")
fi

# Generic API key patterns (key=..., token=..., secret=... with long values)
if echo "$new_content" | grep -qPi '(api[_-]?key|api[_-]?secret|access[_-]?token|auth[_-]?token)\s*[=:]\s*["\x27]?[a-zA-Z0-9_-]{20,}' 2>/dev/null; then
  blocked+=("API key/token pattern detected")
fi

# GitHub tokens
if echo "$new_content" | grep -qP '(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,}' 2>/dev/null; then
  blocked+=("GitHub token detected")
fi

# Private keys
if echo "$new_content" | grep -q 'BEGIN.*PRIVATE KEY' 2>/dev/null; then
  blocked+=("Private key detected")
fi

if [ ${#blocked[@]} -gt 0 ]; then
  echo "BLOCKED: Secrets detected in content being written to $file_path:" >&2
  for msg in "${blocked[@]}"; do
    echo "  - $msg" >&2
  done
  echo "Move secrets to .env or a secrets manager. Never commit them." >&2
  exit 2
fi
