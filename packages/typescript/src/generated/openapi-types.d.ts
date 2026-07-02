/* Generated from docs/openapi/jarvis-openapi.yaml. Do not edit by hand. */

export type JarvisId = string;

export type OpaqueRef = string;

export type Timestamp = string;

export type NamespacedExtensions = Record<string, PortableValue>;

export type PortableValue = null | boolean | number | string | PortableValue[] | { [key: string]: PortableValue };

export type WorkerType = "human" | "agent" | "service" | "tool";

export type ActorType = "human" | "agent" | "service" | "tool";

export type ContributionRole = "human" | "agent" | "shared" | "service" | "tool";

export type AutonomyLevel = "observe_only" | "propose_only" | "execute_with_review" | "bounded_execute" | "full_execute_in_scope";

export type WorkSessionStatus = "active" | "waiting_on_human" | "takeover" | "reconciling" | "completed" | "failed" | "cancelled" | "closed";

export type PolicyDecisionResult = "allow" | "deny" | "narrow" | "review_required";

export type RiskClass = "low" | "medium" | "high" | "critical";

export type DataSensitivity = "public" | "private" | "confidential" | "restricted";

export type RequestType = "permission" | "context" | "judgment" | "review" | "correction" | "takeover" | "escalation";

export type RequestStatus = "pending" | "acknowledged" | "approved" | "denied" | "narrowed" | "answered" | "needs_revision" | "takeover" | "expired" | "cancelled" | "superseded";

export type BlockingScope = "action" | "branch" | "artifact" | "tool_call" | "external_send" | "final_submission" | "work_session";

export type ReviewDecision = "answer" | "approve" | "deny" | "narrow" | "correct" | "takeover" | "needs_revision";

export type TakeoverState = "requested" | "locked" | "human_active" | "reconciliation_required" | "resumed" | "closed";

export type ContributorType = "human" | "agent" | "service" | "tool" | "shared";

export type ContributionType = "intent" | "instruction" | "plan" | "research" | "execution" | "artifact" | "review" | "correction" | "decision" | "evidence_capture" | "memory_proposal" | "skill_proposal" | "submission";

export type LearningSubjectType = "human" | "agent" | "pair";

export type LearningReviewState = "proposed" | "accepted" | "rejected" | "superseded";

export type ProposalTargetType = "human" | "agent" | "pair" | "project" | "task";

export type MemoryProposalStatus = "proposed" | "pending_review" | "accepted" | "rejected" | "superseded" | "expired";

export type SkillProposalStatus = "proposed" | "pending_review" | "accepted" | "rejected" | "superseded" | "archived";

export type ProtocolErrorId = "invalid_transition" | "unknown_state" | "missing_protocol_version" | "unsupported_protocol_version" | "missing_request_timestamp" | "stale_request_timestamp" | "missing_expected_work_session_revision" | "missing_previous_event_hash" | "stale_work_session_revision" | "missing_idempotency_key" | "missing_actor" | "path_body_id_mismatch" | "actor_body_id_mismatch" | "invalid_extension_namespace" | "extension_core_field_override" | "missing_policy" | "missing_policy_decision" | "missing_objective" | "policy_denied" | "request_unresolved" | "review_required" | "invalid_request_transition" | "missing_review_resolution" | "missing_takeover_resolution" | "missing_superseding_request" | "invalid_approval_scope" | "approval_scope_expired" | "approval_scope_mismatch" | "stale_takeover_epoch" | "invalid_event_hash" | "invalid_previous_event_hash" | "duplicate_idempotency_key_mismatch" | "request_livelock" | "duplicate_request_mismatch" | "missing_jarvis_event" | "missing_blocked_scope_resolution_refs" | "missing_reconciliation_refs" | "mutation_after_closed" | "unauthorized_actor" | "invalid_export" | "invalid_export_state" | "invalid_evidence_export_state" | "missing_contribution_actor" | "invalid_contributor_refs" | "shared_contribution_without_individual_refs" | "duplicate_contributor_ref" | "evidence_after_the_fact" | "missing_evidence_event_refs" | "duplicate_evidence_item_ref" | "forbidden_export_field" | "silent_memory_mutation" | "silent_skill_activation" | "model_self_confirmed_memory" | "tool_self_confirmed_memory" | "skill_expands_tool_access_without_policy_review" | "sealed_work_session_mutation" | "sealed_evidence_mutation" | "outcome_report_without_learning_record" | "outcome_report_requires_terminal_source" | "unsupported_capability" | "forbidden_host_private_field";

export interface AuthorityScope {
  grants: Array<string>;
}

export interface AccountabilityScope {
  accountable_for: Array<string>;
}

export interface CapabilityRef {
  capability_type?: string;
  ref: OpaqueRef;
  required?: boolean;
}

