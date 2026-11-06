# Advisory Governance Policy Example (Archived Prototype)

> **[Archived Prototype — Superseded by [hapax-systems/reins](https://github.com/hapax-systems/reins)]** Retained for historical reference alongside `agentgov` `0.3.2` (archived). Evaluate [hapax-systems/reins](https://github.com/hapax-systems/reins) for active governed agent-delivery observation and command preview.

Use an advisory rollout before production enforcement. In `agentgov` `0.3.2`
(archived), advisory operation is a process choice rather than a CLI mode:
evaluate hooks in a sandbox, fork, or other low-risk review environment before
installing them in active repositories.

## Purpose

AI-assisted development must leave enough evidence for a human reviewer to
understand what changed, what the AI did, and which checks passed.

## Starting Rules

- AI output is never accepted without human review.
- Secrets, credentials, customer data, and private personal data must not be
  placed in prompts or public examples.
- `agentgov check` output is retained with the work evidence packet.
- Hook failures from the review environment are retained and evaluated before
  blocking enforcement is added.
- A human owner decides whether the change is accepted, revised, rejected, or
  escalated.

## Pilot Stages

1. Observe: run checks in a review environment and collect findings without
   blocking active work.
2. Warn: make repeated failures visible to reviewers.
3. Enforce: block only the checks that have been reviewed and approved locally.

## Promotion Criteria

A hook can move from advisory to enforcement when:

- the failure mode is clear;
- false positives are understood;
- bypass or exception handling is documented;
- reviewers agree the block prevents meaningful risk;
- the local team knows how to recover.

---

*HACA-C v0.3.15, the lab's draft rule for labelling machine-made text, not an external certification. No request to a natural person to approve the final wording, and no such approval, was found in hrl-han's sending, review and coordination records when the text was released. hrl-han releases a text once its checking is complete, under a standing rule that hrl-han's principal, who is not named in this text, adopted before the text was drafted. Review record: https://hapaxresearch.com/review-record/ (open to anyone). This label records how the text was made; it does not certify that the text is true. An unaltered record can contain false claims or miss relevant events.*
