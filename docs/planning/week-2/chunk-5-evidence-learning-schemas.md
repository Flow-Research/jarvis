# Week 2 Chunk 5: Evidence And Learning Schemas

## Goal

Encode the OpenAPI schemas that make attribution, portable evidence, governed
learning, memory proposals, skill proposals, and post-session feedback explicit
protocol records.

## Scope

This chunk locks:

- `Contribution`
- `ContributorRef`
- `EvidenceItemRef`
- `EvidenceManifest`
- `ExportProfile`
- `LearningRecord`
- `MemoryProposal`
- `SkillProposal`
- `OutcomeReport`
- contribution type enum
- contributor type enum
- learning subject type enum
- learning review state enum
- proposal target type enum
- memory proposal status enum
- skill proposal status enum
- forbidden-field metadata for the new schemas
- invariant metadata for sealed evidence, governed memory, governed skills, and
  OutcomeReport boundaries
- schema validation for locked required fields
- conditional validation for shared Contribution attribution
- conditional validation for accepted MemoryProposal and SkillProposal review
  refs

This chunk does not define:

- path operation bodies
- operation-specific security requirements
- examples
- conformance fixtures
- runtime execution
- host implementation behavior
- payment, compensation, scoring, settlement, or marketplace logic

## Files

- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../openapi/README.md](../../openapi/README.md)
- [../../../scripts/check_openapi_skeleton.py](../../../scripts/check_openapi_skeleton.py)

## Acceptance

Chunk 5 is complete when:

- the OpenAPI file parses as YAML
- `Contribution`, `ContributorRef`, `EvidenceItemRef`, `EvidenceManifest`,
  `ExportProfile`, `LearningRecord`, `MemoryProposal`, `SkillProposal`, and
  `OutcomeReport` exist under `components.schemas`
- the new schemas encode the required fields from
  [../../protocol/11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
- the new schemas reject unspecified top-level fields with
  `additionalProperties: false`
- the new schemas list forbidden host-private fields in
  `x-jarvis-forbidden-fields`
- shared Contribution requires multiple contributor refs
- Contribution contributor refs declare identity uniqueness by `worker_id` and
  `actor_id`
- EvidenceItemRef requires at least one source event ref
- EvidenceManifest requires evidence item refs and contribution refs
- EvidenceManifest evidence item refs declare identity uniqueness by `id`
- LearningRecord requires at least one source event ref
- accepted MemoryProposal requires review refs
- accepted SkillProposal requires review refs
- OutcomeReport requires at least one LearningRecord ref
- EvidenceManifest declares terminal-state export, sealed mutation rejection,
  and redaction-source preservation invariants
- MemoryProposal declares review and self-confirmation rejection invariants
- SkillProposal declares review, tool-access policy review, and unreviewed
  activation rejection invariants
- OutcomeReport declares terminal-source, sealed WorkSession, sealed
  EvidenceManifest, and learning-record invariants
- no schema includes credentials, secrets, database ids, raw runtime state,
  billing fields, deployment details, payment fields, settlement fields,
  private scores, unreviewed memory writes, unreviewed skill activation, or UI
  state as protocol properties
- local validation passes

## Boundary

These schemas record attribution, evidence, learning, proposal, and feedback
contracts for human-agent collaboration. They do not store files, execute
work, activate memory, activate skills, evaluate tasks, calculate scores,
settle payments, authenticate callers, or define host workflow.
