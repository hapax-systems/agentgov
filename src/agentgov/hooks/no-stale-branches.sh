#!/usr/bin/env bash
# no-stale-branches.sh — Block new branch creation when unmerged branches exist.
# Enforces "finish before starting" discipline.
set -euo pipefail

INPUT="$(cat)"
TOOL="$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null)" || exit 0

[ "$TOOL" = "Bash" ] || exit 0

CMD="$(echo "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)" || exit 0
[ -n "$CMD" ] || exit 0

is_create=false
echo "$CMD" | grep -qE '^\s*git\s+checkout\s+-[bB]\s' && is_create=true
echo "$CMD" | grep -qE '^\s*git\s+switch\s+(-c|--create)\s' && is_create=true
echo "$CMD" | grep -qE '^\s*git\s+branch\s+[a-zA-Z]' && is_create=true

[ "$is_create" = true ] || exit 0

git rev-parse --is-inside-work-tree &>/dev/null || exit 0

default_branch="main"
git show-ref --verify --quiet refs/heads/main || default_branch="master"

stale=""
while IFS= read -r branch; do
    [ -z "$branch" ] && continue
    [ "$branch" = "$default_branch" ] && continue
    ahead=$(git rev-list --count "${default_branch}..${branch}" 2>/dev/null || echo 0)
    if [ "$ahead" -gt 0 ]; then
        stale="${stale}  ${branch} (${ahead} commits ahead)\n"
    fi
done < <(git for-each-ref --format='%(refname:short)' refs/heads/ 2>/dev/null)

if [ -n "$stale" ]; then
    echo "BLOCKED: Cannot create new branch — unmerged branches exist:" >&2
    printf '%b' "$stale" >&2
    echo "" >&2
    echo "Merge or delete these branches before starting new work." >&2
    exit 2
fi

exit 0
