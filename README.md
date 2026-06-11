# hapax-agentgov

Governance hooks for AI coding agents. Extracted from a production system running 47 hooks across 200+ agents.

Works with [Claude Code](https://docs.anthropic.com/en/docs/claude-code) hooks. Enforces safety, git hygiene, and project rules automatically — before the agent acts, not after.

## Quick start

```bash
pip install hapax-agentgov
cd your-project
agentgov init
```

This scaffolds `.claude/hooks/` with safety hooks and registers them in `.claude/settings.local.json`.

## What it does

Hooks intercept Claude Code tool calls (file edits, bash commands) and block dangerous actions before they execute:

| Hook | Category | What it blocks |
|------|----------|----------------|
| `pii-guard` | safety | Email addresses, SSNs, phone numbers, home directory paths in tracked files |
| `secrets-guard` | safety | AWS keys, GitHub tokens, API keys, private keys |
| `conflict-marker-scan` | safety | Warns when `<<<<<<<` markers appear after git merge/rebase |
| `safe-stash-guard` | git | `git stash pop` (use `apply + drop` instead — pop can't recover from conflicts) |
| `push-gate` | git | Autonomous `git push`, `gh pr create/merge` without user approval |
| `no-stale-branches` | git | Creating new branches when unmerged work exists |
| `work-resolution-gate` | workflow | Editing code on branches with no open PR |
| `pkg-manager-guard` | tooling | Direct `pip install` (enforces `uv` or `poetry`) |
| `protected-paths` | workflow | Writes to `*.pem`, `*.key`, and other sensitive file patterns |

## CLI

### `agentgov init`

Scaffold hooks into your project.

```bash
agentgov init                    # "safe" preset (recommended 6 hooks)
agentgov init --preset strict    # all 9 hooks
agentgov init --preset minimal   # just pii-guard + conflict-marker-scan
agentgov init --force            # overwrite existing hook scripts
```

### `agentgov check`

Validate your hook configuration.

```bash
agentgov check
# agentgov: 6 hooks configured and valid
#   OK  pii-guard.sh (PreToolUse)
#   OK  secrets-guard.sh (PreToolUse)
#   ...
```

### `agentgov report`

Show governance coverage.

```bash
agentgov report
# agentgov: 6/9 hooks active (67% coverage)
#
# Active:
#   [safety] pii-guard: Block writes that introduce PII patterns
#   [safety] secrets-guard: Block writes containing API keys and tokens
#   ...

agentgov report --json    # machine-readable output
```

## Enterprise adoption

Start with an advisory pilot before enforcement in production. In this release,
installed hooks enforce their checks; advisory means using a sandbox, fork, or
low-risk repository to inspect findings before promotion. The enterprise guide
covers a safe pilot shape, license and attribution expectations, security
readiness checks, and the boundary between free adoption and paid support:

- [Enterprise adoption guide](docs/enterprise-adoption.md)
- [AI work evidence packet example](examples/ai-work-evidence-packet.md)
- [Advisory governance policy example](examples/advisory-governance-policy.md)

## How hooks work

Claude Code hooks are shell scripts that run before (`PreToolUse`) or after (`PostToolUse`) tool calls. They receive the tool name and input as JSON on stdin:

```json
{
  "tool_name": "Edit",
  "tool_input": {
    "file_path": "/path/to/file.py",
    "new_string": "API_KEY = 'sk-abc123...'"
  }
}
```

A hook exits 0 to allow, exits 2 to block (with a message on stderr).

## Writing custom hooks

Drop any `.sh` script in `.claude/hooks/` and register it in `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": ".claude/hooks/my-hook.sh" }]
      }
    ]
  }
}
```

## Origin

Extracted from [hapax-council](https://github.com/hapax-systems/hapax-council), a personal operating environment running 200+ AI agents with 47 governance hooks enforcing safety, privacy, git discipline, and project rules across all agent sessions.

## License

MIT
