#!/usr/bin/env python3
"""Validate the Jarvis v0.1 OpenAPI contract."""

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
OPENAPI_PATH = ROOT / "docs" / "openapi" / "jarvis-openapi.yaml"
GOLDEN_PATH_CONFORMANCE = ROOT / "docs" / "conformance" / "golden-path.md"
FAILURE_MODE_CONFORMANCE = ROOT / "docs" / "conformance" / "failure-modes.md"

REQUIRED_TOP_LEVEL = {
    "openapi",
    "jsonSchemaDialect",
    "info",
    "servers",
    "security",
    "tags",
    "paths",
    "components",
    "x-jarvis-protocol",
}

REQUIRED_COMPONENTS = {
    "schemas",
    "parameters",
    "headers",
    "requestBodies",
    "responses",
    "securitySchemes",
    "examples",
}

REQUIRED_PROTOCOL_METADATA = {
    "version",
    "layer",
    "source_of_truth",
    "owns",
    "outside_jarvis",
    "chunk_lock",
}

REQUIRED_SCHEMAS = {
    "JarvisId",
    "OpaqueRef",
    "Timestamp",
    "NamespacedExtensions",
    "PortableValue",
    "WorkerType",
    "ActorType",
    "ContributionRole",
    "AutonomyLevel",
    "WorkSessionStatus",
    "PolicyDecisionResult",
    "RiskClass",
    "DataSensitivity",
    "RequestType",
    "RequestStatus",
    "BlockingScope",
    "ReviewDecision",
    "TakeoverState",
    "ContributorType",
    "ContributionType",
    "LearningSubjectType",
    "LearningReviewState",
    "ProposalTargetType",
    "MemoryProposalStatus",
    "SkillProposalStatus",
    "ProtocolErrorId",
    "AuthorityScope",
    "AccountabilityScope",
    "CapabilityRef",
    "EventAuthority",
    "ContributionScope",
    "CanonicalizationProfile",
    "ProtocolTraceContext",
    "JarvisEventPayload",
    "PolicyConstraint",
    "EscalationRule",
    "PolicyActionRule",
    "PolicyRequestLimits",
    "PolicyActionRequest",
    "RequestOption",
    "SafeFallback",
    "ApprovalBoundary",
    "TakeoverScope",
    "ApprovalScope",
    "ContributorRef",
    "ExportProfile",
    "EvidenceItemRef",
    "Worker",
    "Actor",
    "HumanWorker",
    "AgentWorker",
    "WorkSession",
    "JarvisEvent",
    "Policy",
    "PolicyDecision",
    "Request",
    "Review",
    "Takeover",
    "Contribution",
    "EvidenceManifest",
    "LearningRecord",
    "MemoryProposal",
    "SkillProposal",
    "OutcomeReport",
    "ProtocolError",
}

REQUIRED_PARAMETERS = {
    "WorkerIdPath",
    "ActorIdPath",
    "WorkSessionIdPath",
    "ProtocolVersionHeader",
    "ActorHeader",
    "IdempotencyHeader",
    "RequestTimestampHeader",
    "RevisionHeader",
    "PreviousHashHeader",
    "RequiredCapabilitiesHeader",
    "ExtensionsHeader",
}

HEADER_PARAMETER_NAMES = {
    "ProtocolVersionHeader": "Jarvis-Protocol-Version",
    "ActorHeader": "Jarvis-Actor-Id",
    "IdempotencyHeader": "Jarvis-Idempotency-Key",
    "RequestTimestampHeader": "Jarvis-Request-Timestamp",
    "RevisionHeader": "Jarvis-Expected-WorkSession-Revision",
    "PreviousHashHeader": "Jarvis-Previous-Event-Hash",
}

OPTIONAL_HEADER_PARAMETER_NAMES = {
    "RequiredCapabilitiesHeader": "Jarvis-Required-Capabilities",
    "ExtensionsHeader": "Jarvis-Extensions",
}

REQUIRED_REQUEST_BODIES = {
    "WorkerBody": "Worker",
    "ActorBody": "Actor",
    "WorkSessionBody": "WorkSession",
    "JarvisEventBody": "JarvisEvent",
    "PolicyDecisionBody": "PolicyDecision",
    "RequestBody": "Request",
    "ReviewBody": "Review",
    "TakeoverBody": "Takeover",
    "ContributionBody": "Contribution",
    "LearningRecordBody": "LearningRecord",
    "MemoryProposalBody": "MemoryProposal",
    "SkillProposalBody": "SkillProposal",
    "OutcomeReportBody": "OutcomeReport",
}

REQUIRED_RESPONSES = {
    "WorkerResponse": "Worker",
    "ActorResponse": "Actor",
    "WorkSessionResponse": "WorkSession",
    "JarvisEventResponse": "JarvisEvent",
    "PolicyDecisionResponse": "PolicyDecision",
    "RequestResponse": "Request",
    "ReviewResponse": "Review",
    "TakeoverResponse": "Takeover",
    "ContributionResponse": "Contribution",
    "LearningRecordResponse": "LearningRecord",
    "MemoryProposalResponse": "MemoryProposal",
    "SkillProposalResponse": "SkillProposal",
    "EvidenceManifestResponse": "EvidenceManifest",
    "OutcomeReportResponse": "OutcomeReport",
    "ProtocolErrorResponse": "ProtocolError",
}

REQUIRED_EXAMPLES = {
    "WorkSessionCreateExample": {
        "id",
        "protocol_version",
        "created_by_actor_id",
        "objective",
        "human_worker_id",
        "agent_worker_id",
        "policy_id",
        "status",
        "revision",
        "last_event_hash",
        "event_log_ref",
        "created_at",
        "updated_at",
    },
    "PolicyDecisionDeniedExample": {
        "id",
        "work_session_id",
        "actor_id",
        "policy_id",
        "requested_action",
        "normalized_action_hash",
        "risk_class",
        "result",
        "reason",
        "created_at",
    },
    "RequestBlockedActionExample": {
        "id",
        "protocol_version",
        "work_session_id",
        "requester_actor_id",
        "requester_worker_id",
        "target_human_worker_id",
        "policy_decision_id",
        "type",
        "blocking_scope",
        "reason_code",
        "reason_summary",
        "requested_action",
        "requested_outcome",
        "risk_class",
        "human_decision_needed",
        "options",
        "default_if_no_response",
        "status",
        "created_at",
        "expires_at",
    },
    "ReviewApproveRequestExample": {
        "id",
        "work_session_id",
        "reviewer_actor_id",
        "reviewer_worker_id",
        "target_ref",
        "decision",
        "approval_scope",
        "created_at",
    },
    "EvidenceManifestExportExample": {
        "id",
        "work_session_id",
        "generated_by_actor_id",
        "objective",
        "event_chain_root",
        "evidence_item_refs",
        "policy_decision_refs",
        "request_refs",
        "review_refs",
        "takeover_refs",
        "contribution_refs",
        "export_profile",
        "generated_at",
    },
    "ProtocolErrorExample": {
        "error_id",
        "protocol_version",
        "object_type",
        "field",
        "reason",
        "remediation",
        "trace_id",
    },
}

EXAMPLE_REQUIRED_VALUES = {
    ("WorkSessionCreateExample", "revision"): 1,
    ("WorkSessionCreateExample", "last_event_hash"): "hash:event-worksession-created",
    ("PolicyDecisionDeniedExample", "result"): "deny",
    ("RequestBlockedActionExample", "status"): "pending",
    ("ReviewApproveRequestExample", "decision"): "approve",
}

EXAMPLE_REQUIRED_OBJECTS = {
    ("ReviewApproveRequestExample", "approval_scope"),
}

EXAMPLE_REQUIRED_NON_EMPTY_FIELDS = {
    ("RequestBlockedActionExample", "blocking_scope"),
}

EXAMPLE_REQUIRED_NON_EMPTY_ARRAYS = {
    ("EvidenceManifestExportExample", "evidence_item_refs"),
    ("EvidenceManifestExportExample", "policy_decision_refs"),
    ("EvidenceManifestExportExample", "request_refs"),
    ("EvidenceManifestExportExample", "review_refs"),
    ("EvidenceManifestExportExample", "contribution_refs"),
}

WORKSESSION_MUTATION_HEADERS = {
    "ProtocolVersionHeader",
    "ActorHeader",
    "IdempotencyHeader",
    "RequestTimestampHeader",
    "RevisionHeader",
    "PreviousHashHeader",
}

NON_WORKSESSION_MUTATION_HEADERS = {
    "ProtocolVersionHeader",
    "ActorHeader",
    "IdempotencyHeader",
    "RequestTimestampHeader",
}

READ_HEADERS = {
    "ProtocolVersionHeader",
    "ActorHeader",
}

READ_OPTIONAL_NEGOTIATION_HEADERS = {
    "RequiredCapabilitiesHeader",
    "ExtensionsHeader",
}

