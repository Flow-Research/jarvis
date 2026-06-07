# Week 1 Execution Spec

Week 1 locks the Jarvis protocol before OpenAPI contract drafting starts.

This week does not build Garden POC, runtime features, adapters, product UI, or
demo flows. This week locks the protocol meaning, lifecycle, zero-trust
security boundary, and positioning needed for Week 2 OpenAPI work.

## Week 1 Goal

Freeze the core protocol vocabulary, communication strategy, and security
boundary.

Week 1 is complete when:

- every protocol object has a clear reason to exist
- every core lifecycle transition is named
- PolicyDecision semantics are locked
- Request, Review, and Takeover lifecycle rules are locked
- EvidenceManifest, Contribution, LearningRecord, MemoryProposal,
  SkillProposal, and OutcomeReport semantics are locked
- OpenAPI 3.1 remains the machine-readable communication contract
- zero-trust headers, security schemes, and forbidden export fields are locked
- Jarvis is explained without relying on Garden, Workstream, Harnessy, any
  runtime, or any product proof
- no document describes Jarvis as a runtime, product, agent framework, or
  personal agent

## Chunk Gate

Every Week 1 chunk follows this gate.

```txt
1. Create or update the chunk spec.
2. Implement the document changes for that chunk.
3. Run deterministic local checks.
4. Spawn at least four reviewer agents.
5. Give every reviewer the repo docs, changed files, and chunk spec.
6. Wait for all reviewer reports.
7. Integrate valid findings.
8. Record rejected findings with concrete reasons.
9. Run final checks.
10. Open a PR for the chunk.
```

A chunk is not complete without the Zero-Trust Security Reviewer plus at least
three other completed reviewer reports.

The reviewer pool is:

```txt
Protocol Thesis Reviewer
  Checks that Jarvis stays the human-agent collaboration and learning-loop
  protocol.

Zero-Trust Security Reviewer
  Checks replay protection through `Jarvis-Idempotency-Key` and
  `Jarvis-Request-Timestamp`, actor authority through `Jarvis-Actor-Id`,
  WorkSession revision safety through `Jarvis-Expected-WorkSession-Revision`,
  event hash linkage through `Jarvis-Previous-Event-Hash`, export boundaries,
  and forbidden host-private fields.

Chief Engineer Reviewer
  Checks architecture, naming, object boundaries, maintainability, and
  implementation readiness.

Conformance And Interop Reviewer
  Checks that existing agents, hosts, and external products map into Jarvis
  without runtime rewrites or product-specific assumptions.

Human Workflow Reviewer
  Checks that Requests, Reviews, Takeovers, Contributions, Evidence,
  LearningRecords, MemoryProposals, and SkillProposals preserve human
  judgment, agent autonomy, pair learning, and understandable work handoff.
```

Every chunk must include the Zero-Trust Security Reviewer plus at least three
other reviewer lanes. Five lanes are required for high-risk chunks.

## Required Reviewer Context

Every reviewer receives:

