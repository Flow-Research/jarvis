# Host Integration

Jarvis is implemented by a host.

A host is any implementation that produces and consumes Jarvis protocol
records. The host owns execution and infrastructure. Jarvis owns the protocol
records the host must produce.

## Host Responsibilities

A Jarvis-compatible host must:

- create HumanWorker records
- create AgentWorker records
- start and complete WorkSessions
- attach Policy to WorkSessions
- evaluate meaningful agent actions against Policy
- create Requests when action is blocked
- record Reviews from the HumanWorker
- enforce Takeover state
- record Contributions
- capture EvidenceManifest entries during work
- propose LearningRecords, MemoryProposals, and SkillProposals
- export portable Jarvis protocol records

## Host Freedom

A host owns these choices:

- UI
- auth
- model provider
- tool system
- MCP hosting
- sandbox
- storage
- queue
- cloud
- local execution
- deployment
- monitoring
- billing

None of these choices belong to Jarvis.

## Minimal Protocol Flow

```ts
const human = createHumanWorker({
  role: "reviewer",
  policy_authority: true,
  review_authority: true
});

const agent = createAgentWorker({
  role: "executor",
  autonomy_level: "bounded_execute"
});

const work = startWorkSession({
  objective: "Inspect this project and propose the next implementation step",
  human_worker_id: human.worker_id,
  agent_worker_id: agent.worker_id,
  policy_id: "bounded_policy"
});

recordEvent(work.id, {
  actor_id: human.actor_id,
  type: "objective_recorded"
});

const decision = evaluatePolicy({
  work_session_id: work.id,
  actor_id: agent.actor_id,
  requested_action: "network_fetch:example.com"
});

if (decision.result === "denied") {
  const request = createRequest({
    work_session_id: work.id,
    requester_worker_id: agent.worker_id,
    requester_actor_id: agent.actor_id,
    reason: "missing_permission",
    requested_action: "network_fetch:example.com",
    risk_class: "network_fetch"
  });

  recordReview({
    work_session_id: work.id,
    reviewer_worker_id: human.worker_id,
    reviewer_actor_id: human.actor_id,
    target_ref: request.id,
    decision: "narrow",
    required_changes: "Allow one host for this WorkSession only."
  });
}

recordContribution({
  work_session_id: work.id,
  contributor_worker_id: agent.worker_id,
  contributor_actor_id: agent.actor_id,
  contributor_type: "agent",
  contribution_type: "draft_artifact"
});

exportEvidenceManifest(work.id);
```

This is protocol shape only. It does not prescribe how functions are hosted,
where records are stored, or how the agent executes.

## Export Boundary

A host has private implementation fields. Those fields stay outside the
Jarvis export.

A portable Jarvis export contains:

- protocol_version
- WorkSession
- Workers
- Actors
- JarvisEvents
- PolicyDecisions
- Requests
- Reviews
- Takeovers
- Contributions
- EvidenceManifest
- LearningRecords
- MemoryProposals
- SkillProposals
- limitations

OutcomeReport is outside this sealed WorkSession export. When distributed,
OutcomeReport travels as a separate v0.1 extension record linked by
`work_session_id` and `learning_record_refs`.

## Compatibility

A host is Jarvis-compatible when it passes the conformance suite and exports
portable protocol records without requiring another host to understand its
private infrastructure.
