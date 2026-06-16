# Chunk 1: Fixture Architecture

Chunk 1 defines the Week 3 conformance fixture architecture.

This chunk does not create valid or invalid fixture files. Later chunks add
fixtures after this architecture is locked.

## Purpose

Conformance fixtures turn the OpenAPI contract into executable protocol proof.

Fixtures prove:

- a compatible implementation records the golden human-agent collaboration loop
- unsafe or incomplete records reject with the required protocol error id
- host-owned implementation details stay outside portable Jarvis records
- existing agent work maps into protocol objects without runtime ownership

## Fixture Directory

Week 3 fixture work uses this directory shape:

```txt
docs/conformance/fixtures/
  README.md
  valid/
    golden-path.json
  invalid/
    missing-protocol-version.json
    missing-actor.json
    unauthorized-actor.json
    missing-idempotency-key.json
    missing-request-timestamp.json
    stale-request-timestamp.json
    missing-expected-work-session-revision.json
    missing-previous-event-hash.json
    missing-policy-decision.json
    missing-review-resolution.json
    missing-takeover-resolution.json
    invalid-approval-scope.json
    stale-work-session-revision.json
    invalid-previous-event-hash.json
    stale-takeover-continuation.json
    invalid-evidence-export-state.json
    sealed-work-session-mutation.json
    sealed-evidence-mutation.json
    forbidden-host-private-export-field.json
    silent-memory-mutation.json
    silent-skill-activation.json
    outcome-report-without-learning-record.json
    unresolved-request.json
```

Chunk 3 opens `valid/`.
Chunk 4 opens `invalid/`.
Chunk 5 adds validator checks.

## Fixture Envelope

Every fixture uses one envelope:

```txt
fixture_id
protocol_version
kind
title
description
source_contract_refs
host_shape_ref
records
operations
assertions
expected_result
expected_error_id
expected_error_field
```

Rules:

- `fixture_id` is stable.
- `protocol_version` is `0.1`.
- `kind` is `valid` or `invalid`.
- `source_contract_refs` points to the protocol docs or OpenAPI components that
  define the behavior under test.
- `host_shape_ref` identifies the implementation shape used for compatibility
  mapping.
- `records` contains protocol records only.
- `operations` contains protocol operation attempts and required headers.
- `assertions` contains the expected protocol checks.
- `expected_result` is `pass` or `reject`.
- `expected_error_id` is present only when `expected_result` is `reject`.
- `expected_error_field` is present when the rejection belongs to a specific
  field.
- `host_shape_ref` never records host-private behavior.

## Operation Entry

Every operation entry records:

```txt
operation_id
method
path
headers
body_ref
actor_id
work_session_id
expected_status
expected_event_ref
expected_error_id
```

Rules:

- `operation_id`, `method`, `path`, `headers`, `actor_id`, and
  `expected_status` are required.
- `work_session_id` is present only for WorkSession-scoped operations.
- `body_ref` is present only when the operation has a request body.
- `expected_event_ref` is present only when an accepted operation creates or
  appends a JarvisEvent.
- `expected_error_id` is present only when the operation rejects.
- WorkSession-scoped mutations include all six zero-trust headers.
- Non-WorkSession mutations include the non-WorkSession mutation headers.
- Read operations include protocol version, actor id, and caller auth.
- Accepted WorkSession-scoped mutations link to the previous event hash.
- Rejected operations record the protocol error id.

## Assertion Classes

Fixtures use these assertion classes:

```txt
header_gate
actor_authority_gate
event_chain_gate
policy_decision_gate
request_resolution_gate
approval_scope_gate
takeover_epoch_gate
contribution_attribution_gate
evidence_export_gate
learning_governance_gate
host_private_boundary_gate
```

Each assertion records:

```txt
assertion_id
class
target_ref
required_state
expected_result
expected_error_id
```

Rules:

- `assertion_id`, `class`, `target_ref`, `required_state`, and
  `expected_result` are required.
- `expected_error_id` is present only when `expected_result` is `reject`.
- `target_ref` resolves to an operation, record, event, export item, or
  assertion dependency in the fixture.

## Valid Fixture Requirements

The golden-path fixture proves:

- HumanWorker and AgentWorker exist as Worker records
- HumanWorker and AgentWorker exist as Actor records
- WorkSession starts with objective, policy, revision, and event hash state
- AgentWorker action records PolicyDecision before accepted protocol state
- Policy-denied action creates scoped Request
- Review or Takeover resolves Request
- Review approval or narrowing creates bounded ApprovalScope
- Takeover records lock state before human direct control
- Contribution records attributable work
- EvidenceManifest exports portable proof
- LearningRecord captures human, agent, or pair learning
- MemoryProposal and SkillProposal keep durable learning governed
- OutcomeReport references LearningRecord without mutating sealed records

## Invalid Fixture Requirements

Invalid fixtures prove every required failure-mode rejection id:

- missing protocol version
- missing Actor header
- invalid Actor authority
- missing idempotency key
- missing request timestamp
- stale request timestamp
- missing expected WorkSession revision
- missing previous event hash
- missing PolicyDecision before AgentWorker state change
- missing Review resolution
- missing Takeover resolution
- invalid ApprovalScope
- stale WorkSession revision
- previous event hash mismatch
- stale Takeover continuation
- invalid EvidenceManifest export state
- sealed WorkSession mutation
- sealed EvidenceManifest mutation
- forbidden host-private export field
- silent memory mutation
- silent skill activation
- OutcomeReport without LearningRecord

Invalid fixtures also include an OpenAPI-backed unresolved Request fixture.

Each invalid fixture maps to one primary protocol error id.

## Validator Scope

The Week 3 validator checks:

- fixture envelope fields
- fixture ids
- protocol version
- operation headers
- operation entry field rules
- required records
- required assertions
- assertion entry field rules
- assertion target refs
- expected result
- expected error id
- required failure-mode coverage
- forbidden host-private export fields
- OpenAPI component names referenced by fixtures

The validator does not execute host behavior. It validates protocol fixture
shape, compatibility shape reference, and expected protocol outcome.

## Done Criteria

Chunk 1 is complete when:

- Week 3 execution spec exists
- all Week 3 chunks are named
- fixture directory shape is defined
- fixture envelope is defined
- assertion classes are defined
- validator scope is defined
- host-owned implementation remains outside the fixture architecture