- [AGENTS.md](../../../AGENTS.md)
- [README.md](../../../README.md)
- [docs/protocol/04-work-sessions.md](../../protocol/04-work-sessions.md)
- [docs/protocol/11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
- [docs/protocol/14-protocol-lock.md](../../protocol/14-protocol-lock.md)
- [docs/protocol/15-openapi-communication-binding.md](../../protocol/15-openapi-communication-binding.md)
- [docs/reviews/13-protocol-readiness-review.md](../../reviews/13-protocol-readiness-review.md)
- [docs/planning/12-30-day-roadmap.md](../12-30-day-roadmap.md)
- the current chunk spec
- the changed files

## Local Checks

Every chunk that changes protocol semantics, OpenAPI strategy, lifecycle rules,
portable export, or conformance rules also runs a zero-trust invariant scan for
the required headers, actor authority, revision safety, previous event hash,
PolicyDecision requirement, and forbidden export fields.

Every chunk runs:

```txt
git diff --check
python3 scripts/check_markdown_links.py
python3 scripts/check_week1_wording.py
```

If those scripts do not exist in the branch, the chunk adds them before the PR.

Week 1 chunks do not touch demo assets. Demo checks belong to a later
product-proof or simulation update, not this protocol-lock gate.

Chunks that touch roadmap sheets also run:

```txt
CSV sanity check
XLSX sanity check
```

## Stale Wording Scan

The scan rejects wording that violates the boundaries in `AGENTS.md`, turns
Jarvis into a host-owned implementation concern, makes product proof active
before the conformance gate, or makes locked protocol decisions sound optional.

## Week 1 Chunks

### Chunk 0: Execution Gate

Purpose: lock the Week 1 working method.

Outputs:

- Week 1 chunk spec directory
- reviewer lanes
- required reviewer context
- local checks
- stale wording scan
- completion rules

Done when:

- the chunk gate exists in docs
- Zero-Trust Security Reviewer plus at least three other reviewers validate the
  gate
- findings are integrated or rejected with reasons
- PR is opened

### Chunk 1: Core Object And Extension Field Lock

Purpose: define required fields and reason-to-exist for every core object and
the OutcomeReport extension.

Spec: [chunk-1-core-object-field-lock.md](./chunk-1-core-object-field-lock.md)

Core objects:

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

Extension object:

```txt
OutcomeReport
```

Outputs:

- required fields
- optional fields
- forbidden fields
- stable ids and references
- ownership boundary for every field
- host-private field exclusion rules

Done when:

- every object has a reason to exist
- every required field has a protocol reason
- no object owns host implementation details
- every object maps into OpenAPI `components.schemas`

### Chunk 2: WorkSession Lifecycle Lock

Purpose: lock WorkSession states and transitions.

Spec: [chunk-2-worksession-lifecycle-lock.md](./chunk-2-worksession-lifecycle-lock.md)

Outputs:

- WorkSession state list
- allowed transitions
- rejected transitions
- revision rules
- event hash-chain rules
- close, fail, cancel, and export rules

Done when:

- a host knows exactly when WorkSession state changes
- stale writes are rejected
- event order is verifiable
- export is only valid from a permitted lifecycle state

### Chunk 3: Policy, Request, Review, And Takeover Lock

Purpose: lock the human judgment and control plane.

Spec: [chunk-3-control-plane-lock.md](./chunk-3-control-plane-lock.md)

Outputs:

- PolicyDecision semantics
- Request lifecycle
- Request blocking scope
- Request and non-blocking communication boundary
- anti-livelock Request rules
- Review lifecycle
- Takeover lifecycle
- escalation rules
- review-required action rules
- denied action rules
- takeover lock epoch rules

Done when:

- AgentWorker actions outside policy create Requests
- Requests block only their declared scope
- HumanWorker judgment records Reviews or Takeovers
- approval is scoped and bounded
- Takeover races are rejected
- AgentWorker resumes only after allowed protocol state

### Chunk 4: Contribution, Evidence, And Learning Lock

Purpose: lock attribution, proof, and shared learning.

Spec: [chunk-4-evidence-learning-lock.md](./chunk-4-evidence-learning-lock.md)

Outputs:

- Contribution ledger minimum shape
- EvidenceManifest minimum export shape
- evidence capture timing rules
- LearningRecord semantics
- MemoryProposal review rules
- SkillProposal review rules
- OutcomeReport semantics

Done when:

- human, agent, pair, and service contributions are distinguishable
- evidence is captured during work
- learning is governed
- memory and skill updates do not silently mutate durable state
- OutcomeReport does not turn Jarvis into an evaluation system

### Chunk 5: OpenAPI Security Entry Lock

Purpose: lock the OpenAPI inputs required before Week 2 drafting.

Outputs:

- required headers
- security scheme requirements
- protocol error model
- version negotiation rules
- capability negotiation rules
- extension namespace rules
- forbidden export fields

Done when:

- OpenAPI contract authors have exact inputs
- every mutating operation requires `Jarvis-Protocol-Version`,
  `Jarvis-Actor-Id`, `Jarvis-Idempotency-Key`, `Jarvis-Request-Timestamp`,
  `Jarvis-Expected-WorkSession-Revision`, and
  `Jarvis-Previous-Event-Hash`
- Worker and Actor reference registration does not become identity ownership
- OpenAPI 3.1 remains the default host-facing binding

### Chunk 6: Positioning And Adoption Lock

Purpose: lock why Jarvis exists beside existing agents and protocols.

Outputs:

- positioning against MCP
- positioning against A2A
- positioning against ACP
- positioning against AG-UI
- positioning against agent SDKs
- positioning against coding agents and personal agents
- one-paragraph Jarvis explanation

Done when:

- Jarvis is clearly not another agent
- Jarvis is clearly not another runtime
- existing agents remain first-class
- adoption argument centers on policy, review, attribution, evidence, and
  shared learning

## Chunk Review Record

Each chunk PR must include:

```txt
Reviewer lanes completed:
- Protocol Thesis Reviewer
- Zero-Trust Security Reviewer
- Chief Engineer Reviewer
- Conformance And Interop Reviewer
- Human Workflow Reviewer

Zero-trust decision:
- replay protection:
- actor authority:
- WorkSession revision safety:
- event hash linkage:
- PolicyDecision requirement:
- export boundary:
- forbidden host-private fields:

Findings integrated:
- ...

Findings rejected:
- finding
- reason

Checks:
- ...
```

No chunk is complete without this review record.
