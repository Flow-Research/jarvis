# Integration Boundaries

Jarvis is a compatibility protocol. It does not define how work runs.

Products and hosts decide where and how execution happens. Jarvis defines the
protocol records those systems produce and consume.

The goal is that different humans, agents, products, hosts, and external
systems can share the same collaboration records without sharing the same
infrastructure.

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

Evaluation systems can consume Jarvis protocol outputs:

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

Capability-preparation systems can provide context, skills, checks, and project
setup for a host. They do not define the Jarvis protocol. They feed useful
inputs into a Jarvis-compatible WorkSession.

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

The host can implement this with any infrastructure.

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

Examples and products may mention their implementation choices. The Jarvis
protocol itself does not.

## Conformance

Jarvis conformance is about protocol behavior, not infrastructure.

A conforming implementation proves:

- WorkSession is the source of truth.
- Policy gates autonomous action.
- blocked action creates Request.
- Review can approve, deny, narrow, correct, or take over.
- Takeover prevents stale autonomous mutation.
- Contributions are attributable.
- Evidence is captured during the work.
- Learning is proposed and governed.
- exported records are portable across products.
