# Autonomy And Policy

Jarvis defines policy-governed AgentWorker autonomy.

The HumanWorker defines boundaries. The AgentWorker operates inside them. When
the AgentWorker needs something outside them, it creates a request.

## Autonomy Levels

```txt
observe_only
  inspect and summarize only

propose_only
  propose plans/actions but do not execute

execute_with_review
  run allowed actions, require review for outputs or external effects

bounded_execute
  complete bounded work using granted tools and scope

full_execute_in_scope
  complete the objective independently within explicit limits
```

Autonomy is set at multiple levels:

- AgentWorker default
- HumanWorker + AgentWorker relationship default
- WorkSession
- project/workspace
- tool
- skill
- risk class

## Capability Grants

A capability grant gives the AgentWorker permission to act inside a scope.

```txt
grant
  actor
  capability/tool/tool group
  risk class
  scope
  duration
  budget/rate limits
  review requirement
  created_by
  created_at
  revocation state
```

Examples:

- read local project files
- write files under a workspace path
- run host-provided execution tools under policy
- access selected public hosts
- call a read-only MCP tool
- create drafts but not send them

## Grant Resolution

Every action must bind to an active grant or be denied.

Resolution rules:

- deny by default
- explicit deny beats allow
- expired or revoked grants cannot be used
- scopes are intersected, not unioned
- every action is authorized as a vector
- every risk class, data sensitivity, resource scope, host, credential scope,
  and side-effect class must be covered
- the most restrictive matching grant is selected for each covered dimension
- uncovered dimensions deny the action
- higher sensitivity data raises required review level
- every allow/deny decision records selected grant ids by dimension or denial
  reason

If grants conflict, the resolver denies the action and emits a request with the
conflicting grants, requested action, narrowed safe alternative, and required
approver. The resolver never guesses by model judgment.

## PolicyDecision Results

Every meaningful AgentWorker action records a PolicyDecision before the action
is accepted as protocol state.

PolicyDecision results are:

```txt
allow
  Action is inside Policy and selected grants.

deny
  Action is outside Policy or explicitly denied. The blocked scope cannot
  continue.

narrow
  Action continues only inside a smaller approved scope.

review_required
  Action is covered only after HumanWorker Review or Takeover.
```

Rules:

- Policy denies by default.
- Explicit deny beats allow.
- Uncovered action dimensions deny execution.
- `allow` never creates authority beyond selected grants.
- `deny` creates or references Request.
- `review_required` creates or references Request.
- `narrow` creates or references Review or Request before narrowed execution.
- Every PolicyDecision records `normalized_action_hash`.
- Request, Review, ApprovalScope, EvidenceManifest, and Contribution records
  reference the PolicyDecision when they depend on that decision.
- Missing PolicyDecision rejects AgentWorker action as
  `missing_policy_decision`.

## Risk Classes

```txt
read_public
  inspect public/non-sensitive data

read_private
  inspect private workspace, account, or user data

write_local
  change workspace/sandbox state

network_fetch
  contact external hosts without sending private data intentionally

data_export
  move private WorkSession or workspace data outside the approved boundary

execute
  run code or commands

send_external
  send data or messages outside the approved boundary

credentialed
  use secrets, tokens, accounts, or delegated identity

public_publish
  publish, post, submit, merge, deploy, or otherwise expose work publicly

financial
  spend, transfer, purchase, price, or trigger payment-affecting actions

privilege_change
  alter auth, grants, memberships, credentials, or permissions

destructive
  delete, publish, deploy, spend, merge, revoke, or perform irreversible action

background_recurring
  schedule repeated or unattended future work
```

Tools carry one or more risk classes.

## Request Types

```txt
permission
  agent needs a capability not granted

context
  agent needs missing information

judgment
  agent needs human judgment

correction
  agent needs human correction because direction, evidence, or requirement
  interpretation conflicts

review
  agent completed work that requires inspection

takeover
  agent determines the human must continue directly

escalation
  agent detects risk, ambiguity, policy conflict, or high-impact action
```

## Request Payload

A Request includes:

```txt
reason
proposed action
risk class
blocking scope
requested scope
expected result
alternatives
default if no response
expiration
work_session_id
evidence/context
```

The policy engine generates canonical request fields. Model-written prose
explains intent only; it never defines risk.

Canonical fields include:

- request_id
- request_version
- canonical_action_hash
- requested_grant_hash
- authorized_approver_ids
- request state
- exact command/API/tool call when known
- files touched
- hosts contacted
- secrets or credentials requested
- data that leaves or is able to leave the approved boundary
- irreversible effects
- requested grant scope and expiry
- narrower alternatives
- default if no response

The human response is one of:

```txt
approve
deny
narrow
correct
takeover
needs_revision
```

Approvals are one-use decisions bound to approver, request version, expiry,
WorkSession, declared blocking scope, and canonical action hash. Request
resolution uses compare-and-set from unresolved state to resolved state. Stale,
replayed, or mismatched approvals are rejected.

Approval does not mutate Policy. Approval creates bounded authority through
ApprovalScope. Durable Policy changes are outside v0.1 mutation semantics unless
they are represented through governed LearningRecord, MemoryProposal, or
SkillProposal records for future work.

## Request Surface Boundary

Hosts surface Requests through any host-owned interface.

Jarvis owns Request state, Review resolution, Takeover transition, and the
event record. Jarvis does not define a host inbox surface.

Request records carry the protocol fields hosts need to represent a blocker:

