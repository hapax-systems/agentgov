"""Hook registry — defines available hooks and their metadata."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HookDef:
    name: str
    description: str
    event: str  # PreToolUse or PostToolUse
    matcher: str  # Tool matcher pattern
    script: str  # Filename in hooks/ dir
    category: str  # safety, git-hygiene, tooling, workflow


HOOKS: dict[str, HookDef] = {
    "pii-guard": HookDef(
        name="pii-guard",
        description="Block writes that introduce PII patterns (emails, SSNs, phones, API keys)",
        event="PreToolUse",
        matcher="Edit|Write|MultiEdit|NotebookEdit",
        script="pii-guard.sh",
        category="safety",
    ),
    "secrets-guard": HookDef(
        name="secrets-guard",
        description="Block writes containing API keys, tokens, passwords, and other secrets",
        event="PreToolUse",
        matcher="Edit|Write|MultiEdit|NotebookEdit",
        script="secrets-guard.sh",
        category="safety",
    ),
    "conflict-marker-scan": HookDef(
        name="conflict-marker-scan",
        description="Warn when conflict markers appear after git operations",
        event="PostToolUse",
        matcher="Bash",
        script="conflict-marker-scan.sh",
        category="safety",
    ),
    "safe-stash-guard": HookDef(
        name="safe-stash-guard",
        description="Block git stash pop (use apply+drop instead to avoid unrecoverable conflicts)",
        event="PreToolUse",
        matcher="Bash",
        script="safe-stash-guard.sh",
        category="git-hygiene",
    ),
    "push-gate": HookDef(
        name="push-gate",
        description="Block autonomous git push and PR create/merge (require user approval)",
        event="PreToolUse",
        matcher="Bash",
        script="push-gate.sh",
        category="git-hygiene",
    ),
    "no-stale-branches": HookDef(
        name="no-stale-branches",
        description="Block new branch creation when unmerged feature branches exist",
        event="PreToolUse",
        matcher="Bash",
        script="no-stale-branches.sh",
        category="git-hygiene",
    ),
    "work-resolution-gate": HookDef(
        name="work-resolution-gate",
        description="Block edits on branches with unresolved work (no PR, failing CI)",
        event="PreToolUse",
        matcher="Edit|Write|MultiEdit|NotebookEdit",
        script="work-resolution-gate.sh",
        category="workflow",
    ),
    "pkg-manager-guard": HookDef(
        name="pkg-manager-guard",
        description="Enforce a single package manager (block pip when uv/poetry is required)",
        event="PreToolUse",
        matcher="Bash",
        script="pkg-manager-guard.sh",
        category="tooling",
    ),
    "protected-paths": HookDef(
        name="protected-paths",
        description="Block writes to protected files/directories (configurable patterns)",
        event="PreToolUse",
        matcher="Edit|Write|MultiEdit|NotebookEdit",
        script="protected-paths.sh",
        category="workflow",
    ),
}

PRESETS: dict[str, list[str]] = {
    "safe": [
        "pii-guard",
        "secrets-guard",
        "conflict-marker-scan",
        "safe-stash-guard",
        "push-gate",
        "pkg-manager-guard",
    ],
    "strict": list(HOOKS.keys()),
    "minimal": [
        "pii-guard",
        "conflict-marker-scan",
    ],
}
