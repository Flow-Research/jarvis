# OpenAPI Communication Binding

Jarvis uses OpenAPI 3.1 as the primary machine-readable communication
contract.

Jarvis is a protocol. A protocol needs shared objects, shared operations, and a
shared communication binding. OpenAPI gives Jarvis the HTTP contract that hosts
and external systems implement.

## Decision

Jarvis v0.1 uses this structure:

```txt
Layer 1: Protocol semantics
  HumanWorker + AgentWorker collaboration and learning loop

Layer 2: Protocol objects
  Worker, Actor, HumanWorker, AgentWorker, WorkSession, JarvisEvent,
  Policy, PolicyDecision, Request, Review, Takeover, Contribution,
  EvidenceManifest, LearningRecord, MemoryProposal, SkillProposal,
  OutcomeReport

Layer 3: Protocol operations
  create WorkSession, append event, create Request, record Review,
  start Takeover, reconcile Takeover, record Contribution,
  export EvidenceManifest, submit OutcomeReport

Layer 4: OpenAPI 3.1 communication binding
  HTTP paths, operations, parameters, request bodies, response bodies,
  component schemas, security scheme, header parameters, errors, examples

Outside Jarvis: Host implementation
  UI, auth, storage, execution, deployment, model calls, and tool execution
```

OpenAPI 3.1 is the contract. Separate schema-file packages are not the primary
contract.

## Research Grounding

MCP uses JSON-RPC for message encoding across stdio and Streamable HTTP. That
fits tool invocation and bidirectional client-server sessions. Jarvis records
human-agent collaboration and evidence. Jarvis does not copy MCP's JSON-RPC
shape.

A2A separates the protocol into data model, operations, and bindings. Its
specification includes JSON-RPC, gRPC, and HTTP+JSON/REST bindings. Jarvis
keeps the same discipline: semantics first, operations second, binding third.

AGNTCY Agent Connect Protocol specifies a standard remote-agent interface with
OpenAPI. It exposes agents, descriptors, runs, threads, interrupts, output
retrieval, and errors through a REST-based OpenAPI contract. Jarvis uses that
lesson for its host-facing communication binding.

OpenAPI 3.1 defines a standard interface description for HTTP APIs that humans
and computers discover and implement without reading source code. OpenAPI 3.1
provides the discoverable HTTP contract that compatible implementations use
without reading source code.

Primary references:

- OpenAPI 3.1.1: https://spec.openapis.org/oas/v3.1.1.html
- MCP transports: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports
- A2A specification: https://a2a-protocol.org/latest/specification/
- AGNTCY ACP specification: https://spec.acp.agntcy.org/

## OpenAPI Contract Shape

The v0.1 OpenAPI document owns:

```txt
info
servers
security
tags
paths
components.schemas
components.parameters
components.responses
components.securitySchemes
components.examples
```

The `components.schemas` section defines the protocol objects. The `paths`
section defines how hosts exchange those objects.

OpenAPI authors MUST NOT add host implementation fields, auth-provider fields,
database ids, runtime ids, billing fields, UI state, or deployment
details to core protocol schemas.

## Core Operations

The first OpenAPI binding defines these operations:

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

Worker and Actor operations register protocol references. They do not create
accounts, authenticate users, issue credentials, or own identity storage.

Worker and Actor registration rules:

```txt
Worker registration records protocol participant refs.
Actor registration records protocol authority refs.
Registration does not create host accounts.
Registration does not authenticate callers.
Registration does not issue credentials.
Registration does not define identity storage.
```

The operations are protocol operations. They do not define how the host runs the
agent, stores records, authenticates users, bills customers, renders UI, or
deploys infrastructure.

## Security Model

Jarvis OpenAPI starts from zero trust.

The contract defines:

```txt
authenticated caller
authorized actor
idempotency key
protocol version header
capability declaration
policy decision requirement
request/review resolution rules
takeover lock epoch
event hash chain
portable export boundary
forbidden host-private fields
```

