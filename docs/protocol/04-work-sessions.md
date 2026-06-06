# Work Sessions

Jarvis centers serious work around a `WorkSession`.

A WorkSession is the durable collaboration record for a focused unit of work.
It is not tied to any product or external task system.

## Why WorkSession Exists

Chat history does not represent real collaboration. A collaboration record
contains:

- human intent
- agent plan
- tool calls
- file and artifact references
- policy decisions
- human corrections
- requests and approvals
- evidence
- memory and skill updates
- final outcome

WorkSession gives these a home.

## Shape

The canonical WorkSession shape is defined in
[11-core-protocol-objects.md](./11-core-protocol-objects.md). This document
explains how the record behaves during collaboration.

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

A WorkSession contains many protocol events. Jarvis records protocol facts, not
host execution objects.

## Lifecycle States

WorkSession states are:

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

State meanings:

```txt
created
  WorkSession exists with HumanWorker, AgentWorker, objective, Policy, initial
  revision, and initial event hash.

active
  HumanWorker and AgentWorker can continue work inside Policy.

waiting_on_human
  One or more declared scopes are blocked on HumanWorker Review, context,
  judgment, or Takeover.

takeover
  HumanWorker has direct control over a declared scope and stale AgentWorker
  continuation is rejected.

reconciling
  HumanWorker takeover output is being reconciled into the WorkSession before
  AgentWorker continuation.

completed
  The WorkSession reached its intended outcome.

failed
  The WorkSession cannot reach its intended outcome.

cancelled
  An authorized Actor stopped the WorkSession before intended completion.

closed
  The WorkSession is sealed for archival/export state. No further mutation is
  accepted except idempotent replay of the same accepted request.
```

`created`, `active`, `waiting_on_human`, `takeover`, and `reconciling` are
mutable states. `completed`, `failed`, and `cancelled` are terminal outcome
states. `closed` is the sealed archival state.

## Transition Table

Compatible implementations MUST enforce this state machine:

```txt
created -> active
created -> cancelled

active -> waiting_on_human
active -> takeover
active -> completed
active -> failed
active -> cancelled

waiting_on_human -> active
waiting_on_human -> takeover
waiting_on_human -> completed
waiting_on_human -> failed
waiting_on_human -> cancelled

takeover -> reconciling
takeover -> failed
takeover -> cancelled

reconciling -> active
reconciling -> waiting_on_human
reconciling -> completed
reconciling -> failed
reconciling -> cancelled

completed -> closed
failed -> closed
cancelled -> closed
```

`closed` has no outgoing transition.

Rejected transitions include:

```txt
created -> completed
created -> failed
created -> closed
active -> closed
waiting_on_human -> closed
takeover -> active
takeover -> completed
takeover -> closed
reconciling -> takeover
completed -> active
completed -> failed
completed -> cancelled
failed -> active
failed -> completed
failed -> cancelled
cancelled -> active
cancelled -> completed
cancelled -> failed
closed -> created
closed -> active
closed -> waiting_on_human
closed -> takeover
closed -> reconciling
closed -> completed
closed -> failed
closed -> cancelled
```

Any transition not listed as allowed is rejected.

## Transition Events

Every allowed WorkSession state transition uses one canonical event type:

```txt
genesis -> created                 work_session_started

created -> active                 work_session_activated
created -> cancelled              work_session_cancelled

active -> waiting_on_human         work_session_waiting_on_human
active -> takeover                 work_session_takeover
active -> completed                work_session_completed
active -> failed                   work_session_failed
active -> cancelled                work_session_cancelled

waiting_on_human -> active         work_session_activated
waiting_on_human -> takeover       work_session_takeover
waiting_on_human -> completed      work_session_completed
waiting_on_human -> failed         work_session_failed
waiting_on_human -> cancelled      work_session_cancelled

takeover -> reconciling            work_session_reconciling
takeover -> failed                 work_session_failed
takeover -> cancelled              work_session_cancelled

reconciling -> active              work_session_activated
reconciling -> waiting_on_human    work_session_waiting_on_human
reconciling -> completed           work_session_completed
reconciling -> failed              work_session_failed
reconciling -> cancelled           work_session_cancelled

completed -> closed                work_session_closed
failed -> closed                   work_session_closed
cancelled -> closed                work_session_closed
```

Takeover object events remain separate:

```txt
human_takeover_started
human_takeover_finished
```

`work_session_takeover` records the WorkSession state transition.
`human_takeover_started` records the Takeover object and declared
human-controlled scope. Both records reference the same takeover id.

## Events

Important transitions and work records are evented:

```txt
work_session_started
work_session_activated
work_session_waiting_on_human
work_session_takeover
work_session_reconciling
work_session_completed
work_session_failed
work_session_cancelled
work_session_closed
message_added
plan_proposed
tool_requested
tool_allowed
tool_denied
tool_executed
artifact_created
request_created
request_resolved
request_closed
human_takeover_started
human_takeover_finished
review_added
memory_proposed
memory_confirmed
skill_proposed
skill_updated
```

