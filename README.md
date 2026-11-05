# agentgov — Archived Early Prototype

> **Archived / Inactive (`v0.3.2`).** `agentgov` (`hapax-agentgov` on PyPI) is an early standalone governance-hook prototype from **Hapax Research Lab** ([hapaxresearch.com](https://hapaxresearch.com)) and is no longer under active development.
>
> - **Active governance cockpit & frontdoor:** [hapax-systems/reins](https://github.com/hapax-systems/reins)
> - **Runtime governance & routing mechanisms:** [hapax-systems/hapax-spine](https://github.com/hapax-systems/hapax-spine)
> - **Lab overview & publications:** [https://hapaxresearch.com](https://hapaxresearch.com)
> - **Security disclosures:** `hrl-han@hapaxresearch.com` (see [SECURITY.md](SECURITY.md))

Release `0.3.2` publishes this retirement notice, updates package metadata to `Development Status :: 7 - Inactive`, and aligns the security disclosure contact with `hrl-han@hapaxresearch.com`. Existing MIT license grants and historical source remain intact for inspection and citation.

---

## Historical Overview

`agentgov` was published as a small MIT-licensed hook toolkit for governing AI coding agents at the local tool boundary before building heavier governance infrastructure. Hooks inspect file edits, shell commands, git actions, and project preconditions before the agent acts; when a check fails, the tool call is blocked with an actionable diagnostic on stderr.

Pattern checks at selected tool boundaries do not establish complete coverage of agent behavior or a general security boundary. New evaluations should inspect [hapax-systems/reins](https://github.com/hapax-systems/reins) and [hapaxresearch.com](https://hapaxresearch.com).

## Historical Quick Start

```bash
pip install hapax-agentgov
cd your-project
agentgov init
```

This scaffolds `.claude/hooks/` and registers the selected hooks in `.claude/settings.local.json`.

## Included Hook Scripts

| Hook | Category | Boundary |
|---|---|---|
| `pii-guard` | safety | Blocks tracked writes that introduce common personal-data or home-path patterns. |
| `secrets-guard` | safety | Blocks tracked writes containing common credential or token patterns. |
| `protected-paths` | safety | Prevents unapproved edits to sensitive or locked repository paths. |
| `conflict-marker-scan` | git-hygiene | Rejects files containing unresolved merge-conflict markers. |
| `no-stale-branches` | git-hygiene | Warns or blocks work on stale feature branches. |
| `push-gate` | git-hygiene | Enforces local verification gates prior to git push operations. |
| `safe-stash-guard` | git-hygiene | Guards against destructive git stash drops or overwrites. |
| `pkg-manager-guard` | project-rules | Enforces consistent package-manager invocation within a repository. |
| `work-resolution-gate` | project-rules | Checks work-item or evidence prerequisites before completion. |

## Historical Documentation & Examples

- [Enterprise adoption guide](docs/enterprise-adoption.md)
- [AI work evidence packet example](examples/ai-work-evidence-packet.md)
- [Advisory governance policy example](examples/advisory-governance-policy.md)

## How Hooks Work

Claude Code hooks are shell scripts that run before or after tool calls. They receive the tool name and input as JSON on stdin. A hook exits `0` to allow the action and exits `2` to block it with a message on stderr.

```json
{
  "tool_name": "Edit",
  "tool_input": {
    "file_path": "/path/to/file.py",
    "new_string": "API_KEY = 'sk-example'"
  }
}
```

## Boundary & License

`agentgov` is MIT licensed (see [LICENSE](LICENSE)). The broader Hapax Research Lab portfolio includes repositories with distinct licenses and support boundaries; do not infer license grants or support commitments for [reins](https://github.com/hapax-systems/reins) or [hapax-spine](https://github.com/hapax-systems/hapax-spine) from this archived package.

GitHub Issues are redirect-only. Governance rules live in [hapax-systems/hapax-constitution](https://github.com/hapax-systems/hapax-constitution).
