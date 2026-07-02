"""Generated from docs/openapi/jarvis-openapi.yaml. Do not edit by hand."""

from __future__ import annotations

from typing import Any, Literal, TypeAlias, TypedDict
from typing_extensions import NotRequired, Required

__all__ = ['JarvisId',
 'OpaqueRef',
 'Timestamp',
 'NamespacedExtensions',
 'PortableValue',
 'WorkerType',
 'ActorType',
 'ContributionRole',
 'AutonomyLevel',
 'WorkSessionStatus',
 'PolicyDecisionResult',
 'RiskClass',
 'DataSensitivity',
 'RequestType',
 'RequestStatus',
 'BlockingScope',
 'ReviewDecision',
 'TakeoverState',
 'ContributorType',
 'ContributionType',
 'LearningSubjectType',
 'LearningReviewState',
 'ProposalTargetType',
 'MemoryProposalStatus',
 'SkillProposalStatus',
 'ProtocolErrorId',
 'AuthorityScope',
 'AccountabilityScope',
 'CapabilityRef',
 'EventAuthority',
 'ContributionScope',
 'CanonicalizationProfile',
 'ProtocolTraceContext',
 'JarvisEventPayload',
 'PolicyConstraint',
 'EscalationRule',
 'PolicyActionRule',
 'PolicyRequestLimits',
 'PolicyActionRequest',
 'RequestOption',
 'SafeFallback',
 'ApprovalBoundary',
 'TakeoverScope',
 'ApprovalScope',
 'ContributorRef',
 'ExportProfile',
 'EvidenceItemRef',
 'Worker',
 'Actor',
 'HumanWorker',
 'AgentWorker',
 'WorkSession',
 'JarvisEvent',
 'Policy',
 'PolicyDecision',
 'Request',
 'Review',
 'Takeover',
 'Contribution',
 'EvidenceManifest',
 'LearningRecord',
 'MemoryProposal',
 'SkillProposal',
 'OutcomeReport',
 'ProtocolError']

JarvisId: TypeAlias = str

OpaqueRef: TypeAlias = str

Timestamp: TypeAlias = str

NamespacedExtensions: TypeAlias = dict[str, Any]

PortableValue: TypeAlias = None | bool | int | float | str | list['PortableValue'] | dict[str, 'PortableValue']

WorkerType: TypeAlias = Literal['human', 'agent', 'service', 'tool']

ActorType: TypeAlias = Literal['human', 'agent', 'service', 'tool']

ContributionRole: TypeAlias = Literal['human', 'agent', 'shared', 'service', 'tool']

AutonomyLevel: TypeAlias = Literal['observe_only', 'propose_only', 'execute_with_review', 'bounded_execute', 'full_execute_in_scope']

WorkSessionStatus: TypeAlias = Literal['active', 'waiting_on_human', 'takeover', 'reconciling', 'completed', 'failed', 'cancelled', 'closed']

PolicyDecisionResult: TypeAlias = Literal['allow', 'deny', 'narrow', 'review_required']

RiskClass: TypeAlias = Literal['low', 'medium', 'high', 'critical']

DataSensitivity: TypeAlias = Literal['public', 'private', 'confidential', 'restricted']

RequestType: TypeAlias = Literal['permission', 'context', 'judgment', 'review', 'correction', 'takeover', 'escalation']

RequestStatus: TypeAlias = Literal['pending', 'acknowledged', 'approved', 'denied', 'narrowed', 'answered', 'needs_revision', 'takeover', 'expired', 'cancelled', 'superseded']

BlockingScope: TypeAlias = Literal['action', 'branch', 'artifact', 'tool_call', 'external_send', 'final_submission', 'work_session']

ReviewDecision: TypeAlias = Literal['answer', 'approve', 'deny', 'narrow', 'correct', 'takeover', 'needs_revision']

TakeoverState: TypeAlias = Literal['requested', 'locked', 'human_active', 'reconciliation_required', 'resumed', 'closed']

ContributorType: TypeAlias = Literal['human', 'agent', 'service', 'tool', 'shared']

