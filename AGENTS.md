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

Jarvis v0.1 has five layers:

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

Every WorkSession-scoped mutating operation requires:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Every non-WorkSession protocol mutation requires:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
```

Worker registration, Actor registration, and OutcomeReport submission are
non-WorkSession protocol mutations. They verify Actor authority, idempotency,
protocol version, and timestamp. They do not require fake WorkSession revision
or previous event hash values.

Every accepted WorkSession-scoped state change records the Actor, verifies
authority, checks the current WorkSession revision, and links to the previous
event hash.

Every AgentWorker action that affects a WorkSession records a PolicyDecision
before the action is accepted as protocol state.

Every export excludes product-private fields, credentials, secrets, raw runtime
state, host-only database ids, deployment details, billing data, private scores,
product UI state, raw auth tokens, provider secrets, session cookies, and
private keys.

## Protocol Drift Guard

Every contributor must hold the protocol boundary.

Jarvis does not become an agent framework because existing agents need
coordination.

Jarvis does not become a runtime because compatible hosts need execution.

Jarvis does not become a personal agent because personal agents implement the
protocol.

Jarvis does not become Garden because Garden is a host.

Jarvis does not become Workstream because Workstream consumes evidence and
submit OutcomeReports.

Jarvis does not become MCP, A2A, ACP, or AG-UI because those protocols are
recorded around WorkSessions.

When a proposed change adds execution, UI, auth, storage, billing, marketplace,
model calls, sandbox behavior, product workflow, or task evaluation, move it
outside Jarvis. Keep only the protocol record, lifecycle rule, security rule,
error rule, or conformance rule that protects human-agent collaboration and
shared learning.

## Current Execution Focus

The active focus is the v0.1 first-30-days protocol contract.

Protocol lock is complete. Current work converts the locked protocol into the
OpenAPI 3.1 contract and conformance entry.

Work on:

- OpenAPI 3.1 document skeleton
- `components.schemas` for core protocol objects
- path layout for core protocol operations
- event envelope component
- portable export component
- security schemes and required protocol headers
- protocol error model
- golden-path conformance checklist
- failure-mode conformance checklist
- first OpenAPI examples for WorkSession, Request, Review, and export

Do not start Garden POC work in this phase.
Do not build runtime features in this repo.
Do not add product-specific assumptions to protocol records.
Do not reopen locked protocol decisions unless a concrete contradiction blocks
OpenAPI drafting.

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

Soft protocol wording is a defect.

Do not write protocol rules with soft modal verbs, speculative phrases,
advisory phrases, or generic implementation-concern phrasing. The wording
guard in [scripts/check_week1_wording.py](./scripts/check_week1_wording.py)
rejects the blocked terms.

Use direct ownership and state language instead:

```txt
Hosts own storage, streaming, execution, auth, deployment, and UI.
Jarvis records governed learning when protocol behavior changes future work.
Review resolves a Request when human judgment resolves the blocked scope.
Takeover resolves a Request when the human assumes direct control.
The protocol rejects missing or invalid required state.
```

Every PR MUST run the wording guard before push. Every CodeRabbit wording
comment MUST be checked and fixed when valid before the PR is treated as done.

Do not write this repo as a third-party review of Jarvis. Write it as the
source of truth for Jarvis.

## Required References

Before changing protocol direction, read:

- [README.md](./README.md)
- [docs/protocol/14-protocol-lock.md](./docs/protocol/14-protocol-lock.md)
- [docs/protocol/15-openapi-communication-binding.md](./docs/protocol/15-openapi-communication-binding.md)
- [docs/protocol/11-core-protocol-objects.md](./docs/protocol/11-core-protocol-objects.md)
- [docs/protocol/12-request-protocol.md](./docs/protocol/12-request-protocol.md)
- [docs/protocol/13-contribution-evidence-learning.md](./docs/protocol/13-contribution-evidence-learning.md)
- [docs/protocol/16-positioning-adoption-lock.md](./docs/protocol/16-positioning-adoption-lock.md)
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
