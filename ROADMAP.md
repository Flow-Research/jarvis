# Jarvis Roadmap

Jarvis is the open-source human-agent collaboration and learning-loop
compatibility protocol.

The roadmap turns the protocol into stable contracts, schemas, conformance
tests, examples, and documentation. It does not create an execution stack.

For the immediate execution plan, see
[12-30-day-roadmap.md](./12-30-day-roadmap.md).

## Roadmap Contract

Jarvis owns:

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
- protocol event envelope
- protocol export format
- conformance tests
- interoperability rules

Jarvis does not own:

- product UI
- authentication
- product internals
- task/evaluation system internals
- capability-preparation system internals
- model providers
- tool execution
- MCP hosting
- sandboxes
- databases
- queues
- cloud providers
- deployment
- local execution
- operational monitoring

Those are product and host responsibilities.

## Release Strategy

```txt
v0.1 Protocol Alpha
  stable vocabulary, schemas, event envelope, and golden-path conformance

v0.2 Evidence And Learning Beta
  stronger EvidenceManifest, Contribution, MemoryProposal, and SkillProposal
  contracts

v0.3 Ecosystem Conformance
  host conformance suite, examples, and product integration guides

v1.0 Stable Protocol
  stable public protocol, compatibility rules, export format, and migration
  policy
```

## v0.1 Protocol Alpha

Goal: prove the smallest complete human-agent collaboration loop.

The alpha proves that the loop is portable, not tied to a single product,
agent, host, or execution stack.

The protocol must express:

```txt
HumanWorker defines intent
Policy defines boundaries
AgentWorker acts inside policy
blocked action becomes Request
HumanWorker reviews or takes over
AgentWorker resumes when allowed
Contribution records who did what
EvidenceManifest captures proof during work
LearningRecord captures what the human, agent, and pair learned
MemoryProposal and SkillProposal remain governed
```

### v0.1 Must-Have Slice

- protocol schemas for all core contracts
- event envelope
- WorkSession status transitions
- Policy decision model
- Request and Review lifecycle
- Takeover lifecycle
- Contribution ledger shape
- EvidenceManifest shape
- LearningRecord shape
- MemoryProposal shape
- SkillProposal shape
- portable export profile
- conformance tests for the golden path
- interoperability checklist
- one static interactive simulation
- one host integration guide

### v0.1 Excludes

- execution packages
- cloud implementation
- local execution implementation
- model calls
- sandbox execution
- persistent storage implementation
- queues and scheduling
- hosted UI
- auth
- billing
- task routing
- product implementation

## Milestone 0: Protocol Lock

Owner: Architecture

Output:

- official definition is frozen
- core terms are frozen
- system boundaries are frozen
- non-goals are frozen

Done when:

- README, Principles, Architecture, Package Contracts, Protocol MVP, and
  Acceptance Criteria all agree.
- no Jarvis document assigns execution, cloud, database, sandbox, or deployment
  ownership to Jarvis.

## Milestone 1: Protocol Schemas

Owner: Protocol

Output:

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
- JarvisEvent

Done when:

- every schema matches `11-core-protocol-objects.md`
- schemas serialize to stable JSON
- required fields are explicit
- status values are enumerated
- references are typed
- no schema requires implementation-private fields

## Milestone 2: WorkSession Lifecycle

Owner: Protocol

Output:

- WorkSession status transition table
- event ordering rules
- event hash-chain rules
- objective recording rules
- completion rules
- failure and close rules

Done when:

- invalid transitions fail conformance tests
- every WorkSession has HumanWorker, AgentWorker, Policy, and objective
- events remain attributable to a Worker or service

## Milestone 3: Policy, Request, Review, Takeover

Owner: Safety

Output:

- policy decision shape
- grant and denial shape
- Request creation rules
- Review decision rules
- approval narrowing rules
- takeover lock rules
- reconciliation rules

Done when:

- policy-denied action creates Request
- Request cannot resolve without Review
- Review can approve, deny, narrow, correct, take over, or request revision
- takeover rejects stale autonomous continuation

## Milestone 4: Contribution And Evidence

Owner: Evidence

Output:

- Contribution record
- EvidenceItem record
- EvidenceManifest record
- artifact reference shape
- limitation shape
- export profile

