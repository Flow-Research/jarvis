# Compatibility Mapping

Jarvis v0.1 compatibility mapping defines how existing human-agent work becomes
Jarvis protocol records.

Jarvis records protocol state. Hosts own native execution.

## Boundary

Compatibility mapping does not add integration code, runtime behavior, UI,
storage, authentication backend, model calls, tool execution, billing, scoring,
payment, or deployment behavior.

Compatible implementations preserve native execution and record the
human-agent collaboration contract around it.

The protocol record MUST stay portable. It MUST NOT contain host-private
fields, credentials, secrets, raw runtime state, host-only database ids,
deployment details, billing data, private scores, UI state, raw auth tokens,
provider secrets, session cookies, or private keys.

## Host Shape Reference

Every Week 3 fixture includes `host_shape_ref`.

Allowed v0.1 fixture shape refs:

```txt
command_line_host_boundary
local_execution_host_boundary
hosted_execution_host_boundary
tool_use_protocol_boundary
```

Rules:

- `host_shape_ref` is fixture metadata only.
- `host_shape_ref` identifies the native execution boundary used by the
  fixture.
- `host_shape_ref` never records host-private behavior.
- `host_shape_ref` never changes the meaning of a Jarvis protocol object.
- `host_shape_ref` MUST NOT appear inside records, operation bodies,
  JarvisEvents, EvidenceManifest, or portable export payloads.
- Two different `host_shape_ref` values prove compatibility only when they
  produce equivalent Jarvis records for the same collaboration loop.

Shape meanings:

```txt
command_line_host_boundary
  records a human-agent loop whose native boundary is a command-line
  interaction

local_execution_host_boundary
  records a human-agent loop whose native boundary is a local workspace or local
  process

hosted_execution_host_boundary
  records a human-agent loop whose native boundary is a hosted service

tool_use_protocol_boundary
  records a human-agent loop whose native boundary includes tool request and
  result protocol records
```

`host_shape_ref` changes no Jarvis record, operation, header, assertion, error
id, or export field.

## Required Mapping

Compatible implementations MUST map this surface:

| Native human-agent surface | Jarvis target | Required protocol proof |
| --- | --- | --- |
| human participant | `Worker`, `HumanWorker`, `Actor` | HumanWorker has Worker ref; Actor records protocol authority |
| agent participant | `Worker`, `AgentWorker`, `Actor` | AgentWorker has Worker ref; Actor records protocol authority |
| work objective | `WorkSession.objective` | WorkSession starts with objective, Policy, revision, and event hash state |
| policy boundary | `Policy` | Policy records allowed, denied, review-required, and request limit rules |
| agent action affecting WorkSession | `PolicyDecision`, `JarvisEvent` | PolicyDecision exists before action becomes accepted protocol state |
| policy-allowed action | `PolicyDecision.result == allow`, `JarvisEvent` | accepted event references actor, revision, and previous event hash |
| policy-denied action | `PolicyDecision.result == deny`, `Request` | Request references PolicyDecision and blocks declared scope |
| review-required action | `PolicyDecision.result == review_required`, `Request` | Request captures reason, risk, options, fallback, expiry, and scope |
| narrowed action | `PolicyDecision.result == narrow`, `Request` or `Review` | narrowed execution stays inside ApprovalScope |
| blocked action | `Request` | Request is scoped deferral, not chat, notification, or authority |
| human approval | `Review`, `ApprovalScope` | Review resolves Request; ApprovalScope binds request id, review id, PolicyDecision, Request revision, Request event hash, action hash, approved action, allowed scope, denied scope, expiry, max uses, WorkSession, and Actor |
| human correction | `Review` | Review records corrected direction and target refs |
| human direct control | `Takeover` | Takeover records lock epoch, blocks stale AgentWorker continuation, and requires reconciliation refs before resume |
| work performed | `Contribution` | Contribution preserves human, agent, shared, service, or tool attribution |
| source, artifact, trace, output | `EvidenceManifest` evidence refs | EvidenceManifest records event chain root, evidence items, PolicyDecisions, Requests, Reviews, Takeovers, Contributions, limitations, export profile, and terminal export state |
| confirmed improvement | `LearningRecord` | LearningRecord subject is human, agent, or pair and references source events |
| memory update proposal | `MemoryProposal` | durable memory stays proposed until governed review accepts it |
| reusable process proposal | `SkillProposal` | active skill behavior stays proposed until governed review accepts it |
| post-session feedback | `OutcomeReport`, `LearningRecord` | OutcomeReport references at least one LearningRecord and does not mutate sealed records |
| unsupported native concept | `limitations` or `unsupported_capability` | portable record states the missing capability or evidence limitation |

## Mapping Order

Compatible implementations MUST create mapped records in this order:

```txt
1. Register Worker records.
2. Register Actor records.
3. Create HumanWorker and AgentWorker records.
4. Start WorkSession with objective, Policy, revision, and event hash state.
5. Record PolicyDecision before AgentWorker action affects protocol state.
6. Append JarvisEvent for accepted protocol state.
7. Create Request for denied, review-required, or blocked scope.
8. Record Review or Takeover for human resolution.
9. Record Contribution for performed work.
10. Capture evidence refs during work from source events and portable artifacts.
11. Record LearningRecord for confirmed human, agent, or pair learning.
12. Record MemoryProposal or SkillProposal when learning changes future work.
13. Submit OutcomeReport only as post-session feedback ingress.
```

