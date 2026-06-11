# Request Protocol

Request is the control-plane object for intelligent deferral.

A Request is a structured, scoped deferral created when an AgentWorker cannot
safely, correctly, or responsibly continue a branch of work without HumanWorker
permission, context, judgment, review, correction, or takeover.

Request is not chat. Request is not a notification. Request is not authority.

Request means one thing:

```txt
AgentWorker cannot continue the declared scope until HumanWorker resolves it or
a terminal protocol transition closes it.
```

The canonical object shape is defined in
[11-core-protocol-objects.md](./11-core-protocol-objects.md). This document
defines how Request behaves.

## Research Grounding

Collaborative Gym shows why Request must be more precise than a message. It
models human-agent collaboration as asynchronous, bidirectional interaction
between human, agent, and task environment. Its results show that collaborative
agents outperform fully autonomous agents when collaboration quality holds,
while communication and situational-awareness failures remain major failure
modes.

Jarvis turns that lesson into protocol law:

```txt
communication informs
Request defers blocked work
Review resolves human judgment
Takeover transfers direct control
```

Primary reference:

- Collaborative Gym: https://arxiv.org/abs/2412.15701

## Request, Notification, Review, And Takeover

Jarvis keeps these concepts separate.

```txt
Notification
  non-blocking information about progress, state, or completion

Request
  scoped blocker requiring HumanWorker resolution

Review
  HumanWorker judgment over a Request or another protocol target

Takeover
  HumanWorker direct control over a declared work scope
```

Notification is not a v0.1 core object. Hosts surface progress messages, inbox
items, or UI notifications outside the v0.1 core protocol. Those records do not
block work unless a Request exists.

Compatible implementations MUST NOT treat ordinary chat, progress updates, or
status notifications as Requests.

## Request Types

Jarvis defines these Request types:

```txt
permission
  AgentWorker needs authority outside current Policy.

context
  AgentWorker lacks information only the HumanWorker provides.

judgment
  AgentWorker needs human taste, preference, priority, or decision.

review
  AgentWorker needs HumanWorker inspection of a plan, artifact, branch, or
  final output.

correction
  AgentWorker detects conflict, uncertainty, or direction drift and needs
  HumanWorker correction.

takeover
  AgentWorker recommends HumanWorker direct control over the declared scope.

escalation
  AgentWorker detects risk, policy conflict, ambiguity, or high-impact action.
```

## PolicyDecision Binding

Every Request is bound to a PolicyDecision.

PolicyDecision records why the AgentWorker action was allowed, denied,
narrowed, or review-required. Request records what HumanWorker input is needed
before the blocked scope continues.

Compatible implementations MUST enforce:

```txt
PolicyDecision.result == deny creates or references Request.
PolicyDecision.result == review_required creates or references Request.
PolicyDecision.result == narrow creates or references Review or Request.
PolicyDecision.result == allow does not create authority outside selected grants.
Request.policy_decision_id references the denied, review-required, or narrowed
decision that requires HumanWorker input.
```

`missing_policy_decision` rejects AgentWorker Request creation and AgentWorker
mutation acceptance when the required PolicyDecision is absent.

## Blocking Scope

Request blocks only its declared scope.

```txt
blocking_scope:
  action
  branch
  artifact
  tool_call
  external_send
  final_submission
  work_session
```

Most Requests block one action, branch, artifact, tool call, external send, or
final submission. `work_session` is reserved for cases where safe continuation
of the whole WorkSession is impossible.

AgentWorker continues unrelated safe branches when Policy allows them.

Compatible implementations MUST enforce the declared blocking scope. They MUST
NOT freeze the whole WorkSession unless `blocking_scope` is `work_session` or a
Takeover lock requires it.

## Required Quality

A valid Request answers six questions:

```txt
1. What is blocked?
2. Why is it blocked?
3. What does the AgentWorker want to do?
4. What are the risks?
5. What options does the HumanWorker have?
6. What happens if the HumanWorker does not respond?
```

The protocol rejects vague Requests.

Invalid:

