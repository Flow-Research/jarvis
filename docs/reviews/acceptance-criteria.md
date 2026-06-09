# Design Acceptance Criteria

Jarvis architecture is accepted only when these criteria hold.

## Scope

- Jarvis is defined as the human-agent collaboration and learning-loop
  protocol.
- [11-core-protocol-objects.md](../protocol/11-core-protocol-objects.md) is
  the source of truth for v0.1 object definitions.
- Jarvis is a compatibility protocol for multiple humans, agents, products,
  hosts, and external systems.
- Jarvis does not define execution stack, cloud, database, queue, sandbox,
  deployment, model provider, authentication, billing, or product UI.
- external products and systems integrate with Jarvis through protocol
  contracts.

## Human-Agent Collaboration

- HumanWorker is an active contributor, reviewer, teacher, and accountable
  actor.
- AgentWorker is an autonomous but policy-bounded contributor.
- HumanWorker and AgentWorker are both actors in the protocol.
- HumanWorker and AgentWorker both learn from completed WorkSessions.
- HumanWorker approves, denies, narrows, corrects, requests revision, or takes
  over.
- Corrections may create or reference LearningRecord, MemoryProposal, or
  SkillProposal records.

## WorkSession

- WorkSession is the source of truth.
- WorkSession captures goals, events, requests, reviews, takeovers,
  contributions, evidence, artifacts, learning, and final outcome.
- WorkSession is not reduced to chat history.

## Policy

- Policy defines what the AgentWorker does.
- Action outside policy creates Request.
- Request is reviewable and attributable.
- Review decisions are explicit.
- Takeover prevents stale autonomous continuation.

## Memory And Skills

- Memory scopes are explicit.
- Memory has lifecycle and provenance.
- Durable memory changes require MemoryProposal and review state.
- Skills are procedural memory.
- Skill changes require SkillProposal and review state.

## Evidence And Contribution

- Contributions distinguish human, agent, service, tool, and shared work.
- Evidence is captured during work.
- EvidenceManifest includes policy decisions, requests, reviews,
  contributions, artifacts, and limitations.
- EvidenceManifest is portable across products.

## v0.1 Protocol Acceptance

The first protocol release passes these checks:

```txt
create HumanWorker
create AgentWorker
start WorkSession
attach Policy
record objective
record allowed AgentWorker action
record policy-denied AgentWorker action
create Request
record HumanWorker Review
resume work after approval or correction
record Contribution
record EvidenceManifest item
record LearningRecord for human, agent, or pair learning
create MemoryProposal or SkillProposal
export protocol record
```

Expected result:

- all records validate against the OpenAPI 3.1 contract
- WorkSession status transitions are valid
- invalid WorkSession transitions are rejected
- stale WorkSession revision is rejected
- stale previous event hash is rejected
- every accepted WorkSession state change records Actor, verifies authority,
  checks current WorkSession revision, and links to previous event hash
- every AgentWorker action that affects a WorkSession records a PolicyDecision
  before the action is accepted as protocol state
- every transition out of `waiting_on_human` records blocker accounting
- WorkSession lifecycle rejection ids include `unknown_state`,
  `missing_idempotency_key`, `duplicate_idempotency_key_mismatch`,
  `missing_jarvis_event`, `missing_policy_decision`,
  `missing_blocked_scope_resolution_refs`, `missing_reconciliation_refs`,
  `mutation_after_closed`, `invalid_export_state`, and `unauthorized_actor`
- final EvidenceManifest export is valid only from completed, failed,
  cancelled, or closed WorkSession state
- Request cannot reach human-resolved state without Review or Takeover
- Review supports approve, deny, narrow, correct, takeover, and needs_revision
- Request blocks only its declared scope unless scope is whole WorkSession
- invalid Request transitions are rejected
- ApprovalScope rejects stale, mismatched, expired, or over-broad execution
- repeated unchanged Requests reject as livelock or supersede without weakening
  policy fields
- control-plane rejection ids include `invalid_request_transition`,
  `missing_review_resolution`, `missing_takeover_resolution`,
  `invalid_approval_scope`, `approval_scope_expired`,
  `approval_scope_mismatch`, `stale_takeover_epoch`, `request_livelock`, and
  `duplicate_request_mismatch`
