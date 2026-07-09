<!-- hapax-sdlc:preamble:begin -->
<!-- hapax-public:surface=github.repo.agentgov.readme.preamble:begin -->

# agentgov

`agentgov` is the bounded adoption-commons repository in the Hapax Systems portfolio. It is published so adopters can inspect and pilot the governance-hook surface without inheriting the Hapax runtime estate.

## Reader promise

Portable governance hooks that an adopter can install, audit, and pilot without inheriting the Hapax estate.

## Reader value

Turns common AI coding-agent risks into installable pre-action checks that teams can pilot before buying or building heavier governance.

## Claim ceiling

Adoption commons for hooks only; not the full Hapax governance system, not policyflow, and not a staffed support service.

## License and rights

Permissive adoption surface; copy may say MIT for agentgov only and must not imply broader Hapax runtime rights or support obligations.

Rendered summary: MIT. See `LICENSE` for the authority surfaces.

## Public boundary

- Issues are redirect-only and support is bounded; pull requests are not the intake path for this repository
- Public copy must use `hapax-systems` organization links for first-party Hapax repositories.
- README text is orientation, not a freshness witness; current public claims require surface-specific release, reconcile, or publication receipts.
- Publication, weblog, RSS, social, DOI/archive, and other public fanout paths must route through the governed publication bus or a documented guarded legacy surface.
- Governance reference: https://github.com/hapax-systems/hapax-constitution

## Portfolio position

Public adoption commons. Separate from council-local policyflow primitives and from the Hapax council runtime.

<!-- hapax-public:surface=github.repo.agentgov.readme.preamble:end -->
<!-- hapax-sdlc:preamble:end -->

# agentgov

`agentgov` is the Hapax Systems adoption commons: a small MIT-licensed
hook layer for governing AI coding agents at the tool boundary.

It gives teams a concrete place to start before they build a full agent
governance program. Hooks inspect file edits, shell commands, git actions,
and project preconditions before the agent acts. When a check fails, the
tool call is blocked and the agent receives a specific error to work from.

`agentgov` is not the Hapax runtime, not Reins, and not a hosted service. It
is the portable part: inspectable shell hooks, configuration, and examples
that an adopter can pilot in a low-risk repository.

## Quick start

```bash
pip install hapax-agentgov
cd your-project
agentgov init
```

This scaffolds `.claude/hooks/` and registers the selected hooks in
`.claude/settings.local.json`.

## What ships

| Hook | Category | Boundary | Reader value |
|---|---|---|---|
| `pii-guard` | safety | Blocks tracked writes that introduce common personal-data patterns. | Reduces the risk that an agent turns a routine edit into a privacy incident. |
| `secrets-guard` | safety | Blocks common API keys, tokens, and private-key material. | Catches one of the fastest ways an autonomous coding run can create cleanup work. |
| `conflict-marker-scan` | safety | Warns when merge-conflict markers appear after a merge or rebase. | Keeps mechanical merge residue from being treated as finished code. |
| `safe-stash-guard` | git | Blocks `git stash pop`; use `apply` plus explicit `drop` after review. | Preserves a reviewable rollback path when work is recovered from a stash. |
| `push-gate` | git | Blocks autonomous push and PR mutation paths without approval evidence. | Makes repository publication a governed act instead of an accidental tool call. |
| `no-stale-branches` | git | Blocks new branch creation while unresolved unmerged work exists. | Keeps agent work from spreading across hidden branches before prior work is resolved. |
| `work-resolution-gate` | workflow | Blocks code edits on branches that have no open PR resolution path. | Forces implementation work to stay attached to a visible review and closeout path. |
| `pkg-manager-guard` | tooling | Enforces the configured package manager boundary. | Prevents dependency churn caused by an agent choosing a different local toolchain. |
| `protected-paths` | workflow | Blocks edits to sensitive path patterns such as keys and certificates. | Gives high-risk files an explicit tripwire before generated edits land. |

## CLI

```bash
agentgov init                    # safe preset
agentgov init --preset strict    # all bundled hooks
agentgov init --preset minimal   # pii-guard + conflict-marker-scan
agentgov init --force            # overwrite generated hook scripts

agentgov check                   # validate installed hook configuration
agentgov report                  # summarize configured coverage
agentgov report --json           # machine-readable coverage
```

## Pilot Shape

Start advisory in a sandbox, fork, or low-risk repository. The installed
hooks enforce their checks, so "advisory" means evaluating the findings and
operational fit before promotion to production repos.

- [Enterprise adoption guide](docs/enterprise-adoption.md)
- [AI work evidence packet example](examples/ai-work-evidence-packet.md)
- [Advisory governance policy example](examples/advisory-governance-policy.md)

## How Hooks Work

Claude Code hooks are shell scripts that run before or after tool calls. They
receive the tool name and input as JSON on stdin. A hook exits `0` to allow
the action and exits `2` to block it with a message on stderr.

```json
{
  "tool_name": "Edit",
  "tool_input": {
    "file_path": "/path/to/file.py",
    "new_string": "API_KEY = 'sk-example'"
  }
}
```

Custom hooks can be dropped into `.claude/hooks/` and registered in
`.claude/settings.local.json`.

## Boundary

`agentgov` is the permissive adoption surface. The broader Hapax Systems
portfolio includes source-available and source-visible repositories with
different licenses and support boundaries. Do not infer rights for Reins,
hapax-spine, or hapax-council from the MIT license on this package.

GitHub Issues are redirect-only. Support, commercial engagement, roadmap
commitments, and feature-request handling do not happen through this repo.

## License

MIT. See [LICENSE](LICENSE).