REQUIRED_OPERATIONS = {
    ("put", "/workers/{worker_id}"): {
        "operation_id": "registerWorker",
        "operation_class": "non_worksession_mutation",
        "tag": "Workers",
        "headers": NON_WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkerIdPath"},
        "request_body": "WorkerBody",
        "success_status": "200",
        "success_response": "WorkerResponse",
    },
    ("put", "/actors/{actor_id}"): {
        "operation_id": "registerActor",
        "operation_class": "non_worksession_mutation",
        "tag": "Workers",
        "headers": NON_WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"ActorIdPath"},
        "request_body": "ActorBody",
        "success_status": "200",
        "success_response": "ActorResponse",
    },
    ("post", "/work-sessions"): {
        "operation_id": "createWorkSession",
        "operation_class": "worksession_genesis_mutation",
        "tag": "WorkSessions",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": set(),
        "request_body": "WorkSessionBody",
        "success_status": "201",
        "success_response": "WorkSessionResponse",
    },
    ("get", "/work-sessions/{work_session_id}"): {
        "operation_id": "getWorkSession",
        "operation_class": "worksession_scoped_read",
        "tag": "WorkSessions",
        "headers": READ_HEADERS | READ_OPTIONAL_NEGOTIATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": None,
        "success_status": "200",
        "success_response": "WorkSessionResponse",
    },
    ("post", "/work-sessions/{work_session_id}/events"): {
        "operation_id": "appendJarvisEvent",
        "operation_class": "worksession_scoped_mutation",
        "tag": "WorkSessions",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": "JarvisEventBody",
        "success_status": "201",
        "success_response": "JarvisEventResponse",
    },
    ("post", "/work-sessions/{work_session_id}/policy-decisions"): {
        "operation_id": "recordPolicyDecision",
        "operation_class": "worksession_scoped_mutation",
        "tag": "ControlPlane",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": "PolicyDecisionBody",
        "success_status": "201",
        "success_response": "PolicyDecisionResponse",
    },
    ("post", "/work-sessions/{work_session_id}/requests"): {
        "operation_id": "createRequest",
        "operation_class": "worksession_scoped_mutation",
        "tag": "ControlPlane",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": "RequestBody",
        "success_status": "201",
        "success_response": "RequestResponse",
    },
    ("post", "/work-sessions/{work_session_id}/reviews"): {
        "operation_id": "recordReview",
        "operation_class": "worksession_scoped_mutation",
        "tag": "ControlPlane",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": "ReviewBody",
        "success_status": "201",
        "success_response": "ReviewResponse",
    },
    ("post", "/work-sessions/{work_session_id}/takeovers"): {
        "operation_id": "recordTakeover",
        "operation_class": "worksession_scoped_mutation",
        "tag": "ControlPlane",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": "TakeoverBody",
        "success_status": "201",
        "success_response": "TakeoverResponse",
    },
    ("post", "/work-sessions/{work_session_id}/contributions"): {
        "operation_id": "recordContribution",
        "operation_class": "worksession_scoped_mutation",
        "tag": "Attribution",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": "ContributionBody",
        "success_status": "201",
        "success_response": "ContributionResponse",
    },
    ("post", "/work-sessions/{work_session_id}/learning-records"): {
        "operation_id": "createLearningRecord",
        "operation_class": "worksession_scoped_mutation",
        "tag": "Learning",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": "LearningRecordBody",
        "success_status": "201",
        "success_response": "LearningRecordResponse",
    },
    ("post", "/work-sessions/{work_session_id}/memory-proposals"): {
        "operation_id": "createMemoryProposal",
        "operation_class": "worksession_scoped_mutation",
        "tag": "Learning",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": "MemoryProposalBody",
        "success_status": "201",
        "success_response": "MemoryProposalResponse",
    },
    ("post", "/work-sessions/{work_session_id}/skill-proposals"): {
        "operation_id": "createSkillProposal",
        "operation_class": "worksession_scoped_mutation",
        "tag": "Learning",
        "headers": WORKSESSION_MUTATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": "SkillProposalBody",
        "success_status": "201",
        "success_response": "SkillProposalResponse",
    },
    ("get", "/work-sessions/{work_session_id}/export"): {
        "operation_id": "exportEvidenceManifest",
        "operation_class": "export_read",
        "tag": "Evidence",
        "headers": READ_HEADERS | READ_OPTIONAL_NEGOTIATION_HEADERS,
        "path_parameters": {"WorkSessionIdPath"},
        "request_body": None,
        "success_status": "200",
        "success_response": "EvidenceManifestResponse",
    },
    ("post", "/outcome-reports"): {
        "operation_id": "submitOutcomeReport",
        "operation_class": "non_worksession_mutation",
        "tag": "Feedback",
        "headers": NON_WORKSESSION_MUTATION_HEADERS,
        "path_parameters": set(),
        "request_body": "OutcomeReportBody",
        "success_status": "202",
        "success_response": "OutcomeReportResponse",
    },
}

REQUIRED_SCHEMA_FIELDS = {
    "Worker": {
        "id",
        "type",
        "role",
        "authority_scope",
        "accountability_scope",
    },
    "Actor": {
        "id",
        "worker_id",
        "type",
        "event_authority",
        "contribution_scope",
        "created_at",
    },
    "HumanWorker": {
        "worker_id",
        "actor_id",
        "role",
        "policy_authority",
        "review_authority",
    },
    "AgentWorker": {
        "worker_id",
        "actor_id",
        "agent_ref",
        "role",
        "capability_refs",
        "autonomy_level",
        "operating_constraints",
    },
    "WorkSession": {
        "id",
        "protocol_version",
        "created_by_actor_id",
        "objective",
        "human_worker_id",
        "agent_worker_id",
        "policy_id",
        "status",
        "revision",
        "last_event_hash",
        "event_log_ref",
        "created_at",
        "updated_at",
    },
    "JarvisEvent": {
        "id",
        "sequence",
        "type",
        "work_session_id",
        "actor_id",
        "timestamp",
        "payload",
        "previous_hash",
        "event_hash",
        "canonicalization",
    },
    "Policy": {
        "id",
        "owner_worker_id",
        "created_by_actor_id",
        "autonomy_level",
        "allowed_actions",
        "denied_actions",
        "review_required_actions",
        "risk_classes",
        "escalation_rules",
        "created_at",
    },
    "PolicyDecision": {
        "id",
        "work_session_id",
        "actor_id",
        "policy_id",
        "requested_action",
        "normalized_action_hash",
        "risk_class",
        "result",
        "reason",
        "created_at",
    },
    "ApprovalScope": {
        "request_id",
        "review_id",
        "policy_decision_id",
        "request_revision",
        "request_event_hash",
        "normalized_action_hash",
        "approved_action",
        "allowed_scope",
        "denied_scope",
        "expires_at",
        "max_uses",
        "applies_to_work_session_id",
        "applies_to_actor_id",
    },
    "TakeoverScope": {
        "blocking_scope",
        "scope_ref",
    },
    "Request": {
        "id",
        "protocol_version",
        "work_session_id",
        "requester_actor_id",
        "requester_worker_id",
        "target_human_worker_id",
        "policy_decision_id",
        "type",
        "blocking_scope",
        "reason_code",
        "reason_summary",
        "requested_action",
        "requested_outcome",
        "risk_class",
        "human_decision_needed",
        "options",
        "default_if_no_response",
        "status",
        "created_at",
        "expires_at",
    },
    "Review": {
        "id",
        "work_session_id",
        "reviewer_actor_id",
        "reviewer_worker_id",
        "target_ref",
        "decision",
        "created_at",
    },
    "Takeover": {
        "id",
        "work_session_id",
        "requested_by_actor_id",
        "controlling_actor_id",
        "affected_scope",
        "reason",
        "lock_epoch",
        "state",
        "created_at",
    },
    "ContributorRef": {
        "worker_id",
        "actor_id",
        "contribution_role",
    },
    "ExportProfile": {
        "profile",
    },
    "EvidenceItemRef": {
        "id",
        "work_session_id",
        "source_event_refs",
        "captured_by_actor_id",
        "evidence_type",
        "artifact_ref",
        "content_hash",
        "trust_label",
        "redaction_state",
        "captured_at",
        "limitation_refs",
    },
    "Contribution": {
        "id",
        "work_session_id",
        "contributor_refs",
        "contributor_type",
        "contribution_type",
        "event_refs",
        "created_at",
    },
    "EvidenceManifest": {
        "id",
        "work_session_id",
        "generated_by_actor_id",
        "objective",
        "event_chain_root",
        "evidence_item_refs",
        "policy_decision_refs",
        "request_refs",
        "review_refs",
        "takeover_refs",
        "contribution_refs",
        "export_profile",
        "generated_at",
    },
    "LearningRecord": {
        "id",
        "work_session_id",
        "created_by_actor_id",
        "subject_type",
        "subject_ref",
        "lesson_type",
        "source_event_refs",
        "review_state",
        "scope",
        "created_at",
    },
    "MemoryProposal": {
        "id",
        "work_session_id",
        "proposed_by_actor_id",
        "proposed_for",
        "memory_scope",
        "memory_type",
        "content",
        "provenance",
        "confidence",
        "review_required",
        "status",
        "created_at",
    },
    "SkillProposal": {
        "id",
        "work_session_id",
        "proposed_by_actor_id",
        "proposed_for",
        "skill_scope",
        "skill_name",
        "trigger_conditions",
        "procedure",
        "review_checks",
        "failure_cases",
        "provenance",
        "status",
        "created_at",
    },
    "OutcomeReport": {
        "id",
        "work_session_id",
        "source_ref",
        "reporter_ref",
        "accepted_by_actor_id",
        "outcome",
        "learning_record_refs",
        "received_at",
    },
    "ProtocolError": {
        "error_id",
        "protocol_version",
        "object_type",
        "field",
        "reason",
        "remediation",
        "trace_id",
    },
}

