#!/usr/bin/env bash
# safe-stash-guard.sh — Block git stash pop (use apply+drop instead).
# git stash pop does a three-way merge on conflict with no --abort. The stash
# is not dropped on conflict either, leaving a broken working tree.
set -euo pipefail

INPUT="$(cat)" || exit 0
TOOL="$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null)" || exit 0

[ "$TOOL" = "Bash" ] || exit 0

CMD="$(echo "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)" || exit 0
[ -n "$CMD" ] || exit 0

CMD_STRIPPED="$(printf '%s' "$CMD" | sed -zE "s/'[^']*'//g; s/\"[^\"]*\"//g")"

if echo "$CMD_STRIPPED" | grep -qE '(^|\s|&&|;)\s*git\s+stash\s+pop\b'; then
    cat >&2 <<'MSG'
BLOCKED: git stash pop can leave unrecoverable conflict markers.

Safe alternatives:
  1. git stash apply && git stash drop   # two-step with validation
  2. git stash branch <name>             # zero-conflict guarantee
  3. git commit -m "WIP" before rebase   # prefer commits over stash
MSG
    exit 2
fi

exit 0
