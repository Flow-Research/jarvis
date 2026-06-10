# Chunk 2: WorkSession Lifecycle Lock

Chunk 2 locks the WorkSession state machine that Week 2 OpenAPI operations
encode.

This chunk does not create the OpenAPI document. It defines the protocol
lifecycle rules, state transitions, revision requirements, hash-chain
requirements, and export eligibility that OpenAPI must preserve.

## Scope

Chunk 2 locks:

```txt
WorkSession states
allowed transitions
rejected transitions
state-change event requirements
waiting_on_human blocker accounting
revision rules
event hash-chain rules
stale-write rejection
completion, failure, cancellation, and closure rules
export eligibility
```

## Non-Goals

Chunk 2 does not:

- define runtime execution
- define host storage
- define product workflow
- define host implementation behavior
- define queue behavior
- define model calls
- define billing, deployment, or monitoring
- change Request, Review, Takeover, Contribution, Evidence, or Learning
  semantics except where WorkSession lifecycle references them

## WorkSession States

Chunk 2 locks these WorkSession states:

```txt
created
active
waiting_on_human
takeover
reconciling
completed
failed
cancelled
closed
```

`created`, `active`, `waiting_on_human`, `takeover`, and `reconciling` are
mutable states.

`completed`, `failed`, and `cancelled` are terminal outcome states.

`closed` is the sealed archival state. It never transitions to another state.

## Required Transition Rules

Compatible implementations MUST enforce the transition table in
[04-work-sessions.md](../../protocol/04-work-sessions.md).

Every state change requires:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Every accepted state change records a JarvisEvent, increments `revision`, and
sets `last_event_hash` to the new event hash.

WorkSession creation starts from expected revision `0` and
`Jarvis-Previous-Event-Hash` equal to the protocol genesis hash. The start event
sets `JarvisEvent.previous_hash` to the same genesis hash.

Every transition out of `waiting_on_human` records
`blocked_scope_resolution_refs`. The refs prove that each blocked scope was
resolved, closed, transferred into Takeover, or recorded as an evidence
limitation.

## Rejection Rules

Compatible implementations reject:

```txt
missing_actor
missing_policy
missing_policy_decision
missing_objective
unknown_state
invalid_transition
stale_work_session_revision
invalid_previous_event_hash
missing_idempotency_key
duplicate_idempotency_key_mismatch
missing_jarvis_event
missing_blocked_scope_resolution_refs
missing_reconciliation_refs
mutation_after_closed
invalid_export_state
unauthorized_actor
```

## Export Rules

Final portable export is valid only from:

```txt
completed
failed
cancelled
closed
```

Export from `active`, `waiting_on_human`, `takeover`, or `reconciling` is an
interim host snapshot, not a final Jarvis EvidenceManifest export.

Export never includes product-private fields, credentials, secrets, raw runtime
state, host-only database ids, deployment details, billing data, private scores,
or product UI state.

## Reviewer Focus

Reviewers must verify:

- WorkSession states are named once and used consistently
- transition rules do not create hidden runtime ownership
- stale writes are rejected by revision and previous event hash
- every transition out of `waiting_on_human` accounts for blocked scopes
- `closed` is sealed
- terminal outcome states do not grant new authority
- export is only valid from permitted states
- the lifecycle supports human-agent collaboration without becoming product UI

## Done Criteria

Chunk 2 is complete when:

- [04-work-sessions.md](../../protocol/04-work-sessions.md) contains the locked
  state machine
- [11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
  lists the same WorkSession states
- [14-protocol-lock.md](../../protocol/14-protocol-lock.md) states the same
  lifecycle rules
- conformance and v0.1 docs mention invalid transition, stale revision, previous
  hash, and export eligibility checks
- local checks pass
- Zero-Trust Security Reviewer plus at least three other reviewer lanes pass
- valid findings are integrated
- rejected findings are recorded with concrete reasons
- PR is opened
