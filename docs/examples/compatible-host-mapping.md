# Compatible Host Mapping Example

This example shows how two different native host shapes produce equivalent
Jarvis records for the same human-agent collaboration loop.

Jarvis records protocol state. Hosts own native execution.

## Boundary

This example defines protocol mapping only.

It does not define host code, adapter code, wrapper code, runtime behavior, UI,
model calls, tool execution, storage, auth, billing, scoring, payment,
deployment, or SDK implementation.

`host_shape_ref` is descriptive metadata only. It names the host boundary shape.
It MUST NOT select behavior, change required records, change conformance
results, enter protocol records, or imply a Jarvis-owned host adapter or
runtime.

Allowed `host_shape_ref` values in this example:

```txt
command_line_host_boundary
local_execution_host_boundary
```

## Native Work

A HumanWorker and AgentWorker work on one evidence-backed research task.

The human defines the objective and policy. The agent collects permitted local
evidence, reaches a blocked external-source action, creates a Request, receives
human Review with narrowed approval, resumes inside the approved scope, records
Contribution and EvidenceManifest records, and creates governed LearningRecord,
MemoryProposal, SkillProposal, and OutcomeReport records.

The same work also includes one high-risk branch where the human takes direct
control through Takeover. The Takeover branch proves lock epoch, stale
continuation rejection, and reconciliation refs.

## Host Shapes

| Host shape metadata | Native boundary | Jarvis requirement |
| --- | --- | --- |
| `command_line_host_boundary` | Human and agent coordinate through a command-line interaction. | The command-line surface maps native actions into Jarvis records without exposing terminal state. |
| `local_execution_host_boundary` | Human and agent coordinate through a local workspace or local process. | The local surface maps native actions into the same Jarvis records without exposing local process state. |

Both host shapes produce the same normalized Jarvis record graph.

## Protocol Actors

| Native role | Jarvis records | Stable ids used in this example |
| --- | --- | --- |
| human operator | `Worker`, `HumanWorker`, `Actor` | `worker-human-researcher`, `human-worker-researcher`, `actor-human-reviewer` |
| native agent | `Worker`, `AgentWorker`, `Actor` | `worker-agent-research`, `agent-worker-research`, `actor-agent-worker` |
| host service | `Actor` for accepted protocol operations only | `actor-host-protocol` |

The host service Actor records accepted protocol mutations. The host service
Actor does not own execution, model calls, tool calls, memory, UI, auth,
storage, billing, scoring, payment, or deployment.

## Shared Protocol Baseline

Both host shapes create the same baseline records:

```txt
WorkSession.id = work-session-research-001
WorkSession.objective = Prepare an evidence-backed answer for a bounded research task.
WorkSession.human_worker_id = human-worker-researcher
WorkSession.agent_worker_id = agent-worker-research
WorkSession.policy_id = policy-research-001
WorkSession.status = active
WorkSession.revision = 0
WorkSession.last_event_hash = hash:genesis

Policy.id = policy-research-001
Policy.allowed_actions = inspect_local_context, summarize_local_evidence, draft_artifact
Policy.denied_actions = send_external_message, access_credentials
Policy.review_required_actions = fetch_external_source, final_submission
Policy.request_limits = max_pending_requests: 3
```

The native host stores execution details privately. Jarvis records only the
portable protocol state.

## Operation Header Classes

WorkSession-scoped mutations in this example require:

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
non-WorkSession protocol mutations. They do not require fake WorkSession
revision or previous event hash values.

Every accepted WorkSession-scoped state change verifies Actor authority,
checks expected WorkSession revision, links previous event hash, and records
the Actor.

## Native-To-Jarvis Mapping

| Native surface | Command-line host mapping | Local execution host mapping | Equivalent Jarvis record |
| --- | --- | --- | --- |
| human starts work | CLI command starts task | local workspace action starts task | `WorkSession` with objective, Policy, revision, and event hash state |
| human authority | CLI operator identity | local workspace user identity | `HumanWorker` and `Actor` |
| agent authority | native agent process identity | local agent process identity | `AgentWorker` and `Actor` |
| local context read | terminal output stays host-owned | local file/process trace stays host-owned | `JarvisEvent` with portable evidence refs only |
| allowed agent action | allowed command step | allowed local step | `PolicyDecision.result = allow` before accepted event |
| external source blocked | CLI step pauses | local process branch pauses | `PolicyDecision.result = review_required` and scoped `Request` |
| human narrowed approval | CLI response narrows scope | local workspace response narrows scope | `Review.decision = narrow` and bounded `ApprovalScope` |
| high-risk branch | human pauses CLI branch | human locks local branch | `Takeover` with `lock_epoch` and `reconciliation_refs` |
| performed work | command transcript summary | local trace summary | `Contribution` with contributor refs |
| evidence export | portable refs from events | portable refs from events | `EvidenceManifest` without host-private fields |
| confirmed improvement | human confirms lesson | human confirms lesson | `LearningRecord` with human, agent, or pair subject |
| future memory | reviewed durable note | reviewed durable note | `MemoryProposal` |
| future procedure | reviewed repeatable procedure | reviewed repeatable procedure | `SkillProposal` |
| post-session result | external feedback ref | external feedback ref | `OutcomeReport` referencing LearningRecord |