Every WorkSession-scoped mutating operation requires:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Required WorkSession-scoped mutating header semantics:

```txt
Jarvis-Protocol-Version
  selects the Jarvis protocol version used by the request

Jarvis-Actor-Id
  identifies the protocol Actor whose authority is checked and recorded

Jarvis-Idempotency-Key
  protects mutation replay for the same Actor, operation, protocol version, and
  canonical payload

Jarvis-Request-Timestamp
  rejects stale or replayed requests outside protocol timestamp tolerance

Jarvis-Expected-WorkSession-Revision
  protects WorkSession optimistic concurrency

Jarvis-Previous-Event-Hash
  links the accepted mutation to the current WorkSession event chain
```

Missing or invalid mutating headers reject the request before protocol state
changes.

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
  requires HostAuth
  requires Jarvis-Protocol-Version
  requires Jarvis-Actor-Id
  requires Jarvis-Idempotency-Key
  requires Jarvis-Request-Timestamp
  requires Jarvis-Expected-WorkSession-Revision
  requires Jarvis-Previous-Event-Hash

Genesis WorkSession mutation
  requires HostAuth
  requires Jarvis-Protocol-Version
  requires Jarvis-Actor-Id
  requires Jarvis-Idempotency-Key
  requires Jarvis-Request-Timestamp
  requires Jarvis-Expected-WorkSession-Revision set to 0
  requires Jarvis-Previous-Event-Hash set to protocol genesis hash

Worker or Actor registration
  requires HostAuth
  requires Jarvis-Protocol-Version
  requires Jarvis-Actor-Id
  requires Jarvis-Idempotency-Key
  requires Jarvis-Request-Timestamp
  does not require Jarvis-Expected-WorkSession-Revision
  does not require Jarvis-Previous-Event-Hash

OutcomeReport submission
  requires HostAuth
  requires Jarvis-Protocol-Version
  requires Jarvis-Actor-Id
  requires Jarvis-Idempotency-Key
  requires Jarvis-Request-Timestamp
  does not require Jarvis-Expected-WorkSession-Revision
  does not require Jarvis-Previous-Event-Hash

WorkSession-scoped or export read
  requires HostAuth
  requires Jarvis-Protocol-Version
  requires Jarvis-Actor-Id
  does not require Jarvis-Idempotency-Key
  does not require Jarvis-Expected-WorkSession-Revision
  does not require Jarvis-Previous-Event-Hash
```

Read operations that return WorkSession-scoped records or portable exports MUST
include host authentication and:

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

Every accepted WorkSession-scoped state change records the Actor, verifies
authority, checks the current WorkSession revision, and links to the previous
event hash. Every AgentWorker action that affects a WorkSession also records a
PolicyDecision before the action is accepted as protocol state.

Jarvis defines `POST /work-sessions` as the genesis WorkSession mutation.
Compatible implementations MUST use expected revision `0` and the protocol
genesis hash as `Jarvis-Previous-Event-Hash`. They MUST require actor
authority, idempotency, timestamp, and protocol version before accepting the
creation event.

Every export excludes host-private fields, credentials, secrets, raw runtime
state, database ids that only the host understands, deployment details, billing
data, private scores, and UI state.

Forbidden export fields include:

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

## Security Scheme And Header Parameters

Jarvis OpenAPI MUST define the host authentication security scheme without
owning identity. Jarvis protocol headers MUST be reusable OpenAPI parameters,
not OpenAPI security schemes.

Required security scheme:

```txt
HostAuth
  records that the host authenticated the caller without prescribing credential
  format, auth provider, token type, session store, or account system
```

Required header parameters:

```txt
ActorHeader
  binds the request to `Jarvis-Actor-Id`

ProtocolVersionHeader
  binds the request to `Jarvis-Protocol-Version`

IdempotencyHeader
  binds the request to `Jarvis-Idempotency-Key`

RequestTimestampHeader
  binds the request to `Jarvis-Request-Timestamp`

RevisionHeader
  binds the request to `Jarvis-Expected-WorkSession-Revision`

