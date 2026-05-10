#!/usr/bin/env bash
# work-resolution-gate.sh — Block edits when current branch has unresolved work.
# If you're on a feature branch with commits but no PR, submit a PR first.
# If you have an open PR with failing checks, edits are allowed (to fix CI).
set -euo pipefail

input="$(cat)"
tool_name="$(printf '%s' "$input" | jq -r '.tool_name // empty')"

case "$tool_name" in
  Edit|Write|MultiEdit|NotebookEdit) ;;
  *) exit 0 ;;
esac

git rev-parse --is-inside-work-tree &>/dev/null || exit 0

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)"
[ -n "$branch" ] || exit 0
[ "$branch" != "main" ] && [ "$branch" != "master" ] && [ "$branch" != "HEAD" ] || exit 0

default_branch="main"
git show-ref --verify --quiet refs/heads/main || default_branch="master"

ahead=$(git rev-list --count "${default_branch}..HEAD" 2>/dev/null || echo 0)
[ "$ahead" -gt 0 ] || exit 0

# Check if there's an open PR for this branch
if command -v gh >/dev/null 2>&1; then
    pr_state="$(gh pr view "$branch" --json state --jq '.state' 2>/dev/null || true)"
    if [ "$pr_state" = "OPEN" ]; then
        exit 0
    fi
fi

echo "BLOCKED: Branch '$branch' has $ahead commit(s) ahead of $default_branch but no open PR." >&2
echo "Submit a PR before continuing work, or merge/delete the branch." >&2
exit 2
