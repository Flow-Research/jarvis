# Chunk 1: SDK Boundary And Package Plan

Issue: #64.

Chunk 1 locks the SDK helper boundary before TypeScript, Python, or CLI
implementation starts.

## Scope

This chunk defines:

- SDK purpose
- SDK non-goals
- allowed helper surfaces
- rejected helper surfaces
- TypeScript package scope
- Python package scope
- OpenAPI generation policy
- validator policy
- conformance runner policy
- versioning policy
- release checklist

This chunk does not create SDK implementation code.

## Required Output

Chunk 1 produces:

```txt
SDK boundary document
package plan
versioning plan
release checklist
implementation chunk gates
```

The output becomes the entry gate for #65, #66, and #67.

## SDK Purpose

A Jarvis SDK is a protocol implementation kit.

It helps compatible implementations create, validate, hash, export, and test
Jarvis protocol records.

## Accepted SDK Surfaces

SDK work is accepted only for:

- generated OpenAPI clients
- protocol types
- protocol record validators
- event envelope helpers
- event hash-chain helpers
- idempotency helpers
- mutation-header helpers
- read-header helpers
- EvidenceManifest helpers
- Request validators
- Review validators
- Takeover validators
- LearningRecord validators
- MemoryProposal validators
- SkillProposal validators
- conformance fixture runners
- protocol error helpers
- example record mappers

## Rejected SDK Surfaces

SDK work is rejected when it adds:

- agent runtime
- agent planner
- model router
- model orchestration
- tool executor
- memory engine
- host adapter
- wrapper
- host UI kit
- auth provider
- storage backend
- queue backend
- sandbox
- billing system
- scoring system
- payment system
- deployment system
- workflow engine

## Package Plan Requirements

The package plan MUST define:

- package names
- source layout
- generated-code policy
- hand-written helper policy
- test layout
- fixture import strategy
- release artifact names
- version labels
- compatibility statement
- deprecation policy

## Locked Package Decisions

Initial package names:

```txt
TypeScript package: @jarvis-protocol/sdk
Python package: jarvis-protocol
CLI package: @jarvis-protocol/cli
CLI command: jarvis
```

Initial source layout:

```txt
packages/typescript/src/generated
packages/typescript/src/validators
packages/typescript/src/headers
packages/typescript/src/events
packages/typescript/src/evidence
packages/typescript/tests
packages/typescript/fixtures/v0.1
packages/python/src/jarvis_protocol/generated
packages/python/src/jarvis_protocol/validators
packages/python/src/jarvis_protocol/headers
packages/python/src/jarvis_protocol/events
packages/python/src/jarvis_protocol/evidence
packages/python/tests
packages/python/fixtures/v0.1
packages/cli/src
packages/cli/tests
packages/cli/fixtures/v0.1
```

Generated-code policy:

- generated OpenAPI output lives only under `generated`
- generated files are not hand-edited
- hand-written helpers import generated types or models
- generator output changes require OpenAPI contract validation
- helper changes require package tests

Fixture import strategy:

- package tests read canonical fixtures from `docs/conformance/fixtures`
- release packages include fixture snapshots under `fixtures/v0.1`
- fixture snapshots preserve source refs to the canonical repository fixtures
- fixture updates require `python3 scripts/check_conformance_fixtures.py`

Release artifact names:

```txt
NPM: @jarvis-protocol/sdk
NPM: @jarvis-protocol/cli
PyPI: jarvis-protocol
CLI binary: jarvis
```

Version labels:

```txt
package release line: 0.1.x
supported protocol line: v0.1
supported OpenAPI artifact version: 0.1.0
supported fixture set: v0.1
release status: Protocol Alpha helper tooling
```

## Versioning Rules

SDK package versions MUST identify:

```txt
package version
supported Jarvis protocol version
supported OpenAPI artifact version
fixture set version
```

The first helper packages target:

```txt
Jarvis protocol line: v0.1
OpenAPI artifact version: 0.1.0
release status: Protocol Alpha
```

## Acceptance Criteria

Chunk 1 is complete when:

- SDK non-goals are explicit.
- accepted helper surfaces are explicit.
- rejected helper surfaces are explicit.
- TypeScript package scope is ready for #65.
- Python package scope is ready for #66.
- conformance runner scope is ready for #67.
- package versioning ties helpers to Jarvis v0.1 and OpenAPI 0.1.0.
- local validation passes.
- review lanes have no valid unresolved findings.

## Boundary

The SDK plan strengthens protocol implementation only.

The SDK plan does not authorize runtime, adapter, wrapper, host behavior,
model calls, tool execution, memory engines, UI, auth, storage, queues,
billing, scoring, payment, deployment, monitoring, observability, host
integration, or host workflow work inside Jarvis.
