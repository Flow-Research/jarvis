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

```txt
WorkSession
  id
  title
  objective
  human_agent_pair_id
  human actor
  agent actor
  interface source
  run refs
  autonomy level
  active policy
  active context
  memory snapshot refs
  skill refs
  tool grants
  events
  contributions
  requests
  reviews
  evidence bundle
  outcome
```

A WorkSession contains many work events and may reference host execution
attempts. Jarvis records protocol facts, not host execution objects.

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

## Contributions

Contribution records make collaboration inspectable:

```txt
Contribution
  actor id
  actor type
  work_session_id
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
  reviewer
  target event/contribution/artifact
  decision: approve | reject | revise | take_over | needs_context
  notes
  resulting actions
```

Reviews are teaching moments. They feed memory and skill proposals.

## Evidence Bundle

Evidence is gathered during work:

```txt
EvidenceBundle
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
  run ids
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

When context is assembled for a run, Jarvis stores a context manifest:

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

## Learning Pass

After a WorkSession produces reviewable output, Jarvis runs a learning pass:

```txt
1. inspect conversation, actions, reviews, artifacts, and outcome
2. propose memory changes
3. propose skill changes
4. classify corrections
5. record tool/policy failures
6. mark reusable context
```

The pass proposes. Policy decides what becomes durable.

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
