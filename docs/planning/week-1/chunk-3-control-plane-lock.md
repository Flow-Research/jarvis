# Chunk 3: Policy, Request, Review, And Takeover Lock

Chunk 3 locks the Jarvis control plane for human judgment and agent autonomy.

This chunk defines how PolicyDecision, Request, Review, ApprovalScope, and
Takeover work together when AgentWorker action is allowed, denied,
review-required, narrowed, or transferred to HumanWorker control.

This chunk does not create product UI, inbox UI, runtime behavior, model calls,
tool execution, queue behavior, Garden POC behavior, or host storage behavior.

## Scope

Chunk 3 locks:

```txt
PolicyDecision result semantics
Request lifecycle
Request blocking scope
Request versus non-blocking communication boundary
anti-livelock Request rules
Review decisions and effects
ApprovalScope requirements
Takeover lifecycle
takeover lock epoch rules
stale AgentWorker continuation rejection
escalation rules
review-required action rules
denied action rules
control-plane conformance checks
```

## Non-Goals

Chunk 3 does not:

- define host inbox UI
- define chat UI
- define notification transport
- define runtime execution
- define sandbox behavior
- define model behavior
- define Garden POC behavior
- define Workstream behavior
- define payment, scoring, or evaluation behavior

## Control-Plane Thesis

Policy governs AgentWorker autonomy.

Every AgentWorker action that affects a WorkSession MUST record a
PolicyDecision before the action is accepted as protocol state. Only then may
the AgentWorker action continue as protocol state.

AgentWorker action outside Policy MUST record a PolicyDecision before the
blocked action is accepted as protocol state. The denied, review-required, or
narrowed decision creates or references Request or Review before the affected
scope continues.

HumanWorker judgment enters through Review or Takeover.

Review resolves, narrows, corrects, denies, or requires revision.

Takeover transfers direct control over a declared scope to HumanWorker and
rejects stale AgentWorker continuation until reconciliation.

## Locked Invariants

Compatible implementations MUST enforce these invariants:

```txt
Every meaningful AgentWorker action records PolicyDecision before acceptance as protocol state.
Policy denies by default.
Explicit deny beats allow.
Denied or review-required PolicyDecision creates or references Request.
Request is not chat.
Request is not notification.
Request is not authority.
Request blocks only its declared scope.
Human-resolved Request states require Review or Takeover.
Approval creates bounded authority through ApprovalScope.
ApprovalScope binds action hash, scope, actor, WorkSession, expiry, and request revision.
Takeover increments lock epoch.
AgentWorker continuation from a stale lock epoch is rejected.
Resume after Takeover requires reconciliation.
Request resolution and Takeover produce evidence and may produce governed learning.
```

## Required State Machines

Request states:

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

Takeover states:

```txt
requested
locked
human_active
reconciliation_required
resumed
closed
```

Review is append-only human judgment. Review does not need a mutable status
machine. Its decision determines the protocol effect.

Every mutating Request, Review, or Takeover operation MUST include:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Every accepted control-plane state change records the Actor, verifies
authority, validates `Jarvis-Expected-WorkSession-Revision` against the current
WorkSession revision, and links to the previous event through
`Jarvis-Previous-Event-Hash`.

## Required Rejection Reasons

Compatible implementations reject:

```txt
missing_policy_decision
policy_denied
review_required
request_unresolved
invalid_request_transition
missing_review_resolution
missing_takeover_resolution
invalid_approval_scope
approval_scope_expired
approval_scope_mismatch
stale_takeover_epoch
missing_reconciliation_refs
request_livelock
duplicate_request_mismatch
```

## Reviewer Focus

Reviewers must verify:

- the control plane keeps Jarvis protocol-only
- PolicyDecision gates AgentWorker action
- Request stays separate from chat and notification
- Request blocks scope, not the whole WorkSession by default
- Review and Takeover are the only human resolution paths
- approval is bounded and replay-resistant
- Takeover rejects stale AgentWorker continuation
- anti-livelock rules prevent Request spam
- learning is governed and not silently durable

## Done Criteria

Chunk 3 is complete when:

- [12-request-protocol.md](../../protocol/12-request-protocol.md) locks Request
  lifecycle, blocking scope, approval scope, anti-livelock rules, and
  conformance checks
- [03-autonomy-policy.md](../../protocol/03-autonomy-policy.md) locks
  PolicyDecision, approval, and Takeover policy semantics
- [11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
  matches the locked control-plane semantics
- [14-protocol-lock.md](../../protocol/14-protocol-lock.md) states the same
  control-plane invariants
- conformance and package docs mention Request, Review, Takeover, stale epoch,
  approval scope, and anti-livelock checks
- local checks pass
- Zero-Trust Security Reviewer plus at least three other reviewer lanes pass
- valid findings are integrated
- rejected findings are recorded with concrete reasons
- PR is opened