- why the agent paused
- what policy blocked it
- what the agent wants to do
- what approving allows
- what the risks are
- what scope/duration is requested
- what alternatives exist

## Takeover

Takeover means:

```txt
agent pauses or lowers autonomy
human continues the work
human edits artifacts or runs actions
agent observes the correction
the WorkSession records the difference
agent resumes with updated context after reconciliation
```

When Takeover changes future WorkSession behavior, compatible implementations
record that change through LearningRecord, MemoryProposal, or SkillProposal
operations. Takeover does not silently mutate durable learning.

Takeover has protocol locking semantics:

- record the affected WorkSession scope
- increment the WorkSession lock epoch
- reject stale AgentWorker continuation for the affected scope
- record HumanWorker edits as protocol events or artifact refs
- require reconciliation refs before AgentWorker autonomy resumes

Every Takeover creates a WorkSession lock epoch. Compatible implementations
MUST reject AgentWorker continuation from an older lock epoch as
`stale_takeover_epoch`.

Takeover follows the locked state machine in
[12-request-protocol.md](./12-request-protocol.md).

During `locked` and `human_active`, AgentWorker autonomous continuation for the
affected scope is paused. Resume requires a reconciliation event.

Takeover states map to the protocol state machine in
[12-request-protocol.md](./12-request-protocol.md). Resume requires
reconciliation refs before AgentWorker autonomy continues.

## PolicyDecision Points

Jarvis records PolicyDecision before an AgentWorker action is accepted as
protocol state for:

- capability visibility
- tool action
- command action
- resource mutation
- network action
- external effect
- memory write
- skill update
- final or irreversible action

Jarvis records evidence, risk, and learning classifications as protocol state.

## Tool Policy Records

Hosts own tool wrapping and tool execution. Jarvis records policy state for
tool use that affects a WorkSession.

Jarvis records:

- tool ref
- requested action
- requested scope
- data sensitivity
- risk class
- PolicyDecision
- Request when blocked
- Review when required
- evidence refs
- output trust label

## External Effect Records

Any AgentWorker action that sends, publishes, submits, deploys, spends, merges,
or exposes data outside the approved WorkSession or host boundary requires
protocol-visible authorization before the action is accepted as protocol state.

Jarvis records:

- external effect type
- payload or artifact ref
- recipient ref when applicable
- tool ref when applicable
- data sensitivity
- risk class
- PolicyDecision
- approval scope when approved
- Review when human judgment is required
- evidence receipt refs

The action remains blocked until the required PolicyDecision, Request, Review,
or Takeover state permits it. Jarvis does not define outbox architecture,
commit tokens, send tokens, delivery mechanisms, or host execution mechanics.

## Credential Exposure Records

Hosts own secret handling. Jarvis records credential exposure decisions as
protocol state when credentials affect a WorkSession.

Jarvis credential-related records include:

- credential source ref
- requested capability
- requested credential scope
- Actor requesting use
- PolicyDecision
- Review when required
- approval scope
- expiry
- evidence refs
- redaction state

Compatible implementations MUST NOT expose raw credentials in Jarvis protocol
records.

Jarvis does not define secret-handling architecture, token format, process
environment behavior, log redaction implementation, or network enforcement.

## Execution Context Records

Hosts own execution systems and isolation. Jarvis records the execution
context refs and policy refs that affect a WorkSession:

- execution context ref
- resource scope ref
- network policy ref
- command policy ref
- dependency policy ref
- credential exposure policy ref
- artifact export policy ref

If the AgentWorker needs a blocked host, secret, package, or external action,
it creates a Request.

Jarvis records:

- execution context ref
- resource scope ref
- network policy ref
- command policy ref
- dependency policy ref
- credential exposure policy ref
- artifact export policy ref
- PolicyDecision
- evidence refs

Jarvis does not define host execution or isolation mechanics.

## Failure Modes

- too many requests causing human fatigue
- over-broad grants
- hidden prompt injection in tool outputs
- unsafe MCP tool metadata
- approval messages that hide real risk
- agent continuing after policy pauses it

Policy decisions must be inspectable: why allowed, why blocked, who approved,
what scope, what evidence.

## Tamper-Evident Audit

Every policy decision creates a `PolicyDecision` and a corresponding
`JarvisEvent`:

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
result
reason
request_id
evidence_refs
created_at
```

Events are sequenced and hash-linked in the host's durable record. Hosts that
cannot support hash-linked audit records mark audit integrity as degraded.

Degraded audit integrity automatically denies `credentialed`, `send_external`,
`public_publish`, `financial`, `destructive`, `privilege_change`,
`background_recurring`, and high-autonomy modes. Jarvis allows only
observe-only, propose-only, or scratch-local work until audit integrity is
restored.

## Policy Profile Records

Jarvis records policy profile refs. Hosts own policy profile implementation.

```txt
observe_only
  observation-only protocol records

research_only
  research actions require declared policy refs

bounded_local_work
  local work actions require declared policy refs

workspace_write
  workspace mutation actions require declared policy refs

host_execution_bounded
  host-owned execution actions require declared policy refs
```

Compatible implementations start with explicit policy refs. Durable Policy
changes are outside v0.1 mutation semantics unless they are represented through
governed LearningRecord, MemoryProposal, or SkillProposal records for future
work.

## Policy Evolution

Repeated successful reviews inform future Policy changes. v0.1 records that
signal through governed LearningRecord, MemoryProposal, or SkillProposal
records. Hosts own durable Policy storage and evolution outside the protocol
mutation surface.

Jarvis does not silently expand autonomy from derived performance signals.
