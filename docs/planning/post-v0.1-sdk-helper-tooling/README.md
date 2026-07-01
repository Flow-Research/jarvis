# Post-v0.1 SDK Helper Tooling Plan

Status: planned.

Jarvis v0.1.0 is released as Protocol Alpha. Post-v0.1 SDK helper tooling
starts after the protocol contract, OpenAPI binding, conformance fixtures,
examples, and release boundary are locked.

This plan covers GitHub issues #64 through #67.

Jarvis SDK work is protocol implementation helper work. It is not runtime
work, adapter work, wrapper work, host UI work, model orchestration work, tool
execution work, storage work, auth work, billing work, scoring work, payment
work, or deployment work.

## Goal

Make Jarvis v0.1.0 easier to implement without weakening the protocol
boundary.

SDK helper tooling must help compatible implementations:

- create protocol records
- validate protocol records
- prepare required protocol headers
- verify event envelope and hash-chain rules
- export EvidenceManifest records
- validate Request, Review, Takeover, LearningRecord, MemoryProposal, and
  SkillProposal records
- run conformance fixtures
- produce precise protocol errors

## Inputs

SDK helper tooling starts from:

- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../protocol/11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
- [../../protocol/12-request-protocol.md](../../protocol/12-request-protocol.md)
- [../../protocol/13-contribution-evidence-learning.md](../../protocol/13-contribution-evidence-learning.md)
- [../../protocol/14-protocol-lock.md](../../protocol/14-protocol-lock.md)
- [../../protocol/15-openapi-communication-binding.md](../../protocol/15-openapi-communication-binding.md)
- [../../conformance/checklist.md](../../conformance/checklist.md)
- [../../conformance/fixtures/README.md](../../conformance/fixtures/README.md)
- [../../releases/v0.1.0.md](../../releases/v0.1.0.md)

## Issue Mapping

| Issue | Chunk | Purpose |
| --- | --- | --- |
| #64 | [chunk-1-sdk-boundary-package-plan.md](./chunk-1-sdk-boundary-package-plan.md) | Lock SDK boundary, package shape, generator policy, and release gates. |
| #65 | [chunk-2-typescript-types-validators.md](./chunk-2-typescript-types-validators.md) | Define TypeScript protocol types, validators, helpers, and tests. |
| #66 | [chunk-3-python-types-validators.md](./chunk-3-python-types-validators.md) | Define Python protocol models, validators, helpers, and tests. |
| #67 | [chunk-4-conformance-runner-cli.md](./chunk-4-conformance-runner-cli.md) | Define conformance runner and protocol helper CLI. |

## Chunk Order

SDK helper tooling proceeds in this order:

```txt
1. SDK boundary and package plan
2. TypeScript protocol types and validators
3. Python protocol types and validators
4. conformance runner and protocol helper CLI
```

Chunk 1 must land before implementation work starts.

Chunks 2 and 3 start only after Chunk 1 locks the package boundary.

Chunk 4 starts after at least one validator surface proves the shared
validation shape.

## Review Lanes

Every SDK helper tooling chunk requires:

```txt
protocol-boundary review
OpenAPI contract review
conformance review
security and zero-trust review
developer-experience review
test review
wording review
```

The protocol-boundary review verifies that helper tooling does not become an
agent framework, runtime, adapter, wrapper, host SDK, model router, tool
executor, memory engine, UI kit, auth provider, storage backend, sandbox, or
workflow engine.

The OpenAPI contract review verifies exact alignment with
`docs/openapi/jarvis-openapi.yaml`.

The conformance review verifies fixture compatibility and rejection ids.

The security and zero-trust review verifies mutation headers, Actor headers,
Actor authority, WorkSession revision, previous event hash, idempotency,
timestamp, the PolicyDecision precondition for every AgentWorker action that
affects a WorkSession, and host-private field rejection.

The developer-experience review verifies that helpers are small, direct, and
usable by compatible implementations.

The test review verifies that valid and invalid protocol records are covered.

The wording review verifies direct protocol language.

## Required Checks

Every SDK helper tooling PR runs:

```txt
python3 scripts/check_conformance_fixtures.py
python3 scripts/check_openapi_contract.py
python3 scripts/check_markdown_links.py
python3 scripts/check_protocol_wording.py
python3 scripts/check_sdk_boundary.py
git diff --check
```

SDK package work also runs the package test command introduced by that package
before PR ready.

## Done State

SDK helper tooling planning is complete when:

- Chunk 1 locks allowed and rejected SDK surfaces.
- Chunk 2 defines TypeScript helper scope without runtime behavior.
- Chunk 3 defines Python helper scope without runtime behavior.
- Chunk 4 defines the conformance runner and helper CLI without host mutation.
- Roadmap entries point contributors to this plan.
- Local validation passes.

## Boundary

Jarvis owns protocol helper contracts, validation helpers, conformance runners,
protocol error helpers, EvidenceManifest helpers, event envelope helpers, and
hash-chain helpers.

Hosts own execution, storage, auth, UI, model calls, tool execution, memory
engines, queues, billing, monitoring, deployment, and host workflow.

Existing agents participate through protocol records without being rewritten as
Jarvis agents.
