# Existing-Agent Compatibility Example

An existing native agent participates in Jarvis by producing Jarvis protocol
records around the human-agent collaboration loop.

Jarvis records protocol state. The existing agent keeps its native runtime.

## Boundary

Existing-agent compatibility covers protocol records only.

Hosts own the native agent runtime, model calls, tool calls, memory, skills,
tracing, session handling, execution flow, UI, storage, auth, billing, scoring,
payment, deployment, adapters, wrappers, and host-specific SDK integration.

Jarvis owns the portable collaboration record:

```txt
HumanWorker
AgentWorker
WorkSession
Policy
PolicyDecision
Request
Review
Takeover
Contribution
EvidenceManifest
LearningRecord
MemoryProposal
SkillProposal
OutcomeReport
```

A Jarvis SDK is a protocol implementation kit. It creates, validates, hashes,
exports, and tests Jarvis records. It MUST NOT run the agent, plan the task,
route the model, execute tools, own native memory, own UI, own auth, own
storage, or become the host adapter.

## Example Scope

This example demonstrates this protocol record shape:

```txt
An existing native agent completes work in its own environment while Jarvis
records the human-agent collaboration contract around that work.
```

A public compatibility claim using this example MUST use this format:

```txt
Implementation <name> supports Jarvis v0.1 compatibility, verified against the
existing-agent compatibility example, existing-agent proof plan, public
conformance checklist, and v0.1 golden-path and failure-mode fixtures on
<verification-date>.
```

The existing agent remains native. Jarvis records how the HumanWorker and
AgentWorker coordinate, request help, receive human judgment, transfer control,
record contribution, produce evidence, and carry governed learning into future
WorkSessions.

## Native Agent Scenario

A human uses an existing agent to complete one evidence-backed research and
drafting task.

The native agent already owns:

```txt
native session state
native model loop
native tool execution
native memory retrieval
native scratchpad
native traces
native retry behavior
native output formatting
```

Jarvis records only the collaboration contract around that native work:

```txt
objective
policy
allowed action
review-required action
scoped Request
human Review
bounded ApprovalScope
Takeover branch
Contribution
EvidenceManifest
LearningRecord
MemoryProposal
SkillProposal
OutcomeReport
```

## Protocol Actors

| Native role | Jarvis records | Stable ids used in this example |
| --- | --- | --- |
| human operator | `Worker`, `HumanWorker`, `Actor` | `worker-human-existing-agent`, `human-worker-existing-agent`, `actor-human-existing-agent` |
| existing native agent | `Worker`, `AgentWorker`, `Actor` | `worker-native-agent`, `agent-worker-native-agent`, `actor-native-agent` |
| host protocol service | `Actor` for accepted protocol operations only | `actor-host-protocol` |

The host protocol service Actor records accepted protocol mutations. It does
not own native execution, model calls, tool calls, memory, UI, auth, storage,
billing, scoring, payment, or deployment.

## Operation Header Classes

WorkSession-scoped mutations require:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Non-WorkSession protocol mutations require:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
```

Worker registration, Actor registration, and OutcomeReport submission are
non-WorkSession protocol mutations. They verify Actor authority, idempotency,
protocol version, and timestamp. They do not require fake WorkSession revision
or previous event hash values.

Every accepted WorkSession-scoped state change records the Actor, verifies
Actor authority, checks expected WorkSession revision, and links previous event
hash.

## Protocol Baseline

The compatible host creates these records:

```txt
WorkSession.id = work-session-existing-agent-001
WorkSession.objective = Produce an evidence-backed draft with reviewed external-source use.
WorkSession.human_worker_id = human-worker-existing-agent
WorkSession.agent_worker_id = agent-worker-native-agent
WorkSession.policy_id = policy-existing-agent-001
WorkSession.status = active
WorkSession.revision = 0
WorkSession.last_event_hash = hash:genesis