Done when:

- human, agent, service, and shared contributions are distinguishable
- EvidenceManifest references policy decisions, requests, reviews,
  contributions, artifacts, and limitations
- evidence is captured during work, not reconstructed after completion

## Milestone 5: Governed Learning

Owner: Learning

Output:

- LearningRecord
- MemoryProposal
- SkillProposal
- provenance rules
- review-state rules
- scope rules

Done when:

- learning can be attributed to human, agent, or pair
- HumanWorker and AgentWorker can both improve from the same WorkSession
- memory changes require proposal and review state
- skill changes require proposal and review state
- unreviewed learning cannot become durable protocol memory

## Milestone 6: Conformance Suite

Owner: Developer Experience

Output:

- golden-path conformance tests
- failure-mode conformance tests
- export conformance tests
- integration checklist

Done when a host can prove:

- WorkSession is the source of truth
- Policy gates autonomous action
- blocked action creates Request
- Review resolves Request
- Takeover prevents stale continuation
- Contributions are attributable
- EvidenceManifest is portable
- learning is governed

## Milestone 7: Examples And Public Docs

Owner: Developer Experience

Output:

- protocol README
- glossary
- protocol diagrams
- JSON examples
- host integration guide
- evaluation-system integration guide
- host/product integration note
- interactive simulation

Done when:

- a team can understand Jarvis without knowing any specific product
- a product can implement Jarvis without inheriting execution assumptions
- the public simulation matches the protocol definition

## v0.1 Acceptance

v0.1 is accepted when:

- protocol schemas are stable enough for implementation
- conformance tests cover the golden path
- no protocol contract names a cloud, database, sandbox, or deployment
  platform
- public docs describe Jarvis as protocol only
- live simulation describes Jarvis as protocol only

## v0.2 Evidence And Learning Beta

Goal: strengthen the compounding loop.

Output:

- richer contribution taxonomy
- stronger evidence export profiles
- limitation and uncertainty records
- learning proposal review workflows
- memory scope compatibility rules
- skill proposal compatibility rules

Done when:

- evaluation systems can evaluate a task using Jarvis evidence records
- host products can show review, learning, and contribution history without
  changing protocol semantics
- external products can export compatible EvidenceManifest records

## v0.3 Ecosystem Conformance

Goal: make Jarvis implementable outside the original host products.

Output:

- host conformance suite
- compatibility badges
- version negotiation rules
- migration examples
- public implementation checklist

Done when:

- two independent host shapes can pass the same protocol conformance tests
- protocol records remain portable across products
- implementation-private fields stay outside Jarvis exports
- compatible hosts can exchange WorkSession evidence without sharing
  infrastructure

## v1.0 Stable Protocol

Goal: freeze the protocol surface.

Output:

- stable protocol schemas
- stable event envelope
- stable EvidenceManifest export format
- stable conformance suite
- compatibility policy
- migration policy

Done when:

- v1.0 records can be read by future compatible implementations
- product implementations do not need to adopt any Jarvis-owned execution stack
- Jarvis remains protocol-only

## Risk Register

### Execution Creep

Risk: Jarvis starts defining how agents run.

Control: every execution, cloud, sandbox, database, queue, and deployment
choice belongs to products and hosts.

### Product Creep

Risk: Jarvis becomes a product workspace.

Control: products implement Jarvis; Jarvis does not inherit product UI,
identity, operations, or enterprise controls.

### Task-System Creep

Risk: Jarvis becomes a task or evaluation system.

Control: task systems own tasks, rubrics, evaluation, and settlement. Jarvis
owns the collaboration record that can be evaluated.

### Weak Evidence

Risk: Evidence is reconstructed after work and loses trust.

Control: EvidenceManifest entries are captured during the WorkSession.

### Silent Learning

Risk: agent memory mutates without human review.

Control: learning becomes MemoryProposal or SkillProposal until reviewed.

## Immediate Next Actions

1. Keep the repository protocol-only.
2. Keep execution and cloud ownership outside the protocol.
3. Use `11-core-protocol-objects.md` as the source of truth for core terms.
4. Draft JSON examples for each protocol contract.
5. Define conformance tests for the golden path.
6. Update the live simulation to show host/execution as outside Jarvis.
