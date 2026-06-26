# v0.1 Acceptance Review Spec

This spec defines the gates for accepting Jarvis v0.1 as Protocol Alpha.

The review accepts v0.1 only after every gate passes. A failed gate creates a
blocker. Blockers require a fix and linked evidence before acceptance.
Deferrals apply only to non-blocking future work outside the v0.1 acceptance
gates.

Jarvis remains protocol-only throughout the review.

## Gate 1: Protocol Contract

The protocol contract passes when:

```txt
README, AGENTS.md, protocol docs, planning docs, and examples all define
Jarvis as the human-agent collaboration and learning-loop protocol.
```

Required proof:

- core object names match across all public docs
- `WorkSession` remains the central record
- `HumanWorker` and `AgentWorker` remain first-class workers and actors
- `PolicyDecision` exists before accepted AgentWorker protocol state
- `Request` remains scoped deferral, not chat, notification, or authority
- `Review` and `Takeover` remain the only human-resolution paths for Request
- `Contribution` records who did what
- `EvidenceManifest` exports portable proof without host-private fields
- `LearningRecord`, `MemoryProposal`, and `SkillProposal` preserve governed
  learning
- `OutcomeReport` carries post-session feedback without sealed-record mutation
- protocol event envelope remains append-only and attributable
- portable export format excludes forbidden host-private fields
- version negotiation and capability negotiation remain protocol-owned
- extension rules require namespaced extensions and reject core-field override
- protocol error ids and error envelope remain public and portable
- conformance expectations remain protocol-owned and host-implementation neutral

The gate fails when any protocol source assigns host implementation ownership
to Jarvis.

## Gate 2: OpenAPI Binding

The OpenAPI binding passes when:

```txt
docs/openapi/jarvis-openapi.yaml encodes the v0.1 protocol objects,
operations, security headers, error envelope, and examples without
host-private fields.
```

Required proof:

- all core schemas exist
- required fields match `11-core-protocol-objects.md`
- core operations exist for WorkSession, event, PolicyDecision, Request,
  Review, Takeover, Contribution, LearningRecord, MemoryProposal,
  SkillProposal, EvidenceManifest export, Worker, Actor, and OutcomeReport
- mutating operations require OpenAPI security through host authentication
- WorkSession-scoped mutations require the six Jarvis mutation headers
- non-WorkSession mutations require the four Jarvis mutation headers
- Worker registration, Actor registration, and OutcomeReport submission do not
  require fake WorkSession revision or previous event hash values
- WorkSession-scoped reads and export reads require host authentication,
  `Jarvis-Protocol-Version`, and `Jarvis-Actor-Id`
- WorkSession-scoped reads and export reads verify Actor read authority
- protocol errors expose public error fields only

The gate fails when OpenAPI allows unauthenticated mutation, unauthorized read,
or portable protocol records that require runtime ids, database ids, UI state,
credentials, deployment details, billing data, private scores, or provider
secrets.

## Gate 3: Conformance Surface

The conformance surface passes when:

```txt
docs/conformance/checklist.md, fixtures, and validator checks prove the golden
path and required rejection gates.
```

Required proof:

- golden-path fixture validates
- invalid fixtures validate
- fixture-backed rejection ids match the checklist
- unsupported non-fixture rejection ids remain documented without claiming
  fixture coverage
- validator checks required headers, expected revision, previous event hash,
  Actor authority, PolicyDecision ordering, Request resolution, Takeover epoch,
  forbidden host-private fields, and sealed-record mutation
- public checklist covers ApprovalScope bounds
- public checklist covers Contribution attribution
- public checklist covers EvidenceManifest export completeness and capture
  timing
- public checklist covers MemoryProposal and SkillProposal governance
- public checklist covers OutcomeReport learning hook
- public checklist covers protocol error envelope
- public checklist covers capability negotiation and extension rejection

The gate fails when a fake implementation skips policy, review, evidence,
learning, or mutation-header enforcement and still appears compatible.

## Gate 4: Compatibility Examples

Compatibility examples pass when:

```txt
examples show existing human-agent work mapping into Jarvis records without
rewriting the agent or moving host behavior into Jarvis.
```

Required proof:

- compatible host mapping includes at least two host shapes
- existing-agent compatibility preserves native execution
- examples map permissions into Policy, PolicyDecision, Request, Review,
  ApprovalScope, and Takeover
- examples map connectors and tools into host-owned execution with
  protocol-visible evidence refs
- examples map completed work into Contribution, EvidenceManifest,
  LearningRecord, MemoryProposal, SkillProposal, and OutcomeReport
- examples do not define adapters, wrappers, host runtime behavior, host UI
  behavior, model calls, tool execution, storage, auth, billing, scoring,
  payment, or deployment

The gate fails when an example makes Jarvis own Garden-like product behavior,
native agent runtime behavior, external task-system behavior, or connector
execution.

## Gate 5: Public README And Non-Normative Simulation

Public docs pass when:

```txt
README explains Jarvis as protocol-only. The non-normative simulation, when
present, stays aligned with the protocol boundary and does not become protocol
proof.
```

Required proof:

- README one-line definition matches protocol docs
- README positions Jarvis beside MCP, A2A, and AG-UI without replacing them
- README states that hosts own UI, storage, auth, execution, models, tools,
  memory engines, deployment, monitoring, and workflow
- simulation is treated as public explanation only
- simulation remains static explanation, not host UI implementation
- simulation does not define additional protocol objects, operations, or
  conformance rules

The gate fails when public docs make Jarvis sound like a personal agent,
runtime, product workspace, model provider, cloud stack, UI framework, or
agent framework.

## Gate 6: Boundary And Wording

Boundary and wording pass when:

```txt
all changed markdown uses direct protocol language and passes the wording
guard.
```

Required proof:

- protocol statements use direct ownership language
- host-owned responsibilities stay outside Jarvis
- SDK language stays limited to protocol implementation helpers
- docs do not use soft wording for locked protocol rules
- `python3 scripts/check_protocol_wording.py` passes

The gate fails when a document weakens locked decisions or describes Jarvis as
guidance, product strategy, host implementation, or third-party review.

## Gate 7: Local Validation

Local validation passes when this command set passes:

```txt
python3 scripts/check_markdown_links.py
python3 scripts/check_protocol_wording.py
python3 scripts/check_openapi_contract.py
python3 scripts/check_conformance_fixtures.py
git diff --check
```

The gate fails when any required protocol local check fails.

The non-normative demo has a separate public-readiness check while the demo
files remain in the repo:

```txt
node --check demo/assets/app.js
```

Demo syntax failure creates a public-readiness finding. It does not fail the
protocol acceptance gate unless the demo misrepresents Jarvis as a product,
runtime, framework, host UI, or host implementation.

## Decision Rule

The v0.1 acceptance decision MUST record:

```txt
accepted gates
resolved blockers
future-work deferrals outside acceptance gates
remaining risks
release notes required before tag
next-phase entry scope
```

The decision MUST NOT mark v0.1 accepted until all gates pass, all blockers are
resolved, and the decision record links the evidence for each accepted gate.
Future-work deferrals MUST stay outside the v0.1 acceptance gates.
