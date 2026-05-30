# Autonomy And Policy

Jarvis lets the AgentWorker work without human babysitting.

The HumanWorker defines boundaries. The AgentWorker operates inside them. When
the AgentWorker needs something outside them, it creates a request.

## Autonomy Levels

```txt
observe
  inspect and summarize only

suggest
  propose plans/actions but do not execute

execute_with_review
  run allowed actions, require review for outputs or external effects

bounded_autonomy
  complete bounded work using granted tools and scope

full_autonomy_in_scope
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

decision
  agent needs human judgment

review
  agent completed work that requires inspection

takeover
  agent determines the human must continue directly
```

## Request Payload

A request includes:

```txt
reason
proposed action
risk class
requested scope
expected result
alternatives
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
- data that leaves or can leave the harness
- irreversible effects
- requested grant scope and expiry
- narrower alternatives

The human response is one of:

```txt
approve
deny
approve with narrower scope
answer with context
edit the plan
take over
resume/delegate back to agent
```

Approvals are one-use decisions bound to approver, request version, expiry,
WorkSession, and canonical action hash. Request resolution uses compare-and-set
from `pending` to `resolved`. Stale, replayed, or mismatched approvals are
rejected.

## Inbox Semantics

Inbox is the deferred control plane for autonomy.

An inbox item explains:

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
Jarvis records the difference
agent resumes with updated context after reconciliation
```

Takeover is a learning event. Jarvis inspects what changed and proposes
memory or skill updates.

Takeover also has locking semantics:

- acquire a WorkSession/workspace lock
- pause background execution for the session
- cancel or quarantine pending tool calls
- freeze unresolved requests until the human resolves or discards them
- record human edits as authoritative events
- require reconciliation before agent autonomy resumes

Every takeover creates a WorkSession lock epoch. Every tool call,
host-issued action token, background job, memory write, skill update, and
outbox token carries the current epoch and re-checks it at commit. Takeover
increments the epoch, revokes outstanding tokens, and moves unknown in-flight
effects into reconciliation.

Takeover state machine:

```txt
takeover_requested -> locked -> human_active -> reconciliation_required -> resumed | closed
```

During `locked` and `human_active`, no agent tool calls, background jobs,
outbox commits, memory writes, or skill updates execute. Pending actions are
canceled if not started, quarantined if result is unknown, and receipted if
completed. Resume requires a reconciliation event.

## Policy Evaluation Points

Policy runs:

- before tool exposure
- before tool execution
- before command execution
- before filesystem writes
- before network access
- before external sends
- before memory writes
- before skill updates
- before final or irreversible actions

Policy also runs after execution to classify evidence, risk, and learning
signals.

## Policy-Wrapped Tools

The agent receives policy-wrapped tools, not raw dangerous tools.

Wrappers:

- filter arguments
- restrict hosts/paths/scopes
- redact secrets
- require approval when needed
- emit requests
- record evidence
- inspect outputs for untrusted content
- produce audit events

## External Send Outbox

Any action that sends, publishes, submits, deploys, spends, merges, or exposes
data outside Jarvis uses a two-phase outbox:

```txt
draft
  agent prepares exact payload, recipient, command, diff, or artifact

classified
  policy classifies risk, data sensitivity, credentials, and irreversible effects

reviewed
  human approval or materialized send authorization is attached

committed
  host receives a one-time send token and performs the action

receipted
  immutable send receipt is appended to evidence
```

The model never silently sends external effects through raw
tools.

No tool sends, publishes, submits, deploys, spends, merges, or exports outside
Jarvis except through the outbox. Approval binds to payload hash, recipient,
tool id, credential scope, and expiry. Any payload, recipient, credential, or
tool change invalidates approval. Commit uses a one-time token and idempotency
key.

Pre-approved send grants are templates. Before commit, Jarvis materializes a
`SendAuthorization` bound to canonical payload hash, recipient, tool id,
credential scope, data classification, expiry, and idempotency key. Jarvis
requires explicit review for `public_publish`, `financial`, `destructive`, and
`privilege_change` unless the template enumerates the exact safe action class.

## Credential Broker

Credentials are brokered, not exposed.

Rules:

- no raw secret reveal to the model
- raw credentials are never injected into model-visible or command-readable
  environments
- no long-lived secret injection by default
- non-extractable broker handles or broker-executed operations
- tool-bound scoped tokens only when extraction risk is eliminated by host
  controls
- short expiry
- redaction in logs and debug views
- no env dump
- per-use audit
- egress restrictions tied to credential scope
- explicit review for new credential/tool combinations

Jarvis never places raw secrets or bearer tokens inside arbitrary
command-readable state. If a token enters a sandbox, it is single-use,
audience-bound, operation-specific, short-lived, no-readback, and paired with
network restrictions. Jarvis assumes stdout and stderr can leak anything visible
to the command. General env-var secret injection is not a Jarvis default.

## Execution Environment Policy

When a host provides an execution environment, Jarvis policy defines the limits:

- filesystem scope
- network mode
- selected allowed hosts
- private network deny list
- command timeout
- package install policy
- credential exposure policy
- artifact export policy

If the agent needs a blocked host, secret, package, or external action, it asks.

Default sandbox posture:

- execution environment lifecycle is ephemeral per WorkSession unless a
  workspace persistence grant exists
- no host filesystem access
- workspace-scoped mounts
- source files read-only unless write grant exists
- writes go to working directories unless explicitly granted
- network starts denied
- private IP and metadata hosts denied
- DNS/host allowlists are grant-scoped and expire
- package installs quarantined and recorded
- artifact export goes through outbox/export review unless pre-granted
- risky execution tears down automatically after evidence capture

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
observe/suggest or scratch-local work until audit integrity is restored.

## Default Policy Profiles

Jarvis ships safe presets:

```txt
observe
  read-only summaries, no execution

research_only
  public fetches through approved tools, no private data export

local_dev_safe
  read project, write scratch/work dirs, run approved commands, no external send

workspace_write
  modify workspace files with review for broad/destructive changes

sandbox_autonomous
  run commands and write artifacts inside a bounded execution environment
```

Developers start with presets and tighten or extend them.