```txt
Continue?
```

Valid:

```txt
I need network access to fetch package metadata from registry.npmjs.org.
Current Policy denies external network access.
Risk is medium because request metadata leaves the workspace.

Options:
1. Approve access to registry.npmjs.org for this WorkSession.
2. Deny and continue with local package metadata only.
3. Take over dependency inspection manually.

Default if no response:
Continue without network access and record an evidence limitation.
```

## Required Fields

Every Request records:

```txt
id
protocol_version
work_session_id
requester_actor_id
requester_worker_id
target_human_worker_id
policy_decision_id
type
status
blocking_scope
reason_code
reason_summary
requested_action
requested_outcome
risk_class
human_decision_needed
options
default_if_no_response
created_at
expires_at
```

`policy_decision_id` binds the Request to the PolicyDecision that blocked or
flagged the action.

`default_if_no_response` defines the safe fallback. The fallback never grants
new authority. It continues an unrelated safe branch, continues with limited
evidence, cancels the blocked branch, or keeps the blocked scope stopped.

`expires_at` prevents stale unresolved Requests from becoming hidden workflow
debt.

## Optional Fields

Request records these optional fields when present:

```txt
policy_refs
data_sensitivity
missing_permission_or_context
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

Optional fields add protocol-visible context. They do not change the meaning of
required fields.

## Lifecycle

Request states are:

```txt
pending
acknowledged
approved
denied
narrowed
answered
needs_revision
takeover
expired
cancelled
superseded
```

Every mutating Request, Review, or Takeover operation MUST include:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Every accepted Request, Review, or Takeover state change records the Actor,
verifies authority, validates `Jarvis-Expected-WorkSession-Revision` against
the current WorkSession revision, and links to the previous event through
`Jarvis-Previous-Event-Hash`.

State meanings:

```txt
pending
  Request exists and blocks its declared scope.

acknowledged
  HumanWorker has seen the Request but has not resolved it.

approved
  HumanWorker grants the requested action exactly as requested.

narrowed
  HumanWorker grants a smaller scope.

denied
  HumanWorker rejects the requested action.

answered
  HumanWorker provides information or judgment without granting new authority.

needs_revision
  HumanWorker requires the AgentWorker to revise the plan, request, or output.

takeover
  HumanWorker takes control of the affected scope.

expired
  HumanWorker did not respond before expiry; safe fallback applies.

cancelled
  Authorized Actor cancels the Request through an append-only protocol event
  because it is no longer relevant. Cancellation does not allow the blocked
  action to proceed.

superseded
  A newer Request replaces this Request while preserving the blocked action
  hash, policy decision, blocking scope, risk, and event references.
```

Human resolution of a Request requires Review or Takeover. Expiry,
cancellation, and supersession are terminal protocol transitions. They close
the Request, but they do not grant authority and they do not allow the blocked
action to proceed.

Resolved and closed Requests record the protocol reference that changed state:

```txt
resolved_by_review_id
  required when status is approved, denied, narrowed, answered, or
  needs_revision

resolved_by_takeover_id
  required when status is takeover

closed_by_event_ref
  required when status is expired, cancelled, or superseded
```

Missing resolver refs reject with these errors:

```txt
missing_review_resolution
  Request status is approved, denied, narrowed, answered, or needs_revision
  without resolved_by_review_id.

missing_takeover_resolution
  Request status is takeover without resolved_by_takeover_id.

missing_jarvis_event
  Request status is expired, cancelled, or superseded without
  closed_by_event_ref.
```

Allowed transitions:

```txt
pending -> acknowledged
pending -> approved | denied | narrowed | answered | needs_revision | takeover
pending -> expired | cancelled | superseded

acknowledged -> approved | denied | narrowed | answered | needs_revision |
  takeover
