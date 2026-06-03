# Core Protocol Objects

This document is the source of truth for Jarvis v0 core protocol objects.

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
6. A Request MUST be resolved only by Review or Takeover.
7. A Review MUST record human judgment over a protocol target.
8. Takeover MUST create a lock epoch and block stale autonomous continuation.
9. Contribution MUST record who did what.
10. EvidenceManifest MUST record portable proof while the WorkSession happens.
11. LearningRecord MUST record what the human, agent, or pair learned.
12. Durable memory and skill changes MUST remain proposals until governed review
    accepts them.

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
  metadata
```

Requirements:

- A Worker MAY participate in a WorkSession.
- A Worker MAY receive attribution through Contribution.
- A Worker MAY be represented by one or more Actors.
- A service Worker MUST exist only for protocol-visible system behavior, not
  for hiding human or agent responsibility.
- A tool Worker SHOULD exist only when tool activity needs first-class
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
- Human corrections are learning signals.
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
closed
```

Rules:

- A WorkSession is not chat history.
- A WorkSession records the collaboration, not the host execution stack.
- `source_ref` points to the origin of the work, task, product flow, or
  external system reference. It is opaque to Jarvis and never gives the
  protocol ownership of that external system.
- Events are append-only.
- The event log is the protocol source of truth.
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
- Export profiles SHOULD use deterministic JSON canonicalization such as
  [RFC 8785 JCS](https://www.rfc-editor.org/rfc/rfc8785) unless the profile
  declares another method.
- `actor_signature` and `signing_key_ref` are optional. Signed export profiles
  use them to prove authorship; unsigned profiles still require Actor
  attribution.
- AgentWorker action events SHOULD include payload reproducibility references:
  `model_ref`, `input_refs`, `prompt_ref`, `context_manifest_ref`, and related
  evidence hashes when the host provides them.
- Event hashes make the protocol record inspectable and exportable.
- Host-private execution details stay in payload references, not required
  protocol fields.

## Policy

`Policy` defines the boundary for autonomous agent action.

```txt
Policy
  id
  owner_worker_id
  autonomy_level
  allowed_actions
  denied_actions
  review_required_actions
  tool_grants
  memory_grants
  external_send_rules
  risk_classes
  escalation_rules
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
- PolicyDecision records the protocol reason, not a hidden implementation
  judgment.
- PolicyDecision is included in EvidenceManifest.

## Request

`Request` is the structured way an AgentWorker asks the HumanWorker for
permission, context, judgment, review, or takeover.

```txt
Request
  id
  work_session_id
  requester_actor_id
  requester_worker_id
  type: permission | context | decision | review | takeover
  reason
  requested_action
  missing_permission_or_context
  risk_class
  options
  status
  created_at
  expires_at
```

Statuses:

```txt
pending
approved
denied
narrowed
answered
takeover
needs_revision
expired
cancelled
```

Rules:

- Request is not a vague notification.
- Request means the agent cannot continue safely on that branch.
- Request resolution requires Review or Takeover.
- Approval is narrower than the requested action when the human restricts scope.

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
  created_at
```

Rules:

- Review is a protocol object, not only UI feedback.
- Review resolves a Request.
- Review creates learning signals.
- Review narrows future authority.
- Review triggers Takeover.

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
- Takeover is a learning event.

## Contribution

`Contribution` records who did what.

```txt
Contribution
  id
  work_session_id
  contributor_worker_id
  contributor_actor_id
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
- Contribution is not compensation. It is the protocol record that downstream
  systems evaluate.

## EvidenceManifest

`EvidenceManifest` is the portable proof package for a WorkSession.

```txt
EvidenceManifest
  id
  work_session_id
  objective
  event_chain_root
  artifact_refs
  evidence_item_refs
  policy_decision_refs
  request_refs
  review_refs
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

## LearningRecord

`LearningRecord` records what improved because of the WorkSession.

```txt
LearningRecord
  id
  work_session_id
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
  proposed_for: human | agent | shared | project | task
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

## SkillProposal

`SkillProposal` is a proposed reusable way of working.

```txt
SkillProposal
  id
  work_session_id
  proposed_by_actor_id
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
