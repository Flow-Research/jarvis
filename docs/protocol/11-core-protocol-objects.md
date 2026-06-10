# Core Protocol Objects

This document is the source of truth for Jarvis v0.1 core protocol objects.

Jarvis defines the compatibility contracts for human-agent collaboration and
the learning loop. A compatible product, host, CLI, agent system, or external
service uses any infrastructure, but it preserves these object meanings and
state transitions.

## Normative Language

The words `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are used as
protocol requirements.

- `MUST` means a compatible implementation is required to do it.
- `MUST NOT` means a compatible implementation is required not to do it.
- `SHOULD` means the behavior is expected unless a documented compatibility
  reason exists.
- `MAY` means the behavior is optional.

## Object Model

Jarvis models a working relationship:

```txt
HumanWorker + AgentWorker
  -> WorkSession
  -> Policy
  -> Request
  -> Review
  -> Contribution
  -> EvidenceManifest
  -> LearningRecord
  -> MemoryProposal / SkillProposal
```

The protocol does not start from chat. It starts from collaboration between two
workers inside a durable WorkSession.

## Core Invariants

1. Every WorkSession has one primary HumanWorker, one primary AgentWorker, one
   objective, and one active Policy.
2. HumanWorker and AgentWorker MUST both be workers and actors.
3. Every meaningful protocol event MUST be attributable to an Actor.
4. The AgentWorker MUST act autonomously only inside Policy.
5. Action outside Policy MUST create a Request.
6. Human resolution of a Request MUST use Review or Takeover. Expiry,
   cancellation, and supersession close a Request without granting authority.
7. A Review MUST record human judgment over a protocol target.
8. Takeover MUST create a lock epoch and block stale autonomous continuation.
9. Contribution MUST record who did what.
10. EvidenceManifest MUST record portable proof while the WorkSession happens.
11. LearningRecord MUST record what the human, agent, or pair learned.
12. Durable memory and skill changes MUST remain proposals until governed review
    accepts them.

## Core Field Lock

The v0.1 field lock defines the portable protocol fields that Week 2 OpenAPI
components must encode.

Field classes:

```txt
required
optional
extension
forbidden
```

Required fields carry protocol meaning and must appear in compatible records.
Optional fields add protocol-visible context without changing required
semantics. Extension fields must be namespaced. Forbidden fields belong to
hosts, products, identity systems, runtimes, databases, cloud platforms, billing
systems, or private execution stacks.

### Field Class Rules

- Required fields MUST be portable across hosts.
- Required fields MUST NOT depend on product-private infrastructure.
- Optional fields MUST NOT change the meaning of required fields.
- Extension fields MUST be namespaced.
- Extension fields MUST NOT override core field names.
- Portable exports MUST exclude forbidden fields.
- Host-private ids MUST stay outside portable protocol fields. Portable records
  use `source_ref`, `external_system_ref`, evidence refs, or artifact refs as
  opaque references without exposing database ids, runtime ids, deployment ids,
  credentials, billing internals, or product-private state.

### Stable Reference Rules

- `id` identifies the protocol record.
- `worker_id` references a Worker.
- `actor_id` references an Actor.
- `work_session_id` references a WorkSession.
- `policy_id` references a Policy.
- `request_id` references a Request.
- `review_refs`, `event_refs`, `evidence_refs`, `artifact_refs`, and
  `source_event_refs` contain protocol references or opaque external refs.
- `contributor_refs` contains one or more ContributorRef objects:
  `{worker_id, actor_id, contribution_role}`.
- `reporter_ref` identifies an external reporter or protocol reporter without
  requiring Jarvis to own the external system.
- `accepted_by_actor_id` references the Actor that accepted an extension report
  into Jarvis records.
- Opaque external refs MUST NOT require Jarvis to understand the external
  system.
- `extensions` is the only generic extension container.
- Every key in `extensions` MUST be namespaced.
- `extensions` MUST NOT contain credentials, secrets, database ids,
  runtime state, deployment details, billing data, private scores, or product
  UI state.

### Worker Field Lock

Required fields:

```txt
id
type
role
authority_scope
accountability_scope
```

Required field reason: Worker records identify who or what participates in
protocol-visible work, what role the participant plays, what authority it has,
and where accountability attaches.

Optional fields:

```txt
display_name
capabilities
extensions
```

Forbidden fields:

```txt
password
credential
raw_auth_token
billing_account
provider_secret
database_primary_key
deployment_resource_id
```

### Actor Field Lock

Required fields:

```txt
id
worker_id
type
event_authority
contribution_scope
created_at
```

Required field reason: Actor records bind protocol events and contributions to
an authorized acting identity without collapsing human, agent, service, and
tool actions.

Optional fields:

```txt
extensions
valid_from
valid_until
```

Forbidden fields:

```txt
credential
raw_auth_token
session_cookie
private_key
database_primary_key
```

### HumanWorker Field Lock

Required fields:

```txt
worker_id
actor_id
role
policy_authority
review_authority
```

Required field reason: HumanWorker records identify the accountable human,
their acting identity, and the authority used for policy, review, correction,
and takeover decisions.

Optional fields:

```txt
profile_ref
domain_context_refs
preferences
boundaries
known_patterns
```

Forbidden fields:

```txt
password
credential
raw_auth_token
private_profile_data
billing_account
product_account_record
```

### AgentWorker Field Lock

Required fields:

```txt
worker_id
actor_id
agent_ref
role
capability_refs
autonomy_level
operating_constraints
```

Required field reason: AgentWorker records identify the agent participant, its
acting identity, available protocol-visible capabilities, autonomy level, and
constraints that bound autonomous work.

Optional fields:

```txt
tool_access_profile
memory_access_profile
extensions
```

Forbidden fields:

```txt
model_api_key
provider_secret
raw_prompt_store
runtime_process_id
container_id
database_primary_key
```

### WorkSession Field Lock

Required fields:

```txt
id
protocol_version
created_by_actor_id
objective
human_worker_id
agent_worker_id
policy_id
status
revision
last_event_hash
event_log_ref
created_at
updated_at
```

Required field reason: WorkSession records bind the human-agent pair, objective,
policy, lifecycle state, protocol version, creating Actor, current revision,
latest event hash, and event log that forms the source of truth.

Optional fields:

```txt
source_ref
context_manifest_ref
contribution_ledger_ref
evidence_manifest_ref
learning_record_refs
```

Forbidden fields:

```txt
database_primary_key
queue_message_id
runtime_session_id
cloud_resource_id
ui_state
credential
raw_auth_token
```

### JarvisEvent Field Lock

Required fields:

```txt
id
sequence
type
work_session_id
actor_id
timestamp
payload
previous_hash
event_hash
canonicalization
```

Required field reason: JarvisEvent records make WorkSession state attributable,
ordered, append-only, and export-verifiable.

Payload rule: `payload` contains only protocol-defined event fields, portable
refs, or opaque external refs. It MUST NOT contain credentials, secrets,
database ids, runtime state, deployment details, billing data, private scores,
or product UI state.

Optional fields:

```txt
trace_context
actor_signature
signing_key_ref
```

Forbidden fields:

```txt
raw_auth_token
credential
private_key
database_primary_key
runtime_trace_secret
provider_secret
```

### Policy Field Lock

Required fields:

```txt
id
owner_worker_id
created_by_actor_id
autonomy_level
allowed_actions
denied_actions
review_required_actions
risk_classes
escalation_rules
created_at
```

Required field reason: Policy records define the human-owned and attributable
boundary that allows, denies, narrows, or escalates AgentWorker action.

Optional fields:

```txt
tool_grants
memory_grants
external_send_rules
request_limits
extensions
```

Forbidden fields:

```txt
credential
raw_auth_token
provider_secret
billing_rule
cloud_policy_id
database_primary_key
```

### PolicyDecision Field Lock

Required fields:

```txt
id
work_session_id
actor_id
policy_id
requested_action
normalized_action_hash
risk_class
result
reason
created_at
```

Required field reason: PolicyDecision records why an AgentWorker action was
allowed, denied, narrowed, or sent for human review.

Optional fields:

```txt
data_sensitivity
selected_grant_refs
denied_grant_refs
request_id
evidence_refs
```

Forbidden fields:

```txt
hidden_policy_trace
credential
provider_secret
database_primary_key
runtime_decision_object
```

### Request Field Lock

Required fields:

```txt
id
protocol_version
work_session_id
requester_actor_id
requester_worker_id
target_human_worker_id
policy_decision_id
type
blocking_scope
reason_code
reason_summary
requested_action
requested_outcome
risk_class
human_decision_needed
options
default_if_no_response
status
created_at
expires_at
```

Required field reason: Request records the point where AgentWorker work cannot
continue safely without human permission, context, judgment, review, or
takeover. It ties the blocked scope to the PolicyDecision that triggered the
Request and records the safe fallback when the HumanWorker does not respond.

Optional fields:

```txt
missing_permission_or_context
policy_refs
data_sensitivity
recommended_option
safer_alternatives
evidence_refs
artifact_refs
contribution_refs
resolved_at
resolved_by_review_id
resolved_by_takeover_id
closed_by_event_ref
superseded_by_request_id
duplicate_of_request_id
```

Conditionally required fields:

```txt
resolved_at
  required when status is approved, denied, narrowed, answered, needs_revision,
  takeover, expired, cancelled, or superseded