export interface EventAuthority {
  allowed_event_types?: Array<string>;
  can_append_events: boolean;
}

export interface ContributionScope {
  contribution_roles: Array<ContributionRole>;
}

export interface CanonicalizationProfile {
  hash_method: "sha256";
  profile_ref?: OpaqueRef;
  serialization: "json-c14n";
}

export interface ProtocolTraceContext {
  correlation_ref?: OpaqueRef;
  parent_event_id?: JarvisId;
  trace_id?: OpaqueRef;
}

export interface JarvisEventPayload {
  action: string;
  evidence_refs?: Array<OpaqueRef>;
  field_refs?: Array<OpaqueRef>;
  object_id?: JarvisId;
  object_type: "worker" | "actor" | "human_worker" | "agent_worker" | "work_session" | "jarvis_event" | "policy" | "policy_decision" | "request" | "review" | "takeover" | "contribution" | "evidence_manifest" | "learning_record" | "memory_proposal" | "skill_proposal" | "outcome_report" | "protocol_error" | "conformance_result";
  summary?: string;
}

export interface PolicyConstraint {
  kind: string;
  max_count?: number;
  reason?: string;
  scope_ref?: OpaqueRef;
  unit?: string;
  value_ref?: OpaqueRef;
}

export interface EscalationRule {
  reason?: string;
  required_action: "create_request" | "require_review" | "start_takeover" | "deny_action";
  reviewer_ref?: OpaqueRef;
  risk_class?: RiskClass;
  trigger: string;
}

export interface PolicyActionRule {
  action: string;
  constraints?: Array<PolicyConstraint>;
  grant_refs?: Array<OpaqueRef>;
  scope_ref?: OpaqueRef;
}

export interface PolicyRequestLimits {
  default_expiry_seconds?: number;
  max_pending_requests?: number;
  max_repeated_denials?: number;
}

export interface PolicyActionRequest {
  action: string;
  input_refs?: Array<OpaqueRef>;
  parameter_refs?: Array<OpaqueRef>;
  scope_ref?: OpaqueRef;
  target_ref?: OpaqueRef;
}

export interface RequestOption {
  effect: string;
  id: JarvisId;
  label: string;
  risk_class?: RiskClass;
  scope_ref?: OpaqueRef;
}

export interface SafeFallback {
  action: "continue_unrelated_safe_work" | "continue_with_limited_evidence" | "cancel_blocked_scope" | "keep_blocked_scope_stopped";
  limitation_ref?: OpaqueRef;
  reason: string;
}

export interface ApprovalBoundary {
  constraint_refs?: Array<OpaqueRef>;
  grant_refs?: Array<OpaqueRef>;
  scope_ref: OpaqueRef;
}

export interface TakeoverScope {
  artifact_refs?: Array<OpaqueRef>;
  blocking_scope: BlockingScope;
  normalized_action_hash?: string;
  scope_ref: OpaqueRef;
}

export interface ApprovalScope {
  allowed_scope: ApprovalBoundary;
  applies_to_actor_id: JarvisId;
  applies_to_work_session_id: JarvisId;
  approved_action: PolicyActionRequest;
  denied_scope: ApprovalBoundary;
  expires_at: Timestamp;
  max_uses: number;
  normalized_action_hash: string;
  policy_decision_id: JarvisId;
  request_event_hash: string;
  request_id: JarvisId;
  request_revision: number;
  review_id: JarvisId;
}

export interface ContributorRef {
  actor_id: JarvisId;
  contribution_role: ContributionRole;
  worker_id: JarvisId;
}

export interface ExportProfile {
  profile: string;
  redaction_profile_ref?: OpaqueRef;
  version?: string;
}

export interface EvidenceItemRef {
  artifact_ref: OpaqueRef;
  captured_at: Timestamp;
  captured_by_actor_id: JarvisId;
  content_hash: string;
  evidence_type: string;
  id: JarvisId;
  limitation_refs: Array<OpaqueRef>;
  redaction_state: string;
  source_event_refs: Array<JarvisId>;
  trust_label: string;
  work_session_id: JarvisId;
}

export interface Worker {
  accountability_scope: AccountabilityScope;
  authority_scope: AuthorityScope;
  capabilities?: Array<CapabilityRef>;
  display_name?: string;
  extensions?: NamespacedExtensions;
  id: JarvisId;
  role: string;
  type: WorkerType;
}

export interface Actor {
  contribution_scope: ContributionScope;
  created_at: Timestamp;
  event_authority: EventAuthority;
  extensions?: NamespacedExtensions;
  id: JarvisId;
  type: ActorType;
  valid_from?: Timestamp;
  valid_until?: Timestamp;
  worker_id: JarvisId;
}