ContributionType: TypeAlias = Literal['intent', 'instruction', 'plan', 'research', 'execution', 'artifact', 'review', 'correction', 'decision', 'evidence_capture', 'memory_proposal', 'skill_proposal', 'submission']

LearningSubjectType: TypeAlias = Literal['human', 'agent', 'pair']

LearningReviewState: TypeAlias = Literal['proposed', 'accepted', 'rejected', 'superseded']

ProposalTargetType: TypeAlias = Literal['human', 'agent', 'pair', 'project', 'task']

MemoryProposalStatus: TypeAlias = Literal['proposed', 'pending_review', 'accepted', 'rejected', 'superseded', 'expired']

SkillProposalStatus: TypeAlias = Literal['proposed', 'pending_review', 'accepted', 'rejected', 'superseded', 'archived']

ProtocolErrorId: TypeAlias = Literal['invalid_transition', 'unknown_state', 'missing_protocol_version', 'unsupported_protocol_version', 'missing_request_timestamp', 'stale_request_timestamp', 'missing_expected_work_session_revision', 'missing_previous_event_hash', 'stale_work_session_revision', 'missing_idempotency_key', 'missing_actor', 'path_body_id_mismatch', 'actor_body_id_mismatch', 'invalid_extension_namespace', 'extension_core_field_override', 'missing_policy', 'missing_policy_decision', 'missing_objective', 'policy_denied', 'request_unresolved', 'review_required', 'invalid_request_transition', 'missing_review_resolution', 'missing_takeover_resolution', 'missing_superseding_request', 'invalid_approval_scope', 'approval_scope_expired', 'approval_scope_mismatch', 'stale_takeover_epoch', 'invalid_event_hash', 'invalid_previous_event_hash', 'duplicate_idempotency_key_mismatch', 'request_livelock', 'duplicate_request_mismatch', 'missing_jarvis_event', 'missing_blocked_scope_resolution_refs', 'missing_reconciliation_refs', 'mutation_after_closed', 'unauthorized_actor', 'invalid_export', 'invalid_export_state', 'invalid_evidence_export_state', 'missing_contribution_actor', 'invalid_contributor_refs', 'shared_contribution_without_individual_refs', 'duplicate_contributor_ref', 'evidence_after_the_fact', 'missing_evidence_event_refs', 'duplicate_evidence_item_ref', 'forbidden_export_field', 'silent_memory_mutation', 'silent_skill_activation', 'model_self_confirmed_memory', 'tool_self_confirmed_memory', 'skill_expands_tool_access_without_policy_review', 'sealed_work_session_mutation', 'sealed_evidence_mutation', 'outcome_report_without_learning_record', 'outcome_report_requires_terminal_source', 'unsupported_capability', 'forbidden_host_private_field']

class AuthorityScope(TypedDict, total=False):
    grants: Required[list[str]]

class AccountabilityScope(TypedDict, total=False):
    accountable_for: Required[list[str]]

class CapabilityRef(TypedDict, total=False):
    capability_type: NotRequired[str]
    ref: Required[OpaqueRef]
    required: NotRequired[bool]

class EventAuthority(TypedDict, total=False):
    allowed_event_types: NotRequired[list[str]]
    can_append_events: Required[bool]

class ContributionScope(TypedDict, total=False):
    contribution_roles: Required[list[ContributionRole]]

class CanonicalizationProfile(TypedDict, total=False):
    hash_method: Required[Literal['sha256']]
    profile_ref: NotRequired[OpaqueRef]
    serialization: Required[Literal['json-c14n']]

class ProtocolTraceContext(TypedDict, total=False):
    correlation_ref: NotRequired[OpaqueRef]
    parent_event_id: NotRequired[JarvisId]
    trace_id: NotRequired[OpaqueRef]

class JarvisEventPayload(TypedDict, total=False):
    action: Required[str]
    evidence_refs: NotRequired[list[OpaqueRef]]
    field_refs: NotRequired[list[OpaqueRef]]
    object_id: NotRequired[JarvisId]
    object_type: Required[Literal['worker', 'actor', 'human_worker', 'agent_worker', 'work_session', 'jarvis_event', 'policy', 'policy_decision', 'request', 'review', 'takeover', 'contribution', 'evidence_manifest', 'learning_record', 'memory_proposal', 'skill_proposal', 'outcome_report', 'protocol_error', 'conformance_result']]
    summary: NotRequired[str]

