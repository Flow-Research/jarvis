# Week 3: Protocol Compatibility Mapping And Conformance Fixtures

Week 3 proved the Week 2 OpenAPI contract through protocol compatibility
mapping and conformance fixtures.

Status: complete.

Week 3 does not build adapters, wrappers, host runtimes, UI, model calls, tool
execution, storage, auth, billing, scoring, payment, or deployment behavior.

Jarvis records the protocol proof. Hosts provide the implementation.

## Goal

Prove that existing human-agent work maps into Jarvis protocol records without
rewriting the agent runtime or moving host behavior into Jarvis.

## Inputs

Week 3 started from:

- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../conformance/golden-path.md](../../conformance/golden-path.md)
- [../../conformance/failure-modes.md](../../conformance/failure-modes.md)
- [../week-2/closeout.md](../week-2/closeout.md)
- [../../protocol/14-protocol-lock.md](../../protocol/14-protocol-lock.md)
- [../../protocol/15-openapi-communication-binding.md](../../protocol/15-openapi-communication-binding.md)

## Week 3 Outputs

Week 3 produced:

- protocol compatibility mapping rules
- fixture architecture
- valid conformance fixtures
- invalid conformance fixtures
- fixture validator checks
- existing-agent compatibility proof plan
- Week 3 closeout

## Chunk Plan

1. [chunk-1-fixture-architecture.md](./chunk-1-fixture-architecture.md)
   Define Week 3 execution, fixture architecture, fixture envelope, assertion
   classes, and validator scope.
2. [chunk-2-compatibility-mapping.md](./chunk-2-compatibility-mapping.md)
   Define how existing human-agent work maps into Jarvis protocol records.
3. [chunk-3-golden-path-fixture.md](./chunk-3-golden-path-fixture.md)
   Add the valid golden-path fixture.
4. [chunk-4-failure-fixtures.md](./chunk-4-failure-fixtures.md)
   Add invalid fixtures for required rejection paths.
5. [chunk-5-fixture-validator.md](./chunk-5-fixture-validator.md)
   Add validator checks for fixture structure and expected protocol outcomes.
6. [chunk-6-existing-agent-proof-plan.md](./chunk-6-existing-agent-proof-plan.md)
   Define the existing-agent compatibility proof plan without adapter code.
7. [chunk-7-closeout.md](./chunk-7-closeout.md)
   Close Week 3 and define readiness for compatible examples.

For closeout, see [closeout.md](./closeout.md).

## Done State

Week 3 is complete when:

- valid fixtures prove the golden path
- invalid fixtures prove required rejection ids
- compatibility mapping preserves host-owned execution
- fixture validation runs locally
- two host shapes map to equivalent Jarvis records on paper
- compatible examples stay behind the conformance gate

## Boundary

Jarvis owns protocol records and conformance expectations.

Hosts own execution, storage, identity, UI, runtime behavior, model calls, tool
execution, billing, monitoring, and workflow.

Week 3 strengthens Jarvis only when a change improves compatibility mapping,
fixture correctness, conformance rejection, portable evidence, or governed
learning.