resolved_by_review_id
  required when status is approved, denied, narrowed, answered, or
  needs_revision

resolved_by_takeover_id
  required when status is takeover

closed_by_event_ref
  required when status is expired, cancelled, or superseded
```

Forbidden fields:

```txt
private_inbox_id
notification_provider_id
credential
raw_auth_token
database_primary_key
runtime_state
provider_secret
billing_field
deployment_field
product_ui_state
hidden_policy_trace
unbounded_approval
implicit_authority_grant
```

### Review Field Lock

Required fields:

```txt
id
work_session_id
reviewer_actor_id
reviewer_worker_id
target_ref
decision
created_at
```

Required field reason: Review records human judgment over a protocol target and
resolves or changes the course of work.

Optional fields:

```txt
comments
required_changes
```

Conditionally required fields:

```txt
approval_scope
  required when decision is approve or narrow
  forbidden when decision is deny, correct, takeover, or needs_revision
```

Nested component:

```txt
ApprovalScope
  request_id
  review_id
  policy_decision_id
  request_revision
  request_event_hash
  normalized_action_hash
  approved_action
  allowed_scope
  denied_scope
  expires_at
  max_uses
  applies_to_work_session_id
  applies_to_actor_id
```

Forbidden fields:

```txt
private_comment_thread_id
credential
raw_auth_token
database_primary_key
product_ui_state
unbounded_approval
implicit_authority_grant
```

### Takeover Field Lock

Required fields:

```txt
id
work_session_id
requested_by_actor_id
controlling_actor_id
reason
lock_epoch
state
created_at
```

Required field reason: Takeover records direct human control, the lock epoch
that blocks stale autonomous continuation, and the state needed for safe
resumption.

Optional fields:

```txt
resumed_by_actor_id
reconciliation_notes
resolved_at
```

Conditionally required fields:

```txt
reconciliation_refs
  required before state becomes resumed