## Review Resolution Branch

This branch proves a scoped Request resolved through Review.

| Step | Native event | Jarvis operation | Required protocol proof |
| --- | --- | --- | --- |
| 1 | Host registers human and agent participants. | `registerWorker`, `registerActor` | non-WorkSession mutation headers and Actor authority verification |
| 2 | Human starts the task. | `createWorkSession` | expected revision `0`, genesis previous event hash, objective, Policy, HumanWorker, AgentWorker |
| 3 | Agent inspects local context. | `recordPolicyDecision`, `appendJarvisEvent` | PolicyDecision exists before accepted AgentWorker state |
| 4 | Agent reaches external-source action. | `recordPolicyDecision` | result `review_required`, `request_id = request-external-source-001` |
| 5 | Agent asks for human decision. | `createRequest` | scoped blocker, risk, options, fallback, expiry, PolicyDecision ref |
| 6 | Human narrows authority. | `recordReview` | Review resolves Request and creates ApprovalScope |
| 7 | Agent resumes inside bounds. | `appendJarvisEvent` | action hash matches ApprovalScope and previous event hash links the chain |
| 8 | Work is recorded. | `recordContribution` | contributor refs identify human, agent, or shared contribution |
| 9 | Evidence exports. | `exportEvidenceManifest` | source event refs, event chain root, limitations, export profile |
| 10 | Learning records. | `createLearningRecord`, `createMemoryProposal`, `createSkillProposal` | governed future-work change remains review-scoped |
| 11 | Outcome enters. | `submitOutcomeReport` | OutcomeReport references LearningRecord and does not mutate sealed records |

Review branch ids:

```txt
policy_decision_id = policy-decision-external-source-001
request_id = request-external-source-001
review_id = review-external-source-001
approval_scope.request_id = request-external-source-001
approval_scope.review_id = review-external-source-001
approval_scope.policy_decision_id = policy-decision-external-source-001
approval_scope.request_revision = 1
approval_scope.request_event_hash = hash:event-request-external-source
approval_scope.normalized_action_hash = hash:action-fetch-approved-source
approval_scope.approved_action.action = fetch_external_source
approval_scope.allowed_scope.scope_ref = scope:approved-source-family
approval_scope.denied_scope.scope_ref = scope:all-other-external-sends-and-credentials
approval_scope.expires_at = 2026-06-12T18:36:00Z
approval_scope.max_uses = 1
approval_scope.applies_to_work_session_id = work-session-research-001
approval_scope.applies_to_actor_id = actor-agent-worker
```

The Review decision is `narrow`. The allowed scope limits the agent to the
approved source family for the current WorkSession, with expiry and max-use
bounds. The denied scope preserves all other external sends and credential
access as denied.

## Takeover Resolution Branch

This branch proves a scoped Request resolved through Takeover.

| Step | Native event | Jarvis operation | Required protocol proof |
| --- | --- | --- | --- |
| 1 | Agent reaches high-risk final-submission branch. | `recordPolicyDecision` | result `review_required`, Request required before accepted action |
| 2 | Agent creates scoped Request. | `createRequest` | `blocking_scope = final_submission`, risk and fallback recorded |
| 3 | Human assumes direct control. | `recordTakeover` | Takeover links Request, affected scope, normalized action hash, and `lock_epoch` |
| 4 | Stale agent continuation appears. | rejection gate | stale continuation rejects through stale Takeover epoch |
| 5 | Human reconciles branch. | `recordTakeover` resumed state | `reconciliation_refs`, `resumed_by_actor_id`, and `resolved_at` are required |
| 6 | Final contribution records. | `recordContribution` | human, agent, or shared contribution remains attributable |
| 7 | Evidence exports. | `exportEvidenceManifest` | Takeover refs and reconciliation refs are included in portable proof |

Takeover branch ids:

```txt
policy_decision_id = policy-decision-final-submit-001
request_id = request-final-submit-001
takeover_id = takeover-final-submit-001
takeover.request_id = request-final-submit-001
takeover.lock_epoch = 2
takeover.state = resumed
takeover.affected_scope.blocking_scope = final_submission
takeover.affected_scope.scope_ref = scope:final-submission
takeover.affected_scope.normalized_action_hash = hash:action-final-submit
takeover.reconciliation_refs = ref:takeover-reconciliation-final-submit
takeover.resumed_by_actor_id = actor-human-reviewer
takeover.resolved_at = 2026-06-12T18:50:00Z
```

