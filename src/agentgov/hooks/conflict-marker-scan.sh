#!/usr/bin/env bash
# conflict-marker-scan.sh — Warn when conflict markers appear after git operations.
# PostToolUse hook: scans after stash apply, rebase, merge, cherry-pick, pull.
set -euo pipefail

INPUT="$(cat)" || exit 0
TOOL="$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null)" || exit 0

[ "$TOOL" = "Bash" ] || exit 0

CMD="$(echo "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)" || exit 0
[ -n "$CMD" ] || exit 0

if ! echo "$CMD" | grep -qE '\bgit\s+(stash\s+apply|rebase|merge|cherry-pick|pull)\b'; then
    exit 0
fi

GIT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0

CONFLICTS="$(git -C "$GIT_ROOT" diff --name-only --diff-filter=U 2>/dev/null)" || true

if [ -z "$CONFLICTS" ]; then
    CONFLICTS="$(git -C "$GIT_ROOT" grep -l '^<<<<<<<\|^=======$\|^>>>>>>>' -- \
        '*.py' '*.ts' '*.tsx' '*.js' '*.jsx' '*.json' '*.yaml' '*.yml' '*.md' '*.rs' '*.go' \
        ':!node_modules' ':!.venv' ':!*.lock' 2>/dev/null)" || true
fi

if [ -n "$CONFLICTS" ]; then
    cat >&2 <<MSG
WARNING: Conflict markers detected after git operation.

Affected files:
$(echo "$CONFLICTS" | sed 's/^/  - /')

Fix immediately:
  1. Resolve conflicts (remove <<<<<<<, =======, >>>>>>> markers)
  2. Stage resolved files: git add <file>
  3. Continue the operation (e.g., git rebase --continue)
MSG
fi

exit 0
