#!/usr/bin/env bash
# push-gate.sh — Block autonomous git push and PR create/merge.
# These are high-impact actions that should require explicit user approval.
set -euo pipefail

INPUT="$(cat)"
TOOL="$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null)"

if [ "$TOOL" = "Bash" ]; then
    CMD="$(echo "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)"
    [ -n "$CMD" ] || exit 0

    if echo "$CMD" | grep -qE '^\s*git\s+push(\s|$)' && ! echo "$CMD" | grep -q '\-\-dry-run'; then
        echo "BLOCKED: git push requires explicit user approval." >&2
        exit 2
    fi

    if echo "$CMD" | grep -qE '^\s*gh\s+pr\s+(create|merge)(\s|$)'; then
        echo "BLOCKED: PR create/merge requires explicit user approval." >&2
        exit 2
    fi
fi

case "$TOOL" in
    mcp__github__create_pull_request|mcp__github__merge_pull_request|mcp__github__push_files)
        echo "BLOCKED: $TOOL requires explicit user approval." >&2
        exit 2
        ;;
esac

exit 0