OPTIONAL_SCHEMA_FIELDS = {
    "WorkSession": {
        "source_ref",
        "context_manifest_ref",
        "contribution_ledger_ref",
        "evidence_manifest_ref",
        "learning_record_refs",
    },
    "JarvisEvent": {
        "trace_context",
        "actor_signature",
        "signing_key_ref",
    },
    "Policy": {
        "tool_grants",
        "memory_grants",
        "external_send_rules",
        "request_limits",
        "extensions",
    },
    "PolicyDecision": {
        "data_sensitivity",
        "selected_grant_refs",
        "denied_grant_refs",
        "request_id",
        "evidence_refs",
    },
    "Request": {
        "missing_permission_or_context",
        "policy_refs",
        "data_sensitivity",
        "recommended_option",
        "safer_alternatives",
        "evidence_refs",
        "artifact_refs",
        "contribution_refs",
        "resolved_at",
        "resolved_by_review_id",
        "resolved_by_takeover_id",
        "closed_by_event_ref",
        "superseded_by_request_id",
        "duplicate_of_request_id",
    },
    "Review": {
        "comments",
        "required_changes",
        "approval_scope",
        "takeover_id",
    },
    "TakeoverScope": {
        "normalized_action_hash",
        "artifact_refs",
    },
    "Takeover": {
        "request_id",
        "resumed_by_actor_id",
        "reconciliation_notes",
        "reconciliation_refs",
        "resolved_at",
    },
    "ExportProfile": {
        "version",
        "redaction_profile_ref",
    },
    "Contribution": {
        "artifact_refs",
        "review_refs",
        "evidence_refs",
        "confidence",
        "limitations",
    },
    "EvidenceManifest": {
        "artifact_refs",
        "limitation_refs",
        "redaction_refs",
    },
    "LearningRecord": {
        "proposed_change",
        "memory_proposal_refs",
        "skill_proposal_refs",
        "outcome_report_refs",
    },
    "MemoryProposal": {
        "source_event_refs",
        "review_refs",
        "expires_at",
        "learning_record_refs",
    },
    "SkillProposal": {
        "required_tools",
        "source_event_refs",
        "review_refs",
        "learning_record_refs",
    },
    "OutcomeReport": {
        "external_system_ref",
        "reporter_actor_id",
        "reason",
        "reviewer_feedback_refs",
    },
}

REQUIRED_ENUMS = {
    "WorkerType": {
        "human",
        "agent",
        "service",
        "tool",
    },
    "ActorType": {
        "human",
        "agent",
        "service",
        "tool",
    },
    "ContributionRole": {
        "human",
        "agent",
        "shared",
        "service",
        "tool",
    },
    "AutonomyLevel": {
        "observe_only",
        "propose_only",
        "execute_with_review",
        "bounded_execute",
        "full_execute_in_scope",
    },
    "WorkSessionStatus": {
        "created",
        "active",
        "waiting_on_human",
        "takeover",
        "reconciling",
        "completed",
        "failed",
        "cancelled",
        "closed",
    },
    "PolicyDecisionResult": {
        "allow",
        "deny",
        "narrow",
        "review_required",
    },
    "RiskClass": {
        "low",
        "medium",
        "high",
        "critical",
    },
    "DataSensitivity": {
        "public",
        "private",
        "confidential",
        "restricted",
    },
    "RequestType": {
        "permission",
        "context",
        "judgment",
        "review",
        "correction",
        "takeover",
        "escalation",
    },
    "RequestStatus": {
        "pending",
        "acknowledged",
        "approved",
        "denied",
        "narrowed",
        "answered",
        "needs_revision",
        "takeover",
        "expired",
        "cancelled",
        "superseded",
    },
    "BlockingScope": {
        "action",
        "branch",
        "artifact",
        "tool_call",
        "external_send",
        "final_submission",
        "work_session",
    },
    "ReviewDecision": {
        "approve",
        "deny",
        "narrow",
        "correct",
        "takeover",
        "needs_revision",
    },
    "TakeoverState": {
        "requested",
        "locked",
        "human_active",
        "reconciliation_required",
        "resumed",
        "closed",
    },
    "ContributorType": {
        "human",
        "agent",
        "service",
        "tool",
        "shared",
    },
    "ContributionType": {
        "intent",
        "instruction",
        "plan",
        "research",
        "execution",
        "artifact",
        "review",
        "correction",
        "decision",
        "evidence_capture",
        "memory_proposal",
        "skill_proposal",
        "submission",
    },
    "LearningSubjectType": {
        "human",
        "agent",
        "pair",
    },
    "LearningReviewState": {
        "proposed",
        "accepted",
        "rejected",
        "superseded",
    },
    "ProposalTargetType": {
        "human",
        "agent",
        "pair",
        "project",
        "task",
    },
    "MemoryProposalStatus": {
        "proposed",
        "pending_review",
        "accepted",
        "rejected",
        "superseded",
        "expired",
    },
    "SkillProposalStatus": {
        "proposed",
        "pending_review",
        "accepted",
        "rejected",
        "superseded",
        "archived",
    },
    "ProtocolErrorId": {
        "invalid_transition",
        "unknown_state",
        "missing_protocol_version",
        "unsupported_protocol_version",
        "missing_request_timestamp",
        "stale_request_timestamp",
        "missing_expected_work_session_revision",
        "missing_previous_event_hash",
        "stale_work_session_revision",
        "missing_idempotency_key",
        "missing_actor",
        "invalid_extension_namespace",
        "extension_core_field_override",
        "missing_policy",
        "missing_policy_decision",
        "missing_objective",
        "policy_denied",
        "request_unresolved",
        "review_required",
        "invalid_request_transition",
        "missing_review_resolution",
        "missing_takeover_resolution",
        "invalid_approval_scope",
        "approval_scope_expired",
        "approval_scope_mismatch",
        "stale_takeover_epoch",
        "invalid_event_hash",
        "invalid_previous_event_hash",
        "duplicate_idempotency_key_mismatch",
        "request_livelock",
        "duplicate_request_mismatch",
        "missing_jarvis_event",
        "missing_blocked_scope_resolution_refs",
        "missing_reconciliation_refs",
        "mutation_after_closed",
        "unauthorized_actor",
        "invalid_export",
        "invalid_export_state",
        "invalid_evidence_export_state",
        "missing_contribution_actor",
        "invalid_contributor_refs",
        "shared_contribution_without_individual_refs",
        "duplicate_contributor_ref",
        "evidence_after_the_fact",
        "missing_evidence_event_refs",
        "duplicate_evidence_item_ref",
        "forbidden_export_field",
        "silent_memory_mutation",
        "silent_skill_activation",
        "model_self_confirmed_memory",
        "tool_self_confirmed_memory",
        "skill_expands_tool_access_without_policy_review",
        "sealed_work_session_mutation",
        "sealed_evidence_mutation",
        "outcome_report_without_learning_record",
        "unsupported_capability",
        "forbidden_host_private_field",
    },
}

REQUIRED_CLOSED_OBJECT_SCHEMAS = {
    "AuthorityScope",
    "AccountabilityScope",
    "CapabilityRef",
    "EventAuthority",
    "ContributionScope",
    "CanonicalizationProfile",
    "ProtocolTraceContext",
    "JarvisEventPayload",
    "PolicyConstraint",
    "EscalationRule",
    "PolicyActionRule",
    "PolicyRequestLimits",
    "PolicyActionRequest",
    "RequestOption",
    "SafeFallback",
    "ApprovalBoundary",
    "TakeoverScope",
    "ApprovalScope",
    "ContributorRef",
    "ExportProfile",
    "EvidenceItemRef",
    "Worker",
    "Actor",
    "HumanWorker",
    "AgentWorker",
    "WorkSession",
    "JarvisEvent",
    "Policy",
    "PolicyDecision",
    "Request",
    "Review",
    "Takeover",
    "Contribution",
    "EvidenceManifest",
    "LearningRecord",
    "MemoryProposal",
    "SkillProposal",
    "OutcomeReport",
    "ProtocolError",
}

