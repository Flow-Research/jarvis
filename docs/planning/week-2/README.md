# Week 2: OpenAPI Contract And Conformance Entry

Status: complete.

This is a historical v0.1 planning record. Current normative protocol rules
live in [../../protocol](../../protocol), [../../openapi](../../openapi), and
[../../conformance](../../conformance).

Week 2 turned the locked protocol into the first OpenAPI 3.1 contract shape and
conformance entry.

Week 2 locked the OpenAPI protocol contract and conformance entry only.

## Chunks

1. [chunk-1-openapi-skeleton.md](./chunk-1-openapi-skeleton.md)
   Lock the OpenAPI entry point, required buckets, tag taxonomy, and skeleton validation.
2. [chunk-2-participant-schemas.md](./chunk-2-participant-schemas.md)
   Lock shared schema primitives, Worker, Actor, HumanWorker, and AgentWorker.
3. [chunk-3-worksession-policy-schemas.md](./chunk-3-worksession-policy-schemas.md)
   Lock WorkSession, JarvisEvent, Policy, and PolicyDecision schemas.
4. [chunk-4-control-plane-schemas.md](./chunk-4-control-plane-schemas.md)
   Lock Request, Review, ApprovalScope, and Takeover schemas.
5. [chunk-5-evidence-learning-schemas.md](./chunk-5-evidence-learning-schemas.md)
   Lock Contribution, EvidenceManifest, LearningRecord, MemoryProposal,
   SkillProposal, and OutcomeReport schemas.
6. [chunk-6-path-security-binding.md](./chunk-6-path-security-binding.md)
   Lock path operations, protocol header parameters, request bodies, responses,
   HostAuth security binding, and ProtocolError.
7. [chunk-7-examples-conformance-entry.md](./chunk-7-examples-conformance-entry.md)
   Lock OpenAPI examples and conformance entry documents.

## Week 2 Done State

Status: complete.

Week 2 completed these checks. The OpenAPI contract answers:

```txt
how a host creates a WorkSession
how a host appends JarvisEvent records
how AgentWorker actions record PolicyDecision
how blocked action creates Request
how HumanWorker response records Review or Takeover
how Contribution and EvidenceManifest records are exported
how OutcomeReport references governed LearningRecord records through
learning_record_refs
```

The contract remains protocol-only. Hosts own implementation.

For closeout, see [closeout.md](./closeout.md).