The event log supports observability, debugging, evidence, and learning.

The event log is append-only. Host checkpoints accelerate resume, but
events are the source of truth.

Every WorkSession state change records a JarvisEvent. The event payload records:

```txt
from_status
to_status
reason
previous_revision
next_revision
```

The JarvisEvent envelope records `actor_id`, `previous_hash`, and `event_hash`.
State-change payloads do not duplicate those envelope fields.

State-change events include `blocked_scope_resolution_refs` whenever the
transition leaves `waiting_on_human`. State-change events include
`reconciliation_refs` only when the transition leaves `reconciling`.

`work_session_started` creates the initial `created` state. WorkSession creation
uses expected revision `0` and `Jarvis-Previous-Event-Hash` equal to the
protocol genesis hash. The start event sets `JarvisEvent.previous_hash` to the
same genesis hash. The accepted start event sets `revision` to `1` and
`last_event_hash` to the first event hash.

Every transition from `waiting_on_human` requires every blocked scope to be
accounted for by Review, Takeover, Request closure, or EvidenceManifest
limitation refs. A WorkSession cannot leave `waiting_on_human` by ignoring
unresolved blockers.

The state-change event records this proof in `blocked_scope_resolution_refs`:

```txt
review_refs
takeover_refs
request_closure_refs
evidence_limitation_refs
```

Completion from `waiting_on_human` is rejected while unresolved blockers remain
for `whole_work_session`, `final_submission`, required review, or required
evidence.

`waiting_on_human -> active` requires every blocked scope to be resolved or
closed. `waiting_on_human -> takeover` requires unresolved blocked scopes to be
transferred into the referenced Takeover scope. `waiting_on_human -> failed` and
`waiting_on_human -> cancelled` require unresolved blocked scopes to be recorded
as evidence limitations or request closures.

Every transition out of `reconciling` requires `reconciliation_refs`:

```txt
takeover_id
human_contribution_refs
affected_artifact_refs
evidence_refs
agent_event_refs
context_manifest_refs
learning_record_refs
memory_proposal_refs
skill_proposal_refs
```

This applies to:

```txt
reconciling -> active
reconciling -> waiting_on_human
reconciling -> completed
reconciling -> failed
reconciling -> cancelled
```

Learning, memory, and skill refs are required when reconciliation creates
governed learning. They are omitted only when the reconciliation event records
that no durable learning change was proposed.

## Revision And Hash Chain

Every mutating operation against a WorkSession requires:

```txt
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
Jarvis-Idempotency-Key
Jarvis-Actor-Id
Jarvis-Request-Timestamp
Jarvis-Protocol-Version
```

The protocol accepts a new mutation only when:

```txt
Jarvis-Expected-WorkSession-Revision == WorkSession.revision
Jarvis-Previous-Event-Hash == WorkSession.last_event_hash
Actor has authority for the requested transition or event
Idempotency key is unused
```

If `Jarvis-Idempotency-Key` was already accepted with the same Actor, protocol
version, operation, and canonical payload, the compatible implementation returns
the original accepted result. It MUST NOT append another JarvisEvent, increment
`revision`, or update `last_event_hash`. This replay check happens before stale
revision and previous hash rejection.

If the same idempotency key appears with a different Actor, protocol version,
operation, or canonical payload, the mutation is rejected as
`duplicate_idempotency_key_mismatch`.

For `POST /work-sessions`, the protocol treats the creation request as expected
revision `0` with previous event hash equal to the protocol genesis hash. The
operation still requires actor authority, idempotency, timestamp, and protocol
version. The idempotency key is scoped to the creating Actor, protocol version,
operation, and canonical create payload.

Accepted mutation behavior:

```txt
1. append JarvisEvent
2. increment WorkSession.revision by 1
3. set WorkSession.last_event_hash to JarvisEvent.event_hash
4. update WorkSession.updated_at
5. update WorkSession.status when the event is a state transition
```

Rejected mutation reasons:

```txt
missing_actor
missing_policy
missing_objective
unknown_state
invalid_transition
stale_work_session_revision
invalid_previous_event_hash
missing_idempotency_key
duplicate_idempotency_key_mismatch
missing_jarvis_event
missing_blocked_scope_resolution_refs
missing_reconciliation_refs
mutation_after_closed
invalid_export_state
unauthorized_actor
```

Hosts may store checkpoints, projections, or indexes. Those records never
replace the append-only JarvisEvent log.

Derived metrics such as revision rounds, elapsed time, blocked-action count,
and response latency are computed from events and timestamps. Derived
metrics do not replace source events and do not become required core fields.

## Contributions

Contribution records make collaboration inspectable:

```txt
Contribution
  work_session_id
  contributor_worker_id
  contributor_actor_id
  contributor_type: human | agent | service | tool | shared
  event refs
  contribution type
  content/artifact refs
  source refs
  review status
  timestamp
```

