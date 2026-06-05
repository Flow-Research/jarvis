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
agents can outperform fully autonomous agents, while communication and
situational-awareness failures remain major failure modes.

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

Notification is not a v0 core object. Hosts may surface progress messages,
inbox items, or UI notifications, but those records do not block work unless a
Request exists.

Compatible implementations MUST NOT treat ordinary chat, progress updates, or
status notifications as Requests.

## Request Types

Jarvis defines these Request types:

```txt
permission
  AgentWorker needs authority outside current Policy.

context
  AgentWorker lacks information only the HumanWorker can provide.

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

AgentWorker may continue unrelated safe branches when Policy allows them.

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
Can I continue?
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
new authority. It may continue an unrelated safe branch, continue with limited
evidence, cancel the blocked branch, or keep the blocked scope stopped.

`expires_at` prevents stale unresolved Requests from becoming hidden workflow
debt.

## Optional Fields

Request may also record:

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
Terminal states do not change status again. A later Request may reference a
terminal Request, but it never mutates the original Request.

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
2. Similar Requests are batched when safe.
3. Low-risk uncertainty MUST NOT create a Request. Hosts may surface it as
   non-blocking communication, but Jarvis does not require a Notification object
   in v0.
4. Every Request includes default_if_no_response.
5. Every Request includes expires_at.
6. AgentWorker may continue unrelated safe branches.
7. Hosts enforce maximum pending Requests per WorkSession.
8. Rejected Requests cannot be recreated unchanged immediately.
9. Repeated failed Requests escalate to Review or Takeover.
```

## Learning Loop

Every resolved or closed Request is teaching material.

Request resolution or closure may create or reference:

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
  Policy may gain a more precise grant pattern.

HumanWorker corrects final submission.
  SkillProposal may capture the corrected review process.

HumanWorker takes over.
  The pair records that this branch requires human control.
```

Learning remains governed. Request resolution or closure can propose learning,
but it cannot silently confirm durable memory, skill, or policy changes.

## Conformance Tests

A Jarvis-compatible implementation MUST pass these Request tests:

```txt
1. Policy-denied action creates Request.
2. AgentWorker cannot execute the blocked action before resolution.
3. Human resolution requires Review or Takeover; expiry, cancellation, or
   supersession only closes the Request.
4. Approval can be narrowed.
5. Narrowed approval prevents execution outside the approved scope.
6. Expired Request applies default_if_no_response.
7. Takeover creates lock epoch and blocks stale AgentWorker continuation.
8. Duplicate Requests are deduplicated or superseded.
9. Request resolution or closure chain appears in EvidenceManifest, including
   Review, Takeover, or closure event refs as applicable.
10. Request resolution can create governed learning proposals.
11. Non-blocking host communication does not block WorkSession state.
12. Request blocks only its declared scope unless scope is work_session.
```