The stale continuation rejection maps to `stale_takeover_epoch`. Resume
requires `reconciliation_refs`.

## Evidence And Learning Records

Both host shapes export the same portable proof:

```txt
EvidenceManifest.id = evidence-manifest-research-001
EvidenceManifest.work_session_id = work-session-research-001
EvidenceManifest.event_chain_root = hash:event-final
EvidenceManifest.policy_decision_refs = policy-decision-local-001, policy-decision-external-source-001, policy-decision-final-submit-001
EvidenceManifest.request_refs = request-external-source-001, request-final-submit-001
EvidenceManifest.review_refs = review-external-source-001
EvidenceManifest.takeover_refs = takeover-final-submit-001
EvidenceManifest.contribution_refs = contribution-research-001
EvidenceManifest.export_profile.profile = portable-v0.1
```

Evidence item refs point to source JarvisEvents. They do not expose raw
terminal state, local process state, credentials, raw auth tokens,
provider secrets, host-only database ids, billing data, private scores, UI
state, deployment details, private keys, or raw runtime state.

Learning records preserve the human-agent learning loop:

```txt
LearningRecord.id = learning-record-research-001
LearningRecord.subject_type = pair
LearningRecord.subject_ref = ref:pair:human-worker-researcher:agent-worker-research
LearningRecord.source_event_refs = event-review-external-source-001, event-evidence-export-001
LearningRecord.review_state = accepted

MemoryProposal.id = memory-proposal-source-boundary-001
MemoryProposal.proposed_for = pair
MemoryProposal.review_required = true
MemoryProposal.status = proposed

SkillProposal.id = skill-proposal-source-review-001
SkillProposal.proposed_for = pair
SkillProposal.status = proposed
```

MemoryProposal and SkillProposal records do not silently mutate durable memory
or active skill behavior.

OutcomeReport stays post-session:

```txt
OutcomeReport.id = outcome-report-research-001
OutcomeReport.work_session_id = work-session-research-001
OutcomeReport.source_ref = ref:external-evaluation:research-task
OutcomeReport.reporter_ref = ref:reviewer:external
OutcomeReport.accepted_by_actor_id = actor-human-reviewer
OutcomeReport.outcome = accepted
OutcomeReport.learning_record_refs = learning-record-research-001
```

OutcomeReport does not mutate the sealed WorkSession or EvidenceManifest.

## Public Questions Answered

What happened?

```txt
A human and existing agent completed one evidence-backed WorkSession under
Policy, with one Review-resolution branch and one Takeover-resolution branch.
```

Who acted?

```txt
HumanWorker, AgentWorker, and protocol service Actor records identify every
accepted protocol mutation and Contribution.
```

What did policy allow or block?

```txt
Policy allowed local inspection and drafting, required Review for external
source access and final submission, and denied credential access and external
sends outside approved scope.
```

Where did the agent request human help?

```txt
Request `request-external-source-001` blocked external source access.
Request `request-final-submit-001` blocked final submission until Takeover.
```

What did the human review or take over?

```txt
Review `review-external-source-001` narrowed external source authority.
Takeover `takeover-final-submit-001` transferred direct control over final
submission scope.
```

What evidence proves the work?

```txt
EvidenceManifest `evidence-manifest-research-001` references source events,
PolicyDecisions, Requests, Review, Takeover, Contributions, limitations, and
export profile.
```

What learning carries forward?

```txt
LearningRecord `learning-record-research-001` records pair learning.
MemoryProposal and SkillProposal preserve governed future-work changes.
```

What stays host-owned?

```txt
Native execution, model calls, tool calls, local files, terminal state, process
state, storage, auth, UI, billing, scoring, payment, deployment, and monitoring
stay outside Jarvis records.
```

## Conformance Links

This example is governed by:

- [Compatibility mapping](../conformance/compatibility-mapping.md)
- [Existing-agent compatibility proof plan](../conformance/existing-agent-proof-plan.md)
- [Golden-path conformance entry](../conformance/golden-path.md)
- [Fixture documentation](../conformance/fixtures/README.md)
- [Week 4 Chunk 2 spec](../planning/week-4/chunk-2-compatible-host-mapping.md)

## Done State

This mapping satisfies Chunk 2 when:

- both host shapes produce equivalent Jarvis records
- `host_shape_ref` stays metadata only
- WorkSession-scoped mutations show required headers, Actor authority,
  expected revision, and previous event hash linkage
- AgentWorker actions record PolicyDecision before accepted protocol state
- Request resolves only through Review or Takeover
- Takeover resume requires reconciliation refs
- Contribution remains attributable
- EvidenceManifest excludes forbidden host-private fields
- LearningRecord, MemoryProposal, and SkillProposal stay governed
- OutcomeReport remains post-session feedback without sealed-record mutation
