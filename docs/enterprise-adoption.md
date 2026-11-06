# Enterprise Adoption Guide (Archived Prototype)

> **[Archived Prototype — Superseded by [hapax-systems/reins](https://github.com/hapax-systems/reins)]** `agentgov` (`0.3.2`, inactive) is retained for historical inspection and citation only. Evaluate [hapax-systems/reins](https://github.com/hapax-systems/reins) and [hapaxresearch.com](https://hapaxresearch.com) for active governed agent-delivery tooling.

`agentgov` was published as an MIT-licensed prototype for local AI coding
governance hooks covering safety, git hygiene, and project-rule checks.

It is not:

- the Hapax Research Lab runtime;
- a compliance certification;
- a replacement for human review;
- a warranty or support commitment;
- a live bridge to any external system.

## Historical Sandbox Inspection Shape

1. Inventory local AI-assisted development workflows.
2. Select one low-risk repository, fork, or isolated sandbox.
3. Inspect the archived `v0.3.2` source from [GitHub Releases](https://github.com/hapax-systems/agentgov/releases) under standard open-source intake rules.
4. Run `agentgov init --preset minimal` or `agentgov init --preset safe` only in that sandbox environment. Installed hooks enforce by exiting non-zero when they block; there is no separate CLI advisory switch.
5. Run `agentgov check` and `agentgov report` and retain the output as local evidence.
6. Review sandbox findings before enabling any hook in an active repository.
7. Pair changes with an AI work evidence packet (`examples/ai-work-evidence-packet.md`).
8. Promote individual hooks only after local human review.

## License and Attribution

`agentgov` is MIT licensed (`LICENSE`, `Copyright (c) 2026 Hapax Research LLC`).
Users may use, copy, modify, merge, publish, distribute, sublicense, and sell
copies under the MIT license terms.

Required:

- preserve the MIT copyright and license notice;
- record the git tag (`v0.3.2`) or commit SHA inspected;
- keep local modifications identified.

Not included:

- warranty;
- indemnity;
- support or response-time guarantees;
- rights to any other Hapax Research Lab repository (`reins`, `hapax-spine`, `hapax-constitution`).

## Security and Release Readiness Checklist

Before adopting any local hook script in an internal workflow, collect:

- SBOM or dependency inventory with SPDX license identifiers;
- git tag or commit SHA provenance;
- reproducible source archive from [GitHub Releases](https://github.com/hapax-systems/agentgov/releases);
- dependency vulnerability and secret-scan results;
- documented hook coverage and known limitations;
- human review sign-off before enabling blocking mode.

## Boundary Checklist

- [ ] The sandbox repository is owned by the evaluating organization.
- [ ] No confidential organization data is copied into public examples.
- [ ] The `agentgov` tag/commit SHA and MIT license notice are recorded.
- [ ] Evaluation starts in an isolated sandbox or fork.
- [ ] Findings are reviewed by a human before blocking enforcement.

---

*HACA-C v0.3.15, the lab's draft rule for labelling machine-made text, not an external certification. No request to a natural person to approve the final wording, and no such approval, was found in hrl-han's sending, review and coordination records when the text was released. hrl-han releases a text once its checking is complete, under a standing rule that hrl-han's principal, who is not named in this text, adopted before the text was drafted. Review record: https://hapaxresearch.com/review-record/ (open to anyone). This label records how the text was made; it does not certify that the text is true. An unaltered record can contain false claims or miss relevant events.*
