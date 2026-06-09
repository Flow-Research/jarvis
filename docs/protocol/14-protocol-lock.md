# Protocol Lock

Jarvis is the human-agent collaboration and learning-loop protocol.

It defines how a HumanWorker and an AgentWorker work together under shared
goals and human-defined policy. The protocol records the work, requests,
reviews, takeovers, contributions, evidence, and learning that happen inside a
WorkSession.

This is the v0.1 lock. OpenAPI contract work starts from here.

## Locked Status

`locked-for-v0.1-openapi-draft`

Locked now:

- thesis
- boundary
- vocabulary
- core field classes
- lifecycle
- object relationships
- core states
- conformance expectations
- portable export shape
- version negotiation
- capability negotiation
- extension namespace rules
- protocol error ids
- OpenAPI security entry requirements
- positioning and adoption boundary

Week 2 drafts:

- exact OpenAPI component syntax
- exact OpenAPI path syntax
- OpenAPI examples
- conformance fixtures

## Definition

Jarvis is the protocol for governed human-agent collaboration and shared
learning.

The HumanWorker brings goals, judgment, context, correction, review, taste, and
accountability.

The AgentWorker brings execution, research, planning, drafting, tool use,
memory retrieval, evidence capture, and workflow acceleration.

Jarvis records how both workers collaborate and improve across WorkSessions.

## Thesis

The valuable unit is the human-agent team.

Not the human alone.
Not the agent alone.
Not a chatbot.
Not a runtime.
Not a product workspace.

The HumanWorker improves.
The AgentWorker improves.
The pair improves.
The next WorkSession carries confirmed learning forward.

## Boundary

Jarvis owns:

- protocol vocabulary
- object semantics
- WorkSession lifecycle
- event envelope
- policy decision semantics
- request, review, and takeover semantics
- contribution semantics
- evidence export semantics
- governed learning semantics
- OpenAPI communication binding requirements
- positioning against adjacent protocols and agent products
- conformance expectations

Jarvis does not own:

- agent runtime
- model provider
- cloud provider
- sandbox implementation
- database implementation
- queue implementation
- product UI
- authentication
- billing
- task marketplace
- payment or settlement
- organization workspace internals
- local execution stack

A host implements Jarvis. A host is not Jarvis.

## Vocabulary

The v0.1 vocabulary is:

```txt
Worker
Actor
HumanWorker
AgentWorker
WorkSession
JarvisEvent
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
```

These names are stable for the v0.1 OpenAPI draft.

## Relationship Model

Jarvis models this:

```txt
HumanWorker + AgentWorker
  collaborate inside WorkSession
  under Policy
  through JarvisEvents
  using Requests, Reviews, and Takeovers
  producing Contributions and EvidenceManifest
  generating LearningRecords, MemoryProposals, and SkillProposals
```

Jarvis does not model this:

```txt
User -> Assistant -> Answer
```

Chat is an interface. The protocol is the collaboration record.

## Lifecycle

The v0.1 lifecycle is:

```txt
1. create Worker records
2. create Actor records
3. create HumanWorker
4. create AgentWorker
5. start WorkSession
6. attach Policy
7. record objective
8. assemble context and available capabilities
9. AgentWorker proposes or performs action
10. Policy produces PolicyDecision
11. allowed action records JarvisEvent and evidence
12. denied or review-required action creates Request
13. HumanWorker responds through Review or Takeover
14. approved work resumes inside confirmed or narrowed Policy
15. Contribution records who did what
16. EvidenceManifest records portable proof
17. LearningRecord captures human, agent, or pair learning
18. MemoryProposal and SkillProposal stay governed until reviewed
19. WorkSession completes, fails, or closes
20. portable export is produced
```

Hosts add internal steps. The external Jarvis lifecycle stays intact.

## WorkSession

WorkSession is the source of truth.

States:

```txt
created
active
waiting_on_human
takeover
reconciling
completed
failed
cancelled
closed
```

Rules:

- WorkSession starts with HumanWorker, AgentWorker, objective, and Policy.
- WorkSession keeps an append-only JarvisEvent log.
- WorkSession state changes follow the transition table in
  [04-work-sessions.md](./04-work-sessions.md).