REQUIRED_FORBIDDEN_METADATA = {
    "Worker": {
        "password",
        "credential",
        "raw_auth_token",
        "billing_account",
        "provider_secret",
        "database_primary_key",
        "deployment_resource_id",
    },
    "Actor": {
        "credential",
        "raw_auth_token",
        "session_cookie",
        "private_key",
        "database_primary_key",
    },
    "HumanWorker": {
        "password",
        "credential",
        "raw_auth_token",
        "private_profile_data",
        "billing_account",
        "host_account_record",
    },
    "AgentWorker": {
        "model_api_key",
        "provider_secret",
        "raw_prompt_store",
        "runtime_process_id",
        "container_id",
        "database_primary_key",
    },
    "WorkSession": {
        "database_primary_key",
        "queue_message_id",
        "runtime_session_id",
        "cloud_resource_id",
        "ui_state",
        "credential",
        "raw_auth_token",
    },
    "JarvisEvent": {
        "raw_auth_token",
        "credential",
        "private_key",
        "database_primary_key",
        "runtime_trace_secret",
        "provider_secret",
    },
    "Policy": {
        "credential",
        "raw_auth_token",
        "provider_secret",
        "billing_rule",
        "cloud_policy_id",
        "database_primary_key",
    },
    "PolicyDecision": {
        "hidden_policy_trace",
        "credential",
        "provider_secret",
        "database_primary_key",
        "runtime_decision_object",
    },
    "TakeoverScope": {
        "runtime_lock_id",
        "database_primary_key",
        "credential",
        "raw_auth_token",
        "ui_session_id",
    },
    "ApprovalScope": {
        "unbounded_approval",
        "implicit_authority_grant",
        "credential",
        "raw_auth_token",
        "database_primary_key",
    },
    "Request": {
        "private_inbox_id",
        "notification_provider_id",
        "credential",
        "raw_auth_token",
        "database_primary_key",
        "runtime_state",
        "provider_secret",
        "billing_field",
        "deployment_field",
        "ui_state",
        "hidden_policy_trace",
        "unbounded_approval",
        "implicit_authority_grant",
    },
    "Review": {
        "private_comment_thread_id",
        "credential",
        "raw_auth_token",
        "database_primary_key",
        "ui_state",
        "unbounded_approval",
        "implicit_authority_grant",
    },
    "Takeover": {
        "runtime_lock_id",
        "database_primary_key",
        "credential",
        "raw_auth_token",
        "ui_session_id",
    },
    "ContributorRef": {
        "payment_account",
        "compensation_rule",
        "private_score",
        "credential",
        "database_primary_key",
    },
    "ExportProfile": {
        "credential",
        "raw_auth_token",
        "provider_secret",
        "session_cookie",
        "private_key",
        "database_primary_key",
        "cloud_storage_secret",
        "unredacted_secret_value",
        "raw_runtime_state",
        "host_only_database_id",
        "deployment_detail",
        "billing_data",
        "private_score",
        "ui_state",
    },
    "EvidenceItemRef": {
        "credential",
        "raw_auth_token",
        "provider_secret",
        "session_cookie",
        "private_key",
        "database_primary_key",
        "cloud_storage_secret",
        "unredacted_secret_value",
        "raw_runtime_state",
        "host_only_database_id",
        "deployment_detail",
        "billing_data",
        "private_score",
        "ui_state",
    },
    "Contribution": {
        "payment_account",
        "compensation_rule",
        "private_score",
        "credential",
        "database_primary_key",
    },
    "EvidenceManifest": {
        "credential",
        "raw_auth_token",
        "provider_secret",
        "session_cookie",
        "private_key",
        "database_primary_key",
        "cloud_storage_secret",
        "unredacted_secret_value",
        "raw_runtime_state",
        "host_only_database_id",
        "deployment_detail",
        "billing_data",
        "private_score",
        "ui_state",
    },
    "LearningRecord": {
        "silent_memory_write",
        "unreviewed_skill_activation",
        "credential",
        "raw_auth_token",
        "database_primary_key",
    },
    "MemoryProposal": {
        "silent_memory_write",
        "credential",
        "raw_auth_token",
        "private_embedding_store_id",
        "database_primary_key",
    },
    "SkillProposal": {
        "automatic_tool_grant",
        "unreviewed_skill_activation",
        "credential",
        "raw_auth_token",
        "database_primary_key",
    },
    "OutcomeReport": {
        "task_marketplace_score_rule",
        "payment_status",
        "settlement_account",
        "credential",
        "raw_auth_token",
        "database_primary_key",
        "sealed_work_session_mutation",
        "sealed_evidence_mutation",
    },
    "ProtocolError": {
        "credential",
        "raw_auth_token",
        "provider_secret",
        "session_cookie",
        "private_key",
        "database_primary_key",
        "raw_runtime_state",
        "host_only_database_id",
        "deployment_detail",
        "billing_data",
        "private_score",
        "ui_state",
    },
}

REQUIRED_SCHEMA_INVARIANTS = {
    "EvidenceManifest": {
        "final_export_requires_terminal_work_session_state",
        "sealed_evidence_manifest_rejects_mutation",
        "redaction_never_replaces_source_evidence",
    },
    "MemoryProposal": {
        "accepted_memory_requires_review_refs",
        "model_derived_memory_cannot_self_confirm",
        "tool_derived_memory_cannot_self_confirm",
    },
    "SkillProposal": {
        "accepted_skill_requires_review_refs",
        "skill_tool_access_expansion_requires_policy_review",
        "unreviewed_skill_change_cannot_activate",
    },
    "OutcomeReport": {
        "outcome_report_requires_terminal_source",
        "outcome_report_does_not_mutate_sealed_work_session",
        "outcome_report_does_not_mutate_sealed_evidence_manifest",
        "outcome_report_requires_learning_record_refs",
    },
}

REQUIRED_IDENTITY_UNIQUE_ARRAYS = {
    ("Contribution", "contributor_refs"): {
        "unique_by": ["worker_id", "actor_id"],
        "duplicate_rejection_id": "duplicate_contributor_ref",
    },
    ("EvidenceManifest", "evidence_item_refs"): {
        "unique_by": ["id"],
        "duplicate_rejection_id": "duplicate_evidence_item_ref",
    },
}

FORBIDDEN_SCHEMA_PROPERTIES = {
    "password",
    "credential",
    "raw_auth_token",
    "billing_account",
    "provider_secret",
    "database_primary_key",
    "deployment_resource_id",
    "session_cookie",
    "private_key",
    "private_profile_data",
    "host_account_record",
    "model_api_key",
    "raw_prompt_store",
    "runtime_process_id",
    "container_id",
    "queue_message_id",
    "runtime_session_id",
    "cloud_resource_id",
    "runtime_trace_secret",
    "billing_rule",
    "cloud_policy_id",
    "hidden_policy_trace",
    "runtime_decision_object",
    "private_inbox_id",
    "notification_provider_id",
    "runtime_state",
    "billing_field",
    "deployment_field",
    "unbounded_approval",
    "implicit_authority_grant",
    "private_comment_thread_id",
    "runtime_lock_id",
    "ui_session_id",
    "payment_account",
    "compensation_rule",
    "private_score",
    "cloud_storage_secret",
    "unredacted_secret_value",
    "raw_runtime_state",
    "host_only_database_id",
    "deployment_detail",
    "billing_data",
    "silent_memory_write",
    "unreviewed_skill_activation",
    "private_embedding_store_id",
    "automatic_tool_grant",
    "task_marketplace_score_rule",
    "payment_status",
    "settlement_account",
    "sealed_work_session_mutation",
    "sealed_evidence_mutation",
}

REQUIRED_TAGS = {
    "Workers",
    "WorkSessions",
    "ControlPlane",
    "Attribution",
    "Learning",
    "Evidence",
    "Feedback",
    "Conformance",
}