Policy.id = policy-existing-agent-001
Policy.allowed_actions = inspect_local_context, summarize_local_evidence, draft_artifact
Policy.denied_actions = access_credentials, send_external_message
Policy.review_required_actions = fetch_external_source, final_submission
Policy.request_limits = max_pending_requests: 3
```

The native agent stores execution details privately. Jarvis records only
portable protocol state.

## Native-To-Jarvis Mapping

| Native agent surface | Host-owned native behavior | Jarvis protocol record |
| --- | --- | --- |
| native agent session | host owns session handling | `AgentWorker` + `Actor` |
| human operator identity | host owns identity provider and auth backend | `HumanWorker` + `Actor` |
| task instruction | host owns prompt transport | `WorkSession.objective` |
| native policy settings | host owns policy UI and storage | `Policy` record |
| native tool step allowed by policy | host owns tool execution | `PolicyDecision.result = allow` before accepted state |
| native tool step requiring human judgment | host pauses affected branch | `PolicyDecision.result = review_required` + `Request` |
| connector-backed source result | host owns connector execution and raw connector response | `Review` grants bounded scope and `EvidenceItemRef` records source event refs, artifact ref, content hash, trust label, and limitations |
| human narrows action | host owns UI or command surface | `Review.decision = narrow` + `ApprovalScope` |
| human takes over final submission | host owns direct control surface | `Takeover` with `lock_epoch` and `reconciliation_refs` |
| native agent output | host owns raw traces and formatting | `Contribution` + evidence refs |
| reviewed lesson | host owns memory engine | `LearningRecord` + governed proposal |
| future memory change | host owns memory storage | `MemoryProposal` |
| future procedure change | host owns skill storage or prompt library | `SkillProposal` |
| external result | external system owns evaluation source | `OutcomeReport` |

Native memory, traces, prompts, tool logs, connector responses, and scratchpads
never enter portable records unless they are converted into permitted evidence
refs without host-private fields.

## Review Resolution Branch

This branch proves that the existing native agent continues inside a bounded
approval after human Review.

| Step | Native event | Jarvis operation | Required protocol proof |
| --- | --- | --- | --- |
| 1 | Host registers human and native agent participants. | `registerWorker`, `registerActor` | non-WorkSession headers and Actor authority verification |
| 2 | Human starts the task. | `createWorkSession` | expected revision `0`, genesis previous hash, objective, Policy, HumanWorker, AgentWorker |
| 3 | Native agent inspects permitted local context. | `recordPolicyDecision`, `appendJarvisEvent` | PolicyDecision exists before accepted AgentWorker state |
| 4 | Native agent reaches external-source action. | `recordPolicyDecision` | result `review_required`, `request_id = request-native-source-001` |
| 5 | Native agent defers the branch to the human. | `createRequest` | Request records scope, reason, risk, options, fallback, expiry, and PolicyDecision ref |
| 6 | Human narrows authority. | `recordReview` | Review resolves Request and creates bounded ApprovalScope |
| 7 | Native agent resumes inside approved scope. | `appendJarvisEvent` | action hash matches ApprovalScope and previous event hash links the chain |
| 8 | Work contribution records. | `recordContribution` | contributor refs identify human and native agent participation |
| 9 | Evidence exports. | `exportEvidenceManifest` | source events, PolicyDecision, Request, Review, Contribution, limitations, and export profile are present |
| 10 | Learning records. | `createLearningRecord`, `createMemoryProposal`, `createSkillProposal` | future-work changes remain governed |

Review branch records:

```txt
PolicyDecision.id = policy-decision-native-local-001
PolicyDecision.result = allow
PolicyDecision.target_action = inspect_local_context

PolicyDecision.id = policy-decision-native-source-001
PolicyDecision.result = review_required
PolicyDecision.request_id = request-native-source-001
PolicyDecision.normalized_action_hash = hash:action-fetch-native-source

Request.id = request-native-source-001
Request.policy_decision_id = policy-decision-native-source-001
Request.type = permission
Request.blocking_scope = tool_call
Request.reason_code = review_required_external_source
Request.risk_class = medium
Request.default_if_no_response = continue_without_external_source
Request.status = narrowed
Request.resolved_by_review_id = review-native-source-001
Request.resolved_at = 2026-06-12T18:36:00Z

