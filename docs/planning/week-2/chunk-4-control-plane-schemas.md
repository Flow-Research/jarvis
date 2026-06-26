# Week 2 Chunk 4: Control-Plane Schemas

## Goal

Encode the OpenAPI schemas that make blocked work, human judgment, bounded
approval, and human takeover explicit protocol records.

## Scope

This chunk locks:

- `Request`
- `Review`
- `ApprovalScope`
- `Takeover`
- Request type enum
- Request status enum
- blocking scope enum
- Review decision enum
- Takeover state enum
- request option schema
- safe fallback schema
- approval boundary schema
- forbidden-field metadata for the new schemas
- schema validation for locked required fields
- conditional validation for Request, Review, and Takeover lifecycle rules

This chunk does not define:

- Contribution schema
- EvidenceManifest schema
- LearningRecord, MemoryProposal, or SkillProposal schema
- OutcomeReport schema
- path operation bodies
- operation-specific security requirements
- examples
- conformance fixtures
- runtime execution
- host implementation behavior

## Files

- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../openapi/README.md](../../openapi/README.md)
- [../../../scripts/check_openapi_contract.py](../../../scripts/check_openapi_contract.py)

## Acceptance

Chunk 4 is complete when:

- the OpenAPI file parses as YAML
- `Request`, `Review`, `ApprovalScope`, and `Takeover` exist under
  `components.schemas`
- the new schemas encode the required fields from
  [../../protocol/11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
- the new schemas reject unspecified top-level fields with
  `additionalProperties: false`
- the new schemas list forbidden host-private fields in
  `x-jarvis-forbidden-fields`
- resolved Request statuses require resolver or closing refs
- pending and acknowledged Requests reject resolver and closing refs
- superseded Requests require `superseded_by_request_id`
- Review decisions `approve` and `narrow` require `ApprovalScope`
- Review decisions `deny`, `correct`, `takeover`, and `needs_revision` reject
  `ApprovalScope`
- Review decision `takeover` requires `takeover_id`
- Takeover records `affected_scope.blocking_scope` and `affected_scope.scope_ref`
- Takeover state `resumed` requires reconciliation refs
- Takeover states `requested`, `locked`, and `human_active` reject resume refs
- no schema includes credentials, secrets, database ids, runtime ids, billing
  fields, deployment ids, notification provider ids, inbox ids, unbounded
  approval, implicit authority grants, or UI state as protocol properties
- local validation passes

## Boundary

These schemas record the control plane for human-agent collaboration. They do
not deliver notifications, render inboxes, execute approvals, lock runtime
processes, store events, authenticate callers, or define host workflow.
