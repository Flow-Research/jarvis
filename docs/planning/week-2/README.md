# Week 2: OpenAPI Contract And Conformance Entry

Week 2 turns the locked protocol into the first OpenAPI 3.1 contract shape and
conformance entry.

This week does not build a host implementation, runtime features, UI, auth,
storage, model calls, adapters, or conformance fixtures beyond the active chunk.

## Chunks

1. [chunk-1-openapi-skeleton.md](./chunk-1-openapi-skeleton.md)
   Lock the OpenAPI entry point, required buckets, tag taxonomy, and skeleton validation.
2. [chunk-2-participant-schemas.md](./chunk-2-participant-schemas.md)
   Lock shared schema primitives, Worker, Actor, HumanWorker, and AgentWorker.

## Week 2 Done State

Week 2 is complete when the OpenAPI contract answers:

```txt
how a host creates a WorkSession
how a host appends JarvisEvent records
how AgentWorker actions record PolicyDecision
how blocked action creates Request
how HumanWorker response records Review or Takeover
how Contribution and EvidenceManifest records are exported
how OutcomeReport feeds post-session learning
```

The contract remains protocol-only. Hosts own implementation.
