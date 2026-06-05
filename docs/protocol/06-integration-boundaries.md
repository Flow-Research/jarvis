# Integration Boundaries

Jarvis is a compatibility protocol. It does not define how work runs.

Products and hosts decide where and how execution happens. Jarvis defines the
protocol records those systems produce and consume.

Jarvis lets different humans, agents, products, hosts, and external systems
share the same collaboration records without sharing the same infrastructure.

## Jarvis Boundary

Jarvis defines protocol contracts:

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

Jarvis defines the meaning of those contracts, the allowed state transitions,
the required provenance, and the evidence that must be produced.

## Host Boundary

A host implementing Jarvis owns:

- user interface
- account and identity integration
- execution environment
- model/provider selection
- tool system
- sandbox selection
- storage
- queues and scheduling
- deployment
- billing
- notifications
- organization controls
- connector hosting
- operational monitoring

None of these choices belong to Jarvis.

## Evaluation Boundary

Evaluation systems consume Jarvis protocol outputs:

- WorkSession references
- Contribution records
- EvidenceManifest exports
- Review records
- policy decisions
- final artifacts
- limitations

Evaluation systems own tasks, rubrics, routing, scoring, acceptance, and
settlement. Jarvis owns the collaboration record that produced the work.

## Capability Boundary

Capability-preparation systems provide context, skills, checks, and project
setup for a host. They do not define the Jarvis protocol. They feed useful
inputs into a Jarvis-compatible WorkSession.

## Adjacent Protocol Boundary

MCP, A2A, and AG-UI are external protocols.

```txt
MCP     agent/app <-> tools, prompts, resources, and context servers
A2A     agent     <-> agent communication and delegation
AG-UI   frontend  <-> agent state, UI events, and user interaction
Jarvis  human     <-> agent collaboration, policy, evidence, and learning
```

Jarvis records policy, attribution, evidence, review, takeover, contribution,
and learning around the use of external protocols. Jarvis does not define their
transport, runtime, tool semantics, UI semantics, or agent-to-agent
coordination semantics.

## Post-Session Outcome Boundary

External systems report what happened after a WorkSession export. That
feedback closes the learning loop without rewriting the completed session.

`OutcomeReport` is an optional extension record:

```txt
OutcomeReport
  id
  work_session_id
  source_ref
  reporter_ref
  accepted_by_actor_id
  outcome: accepted | rejected | needs_revision | disputed | partial
  learning_record_refs
  received_at
  external_system_ref
  reporter_actor_id
  reason
  reviewer_feedback_refs
```

Rules:

- OutcomeReport arrives after a WorkSession is completed.
- It does not mutate the sealed WorkSession or EvidenceManifest.
- The report creates or references a new LearningRecord.
- `source_ref` is required and identifies the completed WorkSession export,
  external task record, evaluation record, or other portable work reference
  whose outcome is being reported.
- `reporter_ref` identifies the external or protocol reporter that supplied the
  outcome.
- `accepted_by_actor_id` records the protocol Actor with review authority that
  accepted the report into Jarvis records.
- `reporter_actor_id` is present only when the reporter is already represented
  as a protocol Actor.
- OutcomeReport is an extension. It does not change the v0 core object list.

## Host Contract

A Jarvis-compatible host must be able to:

```txt
start WorkSession
append protocol events
enforce Policy before agent action
create Request when blocked
record Review decisions
record Takeover and reconciliation
record Contribution entries
capture EvidenceManifest entries during work
propose MemoryProposal and SkillProposal records
export protocol records without product-private internals
```

The host implements this with any infrastructure.

## Forbidden Coupling

Jarvis protocol documents must not require:

- a specific cloud provider
- a local execution stack
- a specific database
- a specific queue
- a specific sandbox
- a specific model provider
- a specific deployment platform
- a specific product UI

Examples and product docs name their implementation choices. The Jarvis
protocol itself does not.

## Conformance

Jarvis conformance is about protocol behavior, not infrastructure.

A conforming implementation proves:

- WorkSession is the source of truth.
- Policy gates autonomous action.
- blocked action creates Request.
- Review approves, denies, narrows, corrects, or takes over.
- Takeover prevents stale autonomous mutation.
- Contributions are attributable.
- Evidence is captured during the work.
- Learning is proposed and governed.
- exported records are portable across products.
