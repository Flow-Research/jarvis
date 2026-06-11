# Chunk 5: OpenAPI Security Entry Lock

Chunk 5 locks the OpenAPI security and negotiation inputs required before
Week 2 OpenAPI drafting starts.

This chunk does not create the OpenAPI YAML document. It defines the required
headers, security scheme requirements, protocol error model, version
negotiation rules, capability negotiation rules, extension namespace rules, and
forbidden export fields that the Week 2 OpenAPI contract must encode.

## Scope

Chunk 5 locks:

```txt
required mutating headers
read-operation header requirements
security scheme requirements
Actor authority requirements
Worker and Actor registration boundary
idempotency and replay requirements
WorkSession revision checks
previous event hash checks
PolicyDecision requirement
version negotiation
capability negotiation
extension namespace rules
protocol error envelope
protocol error ids
forbidden export fields
```

## Non-Goals

Chunk 5 does not:

- create OpenAPI YAML
- define auth provider implementation
- define identity storage
- define host account creation
- define host database schema
- define runtime execution
- define host implementation behavior
- define client SDK code

## Required Mutating Headers

Every WorkSession-scoped mutating protocol operation MUST include:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Compatible implementations MUST reject a WorkSession-scoped mutating request
when any required header is missing, invalid, stale, mismatched, replayed with
a different canonical payload, or outside timestamp tolerance.

Non-WorkSession protocol mutations MUST include:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
```

Worker registration, Actor registration, and OutcomeReport submission are
non-WorkSession protocol mutations. They MUST verify Actor authority,
idempotency, protocol version, and timestamp before state changes. They MUST
NOT require fake WorkSession revision or previous event hash values.

Jarvis timestamp tolerance is five minutes in the past and sixty seconds in the
future. Hosts MAY be stricter. Hosts MUST NOT be looser. Requests outside
tolerance reject as `stale_request_timestamp`.

Operation header matrix:

```txt
WorkSession-scoped mutation
  HostAuth
  Jarvis-Protocol-Version
  Jarvis-Actor-Id
  Jarvis-Idempotency-Key
  Jarvis-Request-Timestamp
  Jarvis-Expected-WorkSession-Revision
  Jarvis-Previous-Event-Hash

Genesis WorkSession mutation
  HostAuth
  Jarvis-Protocol-Version
  Jarvis-Actor-Id
  Jarvis-Idempotency-Key
  Jarvis-Request-Timestamp
  Jarvis-Expected-WorkSession-Revision set to 0
  Jarvis-Previous-Event-Hash set to protocol genesis hash

Worker or Actor registration
  HostAuth
  Jarvis-Protocol-Version
  Jarvis-Actor-Id
  Jarvis-Idempotency-Key
  Jarvis-Request-Timestamp

OutcomeReport submission
  HostAuth
  Jarvis-Protocol-Version
  Jarvis-Actor-Id
  Jarvis-Idempotency-Key
  Jarvis-Request-Timestamp

WorkSession-scoped or export read
  HostAuth
  Jarvis-Protocol-Version
  Jarvis-Actor-Id
```

## Security Schemes

Jarvis OpenAPI MUST define security schemes without owning identity.

The OpenAPI contract MUST support:

```txt
HostAuth
  records that the host authenticated the caller without prescribing credential
  format, auth provider, token type, session store, or account system

ActorHeader
  identifies the protocol Actor for attribution and authority checks

ProtocolVersionHeader
  selects the Jarvis protocol version

IdempotencyHeader
  protects mutation replay

RequestTimestampHeader
  rejects stale mutation requests

RevisionHeader
  protects WorkSession optimistic concurrency

PreviousHashHeader
  protects event-chain continuity
```

Authentication proves caller identity to the host. Authorization verifies that
`Jarvis-Actor-Id` has authority for the protocol operation. Jarvis records the
Actor. Jarvis does not own the host identity provider.

## Negotiation Rules

Version negotiation uses:

```txt
Jarvis-Protocol-Version
```

Capability negotiation uses:

```txt
Jarvis-Host-Capabilities
Jarvis-Required-Capabilities
```

Extension negotiation uses:

```txt
Jarvis-Extensions
```

Unsupported required capability rejects as `unsupported_capability`.

Unknown optional capability is ignored unless it changes a core field meaning.

Extensions MUST be namespaced and MUST NOT override core fields.
Invalid extension namespace rejects as `invalid_extension_namespace`. Extension
core field override rejects as `extension_core_field_override`.

## Read Operation Headers

Read operations that return WorkSession-scoped records or portable exports MUST
include caller authentication and:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
```

Compatible implementations MUST verify that `Jarvis-Actor-Id` has authority to
read the requested protocol record.

Read operations MAY include:

```txt
Jarvis-Required-Capabilities
Jarvis-Extensions
```

Read operations MUST NOT require mutation-only idempotency, expected revision,
or previous event hash headers.

## Protocol Error Envelope

Every protocol error response MUST include:

```txt
error_id
protocol_version
object_type
field
reason
remediation
trace_id
```

When `Jarvis-Protocol-Version` is missing, `protocol_version` records the
server-selected error contract version. When `Jarvis-Protocol-Version` is
unsupported, `protocol_version` records the rejected version and remediation
points to supported versions.

The error response MUST NOT include credentials, secrets, raw runtime state,
host-only database ids, deployment details, billing data, private scores, or
UI state, raw auth tokens, provider secrets, session cookies, or
private keys.

## Forbidden Export Fields

Portable protocol export MUST exclude:

```txt
host-private fields
credentials
secrets
raw runtime state
host-only database ids
deployment details
billing data
private scores
UI state
raw auth tokens
provider secrets
session cookies
private keys
```

## Done Criteria

Chunk 5 is complete when:

- [15-openapi-communication-binding.md](../../protocol/15-openapi-communication-binding.md)
  locks headers, security schemes, negotiation, error envelope, and forbidden
  export fields
- [08-package-contracts.md](../../protocol/08-package-contracts.md) includes
  release tests for required headers, security schemes, negotiation,
  extension namespace rules, protocol errors, and forbidden export fields
- [10-protocol-mvp.md](../../protocol/10-protocol-mvp.md) includes
  conformance checks for OpenAPI security entry rules
- [docs/reviews/acceptance-criteria.md](../../reviews/acceptance-criteria.md)
  includes acceptance checks for the same rules
- local checks pass
- Zero-Trust Security Reviewer plus at least three other reviewer lanes pass
- valid findings are integrated
- rejected findings are recorded with concrete reasons
- PR is opened
