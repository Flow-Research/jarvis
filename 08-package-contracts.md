# Package Contracts

Jarvis v0.1 ships as a small package graph. Each package has a fixed ownership
boundary, allowed imports, forbidden imports, and release tests.

## Package Graph

```txt
@jarvis/core
  no Jarvis package dependencies

@jarvis/memory
  depends on @jarvis/core

@jarvis/policy
  depends on @jarvis/core

@jarvis/skills
  depends on @jarvis/core, @jarvis/memory, @jarvis/policy

@jarvis/tools
  depends on @jarvis/core, @jarvis/policy

@jarvis/runtime-local
  depends on all kernel packages

@jarvis/runtime-cloudflare
  depends on all kernel packages and Cloudflare SDK/runtime libraries
```

Kernel packages never import runtime packages. Runtime packages import kernel
packages and implement runtime ports.

## `@jarvis/core`

Owns the domain contracts:

- Actor
- HumanProfile
- AgentProfile
- Worker
- HumanWorker
- AgentWorker
- WorkSession
- WorkSessionRun
- runtime/internal Session reference type
- Request
- Review
- Contribution
- EvidenceManifest
- EvidenceItem
- event envelope
- trace context
- error envelope

Exports:

```txt
ids
domain records
event types
WorkSessionStatus
RunStatus
RequestStatus
ReviewDecision
ContributionType
EvidenceManifest
TraceContext
JarvisError
```

Forbidden imports:

- Cloudflare runtime types
- local filesystem libraries
- database clients
- model SDKs
- MCP SDKs

Release tests:

- JSON serialization is stable.
- Event envelopes validate required ids and timestamps.
- WorkSession status transitions reject invalid transitions.

## `@jarvis/memory`

Owns durable memory semantics:

- memory record schema
- memory scopes
- memory lifecycle
- provenance
- taint/trust labels
- context manifest
- retrieval policy
- correction pipeline
- memory write matrix

Exports:

```txt
MemoryRecord
MemoryScope
MemoryLifecycleState
MemoryTrustLabel
MemoryWriteProposal
ContextManifest
MemorySelector
MemoryStorePort
```

Forbidden imports:

- runtime packages
- model provider packages
- interface packages

Release tests:

- model-derived memory cannot confirm itself.
- untrusted tool output cannot become durable memory without policy approval.
- project memory never leaks into another project scope.

## `@jarvis/policy`

Owns autonomy and safety:

- autonomy levels
- grants
- risk classes
- grant vector resolution
- request creation
- approval tokens
- takeover lock epochs
- outbox protocol
- credential broker contracts
- audit events

Exports:

```txt
PolicyEngine
GrantResolver
CapabilityGrant
RiskClass
PolicyDecisionEvent
RequestFactory
ApprovalToken
SendAuthorization
TakeoverLock
CredentialBrokerPort
```

Forbidden imports:

- runtime packages
- raw tool implementations
- interface packages

Release tests:

- uncovered action dimensions deny execution.
- conflicting grants deny and create a request.
- stale approval tokens cannot resolve a request.
- degraded audit integrity blocks high-risk modes.

## `@jarvis/skills`

Owns procedural memory:

- skill manifest
- skill inventory
- skill activation gates
- skill versioning
- skill learning proposals
- skill bundle verification

Exports:

```txt
SkillManifest
SkillInventory
SkillResolver
SkillActivationGate
SkillUpdateProposal
SkillBundleRef
```

Forbidden imports:

- runtime packages
- raw connector SDKs

Release tests:

- unreviewed skill updates stay inactive.
- changed skill bundle hashes require classification.
- activation gates block skills outside their scope.

## `@jarvis/tools`

Owns policy-wrapped tools:

- tool manifest
- tool registry
- MCP gateway
- sandbox tool contracts
- tool trust labels
- tool failure records
- tool inventory diffing

Exports:

```txt
ToolManifest
ToolRegistry
PolicyWrappedTool
ToolTrustLabel
ToolInvocationRecord
McpGateway
McpCapabilityInventory
SandboxToolContract
```

Forbidden imports:

- runtime packages
- Cloudflare runtime types

Release tests:

- raw tools cannot bypass policy wrappers.
- MCP capability changes enter quarantine.
- raw MCP prompts/resources never become instruction authority.

## `@jarvis/runtime-local`

Owns the default local runtime:

- SQLite stores
- local filesystem workspace
- Docker or namespace-isolated sandbox execution
- local scheduler
- SSE event streaming
- local model provider configuration
- file-backed Jarvis project config

Exports:

```txt
createJarvisLocalRuntime
LocalRuntimeConfig
LocalRuntimeStores
LocalSandboxRuntime
LocalEventStream
```

Forbidden imports:

- Cloudflare runtime types

Release tests:

- scaffold starts locally.
- WorkSession resumes after process restart.
- pending requests survive restart.
- evidence manifest exports from local storage.

## `@jarvis/runtime-cloudflare`

Owns the production reference adapter:

- Cloudflare Agents and Durable Objects mapping
- Think integration
- Workspace integration
- Sandbox/Container integration
- R2 artifact storage
- Worker Loader/codemode/shell integration
- service bindings
- alarms/background work

Exports:

```txt
createJarvisCloudflareRuntime
CloudflareRuntimeConfig
JarvisHost
JarvisWorkSessionActor
CloudflareStores
CloudflareSandboxRuntime
```

Forbidden ownership:

- memory semantics
- policy semantics
- skill lifecycle semantics
- evidence semantics
- request/review semantics

Release tests:

- Cloudflare adapter invokes kernel services for context, policy, tools,
  events, evidence, and learning.
- kernel packages import no Cloudflare types.
- runtime debug surfaces apply Jarvis redaction rules.