class PolicyConstraint(TypedDict, total=False):
    kind: Required[str]
    max_count: NotRequired[int]
    reason: NotRequired[str]
    scope_ref: NotRequired[OpaqueRef]
    unit: NotRequired[str]
    value_ref: NotRequired[OpaqueRef]

class EscalationRule(TypedDict, total=False):
    reason: NotRequired[str]
    required_action: Required[Literal['create_request', 'require_review', 'start_takeover', 'deny_action']]
    reviewer_ref: NotRequired[OpaqueRef]
    risk_class: NotRequired[RiskClass]
    trigger: Required[str]

class PolicyActionRule(TypedDict, total=False):
    action: Required[str]
    constraints: NotRequired[list[PolicyConstraint]]
    grant_refs: NotRequired[list[OpaqueRef]]
    scope_ref: NotRequired[OpaqueRef]

class PolicyRequestLimits(TypedDict, total=False):
    default_expiry_seconds: NotRequired[int]
    max_pending_requests: NotRequired[int]
    max_repeated_denials: NotRequired[int]

class PolicyActionRequest(TypedDict, total=False):
    action: Required[str]
    input_refs: NotRequired[list[OpaqueRef]]
    parameter_refs: NotRequired[list[OpaqueRef]]
    scope_ref: NotRequired[OpaqueRef]
    target_ref: NotRequired[OpaqueRef]

class RequestOption(TypedDict, total=False):
    effect: Required[str]
    id: Required[JarvisId]
    label: Required[str]
    risk_class: NotRequired[RiskClass]
    scope_ref: NotRequired[OpaqueRef]

class SafeFallback(TypedDict, total=False):
    action: Required[Literal['continue_unrelated_safe_work', 'continue_with_limited_evidence', 'cancel_blocked_scope', 'keep_blocked_scope_stopped']]
    limitation_ref: NotRequired[OpaqueRef]
    reason: Required[str]

class ApprovalBoundary(TypedDict, total=False):
    constraint_refs: NotRequired[list[OpaqueRef]]
    grant_refs: NotRequired[list[OpaqueRef]]
    scope_ref: Required[OpaqueRef]

class TakeoverScope(TypedDict, total=False):
    artifact_refs: NotRequired[list[OpaqueRef]]
    blocking_scope: Required[BlockingScope]
    normalized_action_hash: NotRequired[str]
    scope_ref: Required[OpaqueRef]

class ApprovalScope(TypedDict, total=False):
    allowed_scope: Required[ApprovalBoundary]
    applies_to_actor_id: Required[JarvisId]
    applies_to_work_session_id: Required[JarvisId]
    approved_action: Required[PolicyActionRequest]
    denied_scope: Required[ApprovalBoundary]
    expires_at: Required[Timestamp]
    max_uses: Required[int]
    normalized_action_hash: Required[str]
    policy_decision_id: Required[JarvisId]
    request_event_hash: Required[str]
    request_id: Required[JarvisId]
    request_revision: Required[int]
    review_id: Required[JarvisId]

class ContributorRef(TypedDict, total=False):
    actor_id: Required[JarvisId]
    contribution_role: Required[ContributionRole]
    worker_id: Required[JarvisId]

class ExportProfile(TypedDict, total=False):
    profile: Required[str]
    redaction_profile_ref: NotRequired[OpaqueRef]
    version: NotRequired[str]

class EvidenceItemRef(TypedDict, total=False):
    artifact_ref: Required[OpaqueRef]
    captured_at: Required[Timestamp]
    captured_by_actor_id: Required[JarvisId]
    content_hash: Required[str]
    evidence_type: Required[str]
    id: Required[JarvisId]
    limitation_refs: Required[list[OpaqueRef]]
    redaction_state: Required[str]
    source_event_refs: Required[list[JarvisId]]
    trust_label: Required[str]
    work_session_id: Required[JarvisId]

