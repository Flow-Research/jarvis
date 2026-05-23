# Runtime Adapters

Jarvis is runtime-agnostic by contract and Cloudflare-first by implementation.

## Runtime-Neutral Concepts

```txt
AgentInstance
  durable execution identity for an agent

WorkSessionRun
  one runtime execution attempt inside a WorkSession

Workspace
  files/state visible to a WorkSession run through a runtime adapter

SandboxLease
  bounded execution environment with policy

BackgroundJob
  scheduled or resumable work
```

These are runtime-neutral concepts. Each adapter maps them to its own
infrastructure.

## Runtime Responsibilities

A runtime adapter provides:

```txt
durable actor identity
durable session state
message/event persistence
context snapshot storage
Jarvis-materialized prompt delivery to the model/tool loop
tool invocation runtime
workspace/files
sandboxed command/code execution
scheduled/background work
streaming updates
request/resume support
runtime health/debug surface
run leases
checkpoints
idempotent execution support
```

## Cloudflare Reference Runtime

The Cloudflare reference implementation provides:

- Agents and Durable Objects for persistent actors
- Think for low-level session/message persistence, streaming, model/tool loop
  mechanics, checkpoints, and recovery
- Workspace for durable files and state
- R2 for larger artifacts and skill bundles
- Sandbox/Containers for real command execution
- Worker Loader, codemode, and shell execution plumbing
- alarms/fibers for resumable background work
- service bindings for internal service boundaries

This supplies the production runtime substrate without forking Cloudflare.

## Cloudflare Adapter Shape

```txt
JarvisHost
  runtime actor mapped to one HumanAgentPair
  owns pair-level routing and shared runtime configuration
  does not own Jarvis collaboration semantics

JarvisWorkSessionActor
  runtime actor mapped to one WorkSession or active WorkSessionRun
  owns the runtime/internal Session, workspace binding, leases, checkpoints,
  and streaming
  invokes Jarvis kernel services for context, policy, tools, events, evidence,
  and learning

JarvisSandbox
  Cloudflare Sandbox/Container with Jarvis policy controls

JarvisStores
  memory, skill, event, request, and evidence stores backed by Cloudflare
  primitives or external stores
```

Names are implementation details. The responsibility split is fixed.

## Runtime Ports And Kernel Services

Runtime ports are infrastructure:

```txt
SessionStore
EventStore
WorkspaceStore
SandboxExecutor
TurnRunner
ToolInvocationRuntime
StreamSink
CheckpointStore
LeaseManager
BackgroundJobRunner
ModelProvider
RequestStore
NotificationSink
```

Kernel services are Jarvis semantics:

```txt
PolicyEngine
ContextAssembler
MemorySelector
LearningWorker
SkillResolver
ToolClassifier
GrantResolver
EvidenceBuilder
```

Cloudflare implements runtime ports first. Jarvis owns kernel services.

## Local Development Runtime

The open-source distribution includes a local development runtime profile. It
does not need parity with Cloudflare, but it runs the core harness without
Cloudflare setup.

A local runtime maps the same ports to:

- SQLite
- local filesystem
- Docker or namespace-isolated sandbox
- local process manager
- local MCP servers
- SSE streaming
- local scheduler

Minimum local/dev profile:

- SQLite event/request/checkpoint store
- local filesystem workspace
- Docker or namespace-isolated sandbox behind strict policy
- simple scheduler
- SSE/WebSocket stream
- local model/provider configuration

The local runtime exists for development, testing, examples, and self-hosted
experimentation. The Cloudflare runtime remains the production-grade reference
implementation.

Host shell execution does not satisfy autonomous execution requirements. A
runtime using host shell marks integrity as degraded and restricts execution to
`observe`, `suggest`, or explicit human-run commands with no credentials, no
background execution, and no private workspace writes.

## Adapter Rules

- Kernel primitives do not import Cloudflare types.
- Cloudflare adapter explicitly uses Cloudflare names.
- Interfaces talk to Jarvis APIs, not Cloudflare internals.
- Raw runtime tools must not bypass Jarvis policy.
- Runtime debug exposes sessions, tools, memory context, requests,
  sandbox state, and event logs.

## Observability

Agents are hard to debug. Runtime adapters expose:

- current session state
- loaded context blocks
- selected memories
- visible tools
- policy decisions
- pending requests
- recent tool calls
- sandbox health
- event log
- learning proposals

Every debug/export surface must apply redaction:

- secrets never shown
- private memory scoped by caller
- tool outputs labeled by trust
- credential use summarized
- exported traces scrubbed by default

Debug export is denied by default for private memory, credentials, tool
outputs, and sandbox transcripts unless the caller has explicit inspect grants.
Redaction is applied before persistence to exported traces, not only at display
time.

## Trace Context

Every event, tool call, request, policy decision, memory retrieval, and learning
proposal carries trace context:

```txt
work_session_id
run_id
turn_id
actor_id
tool_call_id when applicable
policy_decision_id when applicable
memory_selection_id when applicable
correlation_id
```

This gives developers traceable runtime behavior across logs.

Inspectability is a runtime requirement.
