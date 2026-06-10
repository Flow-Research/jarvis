# Protocol v0.1

Jarvis v0.1 proves the protocol loop. It does not ship an execution stack.

v0.1 is the OpenAPI 3.1 contract, conformance checks, examples, and protocol
records that define how HumanWorker and AgentWorker collaborate inside a
WorkSession.

## v0.1 Scope

Jarvis v0.1 includes:

- OpenAPI 3.1 contract
- event envelope
- WorkSession lifecycle
- Policy decision model
- Request model
- Review model
- Takeover model
- Contribution ledger model
- EvidenceManifest model
- LearningRecord model
- MemoryProposal model
- SkillProposal model
- conformance tests
- export format

Jarvis v0.1 excludes:

- execution adapters
- cloud integration
- local execution
- model calls
- sandboxes
- storage implementation
- queues
- deployment
- product UI
- authentication
- billing

Hosts own storage, execution, auth, billing, deployment, and UI.

## Golden Path

```txt
1. Create HumanWorker.
2. Create AgentWorker.
3. Start WorkSession.
4. Attach Policy.
5. Record objective.
6. Record AgentWorker action inside policy.
7. Record blocked action outside policy.
8. Create Request from AgentWorker.
9. Record HumanWorker Review decision.
10. Resume work after approval or correction.
11. Record Contribution entries.
12. Capture EvidenceManifest entries.
13. Create LearningRecord for human, agent, or pair learning.
14. Create MemoryProposal or SkillProposal.
15. Export portable protocol record.
```

## Required Protocol Records

```txt
Worker
Actor
HumanWorker
AgentWorker
WorkSession
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
JarvisEvent
```

## Event Envelope

Every protocol event includes:

```txt
id
sequence
type
work_session_id
actor_id
timestamp
trace_context
payload
previous_hash
event_hash
```

The event chain makes the collaboration inspectable and exportable.

## WorkSession Statuses

```txt
created
active
waiting_on_human
takeover
reconciling
completed
failed
cancelled
closed
```

Jarvis defines valid transitions. Hosts own storage, streaming, and execution.

## Conformance Tests

The v0.1 conformance suite checks:

- a WorkSession cannot start without HumanWorker, AgentWorker, objective, and
  Policy.
- invalid WorkSession transitions are rejected.
- stale WorkSession revision is rejected.
- stale previous event hash is rejected.
- every transition out of `waiting_on_human` records blocker accounting.
- WorkSession lifecycle rejection ids include `unknown_state`,
  `missing_idempotency_key`, `duplicate_idempotency_key_mismatch`,
  `missing_jarvis_event`, `missing_policy_decision`,
  `missing_blocked_scope_resolution_refs`, `missing_reconciliation_refs`,
  `mutation_after_closed`, `invalid_export_state`, and
  `unauthorized_actor`.
- final EvidenceManifest export is valid only from completed, failed,
  cancelled, or closed WorkSession state.
- policy-denied action creates Request.
- review-required action creates Request.
- Request blocks only its declared scope unless scope is whole WorkSession.
- Human resolution of a Request requires Review or Takeover.
- invalid Request transitions are rejected.
- approval narrows scope when the human restricts the request.
- narrowed approval rejects execution outside the approved scope.
- stale, mismatched, expired, or over-broad ApprovalScope rejects execution.
- expired Request applies its safe fallback.
- takeover creates a lock epoch.
- stale autonomous events after takeover are rejected.
- takeover resume requires reconciliation refs.
- duplicate pending Requests are deduplicated or superseded.
- repeated unchanged Requests reject as livelock or supersede without weakening
  policy fields.
- control-plane rejection ids include `invalid_request_transition`,
  `missing_review_resolution`, `missing_takeover_resolution`,
  `invalid_approval_scope`, `approval_scope_expired`,
  `approval_scope_mismatch`, `stale_takeover_epoch`, `request_livelock`, and
  `duplicate_request_mismatch`.
- host notifications do not become blocking Requests without Request event and
  PolicyDecision.
- Contribution entries reference events or artifacts.
- shared Contribution preserves individual contributor refs.
- EvidenceManifest references policy decisions, requests, reviews,
  takeovers, contributions, artifacts, evidence items, and limitations.
- EvidenceManifest final export rejects mutable WorkSession states.
- EvidenceManifest excludes forbidden export fields.
- Request resolution records governed learning proposals when the Review,
  Takeover, or safe fallback changes future WorkSession behavior.
- MemoryProposal and SkillProposal require provenance and review state.
- MemoryProposal rejects model-derived or tool-derived self-confirmation.
- SkillProposal rejects activation without review.
- SkillProposal rejects tool access expansion without policy review.
- LearningRecord describes human learning, agent learning, or pair learning.
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
- exported protocol records do not require product-private infrastructure
  fields.
- OpenAPI security entry checks require HostAuth, ActorHeader,
  ProtocolVersionHeader, IdempotencyHeader, RequestTimestampHeader,
  RevisionHeader, and PreviousHashHeader.
- WorkSession-scoped and export read operations require
  `Jarvis-Protocol-Version`, caller authentication, and `Jarvis-Actor-Id`, and
  do not require mutation-only idempotency, expected revision, or previous event
  hash headers.
- Worker and Actor registration does not create accounts, authenticate callers,
  issue credentials, or own identity storage.
- unsupported required capabilities reject as `unsupported_capability`.
- invalid extension namespace rejects as `invalid_extension_namespace`.
- extension core field override rejects as `extension_core_field_override`.
- protocol error envelope includes error_id, protocol_version, object_type,
  field, reason, remediation, and trace_id.
- OpenAPI security rejection ids include `missing_protocol_version`,
  `unsupported_protocol_version`, `missing_actor`, `missing_idempotency_key`,
  `missing_request_timestamp`, `stale_request_timestamp`,
  `missing_expected_work_session_revision`, `missing_previous_event_hash`,
  `invalid_extension_namespace`, and `extension_core_field_override`.
- protocol error responses exclude forbidden host-private fields.

## Success Condition

Jarvis v0.1 succeeds when a compatible implementation runs a HumanWorker and
AgentWorker through a WorkSession, proves policy-governed autonomy, captures
human judgment, records contribution, exports evidence, and carries governed
learning into the next WorkSession without adopting a runtime owned by Jarvis.
