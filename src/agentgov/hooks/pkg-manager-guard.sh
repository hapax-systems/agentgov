#!/usr/bin/env bash
# pkg-manager-guard.sh — Enforce a single Python package manager.
# Blocks direct pip usage, requiring uv (or poetry) instead.
# Read-only pip commands (freeze, list, show) are allowed.
set -euo pipefail

INPUT="$(cat)" || exit 0
TOOL="$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null)" || exit 0

[ "$TOOL" = "Bash" ] || exit 0

CMD="$(echo "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)" || exit 0
[ -n "$CMD" ] || exit 0

FIRST_LINE="$(echo "$CMD" | head -n1)"
CHECK="$(echo "$FIRST_LINE" | sed 's/uv pip/uv_pip/g')"

if echo "$CHECK" | grep -qE '\bpip3?\s+(install|uninstall)\b'; then
    echo "BLOCKED: Direct pip usage not allowed. Use 'uv add', 'uv sync', or 'uv pip install' instead." >&2
    exit 2
fi

if echo "$CHECK" | grep -qE '\bpython3?\s+-m\s+pip\b'; then
    echo "BLOCKED: Direct pip usage not allowed. Use 'uv add', 'uv sync', or 'uv pip install' instead." >&2
    exit 2
fi

exit 0