class Worker(TypedDict, total=False):
    accountability_scope: Required[AccountabilityScope]
    authority_scope: Required[AuthorityScope]
    capabilities: NotRequired[list[CapabilityRef]]
    display_name: NotRequired[str]
    extensions: NotRequired[NamespacedExtensions]
    id: Required[JarvisId]
    role: Required[str]
    type: Required[WorkerType]

class Actor(TypedDict, total=False):
    contribution_scope: Required[ContributionScope]
    created_at: Required[Timestamp]
    event_authority: Required[EventAuthority]
    extensions: NotRequired[NamespacedExtensions]
    id: Required[JarvisId]
    type: Required[ActorType]
    valid_from: NotRequired[Timestamp]
    valid_until: NotRequired[Timestamp]
    worker_id: Required[JarvisId]

class HumanWorker(TypedDict, total=False):
    actor_id: Required[JarvisId]
    boundaries: NotRequired[list[str]]
    domain_context_refs: NotRequired[list[OpaqueRef]]
    known_patterns: NotRequired[list[str]]
    policy_authority: Required[AuthorityScope]
    preferences: NotRequired[dict[str, PortableValue]]
    profile_ref: NotRequired[OpaqueRef]
    review_authority: Required[AuthorityScope]
    role: Required[str]
    worker_id: Required[JarvisId]

class AgentWorker(TypedDict, total=False):
    actor_id: Required[JarvisId]
    agent_ref: Required[OpaqueRef]
    autonomy_level: Required[AutonomyLevel]
    capability_refs: Required[list[CapabilityRef]]
    extensions: NotRequired[NamespacedExtensions]
    memory_access_profile: NotRequired[OpaqueRef]
    operating_constraints: Required[list[str]]
    role: Required[str]
    tool_access_profile: NotRequired[OpaqueRef]
    worker_id: Required[JarvisId]

class WorkSession(TypedDict, total=False):
    agent_worker_id: Required[JarvisId]
    context_manifest_ref: NotRequired[OpaqueRef]
    contribution_ledger_ref: NotRequired[OpaqueRef]
    created_at: Required[Timestamp]
    created_by_actor_id: Required[JarvisId]
    event_log_ref: Required[OpaqueRef]
    evidence_manifest_ref: NotRequired[OpaqueRef]
    human_worker_id: Required[JarvisId]
    id: Required[JarvisId]
    last_event_hash: Required[str]
    learning_record_refs: NotRequired[list[JarvisId]]
    objective: Required[str]
    policy_id: Required[JarvisId]
    protocol_version: Required[Literal['v0.1']]
    revision: Required[int]
    source_ref: NotRequired[OpaqueRef]
    status: Required[WorkSessionStatus]
    updated_at: Required[Timestamp]

class JarvisEvent(TypedDict, total=False):
    actor_id: Required[JarvisId]
    actor_signature: NotRequired[str]
    canonicalization: Required[CanonicalizationProfile]
    event_hash: Required[str]
    id: Required[JarvisId]
    payload: Required[JarvisEventPayload]
    previous_hash: Required[str]
    sequence: Required[int]
    signing_key_ref: NotRequired[OpaqueRef]
    timestamp: Required[Timestamp]
    trace_context: NotRequired[ProtocolTraceContext]
    type: Required[str]
    work_session_id: Required[JarvisId]

class Policy(TypedDict, total=False):
    allowed_actions: Required[list[PolicyActionRule]]
    autonomy_level: Required[AutonomyLevel]
    created_at: Required[Timestamp]
    created_by_actor_id: Required[JarvisId]
    denied_actions: Required[list[PolicyActionRule]]
    escalation_rules: Required[list[EscalationRule]]
    extensions: NotRequired[NamespacedExtensions]
    external_send_rules: NotRequired[list[PolicyActionRule]]
    id: Required[JarvisId]
    memory_grants: NotRequired[list[OpaqueRef]]
    owner_worker_id: Required[JarvisId]
    request_limits: NotRequired[PolicyRequestLimits]
    review_required_actions: Required[list[PolicyActionRule]]
    risk_classes: Required[list[RiskClass]]
    tool_grants: NotRequired[list[OpaqueRef]]

