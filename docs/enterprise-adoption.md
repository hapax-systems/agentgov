# Enterprise Adoption Guide

`hapax-agentgov` is an MIT-licensed package for AI coding governance hooks. It
can help an organization pilot safety, git hygiene, and project-rule checks for
AI-assisted development.

It is not:

- the Hapax private runtime;
- a compliance certification;
- a replacement for human review;
- a warranty or support commitment;
- a live bridge to any external system.

## Pilot Shape

Use this order:

1. Inventory local AI-assisted development workflows.
2. Select one low-risk repository or sandbox.
3. Install `hapax-agentgov` under normal open-source intake rules.
4. Run `agentgov init --preset minimal` or `agentgov init --preset safe`.
5. Run `agentgov check` and keep the output as evidence.
6. Keep the first pilot advisory: collect findings before adding hard blocks.
7. Use an AI work evidence packet for each meaningful AI-assisted change.
8. Promote individual hooks to enforcement only after local review.

## License And Attribution

The package is MIT licensed. Users may use, copy, modify, merge, publish,
distribute, sublicense, and sell copies under the MIT license terms.

Required:

- preserve the MIT copyright and license notice;
- record the package version or commit used in the pilot;
- keep local modifications identified.

Not included:

- warranty;
- indemnity;
- guaranteed support;
- transfer of any private Hapax system or private research artifact.

## Security And Release Readiness

Before a production or public adoption push, collect:

- SBOM or package inventory with SPDX license identifiers;
- package version or commit provenance;
- reproducible source/archive reference where possible;
- OpenSSF Scorecard or equivalent repository health review;
- dependency vulnerability scan;
- secret-scan result;
- documented hook coverage and known limitations;
- human approval for any hook promoted from advisory to enforcement.

Recommended external frameworks for mapping:

- SPDX for license and SBOM communication;
- SLSA for provenance and supply-chain posture;
- NIST SSDF for secure software development practices;
- CISA Secure by Design for customer-security outcome framing.

## Support Expectations

Free adoption means the code and docs are available under the stated license.
It does not imply response-time guarantees, custom integration, production
support, security attestation, or procurement terms.

Paid support, training, enterprise policy packs, or hosted services must be
handled through a separate agreement. Keep public/free adoption and paid
support language distinct.

## Boundary Checklist

- [ ] The pilot repository is owned by the adopting organization.
- [ ] No private Hapax code or runtime state is imported.
- [ ] No confidential organization data is copied into public examples.
- [ ] The package version and license are recorded.
- [ ] The first pilot starts advisory.
- [ ] Findings are reviewed by a human before enforcement.
- [ ] Any outbound feedback is sanitized and generic.