Contribution types:

```txt
instruction
plan
research
execution
artifact
review
correction
decision
memory_update
skill_update
submission
```

Jarvis is not an accounting system. It captures enough
structure to understand who did what and how the work evolved.

## Reviews

A review is human judgment over a target:

```txt
Review
  reviewer_worker_id
  reviewer_actor_id
  target event/contribution/artifact
  decision: approve | deny | narrow | correct | takeover | needs_revision
  notes
  resulting actions
```

Reviews are teaching moments. They feed memory and skill proposals.

## Evidence Items

Evidence is gathered during work:

```txt
EvidenceManifest
  source refs
  command transcripts
  tool outputs
  files created
  diffs
  screenshots/traces
  human reviews
  decision log
  final artifacts
  known limitations
```

Evidence is append-only or versioned. The system never silently rewrites what
happened.

Every evidence item is content-addressed:

```txt
EvidenceItem
  sequence
  previous_hash
  content_hash
  producer
  capture_time
  tool_call_id
  policy_decision_id
  mime/type
  byte length
  storage uri
  redaction lineage
```

Redacted exports are derived artifacts. They never replace raw immutable
evidence inside the WorkSession record.

## Evidence Manifest

Evidence is exportable as a manifest:

```txt
EvidenceManifest
  work_session_id
  event-chain root
  artifact refs
  artifact hashes
  evidence item hashes
  command/tool traces
  source refs
  redactions
  human reviews
  policy decisions
  limitations
  generated at
```

The manifest is not accounting. It is the portable proof package of what Jarvis
observed, produced, reviewed, and decided.

## Memory Snapshot Manifest

When context is assembled for a run, the WorkSession records a context
manifest:

```txt
memory ids
memory versions
retrieval reasons
trust labels
rendered text hash
skill ids/versions
policy profile
tool inventory hash
```

This lets a WorkSession resume and lets humans inspect why the agent saw a
particular context.

## Reproducibility References

AgentWorker action events record enough references to reconstruct what the
agent acted on at that point in time:

```txt
model_ref
input_refs
prompt_ref
context_manifest_ref
policy_id
evidence_hashes
```

These references stay inside event payloads and evidence records. Provider
private runtime details stay outside portable exports unless an export profile
explicitly includes them.

## Learning Pass

After a WorkSession produces reviewable output, a compatible implementation
runs a learning pass:

```txt
1. inspect conversation, actions, reviews, artifacts, and outcome
2. propose memory changes
3. propose skill changes
4. classify corrections
5. record tool/policy failures
6. mark reusable context
```

The pass produces LearningRecord, MemoryProposal, and SkillProposal records.
Policy decides what becomes durable.

## Completion, Failure, Cancellation, And Closure

`completed` means the WorkSession reached its intended outcome.

`failed` means the WorkSession cannot reach its intended outcome. Failure records
the reason, evidence limitations, and remaining unresolved Requests when they
exist.

`cancelled` means an authorized Actor stopped the WorkSession before intended
completion. Cancellation records the Actor, reason, and policy basis. It does
not grant authority to execute blocked work.

After `completed`, `failed`, or `cancelled`, compatible implementations accept
only:

```txt
final EvidenceManifest link or export record
governed LearningRecord, MemoryProposal, or SkillProposal records allowed by
  Policy
transition to closed
idempotent replay of the same accepted request
```

They reject new work events, new AgentWorker actions, new Requests, and
unrelated Contributions.

`closed` seals the WorkSession. After `closed`, compatible implementations MUST
reject every mutating operation except idempotent replay of the same accepted
request.

## Export Eligibility

Final portable EvidenceManifest export is valid only from:

```txt
completed
failed
cancelled
closed
```

Exports from mutable states are interim host snapshots, not final Jarvis
EvidenceManifest exports.

If final export generation appends or links an EvidenceManifest record, that
mutation happens before transition to `closed`. A `closed` WorkSession only
permits read-only reproduction of an already sealed export.

Every final export records:

```txt
work_session_id
status
revision
event_chain_root
last_event_hash
exported_at
generated_by_actor_id
limitations
```

Final export MUST exclude product-private fields, credentials, secrets, raw
runtime state, host-only database ids, deployment details, billing data, private
scores, and product UI state.

## WorkSession Resumption

A WorkSession is resumable:

- restore objective
- restore current state
- restore pending requests
- restore evidence
- restore relevant memory snapshot
- explain what remains

The agent continues without losing context after host interruption, restart, or
human delay.

## Durability And Recovery

Durable collaboration requires:

- append-only event log as source of truth
- checkpoints for fast resume
- idempotency keys for tool calls
- host leases or equivalent guards to prevent duplicate execution
- retry policy for recoverable failures
- recovery states for interrupted work
- external-send outbox for side effects
- request store with resume tokens

If a run fails mid-tool, Jarvis records whether the tool was never started,
started with unknown result, completed with receipt, or needs human
reconciliation.
