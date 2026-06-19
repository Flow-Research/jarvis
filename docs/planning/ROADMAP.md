# Jarvis Roadmap

Jarvis is the open-source human-agent collaboration and learning-loop
compatibility protocol.

The roadmap turns the protocol into a stable OpenAPI 3.1 contract,
conformance tests, examples, and documentation. It does not create an execution
stack.

For the immediate execution plan, see
[12-30-day-roadmap.md](./12-30-day-roadmap.md).

For the OpenAPI entry gate, see
[14-protocol-lock.md](../protocol/14-protocol-lock.md).

## Current Status

Week 1 protocol lock is complete.

Current active work: Week 4 compatible examples and public story.

Week 2 completed the OpenAPI 3.1 component syntax, path syntax, security scheme
encoding, protocol examples, and conformance entry rules from the locked Week 1
protocol decisions.

Week 3 completed protocol compatibility mapping, conformance fixtures, fixture
validation, and existing-agent compatibility proof. Jarvis does not add or own
adapters, runtimes, wrappers, host behavior, or integration code.

Week 4 starts from conformance evidence and prepares compatible examples,
public README tightening, published conformance checklist, and public story.

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
- OpenAPI 3.1 communication binding
- protocol compatibility mapping
- compatibility conformance expectations
- version negotiation rules
- capability negotiation rules
- conformance tests
- interoperability rules

Jarvis does not own:

- UI
- authentication
- host implementation details
- task/evaluation implementation details
- host/tool/environment implementation details
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

Hosts own those responsibilities.

## Release Strategy

```txt
v0.1 Protocol Alpha
  stable vocabulary, OpenAPI 3.1 contract, event envelope, and golden-path
  conformance

v0.2 Evidence And Learning Beta
  stronger EvidenceManifest, Contribution, MemoryProposal, and SkillProposal
  contracts

v0.3 Ecosystem Conformance
  host conformance suite, examples, and host integration guides

v1.0 Stable Protocol
  stable public protocol, compatibility rules, export format, and migration
  policy
```

## v0.1 Protocol Alpha

Goal: prove the smallest complete human-agent collaboration loop.

The alpha proves that the loop is portable, not tied to a single host or
execution stack.

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

- OpenAPI 3.1 contract for all core contracts
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
- protocol compatibility mapping
- one real existing-agent compatibility proof
- valid and invalid conformance fixtures
- version and capability negotiation
- one protocol simulation that visualizes the proof path
- compatible implementation guide

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
- host implementation

## Milestone 0: Protocol Lock

Status: complete.

Owner: Architecture

Output:

- official definition is frozen
- core terms are frozen
- system boundaries are frozen
- non-goals are frozen

Done when:

- README, Principles, Architecture, Package Contracts, Protocol v0.1, and
  Acceptance Criteria all agree.
- no Jarvis document assigns execution, cloud, database, sandbox, or deployment
  ownership to Jarvis.

## Milestone 1: OpenAPI Contract

Status: complete.

Owner: Protocol

Output:

- OpenAPI 3.1 document
- component schemas for Worker, Actor, HumanWorker, AgentWorker, WorkSession,
  JarvisEvent, Policy, PolicyDecision, Request, Review, Takeover,
  Contribution, EvidenceManifest, LearningRecord, MemoryProposal, and
  SkillProposal
- paths for core protocol operations
- security scheme and required protocol headers
- protocol error responses
- examples for WorkSession, Request, Review, and export

Done when:

- every component matches `11-core-protocol-objects.md`
- OpenAPI describes the HTTP communication binding
- required fields are explicit
- status values are enumerated
- references are typed
- no component or path requires implementation-private fields

## Milestone 2: WorkSession Lifecycle

Status: complete.

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
- events remain attributable to an Actor

## Milestone 3: Policy, Request, Review, Takeover

Status: complete.

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
- Request cannot reach human-resolved state without Review or Takeover
- Request blocks only its declared scope
- Review approves, denies, narrows, corrects, takes over, or requests revision
- takeover rejects stale autonomous continuation