acknowledged -> expired | cancelled | superseded
```

Terminal states do not transition back to `pending` or `acknowledged`.
Terminal states do not change status again. A later Request references a
terminal Request only through a new protocol record. It never mutates the
original Request.

Rejected transitions include:

```txt
approved -> pending
approved -> acknowledged
denied -> pending
denied -> approved
narrowed -> approved
answered -> approved
needs_revision -> approved
takeover -> approved
expired -> approved
cancelled -> approved
superseded -> approved
```

Any transition not listed as allowed is rejected as
`invalid_request_transition`.

## Approval Scope

Request does not create authority. Approval creates bounded authority.

A Review with decision `approve` or `narrow` MUST define an ApprovalScope.

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

The AgentWorker resumes only inside the approved scope.

Compatible implementations MUST reject execution outside the ApprovalScope.
They MUST reject stale, replayed, mismatched, or expired approvals.

ApprovalScope validation checks:

```txt
request_id matches the resolved Request
review_id matches the resolving Review
policy_decision_id matches the Request policy_decision_id
request_revision matches the WorkSession revision at the Request state event
request_event_hash matches the JarvisEvent event_hash for the Request state
  event being resolved
normalized_action_hash matches the approved action
allowed_scope is no broader than the resolving Review
allowed_scope is no broader than the requested action
allowed_scope is no broader than the PolicyDecision selected grants
allowed_scope is no broader than the declared blocking scope
applies_to_work_session_id matches the WorkSession
applies_to_actor_id matches the AgentWorker Actor
expires_at has not passed
max_uses is not exhausted
```

Rejections:

```txt
invalid_approval_scope
approval_scope_expired
approval_scope_mismatch
```

ApprovalScope never expands Policy. It grants only the bounded authority
recorded by the Review.

## Review Effects

Review is append-only human judgment.

Review decisions have these protocol effects:

```txt
approve
  resolves the target Request and creates ApprovalScope.

deny
  resolves the target Request and keeps the blocked action denied.

narrow
  resolves the target Request and creates a smaller ApprovalScope.

correct
  records HumanWorker correction. When the Review targets a Request, the
  Request resolves as needs_revision. When the Review targets a non-Request
  protocol object, the target records the correction without changing Request
  status.

takeover
  resolves the target Request by creating or referencing Takeover.

needs_revision
  resolves the target Request and requires AgentWorker revision before the
  affected scope continues.
```

Review does not silently change durable memory, skill behavior, or Policy.
Review creates LearningRecord, MemoryProposal, SkillProposal, or policy change
proposal records when it changes future WorkSession behavior. Those records
remain governed.

## Takeover Lifecycle

Takeover is temporary direct HumanWorker control over a declared scope.

Takeover states:

```txt
requested
locked
human_active
reconciliation_required
resumed
closed
```

Every Takeover state transition is a mutating control-plane operation and MUST
enforce the required mutation headers, Actor authority, WorkSession revision,
previous event hash, and idempotency rules defined in this document.

Allowed transitions:

```txt
requested -> locked
requested -> closed

locked -> human_active
locked -> reconciliation_required
locked -> closed

human_active -> reconciliation_required
human_active -> closed

reconciliation_required -> resumed
reconciliation_required -> closed

resumed -> closed
```

Every Takeover increments the WorkSession lock epoch. AgentWorker protocol
actions or autonomous continuation from an older lock epoch are rejected as
`stale_takeover_epoch`.

Resume from Takeover requires reconciliation refs. The refs connect human
edits, affected artifacts, evidence, context updates, AgentWorker continuation,
and governed learning proposals when learning is created.

## Event Chain

Request is event-backed. The sequence below is behavioral, not a new event
taxonomy. Compatible implementations encode it through canonical JarvisEvents
defined for WorkSessions.

```txt
plan_proposed OR tool_requested
PolicyDecision recorded as protocol state
request_created
review_added OR human_takeover_started OR request_closed
request_resolved OR request_closed
continued work inside approved scope
LearningRecord, MemoryProposal, or SkillProposal
```

The event log remains append-only. Host database rows, inbox records, and UI
notifications do not replace JarvisEvents.

## Anti-Livelock Rules

Jarvis rejects Request spam.

Compatible implementations MUST enforce these rules:

```txt
1. Duplicate pending Requests are deduplicated or superseded without weakening
   `policy_decision_id`, `blocking_scope`, risk, requested action hash, or
   event references.
