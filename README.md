<!-- hapax-sdlc:preamble:begin -->
<!-- hapax-public:surface=github.repo.agentgov.readme.preamble:begin -->

# agentgov

**[Archived Prototype — Superseded by [hapax-systems/reins](https://github.com/hapax-systems/reins)]** `agentgov` is an archived early standalone governance-hook prototype in the **Hapax Research Lab** portfolio ([hapaxresearch.com](https://hapaxresearch.com)). It is retained for historical inspection and citation; evaluate [reins](https://github.com/hapax-systems/reins) for active governed agent-delivery observation and command preview.

## Reader promise

Archived early governance-hook prototype retained for historical inspection and citation; active work lives in hapax-systems/reins.

## Reader value

Preserves historical pre-action hook scripts and MIT source for reference while directing new evaluations to hapax-systems/reins and https://hapaxresearch.com.

## Claim ceiling

Archived prototype (v0.3.2, inactive); pattern checks at local tool boundaries do not establish complete coverage of agent behavior or a general security boundary.

## License and rights

Archived MIT-licensed prototype; existing MIT grants remain intact for historical inspection and citation of agentgov only and do not imply rights or support obligations across active Hapax Research Lab repositories.

Rendered summary: MIT. See `LICENSE`, `NOTICE.md`, `CITATION.cff`, and `.zenodo.json` for the authority surfaces.

## Public boundary

- Repository is archived and read-only; evaluate https://github.com/hapax-systems/reins for active governed agent-delivery inspection
- Published by **Hapax Research Lab** (`hrl-han`, [hapaxresearch.com](https://hapaxresearch.com)). Legal entity (as filed): Hapax Research LLC, organized in Wyoming on 2026-05-10, filing ID 2026-001973400.
- Security disclosures and factual correction proposals: `hrl-han@hapaxresearch.com` (see `SECURITY.md` and [hapaxresearch.com/about/#contact](https://hapaxresearch.com/about/#contact)). The network commits to receipt, retention and published correction. It promises no response time.
- Public copy uses `hapax-systems` organization links for first-party repositories; README text is orientation rather than a live runtime receipt.
- Governance reference: https://github.com/hapax-systems/hapax-constitution

## Portfolio position

Archived early standalone governance-hook prototype. Superseded for active governed agent-delivery inspection and preview by hapax-systems/reins.

<!-- hapax-public:surface=github.repo.agentgov.readme.preamble:end -->
<!-- hapax-sdlc:preamble:end -->

> **Archived / Inactive (`v0.3.2`).** `agentgov` is an archived early standalone governance-hook prototype from **Hapax Research Lab** ([hapaxresearch.com](https://hapaxresearch.com)) and is no longer under active development.
>
> - **Active governance cockpit & front door:** [hapax-systems/reins](https://github.com/hapax-systems/reins)
> - **Runtime governance & routing mechanisms:** [hapax-systems/hapax-spine](https://github.com/hapax-systems/hapax-spine)
> - **Historical source & release archives:** [GitHub Releases (`hapax-systems/agentgov/releases`)](https://github.com/hapax-systems/agentgov/releases)
> - **Lab overview & publications:** [https://hapaxresearch.com](https://hapaxresearch.com)
> - **Security disclosures:** `hrl-han@hapaxresearch.com` (see [SECURITY.md](SECURITY.md))

Release `0.3.2` records this retirement notice, sets package metadata to `Development Status :: 7 - Inactive`, and aligns the security disclosure contact with `hrl-han@hapaxresearch.com`. Existing MIT license grants and historical source remain intact for inspection and citation.

---

## Historical Overview

`agentgov` was published as a small MIT-licensed hook toolkit for governing AI coding agents at the local tool boundary before building heavier governance infrastructure. Hooks inspect file edits, shell commands, git actions, and project preconditions before the agent acts; when a check fails, the tool call is blocked with an actionable diagnostic on stderr.

Pattern checks at selected tool boundaries do not establish complete coverage of agent behavior or a general security boundary. New evaluations should inspect [hapax-systems/reins](https://github.com/hapax-systems/reins) and [hapaxresearch.com](https://hapaxresearch.com).

## Historical Source Inspection

Inspect historical tagged releases directly from [GitHub Releases](https://github.com/hapax-systems/agentgov/releases) or from a pinned git checkout:

```bash
git clone --branch v0.3.2 https://github.com/hapax-systems/agentgov.git
cd agentgov
uv sync --locked
uv run agentgov --help
```

Running `agentgov init` in a local sandbox scaffolds `.claude/hooks/` and registers selected hooks in `.claude/settings.local.json`.

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

---

*HACA-C v0.3.15, the lab's draft rule for labelling machine-made text, not an external certification. No request to a natural person to approve the final wording, and no such approval, was found in hrl-han's sending, review and coordination records when the text was released. hrl-han releases a text once its checking is complete, under a standing rule that hrl-han's principal, who is not named in this text, adopted before the text was drafted. Review record: https://hapaxresearch.com/review-record/ (open to anyone). This label records how the text was made; it does not certify that the text is true. An unaltered record can contain false claims or miss relevant events.*