- Takeover creates lock state
- Takeover rejects stale AgentWorker continuation
- Takeover resume requires reconciliation refs
- mutating WorkSession-scoped attribution, evidence, learning, proposal, and
  export operations require `Jarvis-Protocol-Version`, `Jarvis-Actor-Id`,
  `Jarvis-Idempotency-Key`, `Jarvis-Request-Timestamp`,
  `Jarvis-Expected-WorkSession-Revision`, and
  `Jarvis-Previous-Event-Hash`
- OutcomeReport submission uses the non-WorkSession mutation header set:
  `Jarvis-Protocol-Version`, `Jarvis-Actor-Id`, `Jarvis-Idempotency-Key`, and
  `Jarvis-Request-Timestamp`; it does not require
  `Jarvis-Expected-WorkSession-Revision` or `Jarvis-Previous-Event-Hash`
- Contribution references events or artifacts
- shared Contribution preserves individual contributor refs
- EvidenceManifest references the WorkSession event chain
- EvidenceManifest references policy decisions, requests, reviews, takeovers,
  contributions, artifacts, evidence items, and limitations
- EvidenceManifest excludes forbidden export fields
- MemoryProposal rejects model-derived or tool-derived self-confirmation
- SkillProposal rejects activation without review and rejects tool access
  expansion without policy review
- OutcomeReport creates or references LearningRecord without mutating sealed
  WorkSession or EvidenceManifest
- attribution/evidence/learning rejection ids include
  `missing_contribution_actor`, `invalid_contributor_refs`,
  `shared_contribution_without_individual_refs`, `evidence_after_the_fact`,
  `missing_evidence_event_refs`, `invalid_evidence_export_state`,
  `forbidden_export_field`, `silent_memory_mutation`,
  `silent_skill_activation`, `model_self_confirmed_memory`,
  `tool_self_confirmed_memory`,
  `skill_expands_tool_access_without_policy_review`,
  `sealed_work_session_mutation`, `sealed_evidence_mutation`,
  `outcome_report_without_learning_record`, and
  `forbidden_host_private_field`
- exported records contain no product-private infrastructure requirement
- OpenAPI security entry checks require HostAuth, ActorHeader,
  ProtocolVersionHeader, IdempotencyHeader, RequestTimestampHeader,
  RevisionHeader, and PreviousHashHeader
- Worker registration, Actor registration, and OutcomeReport submission do not
  require `Jarvis-Expected-WorkSession-Revision` or
  `Jarvis-Previous-Event-Hash`
- WorkSession-scoped and export read operations require
  `Jarvis-Protocol-Version`, caller authentication, and `Jarvis-Actor-Id`, and
  do not require mutation-only idempotency, expected revision, or previous event
  hash headers
- Worker and Actor registration does not create accounts, authenticate callers,
  issue credentials, or own identity storage
- unsupported required capabilities reject as `unsupported_capability`
- invalid extension namespace rejects as `invalid_extension_namespace`
- extension core field override rejects as `extension_core_field_override`
- protocol error envelope includes error_id, protocol_version, object_type,
  field, reason, remediation, and trace_id
- OpenAPI security rejection ids include `missing_protocol_version`,
  `unsupported_protocol_version`, `missing_actor`, `missing_idempotency_key`,
  `missing_request_timestamp`, `stale_request_timestamp`,
  `missing_expected_work_session_revision`, `missing_previous_event_hash`,
  `invalid_extension_namespace`, and `extension_core_field_override`
- protocol error responses exclude forbidden host-private fields

## Conformance Acceptance

A product is Jarvis-compatible when it proves:

- WorkSession is the source of truth.
- Policy gates autonomous action.
- blocked action creates Request.
- Review or Takeover resolves Request.
- Request and non-blocking host communication remain separate.
- Takeover prevents stale continuation.
- Contributions are attributable.
- EvidenceManifest is portable.
- Learning is governed.

Conformance does not require any specific execution stack, cloud provider,
database, sandbox, queue, deployment platform, or UI.