## Milestone 4: Contribution And Evidence

Status: complete.

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

Status: complete.

Owner: Learning

Output:

- LearningRecord
- MemoryProposal
- SkillProposal
- provenance rules
- review-state rules
- scope rules

Done when:

- learning is attributed to human, agent, or pair
- HumanWorker and AgentWorker both improve from the same WorkSession
- memory changes require proposal and review state
- skill changes require proposal and review state
- unreviewed learning cannot become durable protocol memory

## Milestone 6: Conformance Suite

Status: complete.

Owner: Developer Experience

Output:

- golden-path conformance tests
- failure-mode conformance tests
- export conformance tests
- integration checklist

Done when a host proves:

- WorkSession is the source of truth
- Policy gates autonomous action
- blocked action creates Request
- Review or Takeover resolves Request
- Takeover prevents stale continuation
- Contributions are attributable
- EvidenceManifest is portable
- learning is governed

## Milestone 7: Examples And Public Docs

Status: active.

Owner: Developer Experience

Output:

- protocol README
- glossary
- protocol diagrams
- OpenAPI examples
- compatible implementation guide
- evaluation-system integration guide
- host integration note
- interactive simulation

Done when:

- a team understands Jarvis without knowing any specific host
- a host implements Jarvis without inheriting execution assumptions
- the public simulation matches the protocol definition

## v0.1 Acceptance

v0.1 is accepted when:

- OpenAPI contract is stable enough for implementation
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

- external reviewers and systems consume Jarvis EvidenceManifest records
- implementations expose review, learning, and contribution history without
  changing protocol semantics
- external systems export compatible EvidenceManifest records

## v0.3 Ecosystem Conformance

Goal: make Jarvis implementable across independent hosts.

Output:

- host conformance suite
- compatibility badges
- version negotiation rules
- migration examples
- public implementation checklist

Done when:

- two independent host shapes pass the same protocol conformance tests
- protocol records remain portable across compatible hosts
- implementation-private fields stay outside portable Jarvis records
- compatible hosts exchange WorkSession evidence without sharing
  infrastructure

## v1.0 Stable Protocol

Goal: freeze the protocol surface.

Output:

- stable OpenAPI contract
- stable event envelope
- stable EvidenceManifest export format
- stable conformance suite
- compatibility policy
- migration policy

Done when:

- future compatible implementations read v1.0 records
- host implementations do not need to adopt any Jarvis-owned execution stack
- Jarvis remains protocol-only

## Risk Register

### Execution Creep

Risk: Jarvis starts defining how agents run.

Control: every execution, cloud, isolation, storage, queue, and deployment
choice belongs to hosts.

### Host Implementation Creep

Risk: Jarvis becomes a host workspace.

Control: hosts implement Jarvis; Jarvis does not inherit UI,
identity, operations, or enterprise controls.

### Task-System Creep

Risk: Jarvis becomes a task or evaluation system.

Control: task systems own tasks, rubrics, evaluation, and settlement. Jarvis
owns the collaboration record that external reviewers and systems evaluate.

### Weak Evidence

Risk: Evidence is reconstructed after work and loses trust.

Control: EvidenceManifest entries are captured during the WorkSession.

### Silent Learning

Risk: agent memory mutates without human review.

Control: learning becomes MemoryProposal or SkillProposal until reviewed.

## Immediate Next Actions

1. Keep the repository protocol-only.
2. Keep execution and cloud ownership outside the protocol.
3. Use `11-core-protocol-objects.md`, `jarvis-openapi.yaml`, and
   `docs/conformance/` as the source of truth for Week 4 work.
4. Prepare compatible examples from the conformance gate.
5. Publish the conformance checklist from existing fixtures and rejection gates.
6. Tighten public README language around Jarvis as protocol only.
7. Update the public simulation to show the OpenAPI proof path.
8. Keep adapter code, wrappers, host behavior, and integration code outside
   Jarvis.