```

Forbidden fields:

```txt
runtime_lock_id
database_primary_key
credential
raw_auth_token
ui_session_id
```

### Contribution Field Lock

Required fields:

```txt
id
work_session_id
contributor_refs
contributor_type
contribution_type
event_refs
created_at
```

Required field reason: Contribution records who did what and keeps human,
agent, service, tool, and shared work distinguishable. `contributor_refs`
contains one or more `{worker_id, actor_id, contribution_role}` references so
shared contribution preserves individual attribution.

Optional fields:

```txt
artifact_refs
review_refs
evidence_refs
confidence
limitations
```

Conditionally required fields:

```txt
contributor_refs
  MUST contain every individual contributor when contributor_type is shared
```

Forbidden fields:

```txt
payment_account
compensation_rule
private_score
credential
database_primary_key
```

### EvidenceManifest Field Lock

Required fields:

```txt
id
work_session_id
generated_by_actor_id
objective
event_chain_root
evidence_item_refs
policy_decision_refs
request_refs
review_refs
takeover_refs
contribution_refs
export_profile
generated_at
```

Required field reason: EvidenceManifest records attributable portable proof of
what was requested, reviewed, observed, produced, decided, attributed, and
exported during the WorkSession.

Optional fields:

```txt
artifact_refs
limitation_refs
redaction_refs
```

Nested component:

```txt
EvidenceItemRef
  id
  work_session_id
  source_event_refs
  captured_by_actor_id
  evidence_type
  artifact_ref
  content_hash
  trust_label
  redaction_state
  captured_at
  limitation_refs
