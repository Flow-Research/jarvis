# Jarvis

Human-agent collaboration and learning-loop protocol.

Jarvis is the protocol for governed collaboration between human workers and
agent workers.

It defines how human workers and agent workers coordinate under shared goals
and human-defined policy, complete work together, review each other, record
contributions, capture evidence, and both improve across WorkSessions.

Jarvis stays focused on the collaboration and learning loop. Hosts and
external systems integrate with Jarvis by implementing its protocol contracts.

Jarvis is the compatibility protocol for any HumanWorker, AgentWorker, host, or
external system that needs to participate in governed human-agent collaboration.

## Interactive Simulation

Open the live simulation here:

https://flow-research.github.io/jarvis/

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

Jarvis defines the rules of that collaboration. Hosts and external systems
implement those rules.

## Protocol Position

MCP connects agents to tools.
A2A connects agents to agents.
AG-UI connects agents to UI.
Jarvis records how HumanWorkers and AgentWorkers collaborate, produce evidence,
and learn.

Jarvis does not replace those protocols. Jarvis defines the collaboration
record around human-agent work: WorkSession, Policy, PolicyDecision, Request,
Review, Takeover, Contribution, EvidenceManifest, LearningRecord,
MemoryProposal, SkillProposal, and OutcomeReport.

Existing agents participate by preserving native execution and emitting
Jarvis-compatible protocol records. Hosts own UI, storage, auth, execution,
models, tools, memory engines, deployment, monitoring, and workflow.

## Compatible Implementations

Compatible implementations MUST prove:

- WorkSession-scoped mutations carry the required Jarvis headers.
- Actor authority is verified before accepted protocol state.
- WorkSession revision and previous event hash are checked before mutation.
- PolicyDecision is recorded before accepted AgentWorker action state.
- Request records blocked or review-required scope.
- Review or Takeover resolves Request.
- ApprovalScope bounds Review-approved continuation.
- Takeover lock epoch and reconciliation refs bind Takeover continuation.
- Contribution records who did what.
- EvidenceManifest exports portable proof without host-private fields.
- LearningRecord records human, agent, or pair learning.
- MemoryProposal and SkillProposal remain governed.
- OutcomeReport carries post-session feedback without sealed-record mutation.

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

The protocol makes this loop portable: different compatible implementations
exchange the same WorkSession, Request, Review, Contribution,
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

Both are workers. Both are actors. Both contribute to the WorkSession. Both
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

Jarvis v0.1 defines these contracts. The canonical object shapes and invariants
are in [docs/protocol/11-core-protocol-objects.md](./docs/protocol/11-core-protocol-objects.md).

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
OutcomeReport
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
9. Execution is delegable; accountability remains attributable.
10. HumanWorker and AgentWorker both learn.
11. Every completed WorkSession improves the next WorkSession.
12. Jarvis stays protocol-only; hosts and external systems implement or
    integrate with it without becoming it.

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

Jarvis does not own host implementation:

- UI
- authentication
- authorization
- storage
- execution
- model providers
- tool execution
- isolation mechanisms
- deployment
- billing
- monitoring
- host-specific workflow

## SDK Boundary

A Jarvis SDK is a protocol implementation kit.

It helps compatible implementations create protocol records, attach required
headers, preserve event hash chains, validate Request/Review/Takeover state,
export EvidenceManifest records, run conformance fixtures, and map example
work into Jarvis records.

A Jarvis SDK does not run agents, orchestrate models, execute tools, own memory
engines, provide UI, manage auth, store records, run sandboxes, schedule work,
or become a host adapter.

Existing agents remain first-class. Jarvis succeeds when existing agents and
hosts produce compatible WorkSession, Request, Review, Contribution,
EvidenceManifest, and LearningRecord records without being rewritten as
Jarvis-owned agents.

## What Jarvis v0.1 Must Prove

```txt
1. Create HumanWorker.
2. Create AgentWorker.
3. Start WorkSession.
4. Attach Policy.
5. Send objective.
6. AgentWorker action records PolicyDecision before accepted protocol state.
7. AgentWorker acts inside policy.
8. AgentWorker hits blocked or review-required scope.
9. AgentWorker creates Request.
10. HumanWorker approves, denies, narrows, answers, or takes over.
11. ApprovalScope bounds approved continuation.
12. Takeover records lock epoch and reconciliation refs.
13. Contribution records who did what.
14. Evidence is captured.
15. LearningRecord records human, agent, or pair learning.
16. MemoryProposal or SkillProposal remains governed.
17. EvidenceManifest exports after terminal WorkSession state.
18. OutcomeReport carries post-session feedback into governed learning.
```

When v0.1 proves this loop, Jarvis is real.

## Docs

- [docs/README.md](./docs/README.md) - docs index.
- [docs/protocol/](./docs/protocol/) - protocol definition, architecture,
  object model, policy, memory, evidence, integration boundaries, package
  contracts, v0.1 protocol proof, protocol lock, OpenAPI binding, and
  positioning lock.
- [docs/architecture_brief/](./docs/architecture_brief/) - shareable protocol
  architecture brief and PDF.
- [docs/conformance/](./docs/conformance/) - compatibility mapping,
  conformance entries, fixtures, validator requirements, and existing-agent
  proof plan.
- [docs/planning/](./docs/planning/) - roadmap, 30-day plan, and upload-ready
  planning sheets.
- [docs/reviews/](./docs/reviews/) - protocol readiness and acceptance review
  criteria.

## Local Checks

Every protocol PR MUST run:

```txt
python3 scripts/check_conformance_fixtures.py
python3 scripts/check_openapi_skeleton.py
python3 scripts/check_markdown_links.py
python3 scripts/check_week1_wording.py
git diff --check
```

Jarvis defines `check_conformance_fixtures.py` as fixture-record validation only.
The validator MUST NOT execute host behavior.