2. Similar Requests use this similarity key:
   `target_human_worker_id`, `type`, `blocking_scope`, `risk_class`,
   `policy_decision_id`, `normalized_action_hash`, and requested action hash.
3. Similar Requests are batched only when batching preserves every blocked
   action hash, PolicyDecision, risk class, blocking scope, and event ref.
4. Low-risk uncertainty MUST NOT create a Request. Hosts surface it as
   non-blocking communication, but Jarvis does not require a Notification object
   in v0.1.
5. Every Request includes default_if_no_response.
6. Every Request includes expires_at.
7. AgentWorker continues unrelated safe branches.
8. Compatible implementations enforce request_limits for each WorkSession.
9. Rejected Requests cannot be recreated unchanged immediately.
10. Repeated failed Requests escalate to Review or Takeover.
11. Superseded Requests preserve the blocked action hash, policy decision,
    blocking scope, risk, and event references.
12. Host UI notifications never convert into Requests without a PolicyDecision
    and Request event.
```

Each WorkSession resolves request_limits from Policy or protocol defaults:

```txt
max_pending_requests_per_work_session
max_pending_requests_per_blocking_scope
duplicate_request_window
repeated_unchanged_request_limit
similarity_key_fields
```

Protocol defaults:

```txt
max_pending_requests_per_work_session: 20
max_pending_requests_per_blocking_scope: 1
duplicate_request_window: WorkSession lifetime
repeated_unchanged_request_limit: 1
similarity_key_fields:
  target_human_worker_id
  type
  blocking_scope
  risk_class
  policy_decision_id
  normalized_action_hash
  requested_action_hash
```

`request_livelock` rejects repeated Request creation that bypasses these rules.
`duplicate_request_mismatch` rejects a deduplication or supersession attempt
that changes the blocked action hash, PolicyDecision, blocking scope, risk, or
event references.

## Learning Loop

Every resolved or closed Request is teaching material.

Request resolution or closure creates or references these records when it
changes future WorkSession behavior:

```txt
LearningRecord
MemoryProposal
SkillProposal
```

Examples:

```txt
HumanWorker denies network access.
  Future work prefers local evidence before external access.

HumanWorker narrows approval.
  PolicyProposal records a more precise grant pattern.

HumanWorker corrects final submission.
  SkillProposal records the corrected review process.

HumanWorker takes over.
  The pair records that this branch requires human control.
```

Learning remains governed. Request resolution or closure records a learning
proposal when the resolved branch changes future WorkSession behavior, but it
cannot silently confirm durable memory, skill, or policy changes.

## Conformance Tests

A Jarvis-compatible implementation MUST pass these Request tests:

```txt
1. Policy-denied action creates Request.
2. AgentWorker cannot execute the blocked action before resolution.
3. Human resolution requires Review or Takeover; expiry, cancellation, or
   supersession only closes the Request.
4. Approval supports narrowed authority.
5. Narrowed approval prevents execution outside the approved scope.
6. Expired Request applies default_if_no_response.
7. Takeover creates lock epoch and blocks stale AgentWorker continuation.
8. Duplicate Requests are deduplicated or superseded.
9. Request resolution or closure chain appears in EvidenceManifest, including
   Review, Takeover, or closure event refs as applicable.
10. Request resolution records governed learning proposals when the Review,
    Takeover, or safe fallback changes future WorkSession behavior.
11. Non-blocking host communication does not block WorkSession state.
12. Request blocks only its declared scope unless scope is work_session.
13. Request status transitions reject `invalid_request_transition`.
14. ApprovalScope rejects stale, mismatched, expired, or over-broad execution.
15. Takeover rejects stale AgentWorker continuation from an older lock epoch.
16. Takeover resume requires reconciliation refs.
17. Repeated unchanged Requests reject as `request_livelock` or supersede a
    prior Request without weakening policy fields.
18. Host notifications do not become blocking Requests without Request event
    and PolicyDecision.
```
