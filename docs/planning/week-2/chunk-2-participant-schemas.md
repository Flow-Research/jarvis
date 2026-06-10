# Week 2 Chunk 2: Participant Schemas

## Goal

Encode the first OpenAPI `components.schemas` slice from the locked core object
field list.

## Scope

This chunk locks:

- shared schema primitives
- `Worker`
- `Actor`
- `HumanWorker`
- `AgentWorker`
- forbidden-field metadata for those participant schemas
- schema validation for the locked required fields

This chunk does not define:

- WorkSession schema
- JarvisEvent schema
- Policy or PolicyDecision schema
- Request, Review, or Takeover schema
- Contribution schema
- EvidenceManifest schema
- LearningRecord, MemoryProposal, or SkillProposal schema
- OutcomeReport schema
- path operation bodies
- operation-specific security requirements
- examples
- conformance fixtures
- runtime execution
- Garden POC behavior

## Files

- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../openapi/README.md](../../openapi/README.md)
- [../../../scripts/check_openapi_skeleton.py](../../../scripts/check_openapi_skeleton.py)

## Acceptance

Chunk 2 is complete when:

- the OpenAPI file parses as YAML
- participant schemas exist under `components.schemas`
- participant schemas encode the required fields from
  [../../protocol/11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
- participant schemas reject unspecified top-level fields with
  `additionalProperties: false`
- participant schemas list forbidden host-private fields in
  `x-jarvis-forbidden-fields`
- `Worker` and `Actor` keep human, agent, service, and tool participation
  distinguishable
- `HumanWorker` and `AgentWorker` reference their Worker and Actor records
- no schema includes credentials, secrets, database ids, runtime ids, billing
  fields, or product UI state as protocol properties
- local validation passes

## Boundary

Participant schemas identify protocol workers and actors. They do not create
accounts, authenticate callers, issue credentials, choose model providers, run
agents, or define product UI.
