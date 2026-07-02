# @jarvis-protocol/sdk

Status: Protocol Alpha helper package.

This package provides TypeScript helpers for Jarvis v0.1 protocol records.

Accepted surfaces:

- generated OpenAPI component types
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

## Public Helpers

The package exports:

- OpenAPI-derived TypeScript declarations for every v0.1 component schema
- `validateMutationHeaders`
- `validateReadHeaders`
- `validateProtocolRecord`
- `validateRequest`
- `validateReview`
- `validateTakeover`
- `validateContribution`
- `validateEvidenceManifest`
- `validateLearningRecord`
- `validateMemoryProposal`
- `validateSkillProposal`
- `validateOutcomeReport`
- `validateFixture`
- `validateEventHashChain`
- `canonicalizeProtocolValue`
- `hashProtocolValue`
- `protocolError`

The package also exports `./package.json` and `./fixtures/v0.1/*` subpaths so
compatible implementations can read package metadata and v0.1 fixture snapshots
from the installed package.

## Local Checks

Run:

```sh
npm --workspace @jarvis-protocol/sdk test
python3 scripts/check_sdk_boundary.py
```

`validateFixture` checks the v0.1 fixture snapshots shipped with this package.
The package rejects invalid protocol records with OpenAPI `ProtocolError`
envelopes.