Review.id = review-native-source-001
Review.work_session_id = work-session-existing-agent-001
Review.reviewer_actor_id = actor-human-existing-agent
Review.reviewer_worker_id = worker-human-existing-agent
Review.decision = narrow
Review.target_ref = request-native-source-001
Review.created_at = 2026-06-12T18:36:00Z
Review.approval_scope.request_id = request-native-source-001
Review.approval_scope.review_id = review-native-source-001
Review.approval_scope.policy_decision_id = policy-decision-native-source-001
Review.approval_scope.request_revision = 1
Review.approval_scope.request_event_hash = hash:event-request-native-source
Review.approval_scope.normalized_action_hash = hash:action-fetch-native-source
Review.approval_scope.approved_action.action = fetch_external_source
Review.approval_scope.allowed_scope.scope_ref = scope:approved-source-family
Review.approval_scope.denied_scope.scope_ref = scope:credentials-and-external-sends
Review.approval_scope.expires_at = 2026-06-12T18:36:00Z
Review.approval_scope.max_uses = 1
Review.approval_scope.applies_to_work_session_id = work-session-existing-agent-001
Review.approval_scope.applies_to_actor_id = actor-native-agent
```

The Review decision narrows the native agent. The native agent resumes only
inside `ApprovalScope`.

## Takeover Resolution Branch

This branch proves that human direct control resolves a high-risk scope without
turning Jarvis into the execution surface.

| Step | Native event | Jarvis operation | Required protocol proof |
| --- | --- | --- | --- |
| 1 | Native agent reaches final submission branch. | `recordPolicyDecision` | result `review_required`, Request required before accepted final submission |
| 2 | Native agent creates scoped Request. | `createRequest` | `blocking_scope = final_submission`, risk and fallback are recorded |
| 3 | Human assumes direct control in the host. | `recordTakeover` | Takeover links Request, affected scope, action hash, and `lock_epoch` |
| 4 | Native agent attempts stale continuation. | rejection gate | stale continuation rejects through stale Takeover epoch |
| 5 | Human reconciles the branch. | `recordTakeover` resumed state | `reconciliation_refs`, `resumed_by_actor_id`, and `resolved_at` are required |
| 6 | Contribution records final work. | `recordContribution` | human, agent, or shared attribution remains explicit |
| 7 | Evidence exports. | `exportEvidenceManifest` | Takeover refs and reconciliation refs appear in portable proof |

Takeover branch records:

```txt
PolicyDecision.id = policy-decision-native-final-001
PolicyDecision.result = review_required
PolicyDecision.request_id = request-native-final-001
PolicyDecision.normalized_action_hash = hash:action-native-final-submit

Request.id = request-native-final-001
Request.policy_decision_id = policy-decision-native-final-001
Request.type = takeover
Request.blocking_scope = final_submission
Request.reason_code = high_risk_final_submission
Request.risk_class = high
Request.default_if_no_response = do_not_submit
Request.status = takeover
Request.resolved_by_takeover_id = takeover-native-final-001
Request.resolved_at = 2026-06-12T18:50:00Z

Takeover.id = takeover-native-final-001
Takeover.work_session_id = work-session-existing-agent-001
Takeover.requested_by_actor_id = actor-native-agent
Takeover.controlling_actor_id = actor-human-existing-agent
Takeover.request_id = request-native-final-001
Takeover.lock_epoch = 2
Takeover.state = resumed
Takeover.affected_scope.blocking_scope = final_submission
Takeover.affected_scope.scope_ref = scope:final-submission
Takeover.affected_scope.normalized_action_hash = hash:action-native-final-submit
Takeover.reason = high_risk_final_submission
Takeover.created_at = 2026-06-12T18:48:00Z
Takeover.reconciliation_refs = ref:takeover-reconciliation-native-final
Takeover.resumed_by_actor_id = actor-human-existing-agent
Takeover.resolved_at = 2026-06-12T18:50:00Z
```

The stale continuation rejection maps to `stale_takeover_epoch`. Resume
requires `reconciliation_refs`.

## Evidence, Contribution, And Learning Records

Referenced event and contribution records:

```txt
JarvisEvent.id = event-native-local-context-001
JarvisEvent.object_ref = policy-decision-native-local-001
JarvisEvent.event_hash = hash:event-native-local-context

JarvisEvent.id = event-request-native-source-001
JarvisEvent.object_ref = request-native-source-001
JarvisEvent.event_hash = hash:event-request-native-source

JarvisEvent.id = event-review-native-source-001
JarvisEvent.object_ref = review-native-source-001
JarvisEvent.event_hash = hash:event-review-native-source

JarvisEvent.id = event-takeover-native-final-001
JarvisEvent.object_ref = takeover-native-final-001
JarvisEvent.event_hash = hash:event-takeover-native-final

JarvisEvent.id = event-evidence-native-export-001
JarvisEvent.object_ref = evidence-manifest-native-agent-001
JarvisEvent.event_hash = hash:event-evidence-native-export