export interface HumanWorker {
  actor_id: JarvisId;
  boundaries?: Array<string>;
  domain_context_refs?: Array<OpaqueRef>;
  known_patterns?: Array<string>;
  policy_authority: AuthorityScope;
  preferences?: Record<string, PortableValue>;
  profile_ref?: OpaqueRef;
  review_authority: AuthorityScope;
  role: string;
  worker_id: JarvisId;
}

export interface AgentWorker {
  actor_id: JarvisId;
  agent_ref: OpaqueRef;
  autonomy_level: AutonomyLevel;
  capability_refs: Array<CapabilityRef>;
  extensions?: NamespacedExtensions;
  memory_access_profile?: OpaqueRef;
  operating_constraints: Array<string>;
  role: string;
  tool_access_profile?: OpaqueRef;
  worker_id: JarvisId;
}

export interface WorkSession {
  agent_worker_id: JarvisId;
  context_manifest_ref?: OpaqueRef;
  contribution_ledger_ref?: OpaqueRef;
  created_at: Timestamp;
  created_by_actor_id: JarvisId;
  event_log_ref: OpaqueRef;
  evidence_manifest_ref?: OpaqueRef;
  human_worker_id: JarvisId;
  id: JarvisId;
  last_event_hash: string;
  learning_record_refs?: Array<JarvisId>;
  objective: string;
  policy_id: JarvisId;
  protocol_version: "v0.1";
  revision: number;
  source_ref?: OpaqueRef;
  status: WorkSessionStatus;
  updated_at: Timestamp;
}

export interface JarvisEvent {
  actor_id: JarvisId;
  actor_signature?: string;
  canonicalization: CanonicalizationProfile;
  event_hash: string;
  id: JarvisId;
  payload: JarvisEventPayload;
  previous_hash: string;
  sequence: number;
  signing_key_ref?: OpaqueRef;
  timestamp: Timestamp;
  trace_context?: ProtocolTraceContext;
  type: string;
  work_session_id: JarvisId;
}

export interface Policy {
  allowed_actions: Array<PolicyActionRule>;
  autonomy_level: AutonomyLevel;
  created_at: Timestamp;
  created_by_actor_id: JarvisId;
  denied_actions: Array<PolicyActionRule>;
  escalation_rules: Array<EscalationRule>;
  extensions?: NamespacedExtensions;
  external_send_rules?: Array<PolicyActionRule>;
  id: JarvisId;
  memory_grants?: Array<OpaqueRef>;
  owner_worker_id: JarvisId;
  request_limits?: PolicyRequestLimits;
  review_required_actions: Array<PolicyActionRule>;
  risk_classes: Array<RiskClass>;
  tool_grants?: Array<OpaqueRef>;
}

export interface PolicyDecision {
  actor_id: JarvisId;
  created_at: Timestamp;
  data_sensitivity?: DataSensitivity;
  denied_grant_refs?: Array<OpaqueRef>;
  evidence_refs?: Array<OpaqueRef>;
  id: JarvisId;
  normalized_action_hash: string;
  policy_id: JarvisId;
  reason: string;
  request_id?: JarvisId;
  requested_action: PolicyActionRequest;
  result: PolicyDecisionResult;
  risk_class: RiskClass;
  selected_grant_refs?: Array<OpaqueRef>;
  work_session_id: JarvisId;
}

export interface Request {
  artifact_refs?: Array<OpaqueRef>;
  blocking_scope: BlockingScope;
  closed_by_event_ref?: OpaqueRef;
  contribution_refs?: Array<JarvisId>;
  created_at: Timestamp;
  data_sensitivity?: DataSensitivity;
  default_if_no_response: SafeFallback;
  duplicate_of_request_id?: JarvisId;
  evidence_refs?: Array<OpaqueRef>;
  expires_at: Timestamp;
  human_decision_needed: string;
  id: JarvisId;
  missing_permission_or_context?: string;
  options: Array<RequestOption>;
  policy_decision_id: JarvisId;
  policy_refs?: Array<OpaqueRef>;
  protocol_version: "v0.1";
  reason_code: string;
  reason_summary: string;
  recommended_option?: JarvisId;
  requested_action: PolicyActionRequest;
  requested_outcome: string;
  requester_actor_id: JarvisId;
  requester_worker_id: JarvisId;
  resolved_at?: Timestamp;
  resolved_by_review_id?: JarvisId;
  resolved_by_takeover_id?: JarvisId;
  risk_class: RiskClass;
  safer_alternatives?: Array<RequestOption>;
  status: RequestStatus;
  superseded_by_request_id?: JarvisId;
  target_human_worker_id: JarvisId;
  type: RequestType;
  work_session_id: JarvisId;
}

