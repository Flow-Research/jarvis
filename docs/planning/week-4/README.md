# Week 4: Compatible Examples And Public Story

Week 4 turns the locked protocol, OpenAPI contract, conformance fixtures, and
existing-agent proof plan into public compatibility artifacts.

Status: active.

Week 4 does not build adapters, wrappers, host runtimes, UI, model calls, tool
execution, storage, auth, billing, scoring, payment, deployment behavior, or
SDK implementation.

Jarvis records the protocol proof. Hosts provide the implementation.

## Goal

Prove that existing human-agent work maps into Jarvis protocol records in a
way that developers understand, verify, and adopt without rewriting their
agents or moving host behavior into Jarvis.

## Inputs

Week 4 starts from:

- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../conformance/compatibility-mapping.md](../../conformance/compatibility-mapping.md)
- [../../conformance/existing-agent-proof-plan.md](../../conformance/existing-agent-proof-plan.md)
- [../../conformance/fixtures/README.md](../../conformance/fixtures/README.md)
- [../week-3/closeout.md](../week-3/closeout.md)
- [../../protocol/08-package-contracts.md](../../protocol/08-package-contracts.md)
- [../../protocol/14-protocol-lock.md](../../protocol/14-protocol-lock.md)
- [../../protocol/15-openapi-communication-binding.md](../../protocol/15-openapi-communication-binding.md)
- [../../protocol/16-positioning-adoption-lock.md](../../protocol/16-positioning-adoption-lock.md)

## Week 4 Outputs

Week 4 produces:

- compatible host mapping example
- existing-agent compatibility example
- public conformance checklist
- protocol record examples
- public README tightening
- public story note
- simulation OpenAPI proof-path update
- Week 4 closeout

## Chunk Plan

1. [chunk-1-execution-spec.md](./chunk-1-execution-spec.md)
   Lock Week 4 scope, gates, chunks, review lanes, and done state.
2. [chunk-2-compatible-host-mapping.md](./chunk-2-compatible-host-mapping.md)
   Define the host-shape mapping example from native human-agent work into
   Jarvis records.
3. [chunk-3-existing-agent-example.md](./chunk-3-existing-agent-example.md)
   Define the existing-agent compatibility example without adapter code or
   runtime ownership.
4. [chunk-4-public-conformance-checklist.md](./chunk-4-public-conformance-checklist.md)
   Publish the readable conformance checklist from the Week 3 fixtures and
   rejection gates.
5. [chunk-5-protocol-record-examples.md](./chunk-5-protocol-record-examples.md)
   Add concrete protocol record examples for the core collaboration loop.
6. [chunk-6-public-story-simulation.md](./chunk-6-public-story-simulation.md)
   Tighten public README language, public story, and simulation proof path.
7. [chunk-7-closeout.md](./chunk-7-closeout.md)
   Close Week 4 after checks, review, CodeRabbit, and public readiness pass.

## Done State

Week 4 is complete when:

- at least two host shapes map to equivalent Jarvis records
- one existing-agent example preserves native execution
- public conformance checklist links to fixture rejection gates
- protocol examples show WorkSession, Request, Review, Takeover, Contribution,
  EvidenceManifest, LearningRecord, MemoryProposal, SkillProposal, and
  OutcomeReport
- README explains Jarvis as protocol only
- simulation shows the OpenAPI proof path
- SDK language stays limited to protocol implementation helpers
- local checks pass
- automated and human review have no actionable comments

## Boundary

Jarvis owns protocol records, examples, conformance expectations, and public
protocol explanation.

Hosts own execution, storage, identity, UI, runtime behavior, model calls, tool
execution, billing, monitoring, workflow, adapters, wrappers, and deployment.

Week 4 strengthens Jarvis only when a change improves public protocol clarity,
compatibility proof, conformance readability, portable evidence, governed
learning, existing-agent adoption, or SDK boundary discipline.
