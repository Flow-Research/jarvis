# Chunk 2: TypeScript Protocol Types And Validators

Issue: #65.

Chunk 2 defines the TypeScript helper package for Jarvis v0.1 protocol records.

## Scope

This chunk creates TypeScript helper tooling for protocol records only.

It includes:

- generated or maintained protocol types
- protocol error types
- mutation header helpers
- read header helpers
- WorkSession event envelope validator
- event hash-chain helpers
- Request validator
- Review validator
- Takeover validator
- Contribution validator
- EvidenceManifest validator
- LearningRecord validator
- MemoryProposal validator
- SkillProposal validator
- OutcomeReport validator
- fixture-backed tests

It does not create an agent runtime, model router, tool executor, host adapter,
wrapper, UI kit, auth provider, storage backend, queue backend, memory engine,
sandbox, billing system, scoring system, payment system, deployment system, or
workflow engine.

## Required Inputs

Chunk 2 starts after Chunk 1 locks the SDK boundary.

Required inputs:

- [chunk-1-sdk-boundary-package-plan.md](./chunk-1-sdk-boundary-package-plan.md)
- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../conformance/fixtures/valid/golden-path.json](../../conformance/fixtures/valid/golden-path.json)
- [../../conformance/fixtures/invalid/](../../conformance/fixtures/invalid/)
- [../../protocol/15-openapi-communication-binding.md](../../protocol/15-openapi-communication-binding.md)

## Type Surface

The TypeScript package MUST expose every OpenAPI component schema from
`docs/openapi/jarvis-openapi.yaml`.

The v0.1.0 type surface includes:

- AccountabilityScope
- Actor
- ActorType
- Worker
- WorkerType
- HumanWorker
- AgentWorker
- ApprovalBoundary
- ApprovalScope
- AuthorityScope
- AutonomyLevel
- BlockingScope
- CanonicalizationProfile
- CapabilityRef
- ContributionRole
- ContributionScope
- ContributionType
- ContributorRef
- ContributorType
- DataSensitivity
- EscalationRule
- EventAuthority
- EvidenceItemRef
- ExportProfile
- WorkSession
- WorkSessionStatus
- JarvisEvent
- JarvisEventPayload
- JarvisId
- Policy
- PolicyActionRequest
- PolicyActionRule
- PolicyConstraint
- PolicyDecision
- PolicyDecisionResult
- PolicyRequestLimits
- Request
- RequestOption
- RequestStatus
- RequestType
- Review
- ReviewDecision
- RiskClass
- SafeFallback
- Takeover
- TakeoverScope
- TakeoverState
- Contribution
- EvidenceManifest
- LearningRecord
- LearningReviewState
- LearningSubjectType
- MemoryProposal
- MemoryProposalStatus
- NamespacedExtensions
- OpaqueRef
- SkillProposal
- SkillProposalStatus
- OutcomeReport
- PortableValue
- ProposalTargetType
- ProtocolError
- ProtocolErrorId
- ProtocolTraceContext
- Timestamp
- protocol error envelope
- mutation headers
- read headers

## Validator Surface

Validators MUST reject:

- missing required fields
- invalid protocol version
- missing Actor identity
- unauthorized Actor
- missing idempotency key on mutation
- stale request timestamp
- missing expected WorkSession revision on WorkSession-scoped mutation
- missing previous event hash on WorkSession-scoped mutation
- actor mismatch between body and `Jarvis-Actor-Id`
- missing PolicyDecision before accepted AgentWorker action state
- Request resolution without Review or Takeover
- invalid ApprovalScope
- stale Takeover continuation
- forbidden host-private export fields
- sealed WorkSession mutation
- sealed EvidenceManifest mutation
- silent memory mutation
- silent skill activation
- OutcomeReport without LearningRecord reference

## Test Requirements

Chunk 2 tests MUST include:

- valid golden-path fixture
- invalid fixture set
- header helper tests
- event hash-chain tests
- EvidenceManifest export tests
- Request/Review/Takeover tests
- LearningRecord, MemoryProposal, and SkillProposal governance tests
- protocol error helper tests

## Acceptance Criteria

Chunk 2 is complete when:

- TypeScript types match the OpenAPI contract.
- TypeScript validators reject every required v0.1 fixture failure class.
- package docs state Protocol Alpha support.
- package docs state SDK boundary and non-goals.
- local protocol validation passes.
- package tests pass.
- review lanes have no valid unresolved findings.

## Boundary

The TypeScript package helps compatible implementations create and validate
Jarvis records.

The TypeScript package does not run agents, call models, execute tools, store
records, authenticate users, render host UI, route work, or deploy hosts.