JarvisEvent.id = event-native-final-001
JarvisEvent.object_ref = contribution-native-agent-001
JarvisEvent.event_hash = hash:event-native-final

Contribution.id = contribution-native-agent-001
Contribution.work_session_id = work-session-existing-agent-001
Contribution.contributor_refs[0].worker_id = worker-human-existing-agent
Contribution.contributor_refs[0].actor_id = actor-human-existing-agent
Contribution.contributor_refs[0].contribution_role = human
Contribution.contributor_refs[1].worker_id = worker-native-agent
Contribution.contributor_refs[1].actor_id = actor-native-agent
Contribution.contributor_refs[1].contribution_role = agent
Contribution.contributor_type = shared
Contribution.contribution_type = artifact
Contribution.event_refs = event-review-native-source-001, event-takeover-native-final-001, event-evidence-native-export-001, event-native-final-001
```

Both Review and Takeover branches export one portable proof:

```txt
EvidenceItemRef.id = evidence-item-native-summary-001
EvidenceItemRef.work_session_id = work-session-existing-agent-001
EvidenceItemRef.source_event_refs = event-review-native-source-001, event-takeover-native-final-001, event-native-final-001
EvidenceItemRef.captured_by_actor_id = actor-native-agent
EvidenceItemRef.evidence_type = reviewed_native_agent_summary
EvidenceItemRef.artifact_ref = artifact:native-agent-reviewed-summary
EvidenceItemRef.content_hash = hash:native-agent-reviewed-summary
EvidenceItemRef.trust_label = reviewed
EvidenceItemRef.redaction_state = redacted
EvidenceItemRef.captured_at = 2026-06-12T18:52:00Z
EvidenceItemRef.limitation_refs = limitation:raw-native-traces-excluded

EvidenceManifest.id = evidence-manifest-native-agent-001
EvidenceManifest.work_session_id = work-session-existing-agent-001
EvidenceManifest.generated_by_actor_id = actor-human-existing-agent
EvidenceManifest.objective = Produce an evidence-backed draft with reviewed external-source use.
EvidenceManifest.event_chain_root = hash:event-native-final
EvidenceManifest.evidence_item_refs = evidence-item-native-summary-001
EvidenceManifest.policy_decision_refs = policy-decision-native-local-001, policy-decision-native-source-001, policy-decision-native-final-001
EvidenceManifest.request_refs = request-native-source-001, request-native-final-001
EvidenceManifest.review_refs = review-native-source-001
EvidenceManifest.takeover_refs = takeover-native-final-001
EvidenceManifest.contribution_refs = contribution-native-agent-001
EvidenceManifest.limitations = raw native traces excluded, native memory excluded
EvidenceManifest.export_profile.profile = portable-v0.1
EvidenceManifest.generated_at = 2026-06-12T18:52:00Z
```

Evidence refs point to JarvisEvents captured during work. EvidenceManifest
MUST NOT contain credentials, secrets, raw runtime state, host-only database
ids, deployment details, billing data, private scores, UI state, raw auth
tokens, provider secrets, session cookies, private keys, raw native traces, or
native memory state.

Learning records capture the team improvement:

```txt
LearningRecord.id = learning-record-native-agent-001
LearningRecord.work_session_id = work-session-existing-agent-001
LearningRecord.created_by_actor_id = actor-human-existing-agent
LearningRecord.subject_type = pair
LearningRecord.subject_ref = ref:pair:human-worker-existing-agent:agent-worker-native-agent
LearningRecord.lesson_type = native_agent_bounded_source_review
LearningRecord.source_event_refs = event-review-native-source-001, event-takeover-native-final-001, event-evidence-native-export-001
LearningRecord.review_state = accepted
LearningRecord.scope = scope:native-agent-source-review
LearningRecord.created_at = 2026-06-12T18:53:00Z
LearningRecord.memory_proposal_refs = memory-proposal-native-source-boundary-001
LearningRecord.skill_proposal_refs = skill-proposal-native-review-flow-001

MemoryProposal.id = memory-proposal-native-source-boundary-001
MemoryProposal.proposed_for = pair
MemoryProposal.learning_record_refs = learning-record-native-agent-001
MemoryProposal.review_required = true
MemoryProposal.status = proposed

