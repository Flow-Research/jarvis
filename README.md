# Jarvis Human-Agent Collaboration And Learning-Loop Protocol

Jarvis is the human-agent collaboration and learning-loop protocol.

It defines how human workers and agent workers coordinate under shared goals
and human-defined policy, so they can complete work together, review each
other, record contributions, capture evidence, and both improve across
WorkSessions.

Jarvis stays focused on the collaboration and learning loop. Products, agents,
execution environments, and external systems integrate with Jarvis by
implementing its protocol contracts.

Jarvis is a compatibility layer for any HumanWorker, AgentWorker, product,
host, or external system that needs to participate in governed human-agent
collaboration.

## Interactive Simulation

Open the live simulation here:

https://flow-research.github.io/jarvis_human_agent/

The page is served directly by GitHub Pages from this repository.

## One-Line Definition

Jarvis is the open protocol that lets HumanWorkers and AgentWorkers collaborate
under shared goals and policy, producing durable WorkSessions, reviewable
Requests, attributable Contributions, governed shared Learning, and portable
Evidence.

## Plain English Definition

Jarvis is how humans and agents work together properly.

The human does not just prompt. The agent does not just answer. They both
participate in the work.

The human gives direction, judgment, context, correction, approval, and
accountability. The agent plans, executes, researches, drafts, uses tools,
collects evidence, and proposes improvements.

Jarvis defines the rules of that collaboration so any product, model, task
system, execution environment, or external service can plug in.

## Thesis

The winning unit is not the human alone and not the agent alone. The winning
unit is the human-agent team that learns together.

The shift is from isolated agent applications to compatible human-agent
collaboration. The human does not outsource judgment, and the agent does not
remain a passive tool. They form a working pair that gets better through
repeated WorkSessions.

The primitive is not:

```txt
User -> Agent -> Answer
```

The loop is:

```txt
HumanWorker + AgentWorker -> WorkSession -> Review -> Evidence -> Shared Learning
```

The human gets better. The agent gets better. The relationship gets better.
WorkSession is the durable record of that collaboration and learning loop.

Jarvis formalizes the loop where:

```txt
human judgment + agent execution + policy + review + evidence + shared learning
```

compound across real work.

The protocol makes this loop portable: different agents, products, hosts, and
task systems can exchange the same WorkSession, Request, Review, Contribution,
EvidenceManifest, and LearningRecord concepts without sharing the same
infrastructure.

## Core Loop

```txt
1. Human defines intent.
2. Policy defines boundaries.
3. Agent works inside those boundaries.
4. Agent asks when blocked.
5. Human reviews, approves, denies, narrows, corrects, or takes over.
6. Work continues.
7. Contributions are recorded.
8. Evidence is captured.
9. Learning is proposed.
10. Confirmed learning improves both workers and the next WorkSession.
```

## Central Record

`WorkSession` is the center of Jarvis.

A WorkSession is not chat history. A WorkSession is the durable record of real
human-agent collaboration around a focused unit of work.

It contains:

- objective
- human worker
- agent worker
- policy
- available capabilities
- context
- events
- requests
- reviews
- tool actions
- artifacts
- contributions
- evidence
- learning proposals
- final outcome

## First-Class Workers

Jarvis does not model `User + Assistant`.

Jarvis models `HumanWorker + AgentWorker`.

Both are workers. Both are actors. Both contribute to the WorkSession. Both can
learn from the loop.

### HumanWorker

The human is:

- goal setter
- domain expert
- reviewer
- teacher
- quality judge
- policy owner
- accountable actor
- source of taste
- source of world context

### AgentWorker

The agent is:

- autonomous worker
- executor
- researcher
- context retriever
- tool user
- draft producer
- evidence collector
- learning participant

## Core Protocol Contracts

Jarvis v0 defines these contracts. The canonical object shapes and invariants
are in [11-core-protocol-objects.md](./11-core-protocol-objects.md).

```txt
Worker
Actor
HumanWorker
AgentWorker
WorkSession
JarvisEvent
Policy
PolicyDecision
Request
Review
Takeover
Contribution
EvidenceManifest
LearningRecord
MemoryProposal
SkillProposal
Request
Review
Takeover
Contribution
EvidenceManifest
LearningRecord
MemoryProposal
SkillProposal
```

## Protocol Laws

1. Jarvis defines human-agent collaboration and shared learning.
2. WorkSession is the source of truth.
3. Jarvis does not prescribe infrastructure.
4. Policy governs autonomy.
5. Learning is governed.
6. Evidence is captured during work.
7. Contributions are attributable.
8. Human judgment remains central.
9. Execution may be delegated; accountability remains attributable.
10. HumanWorker and AgentWorker both learn.
11. Every session should improve the next session.

## Boundaries

Jarvis owns:

- collaboration and learning-loop protocol semantics
- interoperability contracts
- conformance rules
- WorkSession lifecycle
- policy-governed autonomy
- request, review, and takeover semantics
- contribution records
- evidence manifests
- governed memory and learning proposals
- skill proposal semantics
- integration boundary contracts

Jarvis does not own:

- product UI
- external task marketplaces
- external identity systems
- enterprise workspace controls
- model providers
- cloud providers or deployment choices
- sandbox implementations or execution stacks
- database implementations

## What Jarvis v0 Must Prove

```txt
1. Create HumanWorker.
2. Create AgentWorker.
3. Start WorkSession.
4. Attach Policy.
5. Send objective.
6. AgentWorker acts inside policy.
7. AgentWorker hits blocked action.
8. AgentWorker creates Request.
9. HumanWorker approves, denies, narrows, answers, or takes over.
10. AgentWorker resumes.
11. Jarvis records Contribution.
12. Jarvis captures Evidence.
13. Jarvis proposes Learning.
14. Human confirms or rejects Learning.
15. EvidenceManifest exports.
```

If v0 proves this loop, Jarvis is real.

## Document Map

- [00-principles.md](./00-principles.md) - protocol principles, laws,
  non-goals, and design constraints.
- [01-architecture.md](./01-architecture.md) - system layers, protocol
  primitives, and ownership boundaries.
- [02-memory.md](./02-memory.md) - memory taxonomy, lifecycle, provenance,
  retrieval, and write policy.
- [03-autonomy-policy.md](./03-autonomy-policy.md) - autonomy levels,
  capability grants, requests, inbox, and takeover.
- [04-work-sessions.md](./04-work-sessions.md) - collaboration records,
  events, reviews, evidence, and learning loops.
- [05-skills-tools.md](./05-skills-tools.md) - skills, tools, MCP,
  execution-policy semantics, and tool governance.
- [06-integration-boundaries.md](./06-integration-boundaries.md) - product,
  host, and external system boundaries.
- [07-protocol-decisions.md](./07-protocol-decisions.md) - fixed protocol
  decisions and explicit non-decisions.
- [08-package-contracts.md](./08-package-contracts.md) - package graph,
  exports, ownership, forbidden imports, and release tests.
- [09-host-integration.md](./09-host-integration.md) - how products and hosts
  implement Jarvis without inheriting infrastructure assumptions.
- [10-protocol-mvp.md](./10-protocol-mvp.md) - the smallest protocol proof.
- [11-core-protocol-objects.md](./11-core-protocol-objects.md) - canonical
  object definitions, invariants, statuses, and portable export surface.
- [12-30-day-roadmap.md](./12-30-day-roadmap.md) - focused 30-day execution
  plan for protocol lock, schemas, Garden POC, and interoperability proof.
- [ROADMAP.md](./ROADMAP.md) - release roadmap, milestones, decision gates,
  risks, and immediate next actions.