```

Forbidden fields:

```txt
credential
raw_auth_token
provider_secret
database_primary_key
cloud_storage_secret
unredacted_secret_value
raw_runtime_state
host_only_database_id
deployment_detail
billing_data
private_score
product_ui_state
```

### LearningRecord Field Lock

Required fields:

```txt
id
work_session_id
created_by_actor_id
subject_type
subject_ref
lesson_type
source_event_refs
review_state
scope
created_at
```

Required field reason: LearningRecord records who created the learning record,
what the human, agent, or pair learned, and ties that learning to source events
and governed scope.

Optional fields:

```txt
proposed_change
memory_proposal_refs
skill_proposal_refs
outcome_report_refs
```

Source rule: `source_event_refs` is required for every LearningRecord.
OutcomeReport-backed LearningRecords use the OutcomeReport acceptance
JarvisEvent as `source_event_refs` and may also record `outcome_report_refs`.

Review states:

```txt
proposed
accepted
rejected
superseded
```

Forbidden fields:

```txt
silent_memory_write
unreviewed_skill_activation
credential
raw_auth_token
database_primary_key
```

### MemoryProposal Field Lock

Required fields:

```txt
id
work_session_id
proposed_by_actor_id
proposed_for: human | agent | pair | project | task
memory_scope
memory_type
content
provenance
confidence
review_required
status
created_at
```

Required field reason: MemoryProposal records a governed memory change for the
human, agent, pair, project, or task with provenance, scope, confidence, and
review state before durable memory changes.

Optional fields:

```txt
source_event_refs
review_refs
expires_at
learning_record_refs
```

Conditionally required fields:

```txt
review_refs
  required when status is accepted
```

Status values:

```txt
proposed
pending_review
accepted
rejected
superseded
expired
```

Forbidden fields:

```txt
silent_memory_write
credential
raw_auth_token
private_embedding_store_id
database_primary_key
```

### SkillProposal Field Lock

Required fields:

```txt
id
work_session_id
proposed_by_actor_id
proposed_for: human | agent | pair | project | task
skill_scope
skill_name
trigger_conditions
procedure
review_checks
failure_cases
provenance
status
created_at
```

Required field reason: SkillProposal records a reusable way of working, the
human, agent, pair, project, or task scope it improves, and the review checks
required before the skill becomes active.

Optional fields:

```txt
required_tools
source_event_refs
review_refs
learning_record_refs
```

Conditionally required fields:

```txt
review_refs
  required when status is accepted
```

Status values:

```txt
proposed
pending_review
accepted
rejected
superseded
archived
```

Forbidden fields:

```txt
automatic_tool_grant
unreviewed_skill_activation
credential
raw_auth_token
database_primary_key
```

### OutcomeReport Extension Field Lock

`OutcomeReport` is an extension object. It does not change the v0.1 core object
list.

Required fields:

```txt
id
work_session_id
source_ref
reporter_ref
accepted_by_actor_id
outcome
learning_record_refs
received_at
```

Required field reason: OutcomeReport records attributable post-session feedback
and links it to governed LearningRecords without mutating the sealed
WorkSession or EvidenceManifest. `source_ref` identifies the completed, failed,
cancelled, or closed WorkSession export, external task record, evaluation
record, or other portable work reference whose outcome is being reported.
`reporter_ref` identifies the external or protocol reporter.
`accepted_by_actor_id` identifies the protocol Actor with review authority that
accepted the report into Jarvis records.
OutcomeReport does not define evaluation, payment, scoring, settlement, or
marketplace logic.

Optional fields:

```txt
external_system_ref
reporter_actor_id
reason
reviewer_feedback_refs
```

Forbidden fields:

```txt
task_marketplace_score_rule
payment_status
settlement_account
credential
raw_auth_token
database_primary_key
sealed_work_session_mutation
sealed_evidence_mutation
```

## Worker

`Worker` is the base participant contract.

```txt
Worker
  id
  type: human | agent | service | tool
  role
  display_name
  capabilities
  authority_scope
  accountability_scope
  extensions
