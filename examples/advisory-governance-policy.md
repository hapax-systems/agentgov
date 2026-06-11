# Advisory Governance Policy Example

Use an advisory rollout before production enforcement. In `hapax-agentgov`
0.3.1, advisory is a process choice rather than a CLI mode: evaluate hooks in a
sandbox, fork, or other low-risk review environment before installing them in
production repositories.

## Purpose

AI-assisted development must leave enough evidence for a human reviewer to
understand what changed, what the AI did, and which checks passed.

## Starting Rules

- AI output is never accepted without human review.
- Secrets, credentials, customer data, and private personal data must not be
  placed in prompts or public examples.
- `agentgov check` output is retained with the work evidence packet.
- Hook failures from the review environment are retained and evaluated before
  production enforcement is added.
- A human owner decides whether the change is accepted, revised, rejected, or
  escalated.

## Pilot Stages

1. Observe: run checks in a review environment and collect findings without
   blocking production work.
2. Warn: make repeated failures visible to reviewers.
3. Enforce: block only the checks that have been reviewed and approved locally.

## Promotion Criteria

A hook can move from advisory to enforcement when:

- the failure mode is clear;
- false positives are understood;
- bypass or exception handling is documented;
- reviewers agree the block prevents meaningful risk;
- the local team knows how to recover.
