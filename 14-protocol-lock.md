# Protocol Lock

This document locks the first implementable shape of Jarvis.

Jarvis is the human-agent collaboration and learning-loop protocol. It defines
the durable record of how a HumanWorker and AgentWorker collaborate under
shared goals and human-defined policy, produce reviewable requests, record
contributions, capture portable evidence, and learn together across
WorkSessions.

This lock exists so implementation starts from stable protocol meaning instead
of drifting into another runtime, agent framework, product UI, or internal
workflow.

## Lock Status

Status: `locked-for-v0-schema-draft`

Meaning:

- the thesis is locked
- the boundary is locked
- the core object names are locked
- the core lifecycle is locked
- the conformance expectations are locked
- field-level schemas are not locked yet
- extension and version negotiation are not locked yet

Schema work may begin after this document is accepted.

## Official Definition

Jarvis is the human-agent collaboration and learning-loop protocol.

It defines how HumanWorkers and AgentWorkers coordinate under shared goals and
Policy, so they can complete WorkSessions together, create Requests when the
agent is blocked, capture Reviews and Takeovers from the human, record
Contributions, export EvidenceManifests, and govern LearningRecords,
MemoryProposals, and SkillProposals.

## Locked Thesis

The valuable unit is the human-agent team.

Jarvis does not optimize for an agent alone. Jarvis does not reduce the human
to a prompt source. Jarvis defines the protocol record of both workers acting,
reviewing, correcting, producing evidence, and learning together.

The HumanWorker improves. The AgentWorker improves. The pair improves. The
next WorkSession should benefit from confirmed learning.

## Locked Non-Goals

Jarvis MUST NOT define or own:

- agent runtime
- model provider
- cloud provider
- sandbox implementation
- database implementation
- queue implementation
- product UI
- authentication system
- billing system
- task marketplace
- payment or settlement system
- organization workspace internals
- specific agent framework
- specific local execution stack

Products and hosts MAY use any of those systems. Jarvis only defines the
protocol records and state transitions those systems must preserve to be
Jarvis-compatible.

## Locked Core Vocabulary

The v0 protocol vocabulary is:

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
```

These names are locked for v0 schema drafting.

Any later rename MUST include:

- reason for the rename
- migration impact
- affected schema names
- affected conformance tests
- compatibility policy

## Locked Relationship Model

Jarvis models:

```txt
HumanWorker + AgentWorker
  collaborate inside WorkSession
  under Policy
  through JarvisEvents
  with Requests, Reviews, and Takeovers
  producing Contributions and EvidenceManifest
  generating LearningRecords, MemoryProposals, and SkillProposals
