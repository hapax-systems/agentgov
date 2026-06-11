# AI Work Evidence Packet Example

Use this as a starting point for documenting AI-assisted development work.
Adapt it to local policy before production use.

```yaml
type: ai_work_evidence_packet
schema_version: 1
id: aiwp-YYYYMMDD-N
work_context: local-repository-or-sandbox
human_owner: name_or_role
created_at: YYYY-MM-DDTHH:MM:SSZ
ai_tool_used: tool name
ai_use_mode: brainstorming | drafting | code_generation | review | testing | summarization | other
input_classification: public | internal | confidential | restricted | unknown
output_used: none | partial | substantial

review:
  human_review_completed: true
  reviewer: name_or_role
  review_summary: short description
  known_limitations:
    - item

evidence:
  agentgov_checks:
    - agentgov check output retained locally
  tests_or_checks:
    - item
  source_refs:
    - local reference
  decision_record: human decision and rationale

guardrails:
  contains_customer_data: false
  contains_employee_personal_data: false
  contains_credentials: false
  contains_unapproved_external_disclosure: false
  requires_manager_review: false
  requires_security_review: false

outcome:
  status: accepted | revised | rejected | escalated
  next_action: short next step
```

## Notes

- Keep organization-confidential details in the organization's own systems.
- Do not paste secrets, customer data, private employee information, or
  restricted architecture into public examples.
- Treat AI output as untrusted until reviewed by a human owner.