The order protects the zero-trust contract. A later record never backfills a
missing PolicyDecision, Request resolution, Contribution actor, evidence event
ref, or governed learning review.

## Object-To-Operation Mapping

Fixtures MUST use OpenAPI operation ids from the v0.1 contract.

Policy, HumanWorker, and AgentWorker are fixture records only in v0.1.
Fixtures MUST NOT invent registration operations for them.

Accepted mutation operations that create protocol state record
`expected_event_ref` with the id of the JarvisEvent produced by that operation.
Fixtures MUST NOT duplicate that produced event with a separate
`appendJarvisEvent` operation. `appendJarvisEvent` maps direct event append
operations whose request body is a JarvisEvent.

```txt
Worker            -> registerWorker
Actor             -> registerActor
WorkSession       -> createWorkSession
JarvisEvent       -> appendJarvisEvent
PolicyDecision    -> recordPolicyDecision
Request           -> createRequest
Review            -> recordReview
Takeover          -> recordTakeover
Contribution      -> recordContribution
LearningRecord    -> createLearningRecord
MemoryProposal    -> createMemoryProposal
SkillProposal     -> createSkillProposal
EvidenceManifest  -> exportEvidenceManifest
OutcomeReport     -> submitOutcomeReport
```

## Mutation Header Mapping

WorkSession-scoped mutating operations MUST include:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

`POST /work-sessions` is the genesis WorkSession mutation. It MUST use
`Jarvis-Expected-WorkSession-Revision` set to `0` and
`Jarvis-Previous-Event-Hash` set to the protocol genesis hash.

Non-WorkSession protocol mutations MUST include:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
```

Worker registration, Actor registration, and OutcomeReport submission are
non-WorkSession protocol mutations. They do not require
`Jarvis-Expected-WorkSession-Revision` or `Jarvis-Previous-Event-Hash`.
They MUST verify Actor authority, idempotency, protocol version, and timestamp
before state changes.

WorkSession-scoped reads and export reads require `Jarvis-Protocol-Version`,
`Jarvis-Actor-Id`, and valid Actor authority. They do not require
mutation-only headers.

## Unsupported Native Concepts

Compatible implementations MUST NOT invent evidence, authority, contribution,
learning, or review state when source records lack portable proof.

When a native concept has no valid Jarvis mapping, the implementation records
one of these outcomes:

```txt
limitations
unsupported_capability
```

`limitations` records missing or weakened portable proof in the
EvidenceManifest when the limitation concerns evidence export, or in the
protocol record that carries the unsupported mapping.

`unsupported_capability` rejects a required capability that the implementation
does not support.

Unsupported native concepts never weaken required protocol gates. A missing
native trace does not remove PolicyDecision, Request, Review, Takeover,
Contribution, EvidenceManifest, or LearningRecord requirements.

## Compatibility Assertions

Week 3 fixtures MUST assert:

```txt
host_shape_ref is present
host_shape_ref uses an allowed v0.1 value
host_shape_ref does not contain host-private behavior
all required native surfaces map to Jarvis protocol targets
AgentWorker action affecting WorkSession has PolicyDecision before accepted state
PolicyDecision.result deny or review_required includes request_id
Request.policy_decision_id matches the blocking PolicyDecision
blocked scope creates Request
human resolution uses Review or Takeover
resolved Request states include the required resolver ref
Review approve or narrow includes bounded ApprovalScope
ApprovalScope binds request, review, PolicyDecision, action hash, actor, WorkSession, expiry, and max uses
Takeover rejects stale AgentWorker continuation
Takeover resume requires reconciliation refs
Contribution preserves actor attribution
Contribution contributor_refs point to valid Worker and Actor records
evidence refs are captured during work
EvidenceManifest records event chain root, evidence items, PolicyDecisions, Requests, Reviews, Takeovers, Contributions, limitations, export profile, and terminal export state
Every EvidenceItemRef has nonempty source_event_refs
LearningRecord captures human, agent, or pair learning
unsupported native concept maps to limitations or unsupported_capability
unsupported_capability applies only to unsupported required capabilities
missing optional proof records limitations
portable export excludes forbidden host-private fields
```

## Rejection Mapping

Compatibility fixtures use these rejection ids when mapping fails:

```txt
missing_actor
missing_protocol_version
missing_idempotency_key
missing_request_timestamp
stale_request_timestamp
missing_expected_work_session_revision
missing_previous_event_hash
unauthorized_actor
missing_objective
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
shared_contribution_without_individual_refs
duplicate_contributor_ref
evidence_after_the_fact
missing_evidence_event_refs
duplicate_evidence_item_ref
invalid_evidence_export_state
forbidden_host_private_field
silent_memory_mutation
silent_skill_activation
sealed_work_session_mutation
sealed_evidence_mutation
outcome_report_without_learning_record
unsupported_capability
```

The fixture uses one primary rejection id per invalid case.

## Done State

Compatibility mapping is complete for v0.1 when:

- every required native surface has a Jarvis protocol target
- every unsupported native concept records `limitations` or rejects as
  `unsupported_capability`
- host-owned execution remains outside portable protocol records
- fixture `host_shape_ref` values stay host-private-free
- Week 3 valid and invalid fixtures use this mapping as their source