class PolicyDecision(TypedDict, total=False):
    actor_id: Required[JarvisId]
    created_at: Required[Timestamp]
    data_sensitivity: NotRequired[DataSensitivity]
    denied_grant_refs: NotRequired[list[OpaqueRef]]
    evidence_refs: NotRequired[list[OpaqueRef]]
    id: Required[JarvisId]
    normalized_action_hash: Required[str]
    policy_id: Required[JarvisId]
    reason: Required[str]
    request_id: NotRequired[JarvisId]
    requested_action: Required[PolicyActionRequest]
    result: Required[PolicyDecisionResult]
    risk_class: Required[RiskClass]
    selected_grant_refs: NotRequired[list[OpaqueRef]]
    work_session_id: Required[JarvisId]

class Request(TypedDict, total=False):
    artifact_refs: NotRequired[list[OpaqueRef]]
    blocking_scope: Required[BlockingScope]
    closed_by_event_ref: NotRequired[OpaqueRef]
    contribution_refs: NotRequired[list[JarvisId]]
    created_at: Required[Timestamp]
    data_sensitivity: NotRequired[DataSensitivity]
    default_if_no_response: Required[SafeFallback]
    duplicate_of_request_id: NotRequired[JarvisId]
    evidence_refs: NotRequired[list[OpaqueRef]]
    expires_at: Required[Timestamp]
    human_decision_needed: Required[str]
    id: Required[JarvisId]
    missing_permission_or_context: NotRequired[str]
    options: Required[list[RequestOption]]
    policy_decision_id: Required[JarvisId]
    policy_refs: NotRequired[list[OpaqueRef]]
    protocol_version: Required[Literal['v0.1']]
    reason_code: Required[str]
    reason_summary: Required[str]
    recommended_option: NotRequired[JarvisId]
    requested_action: Required[PolicyActionRequest]
    requested_outcome: Required[str]
    requester_actor_id: Required[JarvisId]
    requester_worker_id: Required[JarvisId]
    resolved_at: NotRequired[Timestamp]
    resolved_by_review_id: NotRequired[JarvisId]
    resolved_by_takeover_id: NotRequired[JarvisId]
    risk_class: Required[RiskClass]
    safer_alternatives: NotRequired[list[RequestOption]]
    status: Required[RequestStatus]
    superseded_by_request_id: NotRequired[JarvisId]
    target_human_worker_id: Required[JarvisId]
    type: Required[RequestType]
    work_session_id: Required[JarvisId]

class Review(TypedDict, total=False):
    approval_scope: NotRequired[ApprovalScope]
    comments: NotRequired[str]
    created_at: Required[Timestamp]
    decision: Required[ReviewDecision]
    id: Required[JarvisId]
    required_changes: NotRequired[list[str]]
    reviewer_actor_id: Required[JarvisId]
    reviewer_worker_id: Required[JarvisId]
    takeover_id: NotRequired[JarvisId]
    target_ref: Required[OpaqueRef]
    work_session_id: Required[JarvisId]

class Takeover(TypedDict, total=False):
    affected_scope: Required[TakeoverScope]
    controlling_actor_id: Required[JarvisId]
    created_at: Required[Timestamp]
    id: Required[JarvisId]
    lock_epoch: Required[int]
    reason: Required[str]
    reconciliation_notes: NotRequired[str]
    reconciliation_refs: NotRequired[list[OpaqueRef]]
    request_id: NotRequired[JarvisId]
    requested_by_actor_id: Required[JarvisId]
    resolved_at: NotRequired[Timestamp]
    resumed_by_actor_id: NotRequired[JarvisId]
    state: Required[TakeoverState]
    work_session_id: Required[JarvisId]

class Contribution(TypedDict, total=False):
    artifact_refs: NotRequired[list[OpaqueRef]]
    confidence: NotRequired[int | float]
    contribution_type: Required[ContributionType]
    contributor_refs: Required[list[ContributorRef]]
    contributor_type: Required[ContributorType]
    created_at: Required[Timestamp]
    event_refs: Required[list[JarvisId]]
    evidence_refs: NotRequired[list[JarvisId]]
    id: Required[JarvisId]
    limitations: NotRequired[list[OpaqueRef]]
    review_refs: NotRequired[list[JarvisId]]
    work_session_id: Required[JarvisId]