```

Requirements:

- A Worker MAY participate in a WorkSession.
- A Worker MAY receive attribution through Contribution.
- A Worker MAY be represented by one or more Actors.
- A service Worker MUST exist only for protocol-visible system behavior, not
  for hiding human or agent responsibility.
- A tool Worker exists only when tool activity needs first-class
  attribution.

## Actor

`Actor` is the event and attribution identity used inside the protocol log.

```txt
Actor
  id
  worker_id
  type: human | agent | service | tool
  event_authority
  contribution_scope
  extensions
  valid_from
  valid_until
  created_at
```

Requirements:

- Every JarvisEvent MUST have an `actor_id`.
- HumanWorker and AgentWorker MUST each have at least one Actor.
- Service Actors MAY emit system events, policy decisions, and evidence capture
  events.
- Tool Actors MAY emit tool-result and evidence-capture events when the host
  exposes tool identity.
- Actor identity MUST NOT collapse human, agent, service, and tool actions into
  one undifferentiated actor.

## HumanWorker

`HumanWorker` is the accountable human participant in the collaboration loop.

```txt
HumanWorker
  worker_id
  actor_id
  profile_ref
  role
  policy_authority
  review_authority
  domain_context_refs
  preferences
  boundaries
  known_patterns
```

The HumanWorker supplies:

- goals
- judgment
- domain context
- world context
- taste
- policy authority
- review
- correction
- teaching
- accountability

Rules:

- The HumanWorker is not modeled as a passive user.
- The HumanWorker approves, denies, narrows, corrects, requests revision,
  answers, or takes over.
- Human corrections may create or reference LearningRecord, MemoryProposal, or
  SkillProposal records.
- Human accountability remains attributable even when execution is delegated.

## AgentWorker

`AgentWorker` is the autonomous but policy-bounded agent participant.

```txt
AgentWorker
  worker_id
  actor_id
  agent_ref
  role
  capability_refs
  tool_access_profile
  memory_access_profile
  autonomy_level
  operating_constraints
  extensions
```

The AgentWorker supplies:

- execution
- research
- planning
- drafting
- tool use
- memory retrieval
- evidence collection
- repeated workflow acceleration
- proposed improvements

Rules:

- The AgentWorker is not modeled as a chatbot.
- The AgentWorker acts inside Policy without asking for every small step.
- The AgentWorker creates a Request when it lacks permission, context, or
  judgment.
- `autonomy_level` uses the standard values defined in
  [03-autonomy-policy.md](./03-autonomy-policy.md): `observe_only`,
  `propose_only`, `execute_with_review`, `bounded_execute`, and
  `full_execute_in_scope`.
- The AgentWorker participates in learning, but it cannot silently confirm
  durable memory or skill changes.

## WorkSession

`WorkSession` is the source of truth for one collaboration loop.

```txt
WorkSession
  id
  protocol_version
  created_by_actor_id
  revision
  last_event_hash
  objective
  source_ref
  human_worker_id
  agent_worker_id
  policy_id
  status
  context_manifest_ref
  event_log_ref
  contribution_ledger_ref
  evidence_manifest_ref
  learning_record_refs
  created_at
  updated_at
