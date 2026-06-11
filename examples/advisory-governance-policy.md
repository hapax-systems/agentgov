# Advisory Governance Policy Example

Use advisory mode before enforcement. This example is intentionally generic.

## Purpose

AI-assisted development must leave enough evidence for a human reviewer to
understand what changed, what the AI did, and which checks passed.

## Starting Rules

- AI output is never accepted without human review.
- Secrets, credentials, customer data, and private personal data must not be
  placed in prompts or public examples.
- `agentgov check` output is retained with the work evidence packet.
- Hook failures are reviewed before enforcement is tightened.
- A human owner decides whether the change is accepted, revised, rejected, or
  escalated.

## Pilot Stages

1. Observe: run checks and collect findings without blocking work.
2. Warn: make repeated failures visible to reviewers.
3. Enforce: block only the checks that have been reviewed and approved locally.

## Promotion Criteria

A hook can move from advisory to enforcement when:

- the failure mode is clear;
- false positives are understood;
- bypass or exception handling is documented;
- reviewers agree the block prevents meaningful risk;
- the local team knows how to recover.
