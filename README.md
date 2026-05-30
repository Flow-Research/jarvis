# Jarvis Human-Agent Collaboration Protocol

Jarvis is the human-agent collaboration protocol.

It defines how human workers and agent workers coordinate under shared goals
and human-defined policy, so they can complete work together, review each
other, record contributions, capture evidence, and learn across WorkSessions.

Jarvis is not a product, personal agent, chatbot, model provider, cloud stack,
sandbox, task marketplace, enterprise workspace, or capability harness.
Products, agents, execution environments, and external systems integrate with
Jarvis by implementing its protocol contracts.

## Interactive Simulation

Open the live simulation here:

https://flow-research.github.io/jarvis_human_agent/

The page is served directly by GitHub Pages from this repository.

## One-Line Definition

Jarvis is the open protocol that lets human workers and agent workers
collaborate under shared goals and policy, producing durable WorkSessions,
reviewable Requests, attributable Contributions, governed Learning, and
portable Evidence.

## Plain English Definition

Jarvis is how humans and agents work together properly.

The human does not just prompt. The agent does not just answer. They both
participate in the work.

The human gives direction, judgment, context, correction, approval, and
accountability. The agent plans, executes, researches, drafts, uses tools,
collects evidence, and proposes improvements.

Jarvis defines the rules of that collaboration so any product, model, task
system, execution environment, or external service can plug in.

## Thesis

The winning unit is not the human alone and not the agent alone. The winning
unit is the human-agent team.

Jarvis is not an agent protocol. Jarvis is a work protocol.

The primitive is not:

```txt
User -> Agent -> Answer
```

The primitive is:

```txt
WorkSession -> HumanWorker -> AgentWorker -> Review -> Evidence -> Learning
```

Work exists first. Humans, agents, services, and tools participate in the work.

Jarvis formalizes the loop where:

```txt
human judgment + agent execution + policy + review + evidence + learning
```

compound across real work.

## Core Loop

```txt
1. Human defines intent.
2. Policy defines boundaries.
3. Agent works inside those boundaries.
4. Agent asks when blocked.
5. Human reviews, approves, denies, narrows, corrects, or takes over.
6. Work continues.
7. Contributions are recorded.
8. Evidence is captured.
9. Learning is proposed.
10. Confirmed learning improves the next WorkSession.
```

## Central Object

`WorkSession` is the center of Jarvis.

A WorkSession is not chat history. A WorkSession is the durable record of real
human-agent collaboration around a focused unit of work.

It contains:

- objective
- human worker
- agent worker
- policy
- available capabilities
- context
- events
- requests
- reviews
- tool actions
- artifacts
- contributions
- evidence
- learning proposals
- final outcome

## First-Class Workers

Jarvis does not model `User + Assistant`.

Jarvis models `HumanWorker + AgentWorker`.

### HumanWorker

The human is:

- goal setter
- domain expert
- reviewer
- teacher
- quality judge
- policy owner
- accountable actor
- source of taste
- source of world context

### AgentWorker

The agent is:

- autonomous worker
- executor
- researcher
- context retriever
- tool user
- draft producer
- evidence collector
- learning participant

## Core Protocol Contracts

Jarvis v0 defines these contracts:

```txt
Worker
  id
  type: human | agent | service
  role
  capabilities
  authority
  accountability_scope

HumanWorker
  worker_id
  profile_ref
  policy_authority
  review_authority
  domain_context_refs
  preferences
  known_patterns

AgentWorker
  worker_id
  model_or_agent_ref
  capability_refs
  tool_access_profile
  memory_access_profile
  autonomy_level

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

Review
  id
  work_session_id
  reviewer_id
  target_ref
  decision: approve | deny | narrow | correct | takeover | needs_revision
  comments
  required_changes

Takeover
  id
  work_session_id
  actor_id
  reason
  lock_epoch
  resumed_by
  reconciliation_notes

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

## Protocol Laws

1. Jarvis is not a product.
2. Jarvis is not a personal agent.
3. Jarvis does not prescribe infrastructure.
4. WorkSession is the source of truth.
5. Policy governs autonomy.
6. Learning is governed.
7. Evidence is captured during work.
8. Contributions are attributable.
9. Human judgment remains central.
10. Execution may be delegated; accountability remains attributable.
11. Every session should improve the next session.

## Boundaries

Jarvis owns:

- collaboration protocol semantics
- WorkSession lifecycle
- policy-governed autonomy
- request, review, and takeover semantics
- contribution records
- evidence manifests
- governed memory and learning proposals
- skill proposal semantics
- implementation boundary contracts

Jarvis does not own:

- product UI
- external task marketplaces
- external identity systems
- enterprise workspace controls
- model providers
- cloud providers or deployment choices
- sandbox implementations or execution stacks
- database implementations

## What Jarvis v0 Must Prove

```txt
1. Create HumanWorker.
2. Create AgentWorker.
3. Start WorkSession.
4. Attach Policy.
5. Send objective.
6. Agent acts inside policy.
7. Agent hits blocked action.
8. Agent creates Request.
9. Human approves, denies, narrows, answers, or takes over.
10. Agent resumes.
11. Jarvis records Contribution.
12. Jarvis captures Evidence.
13. Jarvis proposes Learning.
14. Human confirms or rejects Learning.
15. EvidenceManifest exports.
```

If v0 proves this loop, Jarvis is real.

## Document Map

- [00-principles.md](./00-principles.md) - protocol principles, laws,
  non-goals, and design constraints.
- [01-architecture.md](./01-architecture.md) - system layers, protocol
  primitives, and ownership boundaries.
- [02-memory.md](./02-memory.md) - memory taxonomy, lifecycle, provenance,
  retrieval, and write policy.
- [03-autonomy-policy.md](./03-autonomy-policy.md) - autonomy levels,
  capability grants, requests, inbox, and takeover.
- [04-work-sessions.md](./04-work-sessions.md) - collaboration records,
  events, reviews, evidence, and learning loops.
- [05-skills-tools.md](./05-skills-tools.md) - skills, tools, MCP, sandbox
  policy, and tool wrapping.
- [06-integration-boundaries.md](./06-integration-boundaries.md) - product,
  host, and external system boundaries.
- [07-protocol-decisions.md](./07-protocol-decisions.md) - fixed protocol
  decisions and explicit non-decisions.
- [08-package-contracts.md](./08-package-contracts.md) - package graph,
  exports, ownership, forbidden imports, and release tests.
- [09-host-integration.md](./09-host-integration.md) - how products and hosts
  implement Jarvis without inheriting infrastructure assumptions.
- [10-protocol-mvp.md](./10-protocol-mvp.md) - the smallest protocol proof.
- [ROADMAP.md](./ROADMAP.md) - release roadmap, milestones, team workstreams,
  decision gates, risks, and immediate next actions.