```

Statuses:

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

Rules:

- A WorkSession is not chat history.
- A WorkSession records the collaboration, not the host execution stack.
- `source_ref` points to the origin of the work, task, host work reference, or
  external system reference. It is opaque to Jarvis and never gives the
  protocol ownership of that external system.
- Events are append-only.
- The event log is the protocol source of truth.
- Allowed WorkSession transitions are defined in
  [04-work-sessions.md](./04-work-sessions.md).
- Every mutating WorkSession operation MUST include
  `Jarvis-Protocol-Version`, `Jarvis-Actor-Id`, `Jarvis-Idempotency-Key`,
  `Jarvis-Request-Timestamp`, `Jarvis-Expected-WorkSession-Revision`, and
  `Jarvis-Previous-Event-Hash`.
- The operation MUST record the Actor from `Jarvis-Actor-Id` and verify
  authority before applying changes.
- `Jarvis-Expected-WorkSession-Revision` MUST match `WorkSession.revision`.
- `Jarvis-Previous-Event-Hash` MUST match `WorkSession.last_event_hash`.
- Every accepted WorkSession mutation increments `revision` and updates
  `last_event_hash`.
- Missing headers, stale expected revision, or mismatched previous event hash
  reject the mutation.
- Final EvidenceManifest export is valid only from `completed`, `failed`,
  `cancelled`, or `closed`.
- `closed` is sealed and rejects further mutation except idempotent replay of
  the same accepted request.
- Private host fields stay outside portable Jarvis exports.

## JarvisEvent

`JarvisEvent` is the append-only protocol event envelope.

```txt
JarvisEvent
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
  canonicalization
  actor_signature
  signing_key_ref
```

Rules:

- Every meaningful protocol transition creates a JarvisEvent.
- Every JarvisEvent has an Actor.
- Events are ordered inside a WorkSession.
- `previous_hash` links to the prior event hash in the WorkSession event log.
- `event_hash` is computed over canonical event serialization excluding
  `event_hash`, `actor_signature`, and signature metadata fields.
- `canonicalization` records the serialization and hash method used by the
  export profile.
- Export profiles use deterministic JSON canonicalization such as
  [RFC 8785 JCS](https://www.rfc-editor.org/rfc/rfc8785) unless the profile
  declares another method.
- `actor_signature` and `signing_key_ref` are optional. Signed export profiles
  use them to prove authorship; unsigned profiles still require Actor
  attribution.
- AgentWorker action events include only portable reproducibility refs:
  `model_ref`, `input_refs`, `prompt_ref`, `context_manifest_ref`, and related
  evidence hashes when the host provides them.
- Payload refs MUST NOT expose host-private execution details, runtime state,
  database ids, credentials, deployment ids, billing data, private scores, or
  product UI state.
- Event hashes make the protocol record inspectable and exportable.

## Policy

`Policy` defines the boundary for autonomous agent action.

```txt
Policy
  id
  owner_worker_id
  created_by_actor_id
  autonomy_level
  allowed_actions
  denied_actions
  review_required_actions
  tool_grants
  memory_grants
  external_send_rules
  risk_classes
  escalation_rules
  request_limits
  extensions
  created_at
```

Rules:

- Policy denies by default.
- Explicit deny beats allow.
- Uncovered action dimensions deny execution.
- `autonomy_level` uses the standard values defined in
  [03-autonomy-policy.md](./03-autonomy-policy.md): `observe_only`,
  `propose_only`, `execute_with_review`, `bounded_execute`, and
  `full_execute_in_scope`.
- Policy decisions are protocol events.
- Denied action produces a Request with the reason, requested action, risk,
  safer alternatives, and required reviewer.

## PolicyDecision

`PolicyDecision` records why an action was allowed, denied, narrowed, or sent
for review.

```txt
PolicyDecision
  id
  work_session_id
  actor_id
  policy_id
  requested_action
  normalized_action_hash
  risk_class
  data_sensitivity
  selected_grant_refs
  denied_grant_refs
  result: allow | deny | narrow | review_required
  reason
  request_id
  evidence_refs
  created_at
