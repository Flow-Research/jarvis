# Package Contracts

Jarvis v0 ships protocol packages only.

Jarvis does not ship execution packages, cloud packages, local execution
packages, database packages, sandbox packages, or product UI packages. Products
implement Jarvis on any infrastructure by depending on the protocol contracts.

## Package Graph

```txt
@jarvis/protocol
  no Jarvis package dependencies

@jarvis/memory
  depends on @jarvis/protocol

@jarvis/policy
  depends on @jarvis/protocol

@jarvis/skills
  depends on @jarvis/protocol, @jarvis/memory, @jarvis/policy

@jarvis/evidence
  depends on @jarvis/protocol

@jarvis/conformance
  depends on all Jarvis protocol packages
```

Protocol packages never import product packages, infrastructure packages, model
SDKs, database clients, cloud SDKs, sandbox SDKs, or UI frameworks.

## `@jarvis/protocol`

Owns the core protocol contracts:

Canonical object definitions live in
[11-core-protocol-objects.md](./11-core-protocol-objects.md). The package
exports must match that document.

- ids
- Actor
- Worker
- HumanWorker
- AgentWorker
- WorkSession
- Policy
- PolicyDecision
- Request
- Review
- Takeover
- Contribution
- EvidenceManifest reference fields
- LearningRecord
- MemoryProposal reference fields
- SkillProposal reference fields
- event envelope
- trace context
- status transitions
- error envelope

Exports:

```txt
JarvisId
Actor
Worker
HumanWorker
AgentWorker
WorkSession
WorkSessionStatus
Policy
PolicyDecision
Request
RequestStatus
Review
ReviewDecision
Takeover
Contribution
ContributionType
EvidenceManifestRef
LearningRecord
MemoryProposalRef
SkillProposalRef
JarvisEvent
TraceContext
JarvisError
```

Forbidden imports:

- cloud SDKs
- model SDKs
- database clients
- filesystem libraries
- sandbox libraries
- queue libraries
- UI frameworks
- product packages

Release tests:

- JSON serialization is stable.
- canonical event serialization is stable.
- event envelopes validate required ids and timestamps.
- event hashes exclude `event_hash` and signature fields.
- mutating requests reject missing `Jarvis-Protocol-Version`.
- mutating requests reject missing `Jarvis-Actor-Id`.
- mutating requests reject missing `Jarvis-Idempotency-Key`.
- mutating requests reject missing `Jarvis-Request-Timestamp`.
- mutating requests reject missing `Jarvis-Expected-WorkSession-Revision`.
- mutating requests reject missing `Jarvis-Previous-Event-Hash`.
- WorkSession status transitions reject invalid transitions.
- stale WorkSession revision rejects mutation.
- stale previous event hash rejects mutation.
- final EvidenceManifest export requires completed, failed, cancelled, or closed
  WorkSession state.
- Human resolution of a Request requires Review or Takeover.
- invalid Request transitions reject mutation.
- ApprovalScope rejects stale, mismatched, expired, or over-broad execution.
- repeated unchanged Requests reject as livelock or supersede without weakening
  policy fields.
- Takeover creates a lock epoch.
- Takeover rejects stale AgentWorker continuation.
- Takeover resume requires reconciliation refs.
- shared Contribution preserves individual contributor refs.
- EvidenceManifest references policy decisions, requests, reviews, takeovers,
  contributions, artifacts, evidence items, and limitations.
- EvidenceManifest rejects forbidden export fields.
- MemoryProposal rejects model-derived or tool-derived self-confirmation.
- SkillProposal rejects activation without review and rejects tool access
  expansion without policy review.
- OutcomeReport creates or references LearningRecord without mutating sealed
  WorkSession or EvidenceManifest.
- attribution/evidence/learning rejection ids include
  `missing_contribution_actor`, `invalid_contributor_refs`,
  `shared_contribution_without_individual_refs`, `evidence_after_the_fact`,
  `missing_evidence_event_refs`, `invalid_evidence_export_state`,
  `forbidden_export_field`, `silent_memory_mutation`,
  `silent_skill_activation`, `model_self_confirmed_memory`,
  `tool_self_confirmed_memory`,
  `skill_expands_tool_access_without_policy_review`,
  `sealed_work_session_mutation`, `sealed_evidence_mutation`, and
  `outcome_report_without_learning_record`.

## `@jarvis/policy`

Owns policy semantics:

- autonomy levels
- grants
- risk classes
- grant vector resolution
- request creation
- approval narrowing
- takeover rules
- audit event shape

Exports:

```txt
PolicyEngine
GrantResolver
CapabilityGrant
RiskClass
PolicyDecision
RequestFactory
ApprovalScope
TakeoverRule
```

Forbidden imports:

- raw tool implementations
- product packages
- infrastructure packages

Release tests:

- uncovered action dimensions deny execution.
- conflicting grants deny and create a Request.
- approval narrows scope when the human restricts the request.
- stale action after takeover is rejected.

## `@jarvis/memory`

Owns memory semantics:

- memory scopes
- memory lifecycle
- provenance
- trust labels
- context manifest
- retrieval policy shape
- correction pipeline
- memory proposal rules

Exports:

```txt
MemoryRecord
MemoryScope
MemoryLifecycleState
MemoryTrustLabel
ContextManifest
MemoryProposal
MemoryProposalStatus
MemorySelection
```

Forbidden imports:

- model provider packages
- storage packages
- product packages

Release tests:

- model-derived memory cannot confirm itself.
- untrusted tool output cannot become durable memory without review.
- memory proposals require provenance.

## `@jarvis/skills`

Owns procedural memory semantics:

- skill manifest
- skill inventory shape
- skill activation gates
- skill versioning
- skill proposal rules
- review checks

Exports:

```txt
SkillManifest
SkillInventory
SkillActivationGate
SkillProposal
SkillProposalStatus
SkillVersion
```

Forbidden imports:

- connector SDKs
- execution packages
- product packages

Release tests:

- unreviewed skill proposals stay inactive.
- changed skill hashes require review.
- activation gates block skills outside their scope.

## `@jarvis/evidence`

Owns portable evidence semantics:

- evidence item shape
- evidence manifest shape
- contribution references
- policy decision references
- request/review references
- artifact references
- limitations
- export profiles

Exports:

```txt
EvidenceItem
EvidenceManifest
EvidenceExportProfile
EvidenceLimitation
ContributionRef
ArtifactRef
```

Forbidden imports:

- storage packages
- product packages
- infrastructure packages

Release tests:

- EvidenceManifest references WorkSession.
- EvidenceManifest includes policy decisions, requests, reviews,
  contributions, artifacts, and limitations.
- redacted export remains derived from the same protocol event chain.

## `@jarvis/conformance`

Owns implementation conformance tests.

It verifies that any product claiming Jarvis compatibility implements the
protocol behavior correctly.

Conformance tests check:

- WorkSession lifecycle
- policy-denied action to Request
- Request to Review or Takeover resolution
- takeover and reconciliation
- contribution attribution
- evidence capture
- governed learning
- portable export

The conformance package tests behavior. It does not prescribe infrastructure.
