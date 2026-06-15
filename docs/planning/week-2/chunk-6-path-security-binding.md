# Week 2 Chunk 6: Path And Security Binding

## Goal

Encode the OpenAPI path layout, operation buckets, required protocol headers,
security scheme, and header parameters that make Jarvis v0.1 exchangeable
between compatible hosts.

## Scope

This chunk locks:

- `components.parameters`
- `components.headers`
- `components.requestBodies`
- `components.responses`
- `components.securitySchemes` for caller authentication
- WorkSession-scoped mutation header requirements
- genesis WorkSession mutation header requirements
- non-WorkSession mutation header requirements
- WorkSession-scoped read and export header requirements
- operation path layout for the v0.1 core operations
- request body schemas for the v0.1 core operations
- success response schema refs for the v0.1 core operations
- `ProtocolError` response schema
- protocol error rejection ids required by the security and operation binding
- validator checks for the path/header/security matrix

This chunk defines these operations:

```txt
PUT  /workers/{worker_id}
PUT  /actors/{actor_id}
POST /work-sessions
GET  /work-sessions/{work_session_id}
POST /work-sessions/{work_session_id}/events
POST /work-sessions/{work_session_id}/policy-decisions
POST /work-sessions/{work_session_id}/requests
POST /work-sessions/{work_session_id}/reviews
POST /work-sessions/{work_session_id}/takeovers
POST /work-sessions/{work_session_id}/contributions
POST /work-sessions/{work_session_id}/learning-records
POST /work-sessions/{work_session_id}/memory-proposals
POST /work-sessions/{work_session_id}/skill-proposals
GET  /work-sessions/{work_session_id}/export
POST /outcome-reports
```

This chunk does not define behavior outside the path and security binding.
Chunk 7 locked examples and conformance entry. Week 3 handles protocol
compatibility mapping and conformance fixtures.

## Header Classes

WorkSession-scoped mutating operations require:

```txt
HostAuth
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Genesis WorkSession mutation is `POST /work-sessions`. It requires the same
headers as WorkSession-scoped mutations. `Jarvis-Expected-WorkSession-Revision`
is `0`. `Jarvis-Previous-Event-Hash` is the protocol genesis hash.

Non-WorkSession mutations require:

```txt
HostAuth
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
```

Worker registration, Actor registration, and OutcomeReport submission are
non-WorkSession mutations. They do not require
`Jarvis-Expected-WorkSession-Revision` or `Jarvis-Previous-Event-Hash`.

WorkSession-scoped reads and export reads require:

```txt
HostAuth
Jarvis-Protocol-Version
Jarvis-Actor-Id
```

Reads do not require `Jarvis-Idempotency-Key`,
`Jarvis-Expected-WorkSession-Revision`, or `Jarvis-Previous-Event-Hash`.

## Files

- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../openapi/README.md](../../openapi/README.md)
- [../../../scripts/check_openapi_skeleton.py](../../../scripts/check_openapi_skeleton.py)

## Acceptance

Chunk 6 is complete when:

- every v0.1 operation path exists in `paths`
- every operation has a stable `operationId`
- every operation has the correct tag
- every operation uses `HostAuth`
- `components.securitySchemes` defines `HostAuth`
- `components.parameters` defines `ActorHeader`, `ProtocolVersionHeader`,
  `IdempotencyHeader`, `RequestTimestampHeader`, `RevisionHeader`, and
  `PreviousHashHeader`
- WorkSession-scoped mutations require all six Jarvis protocol headers
- WorkSession-scoped mutation operations use `HostAuth` and all required
  protocol header parameters
- `POST /work-sessions` requires expected revision `0` and protocol genesis
  hash semantics through header descriptions
- Worker registration, Actor registration, and OutcomeReport submission require
  only the non-WorkSession mutation header set
- non-WorkSession mutation operations omit `RevisionHeader` and
  `PreviousHashHeader`
- WorkSession-scoped reads and export reads require only caller auth,
  `Jarvis-Protocol-Version`, and `Jarvis-Actor-Id`
- read and export operations use `HostAuth`, `ProtocolVersionHeader`, and
  `ActorHeader`
- mutation-only headers are absent from read operations
- WorkSession revision and previous event hash headers are absent from
  non-WorkSession mutations
- request bodies reference the locked protocol object schemas
- success responses reference the locked protocol object schemas
- protocol errors use the locked `ProtocolError` envelope
- protocol security rejection ids include `missing_protocol_version`,
  `unsupported_protocol_version`, `missing_actor`, `missing_idempotency_key`,
  `missing_request_timestamp`, `stale_request_timestamp`,
  `missing_expected_work_session_revision`, `stale_work_session_revision`,
  `missing_previous_event_hash`, `invalid_previous_event_hash`,
  `invalid_event_hash`, `duplicate_idempotency_key_mismatch`, and
  `unauthorized_actor`
- protocol error responses exclude forbidden host-private fields
- local validation passes

## Boundary

This chunk defines how compatible hosts exchange Jarvis protocol records over
HTTP. It does not define how hosts authenticate callers, store records, execute
agents, run tools, manage queues, render UI, bill usage, deploy services, or
score outcomes.