```

Rules:

- Every meaningful AgentWorker action has a PolicyDecision.
- Denial and review-required decisions create or reference a Request.
- Narrowed decisions create or reference Review or Request before narrowed
  execution.
- Allowed decisions never create authority outside selected grants.
- `normalized_action_hash` binds Request, Review, ApprovalScope,
  Contribution, and EvidenceManifest records that depend on the action.
- PolicyDecision records the protocol reason, not a hidden implementation
  judgment.
- PolicyDecision is included in EvidenceManifest.

## Request

`Request` is the structured way an AgentWorker asks the HumanWorker for
permission, context, judgment, review, correction, or takeover before safely
continuing a declared scope of work.

```txt
Request
  id
  protocol_version
  work_session_id
  requester_actor_id
  requester_worker_id
  target_human_worker_id
  policy_decision_id
  type: permission | context | judgment | review | correction | takeover |
    escalation
  blocking_scope: action | branch | artifact | tool_call | external_send |
    final_submission | work_session
  reason_code
  reason_summary
  requested_action
  requested_outcome
  missing_permission_or_context
  risk_class
  human_decision_needed
  options
  recommended_option
  safer_alternatives
  default_if_no_response
  status
  created_at
  expires_at
  resolved_at
```

Statuses:

```txt
pending
acknowledged
approved
denied
narrowed
answered
takeover
needs_revision
expired
cancelled
superseded
```

Rules:

- Request is not chat.
- Request is not a notification.
- Request is not authority.
- Request blocks only its declared scope.
- Request means the agent cannot continue safely on that declared scope.
- Human resolution of a Request requires Review or Takeover.
- Resolved Request status records `resolved_by_review_id` or
  `resolved_by_takeover_id`.
- Closed Request status records `closed_by_event_ref`.
- Approval is narrower than the requested action when the human restricts scope.
- Every Request includes options, risk, and default behavior when the human does
  not respond.
- Duplicate pending Requests are deduplicated or superseded.
- Expired Requests apply `default_if_no_response`; expiry never grants new
  authority.
- Invalid Request transitions reject as `invalid_request_transition`.
- Request livelock rejects as `request_livelock`.
- Deduplication or supersession that changes blocked action hash,
  PolicyDecision, blocking scope, risk, or event refs rejects as
  `duplicate_request_mismatch`.

## Review

`Review` records human judgment over a Request, action, contribution, artifact,
memory proposal, skill proposal, evidence item, or final outcome.

```txt
Review
  id
  work_session_id
  reviewer_actor_id
  reviewer_worker_id
  target_ref
  decision: approve | deny | narrow | correct | takeover | needs_revision
  comments
  required_changes
  approval_scope
  created_at
```

Rules:

- Review is a protocol object, not only UI feedback.
- Review resolves a Request when the human decision answers, approves, denies,
  narrows, corrects, or requires revision for the blocked scope.
- Takeover resolves a Request when the human assumes direct control of the
  blocked scope.
- Review records authority changes when the decision changes scope.
- Review with decision `approve` or `narrow` defines an ApprovalScope.
- ApprovalScope binds the approved action to scope, expiry, WorkSession, and
  Actor, and to the Request revision, Request event hash, PolicyDecision, and
  normalized action hash.
- Review creates Takeover only when the decision is `takeover`.
- Review does not silently mutate Policy, MemoryProposal, SkillProposal, or
  durable learning.
- Review may create LearningRecord, MemoryProposal, SkillProposal, or policy
  change proposal records. Those records remain governed.

## Takeover

`Takeover` records temporary direct human control.

```txt
Takeover
  id
  work_session_id
  requested_by_actor_id
  controlling_actor_id
  reason
  lock_epoch
  state
  resumed_by_actor_id
  reconciliation_notes
  reconciliation_refs
  created_at
  resolved_at
```

States:

```txt
requested
locked
human_active
reconciliation_required
resumed
closed
```

Rules:

- Takeover pauses autonomous continuation for the affected WorkSession scope.
- Takeover increments the lock epoch.
- Agent actions from an old lock epoch are stale and rejected.
- Resume requires reconciliation.
- Takeover may create or reference LearningRecord, MemoryProposal, or
  SkillProposal records.
- Allowed Takeover transitions are `requested -> locked`, `requested -> closed`,
  `locked -> human_active`, `locked -> reconciliation_required`,
  `locked -> closed`, `human_active -> reconciliation_required`,
  `human_active -> closed`, `reconciliation_required -> resumed`,
  `reconciliation_required -> closed`, and `resumed -> closed`.
- Takeover resume requires reconciliation refs before AgentWorker autonomy
  continues.
- `reconciliation_refs` is required before Takeover reaches `resumed`.

## Contribution

`Contribution` records who did what.

```txt
Contribution
  id
  work_session_id
  contributor_refs
  contributor_type: human | agent | service | tool | shared
  contribution_type
  event_refs
  artifact_refs
  review_refs
  evidence_refs
  confidence
  limitations
  created_at