class EvidenceManifest(TypedDict, total=False):
    artifact_refs: NotRequired[list[OpaqueRef]]
    contribution_refs: Required[list[JarvisId]]
    event_chain_root: Required[str]
    evidence_item_refs: Required[list[EvidenceItemRef]]
    export_profile: Required[ExportProfile]
    generated_at: Required[Timestamp]
    generated_by_actor_id: Required[JarvisId]
    id: Required[JarvisId]
    limitation_refs: NotRequired[list[OpaqueRef]]
    objective: Required[str]
    policy_decision_refs: Required[list[JarvisId]]
    redaction_refs: NotRequired[list[OpaqueRef]]
    request_refs: Required[list[JarvisId]]
    review_refs: Required[list[JarvisId]]
    takeover_refs: Required[list[JarvisId]]
    work_session_id: Required[JarvisId]

class LearningRecord(TypedDict, total=False):
    created_at: Required[Timestamp]
    created_by_actor_id: Required[JarvisId]
    id: Required[JarvisId]
    lesson_type: Required[str]
    memory_proposal_refs: NotRequired[list[JarvisId]]
    outcome_report_refs: NotRequired[list[JarvisId]]
    proposed_change: NotRequired[PortableValue]
    review_state: Required[LearningReviewState]
    scope: Required[OpaqueRef]
    skill_proposal_refs: NotRequired[list[JarvisId]]
    source_event_refs: Required[list[JarvisId]]
    subject_ref: Required[OpaqueRef]
    subject_type: Required[LearningSubjectType]
    work_session_id: Required[JarvisId]

class MemoryProposal(TypedDict, total=False):
    confidence: Required[int | float]
    content: Required[PortableValue]
    created_at: Required[Timestamp]
    expires_at: NotRequired[Timestamp]
    id: Required[JarvisId]
    learning_record_refs: NotRequired[list[JarvisId]]
    memory_scope: Required[OpaqueRef]
    memory_type: Required[str]
    proposed_by_actor_id: Required[JarvisId]
    proposed_for: Required[ProposalTargetType]
    provenance: Required[list[OpaqueRef]]
    review_refs: NotRequired[list[JarvisId]]
    review_required: Required[Literal[True]]
    source_event_refs: NotRequired[list[JarvisId]]
    status: Required[MemoryProposalStatus]
    work_session_id: Required[JarvisId]

class SkillProposal(TypedDict, total=False):
    created_at: Required[Timestamp]
    failure_cases: Required[list[str]]
    id: Required[JarvisId]
    learning_record_refs: NotRequired[list[JarvisId]]
    procedure: Required[list[str]]
    proposed_by_actor_id: Required[JarvisId]
    proposed_for: Required[ProposalTargetType]
    provenance: Required[list[OpaqueRef]]
    required_tools: NotRequired[list[OpaqueRef]]
    review_checks: Required[list[str]]
    review_refs: NotRequired[list[JarvisId]]
    skill_name: Required[str]
    skill_scope: Required[OpaqueRef]
    source_event_refs: NotRequired[list[JarvisId]]
    status: Required[SkillProposalStatus]
    trigger_conditions: Required[list[str]]
    work_session_id: Required[JarvisId]

class OutcomeReport(TypedDict, total=False):
    accepted_by_actor_id: Required[JarvisId]
    external_system_ref: NotRequired[OpaqueRef]
    id: Required[JarvisId]
    learning_record_refs: Required[list[JarvisId]]
    outcome: Required[str]
    reason: NotRequired[str]
    received_at: Required[Timestamp]
    reporter_actor_id: NotRequired[JarvisId]
    reporter_ref: Required[OpaqueRef]
    reviewer_feedback_refs: NotRequired[list[OpaqueRef]]
    source_ref: Required[OpaqueRef]
    work_session_id: Required[JarvisId]

class ProtocolError(TypedDict, total=False):
    error_id: Required[ProtocolErrorId]
    field: Required[str]
    object_type: Required[str]
    protocol_version: Required[str]
    reason: Required[str]
    remediation: Required[str]
    trace_id: Required[OpaqueRef]
