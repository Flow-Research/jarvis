# Architecture

Jarvis is the protocol for policy-governed collaboration between human workers
and agent workers.

It defines how a human and an agent become a working team: shared goals,
policy, requests, review, takeover, contribution records, evidence, memory,
learning, and skills.

## Layer Model

```txt
Interface layer
  chat, CLI, desktop, mobile, browser, messaging, custom apps

Jarvis protocol layer
  workers, WorkSessions, policies, requests, reviews, takeover,
  contributions, evidence, learning records, memory proposals,
  skill proposals

Capability layer
  tools, MCP servers, files, browser, shell, sandbox actions, connectors

Runtime adapter layer
  model loop, durable actors, sessions, files, tool execution, sandbox,
  scheduling, streaming, recovery

Infrastructure layer
  Cloudflare, local runtime, external services, databases, queues, object
  stores, model providers
```

Interfaces are replaceable. Runtimes are replaceable. Infrastructure is
replaceable. Jarvis protocol semantics are the stable center.

## Core Protocol Contracts

### Worker

A participant in work.

```txt
Worker
  id
  type: human | agent | service
  role
  capabilities
  authority
  accountability_scope
```

### HumanWorker

The human participant.

```txt
HumanWorker
  worker_id
  profile_ref
  policy_authority
  review_authority
  domain_context_refs
  preferences
  known_patterns
```

The human supplies goals, judgment, taste, domain context, world context,
review, correction, approval, and accountability.

### AgentWorker

The agent participant.

```txt
AgentWorker
  worker_id
  model_or_agent_ref
  capability_refs
  tool_access_profile
  memory_access_profile
  autonomy_level
```

The agent supplies speed, execution, research, tool use, memory retrieval,
drafting, automation, evidence collection, and proposed improvements.

### WorkSession

The shared unit of work.

```txt
WorkSession
  id
  objective
  source_ref
  human_worker_id
  agent_worker_id
  policy_id
  status
  context_manifest
  event_log_ref
  contribution_ledger_ref
  evidence_manifest_ref
  learning_records
```

A WorkSession is not chat history. It is the durable record of collaboration.
Every serious Jarvis flow starts or resumes a WorkSession.

### Policy

The human-defined boundary for agent action.

```txt
Policy
  id
  allowed_actions
  denied_actions
  review_required_actions
  tool_grants
  memory_grants
  external_send_rules
  risk_classes
  escalation_rules
```

The agent acts autonomously inside policy. Outside policy, it creates a
Request.

### Request

A structured ask from the agent to the human.

```txt
Request
  id
  work_session_id
  requester_id
  reason
  requested_action
  missing_permission_or_context
  risk_class
  options
  status
```

Requests are created when permission, context, judgment, or takeover is needed.

### Review

A human judgment over work, a request, an artifact, a memory proposal, a skill
proposal, or an action.

```txt
Review
  id
  work_session_id
  reviewer_id
  target_ref
  decision: approve | deny | narrow | correct | takeover | needs_revision
  comments
  required_changes
```

### Takeover

Temporary direct human control.

```txt
Takeover
  id
  work_session_id
  actor_id
  reason
  lock_epoch
  resumed_by
  reconciliation_notes
```

Takeover creates a lock epoch so autonomous execution cannot continue on stale
state.

### Contribution

Who did what.

```txt
Contribution
  id
  work_session_id
  worker_id
  contribution_type
  event_refs
  artifact_refs
  review_refs
  confidence
  limitations
```

Jarvis records human contribution, agent contribution, service contribution,
tool contribution, and shared contribution.

### EvidenceManifest

Portable proof of work.

```txt
EvidenceManifest
  id
  work_session_id
  objective
  event_chain_root
  artifacts
  tool_actions
  policy_decisions
  requests
  reviews
  contribution_refs
  limitations
  export_profile
```

Evidence is captured during work, not reconstructed after work.

### LearningRecord

What the team learned.

```txt
LearningRecord
  id
  work_session_id
  actor_id
  actor_type: human | agent | pair
  lesson_type
  source_event_refs
  proposed_change
  review_state
  scope
```

Jarvis tracks what the human learned, what the agent learned, what the pair
learned, and what should improve next time.