PreviousHashHeader
  binds the request to `Jarvis-Previous-Event-Hash`
```

Optional negotiation header parameters:

```txt
RequiredCapabilitiesHeader
  binds the request to `Jarvis-Required-Capabilities`

ExtensionsHeader
  binds the request to `Jarvis-Extensions`
```

Authentication proves caller identity to the host. Authorization verifies that
`Jarvis-Actor-Id` has authority for the requested protocol operation. Jarvis
records the Actor and authority check result. Jarvis does not own the host
identity provider, auth backend, session store, or account system.

## Version And Capability Negotiation

OpenAPI defines the static contract. Protocol compatibility still uses explicit
version, capability, and extension fields.

Jarvis uses:

```txt
Jarvis-Protocol-Version
Jarvis-Host-Capabilities
Jarvis-Required-Capabilities
Jarvis-Extensions
```

Version negotiation rules:

```txt
Unsupported Jarvis-Protocol-Version rejects the request.
Compatible minor version proceeds only when required capabilities match.
Compatible implementations MUST NOT silently downgrade a request.
A caller requests an older supported version only by explicitly setting
Jarvis-Protocol-Version to that version.
```

Capability negotiation rules:

```txt
Jarvis-Host-Capabilities declares supported optional capabilities.
Jarvis-Required-Capabilities declares capabilities required by the caller.
Unsupported required capability rejects as unsupported_capability.
Unknown optional capability is ignored unless it changes a core field meaning.
```

Extension rules:

```txt
Jarvis-Extensions declares extension namespaces.
Extension fields MUST be namespaced.
Extension fields MUST NOT override core field names.
Extension fields MUST NOT change the meaning of core fields.
Extension fields MUST NOT contain forbidden export fields.
Invalid extension namespace rejects as invalid_extension_namespace.
Extension core field override rejects as extension_core_field_override.
```

## Error Model

Jarvis OpenAPI defines protocol errors for:

```txt
invalid_transition
unknown_state
missing_protocol_version
unsupported_protocol_version
missing_request_timestamp
stale_request_timestamp
missing_expected_work_session_revision
missing_previous_event_hash
stale_work_session_revision
missing_idempotency_key
missing_actor
invalid_extension_namespace
extension_core_field_override
missing_policy
missing_policy_decision
missing_objective
policy_denied
request_unresolved
review_required
invalid_request_transition
missing_review_resolution
missing_takeover_resolution
invalid_approval_scope
approval_scope_expired
approval_scope_mismatch
stale_takeover_epoch
invalid_event_hash
invalid_previous_event_hash
duplicate_idempotency_key_mismatch
request_livelock
duplicate_request_mismatch
missing_jarvis_event
missing_blocked_scope_resolution_refs
missing_reconciliation_refs
mutation_after_closed
unauthorized_actor
invalid_export
invalid_export_state
invalid_evidence_export_state
missing_contribution_actor
invalid_contributor_refs
shared_contribution_without_individual_refs
evidence_after_the_fact
missing_evidence_event_refs
forbidden_export_field
silent_memory_mutation
silent_skill_activation
model_self_confirmed_memory
tool_self_confirmed_memory
skill_expands_tool_access_without_policy_review
sealed_work_session_mutation
sealed_evidence_mutation
outcome_report_without_learning_record
unsupported_capability
forbidden_host_private_field
```

Errors are structured.

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

Error responses MUST NOT include credentials, secrets, raw runtime state,
host-only database ids, deployment details, billing data, private scores,
UI state, raw auth tokens, provider secrets, session cookies, or
private keys.

## Contract Sequence

The OpenAPI contract is locked in this sequence:

```txt
1. OpenAPI 3.1 is the v0.1 machine-readable contract.
2. components.schemas contains protocol objects.
3. paths contains protocol operations.
4. securitySchemes and headers define zero-trust host requirements.
5. examples and conformance fixtures come after the OpenAPI shape is locked.
6. Host implementations stay outside the protocol contract.
```
