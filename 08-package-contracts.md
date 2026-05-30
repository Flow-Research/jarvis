# Package Contracts

Jarvis v0 ships protocol packages only.

Jarvis does not ship execution packages, cloud packages, local execution
packages, database packages, sandbox packages, or product UI packages. Products
can implement Jarvis on any infrastructure by depending on the protocol
contracts.

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

- ids
- Actor
- Worker
- HumanWorker
- AgentWorker
- WorkSession
- Policy
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
- event envelopes validate required ids and timestamps.
- WorkSession status transitions reject invalid transitions.
- Request resolution requires Review.
- Takeover creates a lock epoch.

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
- approval can narrow scope.
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
- Request to Review resolution
- takeover and reconciliation
- contribution attribution
- evidence capture
- governed learning
- portable export

The conformance package tests behavior. It does not prescribe infrastructure.