```

Jarvis does not model:

```txt
User -> Assistant -> Answer
```

Chat MAY be one interface. The protocol is the collaboration record.

## Locked Lifecycle

The v0 lifecycle is:

```txt
1. create Worker records
2. create Actor records
3. create HumanWorker
4. create AgentWorker
5. start WorkSession
6. attach Policy
7. record objective
8. assemble context and available capabilities
9. AgentWorker proposes or performs action
10. Policy produces PolicyDecision
11. allowed action records JarvisEvent and Evidence
12. denied or review-required action creates Request
13. HumanWorker responds through Review or Takeover
14. approved work resumes inside narrowed or confirmed Policy
15. Contribution records who did what
16. EvidenceManifest records portable proof
17. LearningRecord captures human, agent, or pair learning
18. MemoryProposal and SkillProposal remain governed until reviewed
19. WorkSession completes, fails, or closes
20. portable export is produced
```

This lifecycle is the minimum standard. A host MAY add more internal steps, but
it MUST preserve the protocol lifecycle externally.

## Locked WorkSession States

```txt
created
active
waiting_on_human
takeover
reconciling
completed
failed
closed
```

Rules:

- A WorkSession MUST NOT start without HumanWorker, AgentWorker, objective, and
  Policy.
- A WorkSession MUST keep an append-only JarvisEvent log.
- A WorkSession MUST be the source of truth for Requests, Reviews,
  Contributions, EvidenceManifest, and LearningRecords.
- A WorkSession export MUST NOT require product-private infrastructure fields.

## Locked Request States

```txt
pending
approved
denied
narrowed
answered
takeover
needs_revision
expired
cancelled
```

Rules:

- A Request MUST belong to one WorkSession.
- A Request MUST identify requester worker and requester actor.
- A Request MUST state the reason, requested action or missing context, risk
  class, status, and creation time.
- A Request MUST NOT resolve without Review or Takeover.

## Locked Review Decisions

```txt
approve
deny
narrow
correct
takeover
needs_revision
```

Rules:

- A Review MUST identify reviewer worker and reviewer actor.
- A Review MUST target a Request, action, contribution, artifact, memory
  proposal, skill proposal, evidence item, or final outcome.
- A Review MAY resolve a Request.
- A Review MAY create LearningRecord, MemoryProposal, or SkillProposal signals.

## Locked Takeover Model

Takeover is temporary direct human control.

States:

```txt
requested
locked
human_active
reconciliation_required
resumed
closed
```

Rules:

- Takeover MUST create or increment a lock epoch.
- Agent actions from an old lock epoch MUST be rejected.
- Resume MUST require reconciliation.
- Takeover MUST be recorded as a learning signal.

## Locked Contribution Model

Contribution answers who did what.

Contribution types include:

```txt
intent
instruction
plan
research
execution
artifact
review
correction
decision
evidence_capture
memory_proposal
skill_proposal
submission
```

Contributor types are:

```txt
human
agent
service
tool
shared
```

Rules:

- Contributions MUST distinguish human, agent, service, tool, and shared work.
- Shared contribution MUST NOT erase individual contributing actors.
- Contribution is not payment or accounting. It is the protocol attribution
  record downstream systems MAY evaluate.

## Locked Evidence Model

EvidenceManifest is the portable proof package for a WorkSession.

It MUST include references to:

- WorkSession
- event chain root
- artifacts
- evidence items
- policy decisions
- requests
- reviews
- contributions
- limitations
- export profile

Rules:

- Evidence MUST be captured during work.
- Evidence MUST NOT be reconstructed only at the end.
- Redacted exports MUST remain derived from the same event chain.
- EvidenceManifest MUST be portable across compatible products and hosts.

## Locked Learning Model

LearningRecord captures what improved because of the WorkSession.

Subject types are:

```txt
human
agent
pair
```

Rules:

- Learning MUST NOT mean only agent memory.
- Jarvis MUST record human learning, agent learning, and pair learning.
- LearningRecord MAY point to MemoryProposal or SkillProposal.
- Durable memory and active skill behavior MUST require governed review.

## Locked Compatibility Target

Existing agents and products remain first-class.

Jarvis-compatible adapters MUST be able to wrap an existing agent without
rewriting the agent runtime.

A compatible adapter maps:

```txt
human identity or operator       -> HumanWorker + Actor
agent process or agent product   -> AgentWorker + Actor
agent step                       -> JarvisEvent
tool/action authorization        -> PolicyDecision
blocked action                   -> Request
human approval/correction        -> Review
human direct control             -> Takeover
work performed                   -> Contribution
trace/artifact/source/output     -> EvidenceManifest entry
confirmed improvement            -> LearningRecord / MemoryProposal / SkillProposal
```

If an adapter cannot expose a native concept, it MUST either:

- produce the closest valid Jarvis record with explicit limitations, or
- mark the capability unsupported during capability negotiation.

## Locked Host Boundary

A host implements Jarvis. A host is not Jarvis.

Hosts own:

- UI
- accounts and identity integration
- model selection
- tool execution
- MCP hosting
- sandbox choice
- storage
- queues
- deployment
- observability
- billing
- product-specific workflows

Jarvis owns:

- protocol vocabulary
- object semantics
- lifecycle states
- event envelope
- policy decision semantics
- request/review/takeover semantics
- contribution semantics
- evidence export semantics
- governed learning semantics
- conformance expectations

## Locked Conformance Expectations

A v0-compatible host MUST prove:

- WorkSession is the source of truth.
- HumanWorker and AgentWorker both exist.
- Every meaningful JarvisEvent has an Actor.
- Policy gates autonomous AgentWorker action.
- Policy-denied or review-required action creates Request.
- Request cannot resolve without Review or Takeover.
- Review decisions are explicit.
- Takeover blocks stale autonomous continuation.
- Contributions are attributable.
- EvidenceManifest is captured during work and exportable.
- Learning is governed.
- MemoryProposal and SkillProposal do not silently become durable behavior.
- Portable export contains no product-private infrastructure requirement.

## Locked Portable Export

A v0 portable export MUST contain:

```txt
protocol_version
WorkSession
Workers
Actors
JarvisEvents
PolicyDecisions
Requests
Reviews
Takeovers
Contributions
EvidenceManifest
LearningRecords
MemoryProposals
SkillProposals
limitations
```

The export MAY contain extension fields only when they are namespaced and do
not change the meaning of the core protocol fields.

## Open Before Schema Freeze

These questions remain open for the schema phase:

1. Version negotiation shape.
2. Capability negotiation shape.
3. Extension namespace format.
4. Standard error codes.
5. Required vs optional fields per object.
6. JSON Schema package layout.
7. Canonical example WorkSession export.
8. Passing and failing conformance fixtures.

These are schema questions, not thesis questions.

## Entry Gate For Schemas

Schema drafting can begin when this document is accepted.

Schema drafting MUST use:

- this document for locked meaning
- `11-core-protocol-objects.md` for object definitions
- `13-protocol-readiness-review.md` for readiness gaps

Schema drafting MUST NOT reopen:

- whether Jarvis is a protocol
- whether Jarvis owns runtime
- whether any host product is the protocol
- whether human and agent both learn
- whether WorkSession is the source of truth