### MemoryProposal

A proposed durable memory update.

```txt
MemoryProposal
  id
  work_session_id
  proposed_by
  memory_scope
  content
  provenance
  confidence
  review_required
  status
```

Memory does not silently mutate. Durable memory changes are proposed,
reviewed, scoped, and accepted.

### SkillProposal

A proposed reusable way of working.

```txt
SkillProposal
  id
  work_session_id
  proposed_by
  skill_name
  trigger_conditions
  procedure
  required_tools
  review_checks
  failure_cases
  status
```

Skills turn repeated work into reusable process.

## Runtime/Internal Concepts

### Session

`Session` stores runtime message and turn state for an adapter. Session is
runtime/internal by default. Jarvis does not force most adopters to manage
low-level sessions directly.

### WorkSessionRun

`WorkSessionRun` is one execution attempt inside a WorkSession. A WorkSession
can have many runs. Runs bind to runtime execution references, leases,
checkpoints, recovery state, and stream state.

## Standard Work Flow

```txt
1. HumanWorker defines intent.
2. Jarvis starts or resumes a WorkSession.
3. Policy defines the action boundary.
4. AgentWorker receives context, memory, skills, and available capabilities.
5. AgentWorker plans and executes inside policy.
6. Policy wraps every tool/action.
7. Missing permission, context, or judgment becomes a Request.
8. HumanWorker reviews, approves, denies, narrows, corrects, or takes over.
9. AgentWorker resumes when allowed.
10. Jarvis records events, contributions, and evidence.
11. Jarvis proposes memory, skill, and learning updates.
12. HumanWorker confirms or rejects governed learning.
13. EvidenceManifest exports.
14. The next WorkSession starts with confirmed improvements.
```

## Ownership Boundary

Jarvis owns:

- protocol contracts
- worker semantics
- WorkSession lifecycle
- policy-governed autonomy
- request, review, and takeover semantics
- contribution records
- evidence manifests
- learning records
- memory proposal semantics
- skill proposal semantics
- context manifest semantics
- runtime adapter contracts

Runtime adapters own:

- model/tool loop mechanics
- durable actors
- storage primitives
- streaming transport
- sandbox mechanics
- scheduling and recovery
- run leases and checkpoints
- idempotent execution support

Interfaces own:

- visual layout
- notifications
- user interaction controls
- inbox presentation
- local input/output conventions

Products own:

- packaging
- billing
- enterprise controls
- product-specific workflows
- customer-specific integrations

## System Boundaries

```txt
Flow Research
  sets direction, standards, research agenda, public trust

Jarvis
  protocol for human-agent collaboration

Garden
  product workspace built on Jarvis

Workstream
  task, evaluation, rubric, review, and contribution infrastructure

Harnessy
  agent environment and capability preparation

Fellowship
  human development through public work and review
```

Jarvis connects these systems. It does not become them.

## Workstream Connection

Workstream tasks enter Jarvis through protocol boundaries:

```txt
Workstream Task
  -> creates or references WorkSession
  -> HumanWorker + AgentWorker collaborate
  -> Jarvis records requests, reviews, contributions, evidence, learning
  -> EvidenceManifest exports
  -> Workstream evaluates against rubric
```

Workstream owns task source, rubric, review routing, evaluation, acceptance,
and contribution scoring.

Jarvis owns collaboration, policy, requests, reviews, learning, contribution
records, and evidence packages.

## Garden Connection

Garden is a Jarvis-compatible product workspace for human-agent teams.

Garden can implement workspace UI, identity integration, inboxes, connectors,
permissions UI, audit UI, cost tracking, agent operations, and enterprise
controls.

Garden's implementation details remain Garden's product layer. Jarvis exposes
protocol contracts, not Garden internals.

## Minimum Developer Entry Point

```txt
create HumanWorker
create AgentWorker
start WorkSession
attach Policy
attach tools, skills, and memory
send objective
observe events, requests, contributions, and evidence
review or take over when needed
complete WorkSession
inspect learning proposals
export EvidenceManifest
```

Low-level runtime sessions, model turns, context snapshots, and adapter-specific
actors remain below this surface unless an advanced runtime integration
explicitly exposes them.
