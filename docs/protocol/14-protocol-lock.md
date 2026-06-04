# Protocol Lock

Jarvis is the human-agent collaboration and learning-loop protocol.

It defines how a HumanWorker and an AgentWorker work together under shared
goals and human-defined policy. The protocol records the work, requests,
reviews, takeovers, contributions, evidence, and learning that happen inside a
WorkSession.

This is the v0 lock. OpenAPI contract work starts from here.

## Locked Status

`locked-for-v0-openapi-draft`

Locked now:

- thesis
- boundary
- vocabulary
- lifecycle
- object relationships
- core states
- conformance expectations
- portable export shape

Not locked yet:

- exact OpenAPI field definitions
- version negotiation
- capability negotiation
- extension format
- error codes
- conformance fixtures

## Definition

Jarvis is the protocol for governed human-agent collaboration and shared
learning.

The HumanWorker brings goals, judgment, context, correction, review, taste, and
accountability.

The AgentWorker brings execution, research, planning, drafting, tool use,
memory retrieval, evidence capture, and workflow acceleration.

Jarvis records how both workers collaborate and improve across WorkSessions.

## Thesis

The valuable unit is the human-agent team.

Not the human alone.
Not the agent alone.
Not a chatbot.
Not a runtime.
Not a product workspace.

The HumanWorker improves.
The AgentWorker improves.
The pair improves.
The next WorkSession carries confirmed learning forward.

## Boundary

Jarvis owns:

- protocol vocabulary
- object semantics
- WorkSession lifecycle
- event envelope
- policy decision semantics
- request, review, and takeover semantics
- contribution semantics
- evidence export semantics
- governed learning semantics
- conformance expectations

Jarvis does not own:

- agent runtime
- model provider
- cloud provider
- sandbox implementation
- database implementation
- queue implementation
- product UI
- authentication
- billing
- task marketplace
- payment or settlement
- organization workspace internals
- local execution stack

A host implements Jarvis. A host is not Jarvis.

## Vocabulary

The v0 vocabulary is:

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

These names are stable for the v0 OpenAPI draft.

## Relationship Model

Jarvis models this:

```txt
HumanWorker + AgentWorker
  collaborate inside WorkSession
  under Policy
  through JarvisEvents
  using Requests, Reviews, and Takeovers
  producing Contributions and EvidenceManifest
  generating LearningRecords, MemoryProposals, and SkillProposals
```

Jarvis does not model this:

```txt
User -> Assistant -> Answer
```

Chat is an interface. The protocol is the collaboration record.

## Lifecycle

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
11. allowed action records JarvisEvent and evidence
12. denied or review-required action creates Request
13. HumanWorker responds through Review or Takeover
14. approved work resumes inside confirmed or narrowed Policy
15. Contribution records who did what
16. EvidenceManifest records portable proof
17. LearningRecord captures human, agent, or pair learning
18. MemoryProposal and SkillProposal stay governed until reviewed
19. WorkSession completes, fails, or closes
20. portable export is produced
```

Hosts add internal steps. The external Jarvis lifecycle stays intact.

## WorkSession

WorkSession is the source of truth.

States:

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

- WorkSession starts with HumanWorker, AgentWorker, objective, and Policy.
- WorkSession keeps an append-only JarvisEvent log.
- WorkSession owns Requests, Reviews, Takeovers, Contributions,
  EvidenceManifest, and LearningRecords.
- WorkSession export stays free of product-private infrastructure fields.

## Request

Request is the structured way the AgentWorker asks for permission, context,
judgment, review, or takeover.

States:

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

- Request belongs to one WorkSession.
- Request identifies requester worker and requester actor.
- Request states reason, requested action or missing context, risk class,
  status, and creation time.
- Request resolves through Review or Takeover.

## Review

Review records human judgment.

Decisions:

```txt
approve
deny
narrow
correct
takeover
needs_revision
```

Rules:

- Review identifies reviewer worker and reviewer actor.
- Review targets a Request, action, contribution, artifact, memory proposal,
  skill proposal, evidence item, or final outcome.
- Review resolves a Request.
- Review creates learning signals.

## Takeover

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

- Takeover creates or increments a lock epoch.
- Agent actions from an old lock epoch are stale.
- Resume requires reconciliation.
- Takeover is a learning signal.

## Contribution

Contribution answers who did what.

Contribution types:

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

Contributor types:

```txt
human
agent
service
tool
shared
```

Rules:

- Human, agent, service, tool, and shared contributions stay distinguishable.
- Shared contribution does not erase individual actors.
- Contribution is attribution, not payment or accounting.
- Downstream systems evaluate Contribution records.

## Evidence

EvidenceManifest is the portable proof package for a WorkSession.

It references:

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

- Evidence is captured during work.
- Evidence is not reconstructed only at the end.
- Redacted exports stay derived from the same event chain.
- EvidenceManifest is portable across compatible products and hosts.

## Learning

LearningRecord captures what improved because of the WorkSession.

Subject types:

```txt
human
agent
pair
```

Rules:

- Learning is not only agent memory.
- Jarvis records human learning, agent learning, and pair learning.
- LearningRecord points to MemoryProposal or SkillProposal when learning becomes
  a governed memory or skill change.
- Durable memory and active skill behavior require governed review.

## Compatibility

Existing agents and products are first-class.

Compatible hosts and adapters map existing agents into AgentWorker records.
They do not replace the agent runtime.

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

If a host cannot expose a native concept, it records the closest valid Jarvis
object with explicit limitations or marks the capability unsupported.

## Conformance

A v0-compatible host proves:

- WorkSession is the source of truth.
- HumanWorker and AgentWorker both exist.
- Every meaningful JarvisEvent has an Actor.
- Policy gates autonomous AgentWorker action.
- Policy-denied or review-required action creates Request.
- Request resolves through Review or Takeover.
- Review decisions are explicit.
- Takeover blocks stale autonomous continuation.
- Contributions are attributable.
- EvidenceManifest is captured during work and exportable.
- Learning is governed.
- MemoryProposal and SkillProposal do not silently become durable behavior.
- Portable export contains no product-private infrastructure requirement.

## Portable Export

A v0 portable export contains:

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

Extension fields are namespaced. Extensions do not change the meaning of core
protocol fields.

## OpenAPI Contract Work Starts Here

OpenAPI contract work starts with:

1. version negotiation
2. capability negotiation
3. extension namespace format
4. standard error codes
5. required and optional fields per object
6. OpenAPI 3.1 component and path layout
7. canonical WorkSession export example
8. passing and failing conformance fixtures

The thesis is locked. The object model is locked. The lifecycle is locked.