export interface Review {
  approval_scope?: ApprovalScope;
  comments?: string;
  created_at: Timestamp;
  decision: ReviewDecision;
  id: JarvisId;
  required_changes?: Array<string>;
  reviewer_actor_id: JarvisId;
  reviewer_worker_id: JarvisId;
  takeover_id?: JarvisId;
  target_ref: OpaqueRef;
  work_session_id: JarvisId;
}

export interface Takeover {
  affected_scope: TakeoverScope;
  controlling_actor_id: JarvisId;
  created_at: Timestamp;
  id: JarvisId;
  lock_epoch: number;
  reason: string;
  reconciliation_notes?: string;
  reconciliation_refs?: Array<OpaqueRef>;
  request_id?: JarvisId;
  requested_by_actor_id: JarvisId;
  resolved_at?: Timestamp;
  resumed_by_actor_id?: JarvisId;
  state: TakeoverState;
  work_session_id: JarvisId;
}

export interface Contribution {
  artifact_refs?: Array<OpaqueRef>;
  confidence?: number;
  contribution_type: ContributionType;
  contributor_refs: Array<ContributorRef>;
  contributor_type: ContributorType;
  created_at: Timestamp;
  event_refs: Array<JarvisId>;
  evidence_refs?: Array<JarvisId>;
  id: JarvisId;
  limitations?: Array<OpaqueRef>;
  review_refs?: Array<JarvisId>;
  work_session_id: JarvisId;
}

export interface EvidenceManifest {
  artifact_refs?: Array<OpaqueRef>;
  contribution_refs: Array<JarvisId>;
  event_chain_root: string;
  evidence_item_refs: Array<EvidenceItemRef>;
  export_profile: ExportProfile;
  generated_at: Timestamp;
  generated_by_actor_id: JarvisId;
  id: JarvisId;
  limitation_refs?: Array<OpaqueRef>;
  objective: string;
  policy_decision_refs: Array<JarvisId>;
  redaction_refs?: Array<OpaqueRef>;
  request_refs: Array<JarvisId>;
  review_refs: Array<JarvisId>;
  takeover_refs: Array<JarvisId>;
  work_session_id: JarvisId;
}

export interface LearningRecord {
  created_at: Timestamp;
  created_by_actor_id: JarvisId;
  id: JarvisId;
  lesson_type: string;
  memory_proposal_refs?: Array<JarvisId>;
  outcome_report_refs?: Array<JarvisId>;
  proposed_change?: PortableValue;
  review_state: LearningReviewState;
  scope: OpaqueRef;
  skill_proposal_refs?: Array<JarvisId>;
  source_event_refs: Array<JarvisId>;
  subject_ref: OpaqueRef;
  subject_type: LearningSubjectType;
  work_session_id: JarvisId;
}

export interface MemoryProposal {
  confidence: number;
  content: PortableValue;
  created_at: Timestamp;
  expires_at?: Timestamp;
  id: JarvisId;
  learning_record_refs?: Array<JarvisId>;
  memory_scope: OpaqueRef;
  memory_type: string;
  proposed_by_actor_id: JarvisId;
  proposed_for: ProposalTargetType;
  provenance: Array<OpaqueRef>;
  review_refs?: Array<JarvisId>;
  review_required: true;
  source_event_refs?: Array<JarvisId>;
  status: MemoryProposalStatus;
  work_session_id: JarvisId;
}

export interface SkillProposal {
  created_at: Timestamp;
  failure_cases: Array<string>;
  id: JarvisId;
  learning_record_refs?: Array<JarvisId>;
  procedure: Array<string>;
  proposed_by_actor_id: JarvisId;
  proposed_for: ProposalTargetType;
  provenance: Array<OpaqueRef>;
  required_tools?: Array<OpaqueRef>;
  review_checks: Array<string>;
  review_refs?: Array<JarvisId>;
  skill_name: string;
  skill_scope: OpaqueRef;
  source_event_refs?: Array<JarvisId>;
  status: SkillProposalStatus;
  trigger_conditions: Array<string>;
  work_session_id: JarvisId;
}

export interface OutcomeReport {
  accepted_by_actor_id: JarvisId;
  external_system_ref?: OpaqueRef;
  id: JarvisId;
  learning_record_refs: Array<JarvisId>;
  outcome: string;
  reason?: string;
  received_at: Timestamp;
  reporter_actor_id?: JarvisId;
  reporter_ref: OpaqueRef;
  reviewer_feedback_refs?: Array<OpaqueRef>;
  source_ref: OpaqueRef;
  work_session_id: JarvisId;
}

export interface ProtocolError {
  error_id: ProtocolErrorId;
  field: string;
  object_type: string;
  protocol_version: string;
  reason: string;
  remediation: string;
  trace_id: OpaqueRef;
}