EXPECTED_TITLE = "Jarvis Human-Agent Collaboration Protocol"
EXPECTED_PLACEHOLDER_SERVER = "https://jarvis.example.invalid"
EXPECTED_CHUNK_ID = "week-2-chunk-7-examples-conformance-entry"
REQUIRED_CHUNK_LOCKS = {
    "OpenAPI 3.1.1 entry point",
    "v0.1 protocol metadata",
    "required top-level buckets",
    "tag taxonomy",
    "host-owned server boundary",
    "shared schema primitives",
    "Worker schema",
    "Actor schema",
    "HumanWorker schema",
    "AgentWorker schema",
    "WorkSession schema",
    "JarvisEvent schema",
    "Policy schema",
    "PolicyDecision schema",
    "Request schema",
    "Review schema",
    "ApprovalScope schema",
    "Takeover schema",
    "Contribution schema",
    "EvidenceItemRef schema",
    "EvidenceManifest schema",
    "LearningRecord schema",
    "MemoryProposal schema",
    "SkillProposal schema",
    "OutcomeReport schema",
    "ProtocolError schema",
    "path operation layout",
    "request body refs",
    "success response refs",
    "protocol header parameters",
    "HostAuth security scheme",
    "protocol error response",
    "protocol examples",
    "conformance entry documents",
}
REQUIRED_CONFORMANCE_REJECTION_IDS = {
    "missing_protocol_version",
    "missing_actor",
    "unauthorized_actor",
    "missing_idempotency_key",
    "missing_request_timestamp",
    "stale_request_timestamp",
    "missing_expected_work_session_revision",
    "missing_previous_event_hash",
    "missing_policy_decision",
    "missing_review_resolution",
    "missing_takeover_resolution",
    "invalid_approval_scope",
    "stale_work_session_revision",
    "invalid_previous_event_hash",
    "stale_takeover_epoch",
    "invalid_evidence_export_state",
    "sealed_work_session_mutation",
    "sealed_evidence_mutation",
    "forbidden_host_private_field",
    "silent_memory_mutation",
    "silent_skill_activation",
    "outcome_report_without_learning_record",
}
PORTABLE_VALUE_REF = {"$ref": "#/components/schemas/PortableValue"}
FORBIDDEN_PORTABLE_KEY_PATTERN = (
    "^(?!.*(password|credential|token|secret|private_key|session_cookie|"
    "cookie|api_key|access_key|auth_header|oauth|database|billing|runtime|"
    "container|deployment|model_api_key|raw_prompt|host_account|ui_state))"
)
NAMESPACED_EXTENSION_PATTERN = (
    FORBIDDEN_PORTABLE_KEY_PATTERN
    + "[a-z0-9][a-z0-9-]*(\\.[a-z0-9_-]+)+$"
)
PORTABLE_PROPERTY_PATTERN = (
    FORBIDDEN_PORTABLE_KEY_PATTERN
    + "[a-z0-9][a-z0-9._:-]*$"
)


def fail(message: str) -> int:
    print(f"openapi contract check failed: {message}")
    return 1


def schema_requires_field_when_const(
    schema: dict, property_name: str, const_value: str, required_field: str
) -> bool:
    for branch in schema.get("allOf", []):
        if not isinstance(branch, dict):
            continue
        condition = branch.get("if", {})
        consequence = branch.get("then", {})
        if not isinstance(condition, dict) or not isinstance(consequence, dict):
            continue
        properties = condition.get("properties", {})
        if not isinstance(properties, dict):
            continue
        target = properties.get(property_name, {})
        if not isinstance(target, dict):
            continue
        required = consequence.get("required", [])
        if target.get("const") == const_value and required_field in required:
            return True
    return False


def schema_requires_field_when_enum(
    schema: dict, property_name: str, enum_values: set[str], required_field: str
) -> bool:
    for branch in schema.get("allOf", []):
        if not isinstance(branch, dict):
            continue
        condition = branch.get("if", {})
        consequence = branch.get("then", {})
        if not isinstance(condition, dict) or not isinstance(consequence, dict):
            continue
        properties = condition.get("properties", {})
        if not isinstance(properties, dict):
            continue
        target = properties.get(property_name, {})
        if not isinstance(target, dict):
            continue
        actual_values = set(target.get("enum", []))
        required = consequence.get("required", [])
        if actual_values == enum_values and required_field in required:
            return True
    return False


def schema_forbids_field_when_enum(
    schema: dict, property_name: str, enum_values: set[str], forbidden_field: str
) -> bool:
    for branch in schema.get("allOf", []):
        if not isinstance(branch, dict):
            continue
        condition = branch.get("if", {})
        consequence = branch.get("then", {})
        if not isinstance(condition, dict) or not isinstance(consequence, dict):
            continue
        properties = condition.get("properties", {})
        if not isinstance(properties, dict):
            continue
        target = properties.get(property_name, {})
        if not isinstance(target, dict):
            continue
        actual_values = set(target.get("enum", []))
        negative_schema = consequence.get("not")
        if actual_values == enum_values and negative_schema_forbids_field(
            negative_schema, forbidden_field
        ):
            return True
    return False


def negative_schema_forbids_field(negative_schema, forbidden_field: str) -> bool:
    if not isinstance(negative_schema, dict):
        return False
    if forbidden_field in negative_schema.get("required", []):
        return True
    for keyword in ("anyOf", "oneOf"):
        for subschema in negative_schema.get(keyword, []):
            if isinstance(subschema, dict) and forbidden_field in subschema.get(
                "required", []
            ):
                return True
    return False


def schema_forbids_fields_when_enum(
    schema: dict, property_name: str, enum_values: set[str], forbidden_fields: set[str]
) -> bool:
    for branch in schema.get("allOf", []):
        if not isinstance(branch, dict):
            continue
        condition = branch.get("if", {})
        consequence = branch.get("then", {})
        if not isinstance(condition, dict) or not isinstance(consequence, dict):
            continue
        properties = condition.get("properties", {})
        if not isinstance(properties, dict):
            continue
        target = properties.get(property_name, {})
        if not isinstance(target, dict):
            continue
        actual_values = set(target.get("enum", []))
        if actual_values != enum_values:
            continue
        negative_schema = consequence.get("not")
        if all(
            negative_schema_forbids_field(negative_schema, forbidden_field)
            for forbidden_field in forbidden_fields
        ):
            return True
    return False


def schema_requires_min_items_when_const(
    schema: dict, property_name: str, const_value: str, array_field: str, min_items: int
) -> bool:
    for branch in schema.get("allOf", []):
        if not isinstance(branch, dict):
            continue
        condition = branch.get("if", {})
        consequence = branch.get("then", {})
        if not isinstance(condition, dict) or not isinstance(consequence, dict):
            continue
        properties = condition.get("properties", {})
        if not isinstance(properties, dict):
            continue
        target = properties.get(property_name, {})
        if not isinstance(target, dict) or target.get("const") != const_value:
            continue
        consequence_properties = consequence.get("properties", {})
        if not isinstance(consequence_properties, dict):
            continue
        array_schema = consequence_properties.get(array_field, {})
        if isinstance(array_schema, dict) and array_schema.get("minItems") == min_items:
            return True
    return False


