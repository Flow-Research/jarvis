# OpenAPI Communication Binding

Jarvis uses OpenAPI 3.1 as the primary machine-readable communication
contract.

Jarvis is a protocol. A protocol needs shared objects, shared operations, and a
shared communication binding. OpenAPI gives Jarvis the HTTP contract that hosts,
adapters, products, and external systems implement.

## Decision

Jarvis v0 uses this structure:

```txt
Layer 1: Protocol semantics
  HumanWorker + AgentWorker collaboration and learning loop

Layer 2: Protocol objects
  WorkSession, Policy, Request, Review, Takeover, Contribution,
  EvidenceManifest, LearningRecord, MemoryProposal, SkillProposal

Layer 3: Protocol operations
  create WorkSession, append event, create Request, record Review,
  start Takeover, reconcile Takeover, record Contribution,
  export EvidenceManifest, submit OutcomeReport

Layer 4: OpenAPI 3.1 communication binding
  HTTP paths, operations, parameters, request bodies, response bodies,
  component schemas, security schemes, errors, examples

Outside Jarvis: Host implementation
  product workspace, CLI adapter, local host, external agent product,
  enterprise host
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
and computers discover and implement without reading source code. Jarvis needs
that property for adoption.

Primary references:

- OpenAPI 3.1.1: https://spec.openapis.org/oas/v3.1.1.html
- MCP transports: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
- A2A specification: https://github.com/a2aproject/A2A/blob/main/docs/specification.md
- AGNTCY ACP specification: https://github.com/agntcy/acp-spec

## OpenAPI Contract Shape

The v0 OpenAPI document owns:

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

Every mutating operation requires:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Every accepted state change records the Actor, verifies authority, checks the
current WorkSession revision, and links to the previous event hash. Every
AgentWorker action that affects a WorkSession also records a PolicyDecision
before the action is accepted as protocol state.

Every export excludes product-private fields, credentials, secrets, raw runtime
state, database ids that only the host understands, and deployment details.

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

Unsupported capability produces a protocol error. Extension fields are
namespaced and never change the meaning of core fields.

## Error Model

Jarvis OpenAPI defines protocol errors for:

```txt
invalid_transition
missing_actor
missing_policy
policy_denied
request_unresolved
review_required
stale_takeover_epoch
invalid_event_hash
invalid_export
unsupported_capability
forbidden_host_private_field
```

Errors are structured. The error body names the protocol object, field, reason,
and remediation path.

## This Week's Work

This week locks the communication strategy:

```txt
1. OpenAPI 3.1 is the v0 machine-readable contract.
2. components.schemas contains protocol objects.
3. paths contains protocol operations.
4. securitySchemes and headers define zero-trust host requirements.
5. examples and conformance fixtures come after the OpenAPI shape is locked.
6. Garden POC waits until protocol semantics, OpenAPI contract, and conformance
   entry rules are stable.
```
