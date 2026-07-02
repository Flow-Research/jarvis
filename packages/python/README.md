# jarvis-protocol

Status: Protocol Alpha helper tooling.

This package provides Python helpers for Jarvis v0.1 protocol records. It
implements the protocol-helper surface for compatible implementations that need
OpenAPI-derived models, validation helpers, event hashing, EvidenceManifest
checks, and conformance fixture checks.

Accepted surfaces:

- protocol models generated from the OpenAPI contract
- protocol record validators
- mutation-header helpers
- read-header helpers
- event envelope helpers
- event hash-chain helpers
- EvidenceManifest helpers
- Request, Review, and Takeover validators
- LearningRecord, MemoryProposal, and SkillProposal validators
- protocol error helpers
- example record mappers

Rejected surfaces:

- agent runtime
- model router
- tool executor
- host adapter
- wrapper
- UI kit
- auth provider
- storage backend
- memory engine
- sandbox
- billing system
- scoring system
- payment system
- deployment system
- host workflow engine

## Public Surface

The package root exports:

- generated OpenAPI schema metadata
- generated `TypedDict` and `Literal` model names under
  `jarvis_protocol.generated.openapi_types`
- `protocol_error`
- `validate_mutation_headers`
- `validate_read_headers`
- `validate_operation_headers`
- `validate_protocol_record`
- `validate_fixture`
- `validate_event_hash_chain`
- `canonicalize_protocol_value`
- `hash_protocol_value`
- `find_forbidden_host_private_field`

## Local Validation

Run Python package tests from the repository root:

```bash
npm run test:python
```

The package tests load the v0.1 fixture snapshots under `fixtures/v0.1` and
verify that the Python validators accept the golden path and reject every
invalid fixture with the expected protocol error id. The test command also
builds the wheel and sdist, installs the wheel into a temporary target, and
verifies importable package resources through `importlib.resources`.