- Every mutating request that affects a WorkSession MUST include
  `Jarvis-Protocol-Version`, `Jarvis-Actor-Id`, `Jarvis-Idempotency-Key`,
  `Jarvis-Request-Timestamp`, `Jarvis-Expected-WorkSession-Revision`, and
  `Jarvis-Previous-Event-Hash`.
- Accepted mutations record the Actor from `Jarvis-Actor-Id`, verify authority,
  enforce `Jarvis-Expected-WorkSession-Revision`, and enforce
  `Jarvis-Previous-Event-Hash`.
- Every accepted mutation increments `revision` and updates `last_event_hash`.
- Missing headers, stale expected revision, or mismatched previous event hash
  reject the mutation.
- WorkSession owns Requests, Reviews, Takeovers, Contributions,
  EvidenceManifest, and LearningRecords.
- Final EvidenceManifest export is valid only from `completed`, `failed`,
  `cancelled`, or `closed`.
- `closed` rejects further mutation except idempotent replay of the same
  accepted request.
- WorkSession export stays free of product-private infrastructure fields.

## PolicyDecision

PolicyDecision gates AgentWorker autonomy.

Results:

```txt
allow
deny
narrow
review_required
```

Rules:

- Every meaningful AgentWorker action records PolicyDecision before acceptance
  as protocol state.
- Policy denies by default.
- Explicit deny beats allow.
- `allow` never creates authority outside selected grants.
- `deny` creates or references Request.
- `review_required` creates or references Request.
- `narrow` creates or references Review or Request before narrowed execution.
- PolicyDecision records `normalized_action_hash`.
- Request, Review, ApprovalScope, Contribution, and EvidenceManifest records
  reference PolicyDecision when they depend on the action.

## Request

Request is structured, scoped deferral from AgentWorker to HumanWorker.

Request is not chat. Request is not a notification. Request is not authority.
Request blocks only its declared scope. Human resolution requires Review or
Takeover. Expiry, cancellation, and supersession close a Request without
granting authority.

States:

```txt
pending
acknowledged
approved
denied
narrowed
answered
takeover
needs_revision
expired
cancelled
superseded
```

Rules:

- Request belongs to one WorkSession.
- Request identifies requester worker and requester actor.
- Request identifies target HumanWorker.
- Request states type, blocking scope, reason, requested action or missing
  context, risk class, options, default behavior when the human does not
  respond, status, creation time, and expiry.
- Human-resolved Request states require Review or Takeover.
- Closed Request states require an append-only JarvisEvent reference.
- Request blocks only its declared scope unless scope is whole WorkSession.
- Expiry applies the safe fallback and never grants new authority.
- Duplicate pending Requests are deduplicated or superseded.
- Invalid Request transitions reject as `invalid_request_transition`.
- Request livelock rejects as `request_livelock`.
- Supersession preserves blocked action hash, PolicyDecision, blocking scope,
  risk, and event references.

## Review

Review records human judgment.

Decisions:

```txt
approve
deny
narrow
correct
takeover
needs_revision
```

Rules:

- Review identifies reviewer worker and reviewer actor.
- Review targets a Request, action, contribution, artifact, memory proposal,
  skill proposal, evidence item, or final outcome.
- Review can resolve a Request.
- Takeover can resolve a Request.
- Review with decision `approve` or `narrow` defines ApprovalScope.
- ApprovalScope binds action hash, approved scope, expiry, WorkSession, Actor,
  Request revision, Request event hash, PolicyDecision, and max uses.
- Review does not silently mutate Policy, memory, skill behavior, or durable
  learning.

## Takeover

Takeover is temporary direct human control.

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

- Takeover creates or increments a lock epoch.
- AgentWorker actions from an old lock epoch reject as `stale_takeover_epoch`.
- Resume requires reconciliation refs.
- Takeover may create or reference LearningRecord, MemoryProposal, or
  SkillProposal records.
- During locked and human_active states, AgentWorker autonomous continuation for
  the affected scope is paused.

## Contribution

Contribution answers who did what.

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

Contributor types:

```txt
human
agent
service
tool
shared
```

Rules:

- Human, agent, service, tool, and shared contributions stay distinguishable.
- Shared contribution does not erase individual actors.
- Shared contribution preserves individual contributor refs.
- Contribution is attribution, not payment or accounting.
- Downstream systems evaluate Contribution records.

## Evidence

EvidenceManifest is the portable proof package for a WorkSession.

It references:

- WorkSession
- event chain root
- artifacts
- evidence items
- policy decisions
- requests
- reviews
- takeovers
- contributions
- limitations
- export profile

Rules:

- Evidence is captured during work.
- Evidence is not reconstructed only at the end.
- Redacted exports stay derived from the same event chain.
- EvidenceManifest is portable across compatible products and hosts.
- Final EvidenceManifest export is valid only from `completed`, `failed`,
  `cancelled`, or `closed`.
- EvidenceManifest excludes product-private fields, credentials, secrets, raw
  runtime state, host-only database ids, deployment details, billing data,
  private scores, and product UI state.

## Learning

LearningRecord captures what improved because of the WorkSession.

Subject types:

```txt
human
agent
pair
```

Rules:

- Learning is not only agent memory.
- Jarvis records human learning, agent learning, and pair learning.
- LearningRecord review states are `proposed`, `accepted`, `rejected`, and
  `superseded`.
- LearningRecord points to MemoryProposal or SkillProposal when learning becomes
  a governed memory or skill change.
- Durable memory and active skill behavior require governed review.
- MemoryProposal states are `proposed`, `pending_review`, `accepted`,
  `rejected`, `superseded`, and `expired`.
- SkillProposal states are `proposed`, `pending_review`, `accepted`,
  `rejected`, `superseded`, and `archived`.
- OutcomeReport is an optional extension that creates or references governed
  LearningRecord without mutating sealed WorkSession or EvidenceManifest.

## Compatibility

Existing agents and products are first-class.

Compatible hosts and adapters map existing agents into AgentWorker records.
They do not replace the agent runtime.

A compatible adapter maps:

```txt
human identity or operator       -> HumanWorker + Actor
agent process or agent product   -> AgentWorker + Actor
agent step                       -> JarvisEvent
tool/action authorization        -> PolicyDecision
blocked action                   -> Request
human approval/correction        -> Review
human direct control             -> Takeover
work performed                   -> Contribution
trace/artifact/source/output     -> EvidenceManifest entry
confirmed improvement            -> LearningRecord / MemoryProposal / SkillProposal
```

If a host cannot expose a native concept, it records the closest valid Jarvis
object with explicit limitations or marks the capability unsupported.

## Conformance

A v0.1-compatible host proves:

- WorkSession is the source of truth.
- HumanWorker and AgentWorker both exist.
- Every meaningful JarvisEvent has an Actor.
- WorkSession invalid transitions are rejected.
- WorkSession stale revision and previous hash mismatches are rejected.
- Policy gates autonomous AgentWorker action.
- Policy-denied or review-required action creates Request.
- Human-resolved Request states are backed by Review or Takeover.
- Expired, cancelled, and superseded states are backed by closure events and
  never grant authority.
- Invalid Request transitions are rejected.
- ApprovalScope rejects stale, mismatched, expired, or over-broad execution.
- Repeated unchanged Requests reject as livelock or supersede without weakening
  policy fields.
- Review decisions are explicit.
- Takeover blocks stale autonomous continuation.
- Takeover resume requires reconciliation refs.
- Contributions are attributable.
- EvidenceManifest is captured during work and exportable.
- Learning is governed.
- MemoryProposal and SkillProposal do not silently become durable behavior.
- OutcomeReport does not mutate sealed WorkSession or EvidenceManifest.
- Portable export contains no product-private infrastructure requirement.

## Portable Export

A v0.1 portable export contains:

```txt
protocol_version
WorkSession
Workers
Actors
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

Extension fields are namespaced. Extensions do not change the meaning of core
protocol fields.

## OpenAPI Contract Work Starts Here

OpenAPI contract work starts with:

1. OpenAPI 3.1 component syntax.
2. OpenAPI 3.1 path syntax.
3. security scheme encoding from
   [15-openapi-communication-binding.md](./15-openapi-communication-binding.md).
4. required and optional fields per object.
5. canonical WorkSession export example.
6. passing and failing conformance fixtures.
7. examples for WorkSession, Request, Review, Takeover, Contribution,
   EvidenceManifest, LearningRecord, MemoryProposal, SkillProposal, and
   OutcomeReport.

The thesis is locked. The object model is locked. The lifecycle is locked. The
control plane is locked. Evidence and learning are locked. OpenAPI security
entry is locked. Positioning is locked.
