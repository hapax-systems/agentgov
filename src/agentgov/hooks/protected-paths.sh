#!/usr/bin/env bash
# protected-paths.sh — Block writes to protected files/directories.
# Configure protected patterns in .agentgov.toml or via AGENTGOV_PROTECTED_PATHS env var.
# Default: blocks writes to .env, *.pem, *.key files in tracked directories.
set -euo pipefail

input="$(cat)"
tool_name="$(printf '%s' "$input" | jq -r '.tool_name // empty')"

case "$tool_name" in
  Edit|Write|MultiEdit|NotebookEdit) ;;
  *) exit 0 ;;
esac

file_path="$(printf '%s' "$input" | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null || true)"
[ -n "$file_path" ] || exit 0

# Default protected patterns
PROTECTED="${AGENTGOV_PROTECTED_PATHS:-*.pem:*.key:*.p12:*.pfx}"

IFS=':' read -ra patterns <<< "$PROTECTED"
for pattern in "${patterns[@]}"; do
    if [[ "$file_path" == $pattern ]]; then
        echo "BLOCKED: '$file_path' matches protected pattern '$pattern'." >&2
        echo "Configure AGENTGOV_PROTECTED_PATHS to adjust." >&2
        exit 2
    fi
done

exit 0
