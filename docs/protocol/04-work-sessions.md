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
  objective
  human_worker_id
  agent_worker_id
  policy_id
  status
  context_manifest_ref
  event_log_ref
  contribution_ledger_ref
  evidence_manifest_ref
  learning_record_refs
```

A WorkSession contains many protocol events. Jarvis records protocol facts, not
host execution objects.

## Events

Important transitions are evented:

```txt
work_session_started
message_added
plan_proposed
tool_requested
tool_allowed
tool_denied
tool_executed
artifact_created
request_created
request_resolved
human_takeover_started
human_takeover_finished
review_added
memory_suggested
memory_confirmed
skill_suggested
skill_updated
work_session_completed
```

The event log supports observability, debugging, evidence, and learning.

The event log is append-only. Host checkpoints may accelerate resume, but
events are the source of truth.

Derived metrics such as revision rounds, elapsed time, blocked-action count,
and response latency can be computed from events and timestamps. Derived
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

After a WorkSession produces reviewable output, a compatible implementation can
run a learning pass:

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
