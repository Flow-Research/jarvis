# Design Acceptance Criteria

Jarvis architecture is accepted only when these criteria hold.

## Scope

- Jarvis is defined as the human-agent collaboration and learning-loop
  protocol.
- [11-core-protocol-objects.md](../protocol/11-core-protocol-objects.md) is
  the source of truth for v0 object definitions.
- Jarvis is a compatibility protocol for multiple humans, agents, products,
  hosts, and external systems.
- Jarvis does not define execution stack, cloud, database, queue, sandbox,
  deployment, model provider, authentication, billing, or product UI.
- external products and systems integrate with Jarvis through protocol
  contracts.

## Human-Agent Collaboration

- HumanWorker is an active contributor, reviewer, teacher, and accountable
  actor.
- AgentWorker is an autonomous but policy-bounded contributor.
- HumanWorker and AgentWorker are both actors in the protocol.
- HumanWorker and AgentWorker both learn from completed WorkSessions.
- HumanWorker approves, denies, narrows, corrects, requests revision, or takes
  over.
- Corrections become structured learning signals.

## WorkSession

- WorkSession is the source of truth.
- WorkSession captures goals, events, requests, reviews, takeovers,
  contributions, evidence, artifacts, learning, and final outcome.
- WorkSession is not reduced to chat history.

## Policy

- Policy defines what the AgentWorker does.
- Action outside policy creates Request.
- Request is reviewable and attributable.
- Review decisions are explicit.
- Takeover prevents stale autonomous continuation.

## Memory And Skills

- Memory scopes are explicit.
- Memory has lifecycle and provenance.
- Durable memory changes require MemoryProposal and review state.
- Skills are procedural memory.
- Skill changes require SkillProposal and review state.

## Evidence And Contribution

- Contributions distinguish human, agent, service, tool, and shared work.
- Evidence is captured during work.
- EvidenceManifest includes policy decisions, requests, reviews,
  contributions, artifacts, and limitations.
- EvidenceManifest is portable across products.

## v0.1 Protocol Acceptance

The first protocol release passes these checks:

```txt
create HumanWorker
create AgentWorker
start WorkSession
attach Policy
record objective
record allowed AgentWorker action
record policy-denied AgentWorker action
create Request
record HumanWorker Review
resume work after approval or correction
record Contribution
record EvidenceManifest item
record LearningRecord for human, agent, or pair learning
create MemoryProposal or SkillProposal
export protocol record
```

Expected result:

- all records validate against schema
- WorkSession status transitions are valid
- Request cannot resolve without Review
- Review supports approve, deny, narrow, correct, takeover, and needs_revision
- Takeover creates lock state
- Contribution references events or artifacts
- EvidenceManifest references the WorkSession event chain
- exported records contain no product-private infrastructure requirement

## Conformance Acceptance

A product is Jarvis-compatible when it proves:

- WorkSession is the source of truth.
- Policy gates autonomous action.
- blocked action creates Request.
- Review resolves Request.
- Takeover prevents stale continuation.
- Contributions are attributable.
- EvidenceManifest is portable.
- Learning is governed.

Conformance does not require any specific execution stack, cloud provider,
database, sandbox, queue, deployment platform, or UI.