```

Contribution types:

```txt
intent
instruction
plan
research
execution
artifact
review
correction
decision
evidence_capture
memory_proposal
skill_proposal
submission
```

Rules:

- Human, agent, service, tool, and shared contributions remain distinguishable.
- Shared contribution does not erase the individual contributing actors.
- Shared contribution preserves every individual contributor ref.
- Contribution is not compensation. It is the protocol record that downstream
  systems evaluate.

## EvidenceManifest

`EvidenceManifest` is the portable proof package for a WorkSession.

```txt
EvidenceManifest
  id
  work_session_id
  generated_by_actor_id
  objective
  event_chain_root
  artifact_refs
  evidence_item_refs
  policy_decision_refs
  request_refs
  review_refs
  takeover_refs
  contribution_refs
  limitation_refs
  export_profile
  generated_at
```

Rules:

- Evidence is captured during work.
- Evidence is not reconstructed from memory after the fact.
- Redacted exports are derived artifacts.
- Redaction never replaces the raw WorkSession evidence record.
- EvidenceManifest is portable across compatible products and hosts.
- Final EvidenceManifest export is valid only from `completed`, `failed`,
  `cancelled`, or `closed` WorkSession state.
- EvidenceManifest excludes product-private fields, credentials, secrets, raw
  runtime state, host-only database ids, deployment details, billing data,
  private scores, and product UI state.

## LearningRecord

`LearningRecord` records what improved because of the WorkSession.

```txt
LearningRecord
  id
  work_session_id
  created_by_actor_id
  subject_type: human | agent | pair
  subject_ref
  lesson_type
  source_event_refs
  proposed_change
  review_state
  scope
  created_at
```

Rules:

- Learning is not only agent memory.
- Jarvis records human learning, agent learning, and pair learning.
- `review_state` uses `proposed`, `accepted`, `rejected`, or `superseded`.
- A LearningRecord points to MemoryProposal or SkillProposal when learning
  becomes a governed memory or skill change.
- Learning does not become durable memory or active skill behavior without
  governed review.

## MemoryProposal

`MemoryProposal` is a proposed durable memory change.

```txt
MemoryProposal
  id
  work_session_id
  proposed_by_actor_id
  proposed_for: human | agent | pair | project | task
  memory_scope
  memory_type
  content
  provenance
  confidence
  review_required
  status
  created_at
```

Rules:

- Memory does not silently mutate.
- Model-derived memory cannot confirm itself.
- Tool-derived memory cannot confirm itself.
- Durable preferences, boundaries, permissions, and broad facts require
  review.
- Status uses `proposed`, `pending_review`, `accepted`, `rejected`,
  `superseded`, or `expired`.
- Accepted MemoryProposal creates durable memory only inside its declared
  memory_scope.

## SkillProposal

`SkillProposal` is a proposed reusable way of working.

```txt
SkillProposal
  id
  work_session_id
  proposed_by_actor_id
  proposed_for: human | agent | pair | project | task
  skill_scope
  skill_name
  trigger_conditions
  procedure
  required_tools
  review_checks
  failure_cases
  provenance
  status
  created_at
```

Rules:

- Skills are procedural memory.
- Skills encode repeated collaboration patterns.
- Unreviewed skill changes do not become active.
- Skill changes cannot expand tool access without separate policy review.
- Status uses `proposed`, `pending_review`, `accepted`, `rejected`,
  `superseded`, or `archived`.
- Accepted SkillProposal creates active skill behavior only inside its declared
  skill_scope.

## Portable Export

A portable Jarvis export contains:

```txt
protocol_version
WorkSession
Actors
Workers
JarvisEvents
PolicyDecisions
Requests
Reviews
Takeovers
Contributions
EvidenceManifest
LearningRecords
MemoryProposals
SkillProposals
limitations
```

The export must not require a receiving system to understand product-private
database ids, cloud resources, execution objects, UI state, credentials, or
deployment details.