SkillProposal.id = skill-proposal-native-review-flow-001
SkillProposal.proposed_for = pair
SkillProposal.learning_record_refs = learning-record-native-agent-001
SkillProposal.status = proposed
```

MemoryProposal and SkillProposal records do not silently mutate native memory
or active native skills. Governed review controls future-work changes.

OutcomeReport stays post-session:

```txt
OutcomeReport.id = outcome-report-native-agent-001
OutcomeReport.work_session_id = work-session-existing-agent-001
OutcomeReport.source_ref = ref:external-outcome:native-agent-task
OutcomeReport.reporter_ref = ref:external-reviewer
OutcomeReport.accepted_by_actor_id = actor-human-existing-agent
OutcomeReport.outcome = accepted
OutcomeReport.learning_record_refs = learning-record-native-agent-001
```

OutcomeReport does not mutate the sealed WorkSession or EvidenceManifest.

## SDK Boundary Proof

Allowed Jarvis SDK responsibilities:

```txt
create protocol records
validate protocol records
attach required headers
compute event hashes
preserve previous event hash linkage
validate WorkSession revision expectations
export EvidenceManifest
run conformance checks
map native ids to protocol ids outside portable records
```

Rejected Jarvis SDK responsibilities:

```txt
run the native agent
replace the native agent
plan the task
route model calls
execute tools
store native memory
own host UI
own host auth
own host storage
own host adapter
own workflow execution
```

The SDK boundary preserves the protocol claim: Jarvis records collaboration;
the host owns implementation.

## Rejection Gates

The protocol rejects these compatibility failures:

```txt
missing_protocol_version
missing_actor
unauthorized_actor
missing_idempotency_key
missing_request_timestamp
missing_expected_work_session_revision
missing_previous_event_hash
missing_policy
missing_policy_decision
request_unresolved
missing_review_resolution
missing_takeover_resolution
invalid_approval_scope
stale_work_session_revision
invalid_previous_event_hash
stale_takeover_epoch
missing_reconciliation_refs
missing_contribution_actor
invalid_contributor_refs
evidence_after_the_fact
missing_evidence_event_refs
forbidden_host_private_field
silent_memory_mutation
silent_skill_activation
outcome_report_without_learning_record
unsupported_capability
```

Unsupported native concepts record `limitations` or reject as
`unsupported_capability`. They never weaken PolicyDecision, Request, Review,
Takeover, Contribution, EvidenceManifest, or LearningRecord gates.

## Public Questions Answered

What does Jarvis record beyond native agent logs?

```txt
Native agents perform work, but native logs and outputs do not create the
portable collaboration record compatible implementations need. Jarvis records
policy authority, blocked Requests, human Review or Takeover decisions,
attributable Contributions, EvidenceManifest refs, and governed LearningRecords
so the work remains reviewable, portable, and usable in future WorkSessions.
```

What stays native?

```txt
Runtime, model loop, tool execution, memory, traces, retries, prompt handling,
UI, auth, storage, billing, deployment, adapters, and workflow execution stay
host-owned.
```

What becomes portable?

```txt
The protocol record of how the HumanWorker and AgentWorker worked together,
what policy governed the work, what was blocked, how the human resolved it, who
contributed, what evidence exists, and what learning carries forward.
```

What proof does this example show?

```txt
The existing native agent produces the same required Jarvis records without
being rewritten as a Jarvis agent.
```

## Conformance Links

- [Compatibility mapping](../conformance/compatibility-mapping.md)
- [Existing-agent compatibility proof plan](../conformance/existing-agent-proof-plan.md)
- [Compatible host mapping example](./compatible-host-mapping.md)
- [Golden-path conformance entry](../conformance/golden-path.md)
- [Fixture documentation](../conformance/fixtures/README.md)

## Example Conditions

This example is valid only when:

- the existing native agent remains native
- Jarvis records collaboration only
- WorkSession-scoped mutations include required headers, Actor authority,
  expected revision, and previous event hash linkage
- non-WorkSession mutations use only non-WorkSession protocol headers
- every AgentWorker action that affects protocol state records PolicyDecision
  before accepted state
- Request resolves only through Review or Takeover
- ApprovalScope bounds narrowed authority
- Takeover resume requires reconciliation refs
- Contribution remains attributable
- connector execution stays host-owned and EvidenceManifest records only
  protocol-visible evidence refs
- EvidenceManifest excludes forbidden host-private fields
- LearningRecord, MemoryProposal, and SkillProposal stay governed
- OutcomeReport remains post-session feedback without sealed-record mutation
- SDK language stays limited to protocol implementation helpers
