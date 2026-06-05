# Chunk 1: Core Object And Extension Field Lock

Chunk 1 locks the fields that Week 2 OpenAPI components encode.

This chunk does not create the OpenAPI document. It defines the protocol field
contract that the OpenAPI document must preserve.

## Scope

Core objects:

```txt
Worker
Actor
HumanWorker
AgentWorker
WorkSession
JarvisEvent
Policy
PolicyDecision
Request
Review
Takeover
Contribution
EvidenceManifest
LearningRecord
MemoryProposal
SkillProposal
```

Extension object:

```txt
OutcomeReport
```

## Outputs

- required fields for every core object
- optional fields for every core object
- forbidden field classes for every core object
- protocol reason for every required field group
- stable id and reference rules
- OutcomeReport extension field lock
- OpenAPI component mapping notes

## Non-Goals

Chunk 1 does not:

- write the OpenAPI document
- define HTTP paths
- build a runtime
- build a product proof
- start Garden POC work
- implement adapters
- create conformance fixtures
- add product-private fields

## Field Rules

Every field must fall into one category:

```txt
required
optional
extension
forbidden
```

Required fields define portable protocol meaning.

Optional fields add protocol-visible context without changing required
semantics.

Extension fields must be namespaced and must not change the meaning of core
fields.

Forbidden fields belong to hosts, products, identity systems, runtimes,
databases, cloud platforms, billing systems, or private execution stacks.

## OpenAPI Component Mapping Notes

Week 2 maps this field lock into OpenAPI 3.1 components as follows:

- required field blocks become OpenAPI `required` arrays
- optional field blocks become OpenAPI properties outside `required`
- forbidden field blocks become conformance rejection cases
- `extensions` uses namespaced keys only
- nested reference shapes such as `contributor_refs` become named components
- opaque refs stay strings or typed ref objects without host-private structure
- portable exports exclude forbidden fields

## Review Requirements

Chunk 1 requires:

- Zero-Trust Security Reviewer
- Protocol Thesis Reviewer
- Chief Engineer Reviewer
- Conformance And Interop Reviewer
- Human Workflow Reviewer

All five lanes are required because this chunk defines the contract surface
that Week 2 OpenAPI work encodes.

## Zero-Trust Checks

Reviewers must verify:

- every state-changing object remains attributable to an Actor
- every WorkSession-scoped object references `work_session_id`
- every autonomous AgentWorker action is traceable to PolicyDecision
- WorkSession records expose revision and latest event hash values needed for
  Week 2 replay, stale-write, and previous-hash checks
- optional fields do not create a path for credentials, secrets, raw auth
  tokens, database internals, deployment details, runtime internals, or
  product-private state
- event hash fields remain portable and verifiable
- OutcomeReport records required `source_ref`, `reporter_ref`,
  `accepted_by_actor_id`, required `learning_record_refs`, and cannot mutate
  sealed WorkSession or EvidenceManifest records

## Done Criteria

Chunk 1 is complete when:

- `11-core-protocol-objects.md` contains the field lock
- `OutcomeReport` is locked as an extension, not a v0 core object
- every core object has required, optional, and forbidden field classes
- every required field group has a protocol reason
- local checks pass
- all five reviewer lanes complete
- findings are integrated or rejected with concrete reasons
- PR is opened