def iter_refs(value, path: str = "$"):
    if isinstance(value, dict):
        ref = value.get("$ref")
        if isinstance(ref, str):
            yield path, ref
        for key, child in value.items():
            yield from iter_refs(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_refs(child, f"{path}[{index}]")


def local_ref_exists(document: dict, ref: str) -> bool:
    if not ref.startswith("#/"):
        return True
    current = document
    for raw_part in ref[2:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or part not in current:
            return False
        current = current[part]
    return True


def component_ref(bucket: str, name: str) -> str:
    return f"#/components/{bucket}/{name}"


def media_schema_ref(component: dict) -> str | None:
    if not isinstance(component, dict):
        return None
    content = component.get("content", {})
    if not isinstance(content, dict):
        return None
    media = content.get("application/json", {})
    if not isinstance(media, dict):
        return None
    schema = media.get("schema", {})
    if not isinstance(schema, dict):
        return None
    return schema.get("$ref")


def operation_parameter_names(operation: dict) -> set[str]:
    names = set()
    for parameter in operation.get("parameters", []):
        if not isinstance(parameter, dict):
            names.add("__invalid_parameter__")
            continue
        ref = parameter.get("$ref", "")
        if ref.startswith("#/components/parameters/"):
            names.add(ref.rsplit("/", 1)[-1])
        else:
            names.add("__invalid_parameter__")
    return names


def iter_keys(value, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, str(key)
            yield from iter_keys(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_keys(child, f"{path}[{index}]")


def forbidden_example_keys(value) -> list[str]:
    forbidden_terms = {
        "password",
        "credential",
        "token",
        "secret",
        "private_key",
        "session_cookie",
        "cookie",
        "api_key",
        "access_key",
        "auth_header",
        "oauth",
        "database",
        "billing",
        "runtime",
        "container",
        "deployment",
        "model_api_key",
        "raw_prompt",
        "host_account",
        "ui_state",
        "private_score",
    }
    failures = []
    for path, key in iter_keys(value):
        normalized = key.lower()
        if any(term in normalized for term in forbidden_terms):
            failures.append(f"{path}.{key}")
    return failures


def main() -> int:
    if not OPENAPI_PATH.exists():
        return fail(f"missing {OPENAPI_PATH.relative_to(ROOT)}")

    data = yaml.safe_load(OPENAPI_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return fail("root document is not an object")

    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        return fail(f"missing top-level keys: {', '.join(sorted(missing))}")

    if data["openapi"] != "3.1.1":
        return fail("openapi must be 3.1.1")

    info = data["info"]
    if not isinstance(info, dict):
        return fail("info must be an object")
    if info.get("version") != "0.1.0":
        return fail("info.version must be 0.1.0")
    if info.get("title") != EXPECTED_TITLE:
        return fail(f"info.title must be {EXPECTED_TITLE!r}")

    protocol = data["x-jarvis-protocol"]
    if not isinstance(protocol, dict):
        return fail("x-jarvis-protocol must be an object")
    if protocol.get("version") != "v0.1":
        return fail("x-jarvis-protocol.version must be v0.1")
    missing_protocol = REQUIRED_PROTOCOL_METADATA - set(protocol)
    if missing_protocol:
        return fail(
            "missing x-jarvis-protocol keys: "
            + ", ".join(sorted(missing_protocol))
        )

    chunk_lock = protocol["chunk_lock"]
    if not isinstance(chunk_lock, dict):
        return fail("x-jarvis-protocol.chunk_lock must be an object")
    if chunk_lock.get("id") != EXPECTED_CHUNK_ID:
        return fail(f"x-jarvis-protocol.chunk_lock.id must be {EXPECTED_CHUNK_ID}")
    declared_locks = set(chunk_lock.get("locks", []))
    missing_locks = REQUIRED_CHUNK_LOCKS - declared_locks
    if missing_locks:
        return fail(
            "x-jarvis-protocol.chunk_lock.locks missing: "
            + ", ".join(sorted(missing_locks))
        )
    declared_excludes = set(chunk_lock.get("excludes", []))
    if "control-plane schemas" in declared_excludes:
        return fail("chunk_lock.excludes must name out-of-scope schemas directly")

    components = data["components"]
    if not isinstance(components, dict):
        return fail("components must be an object")
    missing_components = REQUIRED_COMPONENTS - set(components)
    if missing_components:
        return fail(
            "missing component buckets: " + ", ".join(sorted(missing_components))
        )
    for bucket in REQUIRED_COMPONENTS:
        if not isinstance(components[bucket], dict):
            return fail(f"components.{bucket} must be an object")

    examples = components["examples"]
    missing_examples = set(REQUIRED_EXAMPLES) - set(examples)
    if missing_examples:
        return fail("missing examples: " + ", ".join(sorted(missing_examples)))
    for example_name, required_fields in REQUIRED_EXAMPLES.items():
        example = examples[example_name]
        if not isinstance(example, dict):
            return fail(f"{example_name} must be an object")
        if not example.get("summary"):
            return fail(f"{example_name} must define summary")
        value = example.get("value")
        if not isinstance(value, dict):
            return fail(f"{example_name}.value must be an object")
        missing_example_fields = required_fields - set(value)
        if missing_example_fields:
            return fail(
                f"{example_name}.value missing fields: "
                + ", ".join(sorted(missing_example_fields))
            )
        forbidden_keys = forbidden_example_keys(value)
        if forbidden_keys:
            return fail(
                f"{example_name}.value contains forbidden host-private keys: "
                + ", ".join(forbidden_keys)
            )

    for (example_name, field), expected_value in EXAMPLE_REQUIRED_VALUES.items():
        actual_value = examples[example_name]["value"].get(field)
        if actual_value != expected_value:
            return fail(
                f"{example_name}.value.{field} must be {expected_value!r}"
            )
    for example_name, field in EXAMPLE_REQUIRED_OBJECTS:
        if not isinstance(examples[example_name]["value"].get(field), dict):
            return fail(f"{example_name}.value.{field} must be an object")
    for example_name, field in EXAMPLE_REQUIRED_NON_EMPTY_FIELDS:
        if not examples[example_name]["value"].get(field):
            return fail(f"{example_name}.value.{field} must be non-empty")
    for example_name, field in EXAMPLE_REQUIRED_NON_EMPTY_ARRAYS:
        value = examples[example_name]["value"].get(field)
        if not isinstance(value, list) or not value:
            return fail(f"{example_name}.value.{field} must be a non-empty array")

    schemas = components["schemas"]
    missing_schemas = REQUIRED_SCHEMAS - set(schemas)
    if missing_schemas:
        return fail("missing schemas: " + ", ".join(sorted(missing_schemas)))

    for schema_name, expected_values in REQUIRED_ENUMS.items():
        schema = schemas[schema_name]
        actual_values = set(schema.get("enum", []))
        if actual_values != expected_values:
            return fail(
                f"{schema_name} enum mismatch. expected "
                + ", ".join(sorted(expected_values))
                + "; got "
                + ", ".join(sorted(actual_values))
            )

    for schema_name in REQUIRED_CLOSED_OBJECT_SCHEMAS:
        schema = schemas[schema_name]
        if not isinstance(schema, dict):
            return fail(f"components.schemas.{schema_name} must be an object")
        if schema.get("type") != "object":
            return fail(f"{schema_name} must be an object schema")
        if schema.get("additionalProperties") is not False:
            return fail(f"{schema_name} must set additionalProperties: false")

    extensions_schema = schemas["NamespacedExtensions"]
    if extensions_schema.get("additionalProperties") != PORTABLE_VALUE_REF:
        return fail("NamespacedExtensions additionalProperties must use PortableValue")
    extension_pattern = (
        extensions_schema.get("propertyNames", {}).get("pattern", "")
    )
    if extension_pattern != NAMESPACED_EXTENSION_PATTERN:
        return fail("NamespacedExtensions must use the canonical property pattern")

    portable_value = schemas["PortableValue"]
    object_branch = None
    for branch in portable_value.get("anyOf", []):
        if isinstance(branch, dict) and branch.get("type") == "object":
            object_branch = branch
            break
    if object_branch is None:
        return fail("PortableValue must include a bounded object branch")
    portable_key_pattern = object_branch.get("propertyNames", {}).get("pattern", "")
    if portable_key_pattern != PORTABLE_PROPERTY_PATTERN:
        return fail("PortableValue object keys must use the canonical property pattern")
    if object_branch.get("additionalProperties") != PORTABLE_VALUE_REF:
        return fail("PortableValue object additionalProperties must use PortableValue")

    for schema_name, required_fields in REQUIRED_SCHEMA_FIELDS.items():
        schema = schemas[schema_name]
        declared_required = set(schema.get("required", []))
        missing_fields = required_fields - declared_required
        if missing_fields:
            return fail(
                f"{schema_name} missing required fields: "
                + ", ".join(sorted(missing_fields))
            )

        properties = schema.get("properties")
        if not isinstance(properties, dict):
            return fail(f"{schema_name}.properties must be an object")
        missing_properties = required_fields - set(properties)
        if missing_properties:
            return fail(
                f"{schema_name} missing properties for required fields: "
                + ", ".join(sorted(missing_properties))
            )

        forbidden_properties = FORBIDDEN_SCHEMA_PROPERTIES & set(properties)
        if forbidden_properties:
            return fail(
                f"{schema_name} exposes forbidden properties: "
                + ", ".join(sorted(forbidden_properties))
            )

        forbidden_metadata = set(schema.get("x-jarvis-forbidden-fields", []))
        expected_metadata = REQUIRED_FORBIDDEN_METADATA[schema_name]
        if forbidden_metadata != expected_metadata:
            return fail(
                f"{schema_name} x-jarvis-forbidden-fields mismatch. expected "
                + ", ".join(sorted(expected_metadata))
                + "; got "
                + ", ".join(sorted(forbidden_metadata))
            )

    for schema_name, expected_invariants in REQUIRED_SCHEMA_INVARIANTS.items():
        actual_invariants = set(schemas[schema_name].get("x-jarvis-invariants", []))
        if actual_invariants != expected_invariants:
            return fail(
                f"{schema_name} x-jarvis-invariants mismatch. expected "
                + ", ".join(sorted(expected_invariants))
                + "; got "
                + ", ".join(sorted(actual_invariants))
            )

    for (schema_name, property_name), expected in REQUIRED_IDENTITY_UNIQUE_ARRAYS.items():
        property_schema = schemas[schema_name]["properties"][property_name]
        if property_schema.get("x-jarvis-unique-by") != expected["unique_by"]:
            return fail(
                f"{schema_name}.{property_name} must declare identity uniqueness by "
                + ", ".join(expected["unique_by"])
            )
        if (
            property_schema.get("x-jarvis-duplicate-rejection-id")
            != expected["duplicate_rejection_id"]
        ):
            return fail(
                f"{schema_name}.{property_name} must declare duplicate rejection id "
                + expected["duplicate_rejection_id"]
            )

    for schema_name, optional_fields in OPTIONAL_SCHEMA_FIELDS.items():
        properties = schemas[schema_name].get("properties", {})
        missing_optional = optional_fields - set(properties)
        if missing_optional:
            return fail(
                f"{schema_name} missing locked optional fields: "
                + ", ".join(sorted(missing_optional))
            )

    policy_decision = schemas["PolicyDecision"]
    for result_value in ("deny", "review_required"):
        if not schema_requires_field_when_const(
            policy_decision, "result", result_value, "request_id"
        ):
            return fail(
                "PolicyDecision must require request_id when result is "
                + result_value
            )

    request = schemas["Request"]
    resolved_statuses = {
        "approved",
        "denied",
        "narrowed",
        "answered",
        "needs_revision",
        "takeover",
        "expired",
        "cancelled",
        "superseded",
    }
    review_resolved_statuses = {
        "approved",
        "denied",
        "narrowed",
        "answered",
        "needs_revision",
    }
    closed_statuses = {
        "expired",
        "cancelled",
        "superseded",
    }
    unresolved_statuses = {
        "pending",
        "acknowledged",
    }
    unresolved_forbidden_fields = {
        "resolved_at",
        "resolved_by_review_id",
        "resolved_by_takeover_id",
        "closed_by_event_ref",
        "superseded_by_request_id",
    }
    if not schema_forbids_fields_when_enum(
        request, "status", unresolved_statuses, unresolved_forbidden_fields
    ):
        return fail("Request must forbid resolver refs for unresolved statuses")
    if not schema_requires_field_when_enum(
        request, "status", resolved_statuses, "resolved_at"
    ):
        return fail("Request must require resolved_at for resolved statuses")
    if not schema_requires_field_when_enum(
        request, "status", review_resolved_statuses, "resolved_by_review_id"
    ):
        return fail(
            "Request must require resolved_by_review_id for review-resolved statuses"
        )
    if not schema_requires_field_when_const(
        request, "status", "takeover", "resolved_by_takeover_id"
    ):
        return fail(
            "Request must require resolved_by_takeover_id when status is takeover"
        )
    if not schema_requires_field_when_enum(
        request, "status", closed_statuses, "closed_by_event_ref"
    ):
        return fail("Request must require closed_by_event_ref for closed statuses")
    if not schema_requires_field_when_const(
        request, "status", "superseded", "superseded_by_request_id"
    ):
        return fail(
            "Request must require superseded_by_request_id when status is superseded"
        )

    review = schemas["Review"]
    approval_decisions = {"approve", "narrow"}
    non_approval_decisions = {"deny", "correct", "takeover", "needs_revision"}
    if not schema_requires_field_when_enum(
        review, "decision", approval_decisions, "approval_scope"
    ):
        return fail("Review must require approval_scope for approve and narrow")
    if not schema_forbids_field_when_enum(
        review, "decision", non_approval_decisions, "approval_scope"
    ):
        return fail(
            "Review must forbid approval_scope for non-approval decisions"
        )
    if not schema_requires_field_when_const(
        review, "decision", "takeover", "takeover_id"
    ):
        return fail("Review must require takeover_id when decision is takeover")

    takeover = schemas["Takeover"]
    if not schema_requires_field_when_const(
        takeover, "state", "resumed", "reconciliation_refs"
    ):
        return fail("Takeover must require reconciliation_refs when state is resumed")
    if not schema_requires_field_when_const(
        takeover, "state", "resumed", "resumed_by_actor_id"
    ):
        return fail("Takeover must require resumed_by_actor_id when state is resumed")
    if not schema_requires_field_when_const(
        takeover, "state", "resumed", "resolved_at"
    ):
        return fail("Takeover must require resolved_at when state is resumed")
    active_takeover_states = {"requested", "locked", "human_active"}
    active_takeover_forbidden_fields = {
        "resumed_by_actor_id",
        "reconciliation_refs",
        "resolved_at",
    }
    if not schema_forbids_fields_when_enum(
        takeover, "state", active_takeover_states, active_takeover_forbidden_fields
    ):
        return fail("Takeover must forbid resume refs before reconciliation states")

    contribution = schemas["Contribution"]
    if contribution["properties"]["contributor_refs"].get("minItems") != 1:
        return fail("Contribution.contributor_refs must require at least one item")
    if contribution["properties"]["contributor_refs"].get("uniqueItems") is not True:
        return fail("Contribution.contributor_refs must be unique")
    if contribution["properties"]["event_refs"].get("minItems") != 1:
        return fail("Contribution.event_refs must require at least one event")
    if not schema_requires_min_items_when_const(
        contribution, "contributor_type", "shared", "contributor_refs", 2
    ):
        return fail("Contribution must require multiple refs for shared contribution")

    evidence_item_ref = schemas["EvidenceItemRef"]
    source_event_refs = evidence_item_ref["properties"]["source_event_refs"]
    if source_event_refs.get("minItems") != 1:
        return fail("EvidenceItemRef.source_event_refs must require at least one event")

    evidence_manifest = schemas["EvidenceManifest"]
    if evidence_manifest["properties"]["evidence_item_refs"].get("minItems") != 1:
        return fail("EvidenceManifest.evidence_item_refs must require at least one item")
    if evidence_manifest["properties"]["contribution_refs"].get("minItems") != 1:
        return fail("EvidenceManifest.contribution_refs must require at least one item")

    learning_record = schemas["LearningRecord"]
    if learning_record["properties"]["source_event_refs"].get("minItems") != 1:
        return fail("LearningRecord.source_event_refs must require at least one event")

    memory_proposal = schemas["MemoryProposal"]
    if not schema_requires_field_when_const(
        memory_proposal, "status", "accepted", "review_refs"
    ):
        return fail("MemoryProposal must require review_refs when accepted")
    if memory_proposal["properties"]["review_refs"].get("minItems") != 1:
        return fail("MemoryProposal.review_refs must require at least one item")
    if memory_proposal["properties"]["review_required"].get("const") is not True:
        return fail("MemoryProposal.review_required must be true")

    skill_proposal = schemas["SkillProposal"]
    if not schema_requires_field_when_const(
        skill_proposal, "status", "accepted", "review_refs"
    ):
        return fail("SkillProposal must require review_refs when accepted")
    if skill_proposal["properties"]["review_refs"].get("minItems") != 1:
        return fail("SkillProposal.review_refs must require at least one item")

    outcome_report = schemas["OutcomeReport"]
    if outcome_report["properties"]["learning_record_refs"].get("minItems") != 1:
        return fail("OutcomeReport.learning_record_refs must require at least one item")

    event_payload_properties = schemas["JarvisEventPayload"].get("properties", {})
    if "extensions" in event_payload_properties:
        return fail("JarvisEventPayload must not expose extensions")

    broken_refs = [
        f"{path} -> {ref}"
        for path, ref in iter_refs(data)
        if not local_ref_exists(data, ref)
    ]
    if broken_refs:
        return fail("unresolved local refs: " + "; ".join(broken_refs))

    preferences = schemas["HumanWorker"]["properties"]["preferences"]
    if preferences.get("additionalProperties") != PORTABLE_VALUE_REF:
        return fail("HumanWorker.preferences additionalProperties must use PortableValue")
    preference_pattern = preferences.get("propertyNames", {}).get("pattern", "")
    if preference_pattern != PORTABLE_PROPERTY_PATTERN:
        return fail("HumanWorker.preferences must use the canonical property pattern")

    security_schemes = components["securitySchemes"]
    if set(security_schemes) != {"HostAuth"}:
        return fail("components.securitySchemes must contain only HostAuth")
    host_auth = security_schemes.get("HostAuth")
    if not isinstance(host_auth, dict):
        return fail("components.securitySchemes.HostAuth is required")
    if host_auth.get("type") != "apiKey" or host_auth.get("in") != "header":
        return fail("HostAuth must be a host-owned header security binding")
    if host_auth.get("name") != "Authorization":
        return fail("HostAuth must use the Authorization header")

    security = data.get("security")
    if security == []:
        return fail("root security must not be an empty no-auth array")
    if security != [{"HostAuth": []}]:
        return fail("root security must require HostAuth")

    tags = data["tags"]
    if not isinstance(tags, list):
        return fail("tags must be a list")
    tag_names = {tag.get("name") for tag in tags if isinstance(tag, dict)}
    missing_tags = REQUIRED_TAGS - tag_names
    if missing_tags:
        return fail(f"missing tags: {', '.join(sorted(missing_tags))}")

    if not isinstance(data["paths"], dict):
        return fail("paths must be an object")

    parameters = components["parameters"]
    missing_parameters = REQUIRED_PARAMETERS - set(parameters)
    if missing_parameters:
        return fail(
            "missing parameters: " + ", ".join(sorted(missing_parameters))
        )
    for name, header_name in HEADER_PARAMETER_NAMES.items():
        parameter = parameters[name]
        if parameter.get("in") != "header":
            return fail(f"{name} must be a header parameter")
        if parameter.get("name") != header_name:
            return fail(f"{name} must use header name {header_name}")
        if parameter.get("required") is not True:
            return fail(f"{name} must be required")
    for name, header_name in OPTIONAL_HEADER_PARAMETER_NAMES.items():
        parameter = parameters[name]
        if parameter.get("in") != "header":
            return fail(f"{name} must be a header parameter")
        if parameter.get("name") != header_name:
            return fail(f"{name} must use header name {header_name}")
        if parameter.get("required") is not False:
            return fail(f"{name} must be optional")
    for name in ("WorkerIdPath", "ActorIdPath", "WorkSessionIdPath"):
        parameter = parameters[name]
        if parameter.get("in") != "path":
            return fail(f"{name} must be a path parameter")
        if parameter.get("required") is not True:
            return fail(f"{name} must be required")

    request_bodies = components["requestBodies"]
    missing_request_bodies = set(REQUIRED_REQUEST_BODIES) - set(request_bodies)
    if missing_request_bodies:
        return fail(
            "missing requestBodies: " + ", ".join(sorted(missing_request_bodies))
        )
    for body_name, schema_name in REQUIRED_REQUEST_BODIES.items():
        body = request_bodies[body_name]
        if body.get("required") is not True:
            return fail(f"{body_name} must be required")
        expected_ref = component_ref("schemas", schema_name)
        if media_schema_ref(body) != expected_ref:
            return fail(f"{body_name} must reference {expected_ref}")

    responses = components["responses"]
    missing_responses = set(REQUIRED_RESPONSES) - set(responses)
    if missing_responses:
        return fail("missing responses: " + ", ".join(sorted(missing_responses)))
    for response_name, schema_name in REQUIRED_RESPONSES.items():
        response = responses[response_name]
        expected_ref = component_ref("schemas", schema_name)
        if media_schema_ref(response) != expected_ref:
            return fail(f"{response_name} must reference {expected_ref}")

    error_ids = set(schemas["ProtocolErrorId"].get("enum", []))
    required_security_error_ids = {
        "missing_protocol_version",
        "unsupported_protocol_version",
        "missing_actor",
        "missing_idempotency_key",
        "missing_request_timestamp",
        "stale_request_timestamp",
        "missing_expected_work_session_revision",
        "stale_work_session_revision",
        "missing_previous_event_hash",
        "invalid_previous_event_hash",
        "invalid_event_hash",
        "duplicate_idempotency_key_mismatch",
        "unauthorized_actor",
    }
    missing_security_error_ids = required_security_error_ids - error_ids
    if missing_security_error_ids:
        return fail(
            "ProtocolErrorId missing security errors: "
            + ", ".join(sorted(missing_security_error_ids))
        )

    protocol_error_example_id = examples["ProtocolErrorExample"]["value"].get(
        "error_id"
    )
    if protocol_error_example_id not in error_ids:
        return fail("ProtocolErrorExample.error_id must exist in ProtocolErrorId")

    for conformance_path in (GOLDEN_PATH_CONFORMANCE, FAILURE_MODE_CONFORMANCE):
        if not conformance_path.exists():
            return fail(f"missing {conformance_path.relative_to(ROOT)}")
    golden_text = GOLDEN_PATH_CONFORMANCE.read_text(encoding="utf-8")
    required_golden_phrases = {
        "Every WorkSession-scoped mutation validates Jarvis-Protocol-Version.",
        "Every WorkSession-scoped mutation validates Jarvis-Actor-Id.",
        "Every WorkSession-scoped mutation validates Jarvis-Idempotency-Key.",
        "Every WorkSession-scoped mutation validates Jarvis-Request-Timestamp.",
        "Every WorkSession-scoped mutation validates Jarvis-Expected-WorkSession-Revision.",
        "Every WorkSession-scoped mutation validates Jarvis-Previous-Event-Hash.",
        "Every accepted WorkSession-scoped state change verifies Actor authority.",
        "AgentWorker action records PolicyDecision before accepted protocol state.",
        "Request resolves only through Review or Takeover.",
        "Review approve or narrow produces bounded ApprovalScope.",
        "EvidenceManifest exports portable proof.",
    }
    missing_golden_phrases = [
        phrase for phrase in sorted(required_golden_phrases) if phrase not in golden_text
    ]
    if missing_golden_phrases:
        return fail(
            "golden-path conformance missing phrases: "
            + "; ".join(missing_golden_phrases)
        )
    failure_text = FAILURE_MODE_CONFORMANCE.read_text(encoding="utf-8")
    missing_conformance_ids = [
        rejection_id
        for rejection_id in sorted(REQUIRED_CONFORMANCE_REJECTION_IDS)
        if rejection_id not in failure_text
    ]
    if missing_conformance_ids:
        return fail(
            "failure-mode conformance missing rejection ids: "
            + ", ".join(missing_conformance_ids)
        )
    unknown_conformance_ids = REQUIRED_CONFORMANCE_REJECTION_IDS - error_ids
    if unknown_conformance_ids:
        return fail(
            "failure-mode conformance ids missing from ProtocolErrorId: "
            + ", ".join(sorted(unknown_conformance_ids))
        )

    paths = data["paths"]
    for (method, path), expected in REQUIRED_OPERATIONS.items():
        path_item = paths.get(path)
        if not isinstance(path_item, dict):
            return fail(f"missing path {path}")
        operation = path_item.get(method)
        if not isinstance(operation, dict):
            return fail(f"missing operation {method.upper()} {path}")
        if operation.get("operationId") != expected["operation_id"]:
            return fail(
                f"{method.upper()} {path} operationId must be "
                + expected["operation_id"]
            )
        if not operation.get("summary"):
            return fail(f"{method.upper()} {path} must define summary")
        description = operation.get("description")
        if not isinstance(description, str) or not description.strip():
            return fail(f"{method.upper()} {path} must define description")
        normalized_description = " ".join(description.split())
        if "Compatible implementations MUST verify" not in normalized_description:
            return fail(
                f"{method.upper()} {path} description must define verification duty"
            )
        if operation.get("x-jarvis-operation-class") != expected["operation_class"]:
            return fail(
                f"{method.upper()} {path} x-jarvis-operation-class must be "
                + expected["operation_class"]
            )
        if expected["operation_class"] in {
            "worksession_scoped_read",
            "export_read",
        }:
            if "Actor read authority" not in normalized_description:
                return fail(
                    f"{method.upper()} {path} description must require Actor read authority"
                )
            if "MUST NOT require mutation-only" not in normalized_description:
                return fail(
                    f"{method.upper()} {path} description must exclude mutation-only headers"
                )
        if expected["operation_class"] == "non_worksession_mutation":
            if (
                "does not require WorkSession revision or previous event hash"
                not in normalized_description
            ):
                return fail(
                    f"{method.upper()} {path} description must exclude WorkSession revision and previous hash"
                )
        if expected["operation_class"] == "worksession_genesis_mutation":
            if "expected revision `0`" not in normalized_description:
                return fail(
                    f"{method.upper()} {path} description must require genesis revision"
                )
            if "`hash:protocol-genesis`" not in normalized_description:
                return fail(
                    f"{method.upper()} {path} description must require protocol genesis hash"
                )
        if operation.get("tags") != [expected["tag"]]:
            return fail(f"{method.upper()} {path} tag must be {expected['tag']}")
        if operation.get("security") != [{"HostAuth": []}]:
            return fail(f"{method.upper()} {path} must require HostAuth")
        actual_parameters = operation_parameter_names(operation)
        expected_parameters = expected["headers"] | expected["path_parameters"]
        if actual_parameters != expected_parameters:
            return fail(
                f"{method.upper()} {path} parameters mismatch. expected "
                + ", ".join(sorted(expected_parameters))
                + "; got "
                + ", ".join(sorted(actual_parameters))
            )
        request_body = expected["request_body"]
        if request_body is None:
            if "requestBody" in operation:
                return fail(f"{method.upper()} {path} must not define requestBody")
        else:
            expected_ref = component_ref("requestBodies", request_body)
            actual_ref = operation.get("requestBody", {}).get("$ref")
            if actual_ref != expected_ref:
                return fail(f"{method.upper()} {path} requestBody must be {expected_ref}")
        responses = operation.get("responses", {})
        success_status = expected["success_status"]
        expected_success_ref = component_ref("responses", expected["success_response"])
        actual_success_ref = responses.get(success_status, {}).get("$ref")
        if actual_success_ref != expected_success_ref:
            return fail(
                f"{method.upper()} {path} {success_status} response must be "
                + expected_success_ref
            )
        if responses.get("400", {}).get("$ref") != component_ref(
            "responses", "ProtocolErrorResponse"
        ):
            return fail(f"{method.upper()} {path} must define ProtocolErrorResponse")

    servers = data.get("servers")
    if not servers:
        return fail("servers must state the host-owned server boundary")
    if not isinstance(servers, list) or not isinstance(servers[0], dict):
        return fail("servers must be a list of server objects")
    if servers[0].get("url") != EXPECTED_PLACEHOLDER_SERVER:
        return fail("server URL must be the Jarvis placeholder URL")
    description = servers[0].get("description", "")
    if "Jarvis does not operate this server" not in description:
        return fail("server description must state that Jarvis does not operate it")

    print("openapi contract ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
