# Week 2 Chunk 3: WorkSession And Policy Schemas

## Goal

Encode the OpenAPI schema spine that carries WorkSession state, append-only
events, Policy boundaries, and PolicyDecision records.

## Scope

This chunk locks:

- `WorkSession`
- `JarvisEvent`
- `Policy`
- `PolicyDecision`
- WorkSession status enum
- PolicyDecision result enum
- risk and data sensitivity enums
- canonicalization profile schema
- policy action request and rule schemas
- forbidden-field metadata for the new schemas
- schema validation for locked required fields

This chunk does not define:

- Request schema
- Review schema
- Takeover schema
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
- [../../../scripts/check_openapi_skeleton.py](../../../scripts/check_openapi_skeleton.py)

## Acceptance

Chunk 3 is complete when:

- the OpenAPI file parses as YAML
- `WorkSession`, `JarvisEvent`, `Policy`, and `PolicyDecision` exist under
  `components.schemas`
- the new schemas encode the required fields from
  [../../protocol/11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
- the new schemas reject unspecified top-level fields with
  `additionalProperties: false`
- the new schemas list forbidden host-private fields in
  `x-jarvis-forbidden-fields`
- `WorkSession` carries protocol version, lifecycle status, revision, previous
  event hash state, event log reference, and the HumanWorker/AgentWorker pair
- `JarvisEvent` carries ordered append-only event attribution, payload,
  previous hash, event hash, and canonicalization profile
- `Policy` carries the human-defined boundary for agent action
- `PolicyDecision` records the required precondition for every AgentWorker
  action that affects WorkSession state
- no schema includes credentials, secrets, database ids, runtime ids, billing
  fields, deployment ids, or UI state as protocol properties
- local validation passes

## Boundary

These schemas record protocol state. They do not evaluate policy, execute
actions, store events, authenticate callers, choose tools, run agents, or define
host workflow.
