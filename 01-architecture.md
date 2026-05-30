# Architecture

Jarvis is the protocol for policy-governed collaboration and shared learning
between human workers and agent workers.

It defines how a human and an agent become a working team: shared goals,
policy, requests, review, takeover, contribution records, evidence, memory,
learning, and skills.

The architectural center is the HumanWorker + AgentWorker learning loop.
WorkSession is the durable record of that loop.

## Layer Model

```txt
Products and hosts
  product workspaces, task systems, CLI apps, chat apps, custom products

Jarvis protocol
  actors, workers, WorkSessions, policies, requests, reviews, takeover,
  contributions, evidence, learning records, memory proposals,
  skill proposals

External implementation choices
  models, tools, MCP servers, sandboxes, storage, queues, clouds,
  local machines, deployment platforms, product interfaces
```

Only the middle layer is Jarvis.

Products and hosts decide how to execute work. Jarvis defines the protocol
records and state transitions that make the work collaborative, governed,
reviewable, attributable, and portable.

## Core Protocol Contracts

### Actor

An entity that can create protocol events or receive attribution.

```txt
Actor
  id
  worker_id
  type: human | agent | service
  event_authority
  contribution_scope
```

### Worker

A participant in a WorkSession.

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
review, correction, approval, accountability, and learning.

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
drafting, automation, evidence collection, adaptation, and proposed
improvements.

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

What the HumanWorker, AgentWorker, or human-agent pair learned.

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

Jarvis tracks what the human learned, what the agent learned, what the
human-agent pair learned, and what should improve next time.

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

## Standard Work Flow

```txt
1. HumanWorker defines intent.
2. Jarvis starts or resumes a WorkSession.
3. Policy defines the action boundary.
4. AgentWorker receives context, memory, skills, and available capabilities.
5. AgentWorker plans and executes inside policy.
6. Policy evaluates every meaningful action.
7. Missing permission, context, or judgment becomes a Request.
8. HumanWorker reviews, approves, denies, narrows, corrects, or takes over.
9. AgentWorker resumes when allowed.
10. Jarvis records events, contributions, and evidence.
11. Jarvis proposes memory, skill, and learning updates for the human, agent,
    and pair.
12. HumanWorker confirms or rejects governed learning.
13. EvidenceManifest exports.
14. The HumanWorker, AgentWorker, and next WorkSession start with confirmed
    improvements.
```

## Ownership Boundary

Jarvis owns:

- protocol contracts
- actor semantics
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
- protocol conformance rules

Products and hosts own:

- user interface
- authentication and accounts
- execution environment
- model/provider selection
- tool execution
- sandboxing
- storage
- queues and scheduling
- deployment
- observability
- billing
- organization controls

## External System Boundary

External systems can start WorkSessions, consume EvidenceManifests, route
Reviews, evaluate Contributions, or provide context and skills. Jarvis defines
the protocol records exchanged with those systems. It does not define their
product architecture.

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

The developer entry point is protocol-first. Execution, hosting, storage, and
UI are implementation choices outside Jarvis.
