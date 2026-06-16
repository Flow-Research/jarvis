# Protocol Artifact Contracts

Jarvis v0.1 publishes protocol artifacts, not implementation packages.

OpenAPI 3.1 is the primary machine-readable communication contract. Supporting
artifacts exist only to keep the protocol readable, testable, and
implementable across compatible hosts.

## Artifact Boundary

Jarvis owns:

- OpenAPI 3.1 communication binding
- protocol object definitions
- protocol operation definitions
- protocol event envelope
- protocol error envelope
- portable EvidenceManifest export shape
- conformance checklists
- conformance fixtures
- examples

Hosts own:

- SDKs
- clients
- engines
- factories
- storage clients
- model clients
- tool clients
- cloud clients
- isolation libraries
- UI frameworks
- runtime adapters
- deployment packages

Jarvis artifacts MUST NOT expose implementation APIs, host service APIs,
storage clients, runtime adapters, or tool executors.

## OpenAPI Contract

The OpenAPI contract defines:

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

The OpenAPI contract is the canonical machine-readable artifact for:

- Worker
- Actor
- HumanWorker
- AgentWorker
- WorkSession
- JarvisEvent
- Policy
- PolicyDecision
- Request
- Review
- Takeover
- Contribution
- EvidenceManifest
- LearningRecord
- MemoryProposal
- SkillProposal
- OutcomeReport
- protocol headers
- protocol errors
- portable exports

Compatible implementations MUST preserve these object meanings, required
fields, state transitions, security headers, and error identifiers.

## Conformance Artifact

Conformance artifacts verify protocol behavior.

They do not prescribe infrastructure, runtime design, storage design, UI,
model calls, tool execution, isolation, or deployment.

Conformance checks include:

- WorkSession lifecycle
- PolicyDecision before accepted AgentWorker action
- policy-denied action creates Request
- Request resolves through Review or Takeover
- ApprovalScope stays bounded
- Takeover creates a lock epoch
- stale AgentWorker continuation is rejected after Takeover
- Contribution remains attributable
- EvidenceManifest references the WorkSession event chain
- forbidden host-private fields stay out of exports
- LearningRecord remains governed
- MemoryProposal cannot self-confirm from model or tool output
- SkillProposal cannot activate or expand tool access without review
- OutcomeReport creates or references LearningRecord without mutating sealed
  WorkSession or EvidenceManifest
- mutating operations enforce required protocol headers
- read operations enforce protocol version, host authentication, and Actor
  authority
- protocol errors use the required error envelope

## Example Artifact

Examples demonstrate valid protocol records and flows.

Examples MUST stay protocol-level. They show objects, operations, headers,
events, decisions, errors, and export records.

Examples MUST NOT define host storage tables, runtime APIs, tool clients, model
clients, connector behavior, secret-handling services, isolation rules, UI
screens, or deployment topology.

## Compatibility Rule

A host is Jarvis-compatible when it produces and consumes Jarvis protocol
records correctly.

Compatibility is proven by protocol behavior:

```txt
HumanWorker + AgentWorker
  -> WorkSession
  -> PolicyDecision
  -> Request when blocked
  -> Review or Takeover
  -> Contribution
  -> EvidenceManifest
  -> governed LearningRecord
```

Host implementation choices stay outside Jarvis.
