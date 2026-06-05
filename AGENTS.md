# AGENTS.md

This repo is for Jarvis.

Jarvis is the human-agent collaboration and learning-loop protocol.

Jarvis defines how HumanWorkers and AgentWorkers coordinate inside
WorkSessions under shared goals and human-defined policy, create Requests when
blocked, capture Reviews and Takeovers from human judgment, record attributable
Contributions, export portable EvidenceManifest records, and carry governed
LearningRecords, MemoryProposals, and SkillProposals into future work.

This thesis is the source of truth for every agent, contributor, and maintainer
working in this repository.

## Non-Negotiable Boundary

Jarvis is not:

- a personal agent
- a chatbot
- an agent SDK
- an agent runtime
- a coding agent
- a cloud stack
- a sandbox
- a database
- an auth system
- a product UI
- Garden
- Workstream
- Harnessy
- MCP
- A2A
- AG-UI
- OpenAPI for generic HTTP APIs

Jarvis integrates with products, runtimes, agents, tools, and protocols. Jarvis
does not replace them.

## What Jarvis Owns

Jarvis owns the protocol contracts for:

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
- protocol event envelope
- portable export format
- OpenAPI 3.1 communication binding
- version negotiation
- capability negotiation
- extension rules
- protocol errors
- conformance expectations

## What Hosts Own

Hosts own implementation details.

That includes:

- product UI
- identity provider
- authentication
- authorization backend
- database
- queues
- cloud provider
- local execution
- sandbox implementation
- model provider
- tool execution
- billing
- deployment
- monitoring
- product-specific workflow

A host implements Jarvis. A host is not Jarvis.

## The Decision Test

Every change must pass this test:

```txt
Does this define how a human and an agent collaborate, request help, review
work, take over, record contribution, produce evidence, or learn together?
```

If yes, the change belongs in Jarvis.

If the change defines execution, UI, auth, storage, billing, cloud,
marketplace, runtime, model calls, or product workflow, it belongs outside
Jarvis.

## Core Thesis

The valuable unit is the human-agent team.

Not the human alone.
Not the agent alone.
Not the model.
Not the runtime.
Not the product.

The HumanWorker improves.
The AgentWorker improves.
The pair improves.
The next WorkSession carries confirmed learning forward.

## Protocol Shape

Jarvis v0 has five layers:

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

OpenAPI 3.1 is the primary machine-readable communication contract. Separate
schema-file packages are not the primary contract.

## Zero-Trust Requirement

Jarvis starts from zero trust.

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
current WorkSession revision, and links to the previous event hash.

Every AgentWorker action that affects a WorkSession records a PolicyDecision
before the action is accepted as protocol state.

Every export excludes product-private fields, credentials, secrets, raw runtime
state, host-only database ids, and deployment details.

## Current Execution Focus

The current focus is Week 1 protocol lock.

Work on:

- core object meanings
- required fields
- lifecycle states
- PolicyDecision semantics
- Request, Review, and Takeover lifecycle
- EvidenceManifest minimum export shape
- LearningRecord, MemoryProposal, and SkillProposal review states
- OutcomeReport semantics
- protocol positioning against MCP, A2A, ACP, AG-UI, and agent SDKs
- zero-trust OpenAPI headers, security schemes, and forbidden export fields

Do not start Garden POC work in this phase.
Do not build runtime features in this repo.
Do not add product-specific assumptions to protocol records.

## Wording Rules

Use direct protocol language.

Write:

```txt
Jarvis defines...
Jarvis owns...
Hosts own...
Compatible implementations MUST...
The protocol rejects...
```

Avoid advisory wording that makes locked protocol decisions sound optional.

Do not write this repo as a third-party review of Jarvis. Write it as the
source of truth for Jarvis.

## Required References

Before changing protocol direction, read:

- [README.md](./README.md)
- [docs/protocol/14-protocol-lock.md](./docs/protocol/14-protocol-lock.md)
- [docs/protocol/15-openapi-communication-binding.md](./docs/protocol/15-openapi-communication-binding.md)
- [docs/protocol/11-core-protocol-objects.md](./docs/protocol/11-core-protocol-objects.md)
- [docs/protocol/12-request-protocol.md](./docs/protocol/12-request-protocol.md)
- [docs/planning/12-30-day-roadmap.md](./docs/planning/12-30-day-roadmap.md)

## Change Discipline

Keep changes scoped.

Do not rename core objects without updating every protocol doc and roadmap
reference.

Do not add a new protocol object until its reason to exist is clear.

Do not add host-private fields to portable protocol records.

Do not weaken the boundary between Jarvis and host implementation.

Do not describe Jarvis as a personal agent, harness, runtime, product, or
framework.

Jarvis is the protocol for governed human-agent collaboration and shared
learning.
