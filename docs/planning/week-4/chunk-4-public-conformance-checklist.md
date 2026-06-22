# Chunk 4: Public Conformance Checklist

Chunk 4 turns Week 3 fixtures and rejection gates into a readable public
conformance checklist.

## Scope

This chunk publishes the compatibility rules a developer uses to understand
whether an implementation follows Jarvis.

This chunk does not add new protocol objects, new OpenAPI paths, new fixture
classes, runtime behavior, adapter code, SDK code, host behavior, UI, storage,
auth, billing, scoring, payment, or deployment behavior.

## Required Output

Chunk 4 creates or updates:

```txt
docs/conformance/checklist.md
```

The checklist covers:

```txt
participant records
WorkSession source of truth
PolicyDecision before accepted AgentWorker state
Request for blocked scope
Review and Takeover resolution
ApprovalScope bounds
Takeover stale-continuation rejection
Contribution attribution
EvidenceManifest source refs
forbidden host-private export fields
governed LearningRecord
MemoryProposal review state
SkillProposal review state
OutcomeReport feedback hook
mutation headers
event hash chain
protocol error envelope
unsupported capability behavior
```

## Required Rejection Coverage

The checklist covers these Week 3 rejection classes and links fixture-backed
classes to the current valid and invalid fixtures:

```txt
missing protocol version
missing Actor
unauthorized Actor
missing idempotency key
missing request timestamp
stale request timestamp
missing expected WorkSession revision
stale WorkSession revision
missing previous event hash
invalid previous event hash
missing policy
missing PolicyDecision
unresolved Request
missing Review resolution
missing Takeover resolution
invalid ApprovalScope
stale Takeover epoch
missing reconciliation refs
invalid EvidenceManifest export state
sealed WorkSession mutation
sealed EvidenceManifest mutation
missing Contribution actor
invalid contributor refs
shared Contribution without individual refs
evidence after the fact
missing evidence event refs
forbidden host-private field
silent memory mutation
silent skill activation
OutcomeReport without LearningRecord
```

The checklist names additional `ProtocolErrorId` values separately as
non-fixture-backed rejection ids. It MUST NOT describe those ids as fixture
links unless fixtures are added.

```txt
unsupported protocol version
duplicate idempotency mismatch
invalid event hash
missing objective
duplicate contributor ref
duplicate evidence item ref
unsupported capability
```

## Public Format

The checklist uses direct conformance language:

```txt
Compatible implementations MUST...
The protocol rejects...
The export excludes...
The record preserves...
```

## Review Focus

Review verifies:

- checklist matches current fixtures
- rejection ids match OpenAPI error ids
- no host behavior becomes protocol behavior
- checklist is readable by public implementers
- wording remains direct

## Done Criteria

Chunk 4 is complete when:

- public checklist exists
- checklist references valid and invalid fixtures
- every Week 3 rejection class appears
- local checks pass
- internal reviewer lanes have no valid unresolved findings
- CodeRabbit has no valid unresolved findings
