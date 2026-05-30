# Jarvis Roadmap

Jarvis is the open-source human-agent collaboration protocol. The roadmap turns
the architecture into buildable releases.

The first release proves one thing: a human and an autonomous agent can work
together through shared memory, governed autonomy, requests, reviews, evidence,
and resumable WorkSessions without requiring a product interface or Cloudflare
account.

## Roadmap Contract

Jarvis v0.1 delivers the protocol implementation, not a product shell.

Jarvis owns:

- HumanWorker
- AgentWorker
- WorkSession
- memory and learning
- policy and autonomy
- requests, reviews, and takeover
- skills and policy-wrapped tools
- evidence and contribution records
- runtime adapter contracts
- local development runtime

Jarvis does not own product interface, external work ownership, external
identity ownership, or enterprise workspace ownership.

Cloudflare remains the first-class production runtime. The local runtime exists
so developers can install, inspect, test, and extend Jarvis without production
infrastructure.

## Release Strategy

```txt
v0.1 Local Alpha
  buildable open-source protocol implementation with local runtime

v0.2 Cloudflare Runtime Beta
  production reference adapter using Cloudflare primitives

v0.3 Connector And Skill Ecosystem
  stronger MCP, skill bundles, examples, and runtime extension points

v1.0 Stable Protocol
  stable public API, runtime adapter contract, policy model, and migration path
```

## v0.1 Local Alpha

Goal: ship the smallest complete Jarvis that proves the human-agent loop.

Exit condition:

```txt
npm create jarvis@latest my-jarvis
cd my-jarvis
npm install
npm run test
npm run jarvis:dev
npm run jarvis:session -- --objective "Inspect this project and propose a plan"
```

The run creates a HumanWorker and AgentWorker, starts a WorkSession, streams
events, blocks a policy-denied action, creates a structured Request, accepts a
scoped approval, resumes work, records contributions and evidence, proposes
learning, and exports an EvidenceManifest.

### v0.1 Must-Have Slice

v0.1 includes only the golden-path subset of each system:

- one HumanWorker
- one AgentWorker
- one active WorkSession at a time per local project
- one local SQLite store
- one local filesystem workspace
- one SSE event stream
- one default policy profile: `local_dev_safe`
- one request flow: blocked action to scoped approval to resume
- one memory path: seed memory, context manifest, learning proposal
- one skill path: local skill manifest loaded through activation gates
- one tool path: policy-wrapped local sandbox command
- one MCP path: capability inventory capture and quarantine only
- one evidence path: JSON EvidenceManifest plus referenced artifacts
- one CLI path matching the TypeScript golden path

v0.1 excludes:

- multi-user collaboration
- recurring background jobs
- hosted UI
- remote artifact replication
- external skill registry
- Cloudflare production runtime implementation
- hosted connector catalog
- billing, reward, or attribution settlement

The Cloudflare runtime package exists in v0.1 as a contract stub only. The
implementation begins in v0.2.

### Milestone 0: Architecture Lock

Owner: Architecture

Supports: Kernel, Policy And Safety, Runtime, Developer Experience

Output:

- design docs remain in `/home/abiorh/flow/jarvis-design`
- architecture contract is frozen for v0.1
- package graph is frozen
- public WorkSession API names are frozen
- local runtime defaults are frozen
- acceptance tests are frozen

Done when:

- [README.md](./README.md), [08-package-contracts.md](./08-package-contracts.md),
  [09-default-project.md](./09-default-project.md), and
  [10-local-runtime-mvp.md](./10-local-runtime-mvp.md) agree
- no v0.1 package invents new ownership outside its contract

### Milestone 1: Repository And Package Scaffold

Owner: Developer Experience

Supports: Kernel, Runtime

Output:

- monorepo initialized
- packages created:
  - `@jarvis/core`
  - `@jarvis/memory`
  - `@jarvis/policy`
  - `@jarvis/skills`
  - `@jarvis/tools`
  - `@jarvis/runtime-local`
  - `@jarvis/runtime-cloudflare` contract stub
- dependency boundaries enforced
- shared build, typecheck, test, and lint commands exist
- generated scaffold package exists as `create-jarvis`

Done when:

- kernel packages import no runtime packages
- kernel packages import no Cloudflare types
- runtime packages import kernel packages through public exports only
- `@jarvis/runtime-cloudflare` exports only contract placeholders in v0.1
- package boundary tests fail on forbidden imports

### Milestone 2: Core Domain Kernel

Owner: Kernel

Supports: Policy And Safety, Runtime, Developer Experience

Output:

- Actor
- HumanProfile
- AgentProfile
- HumanWorker
- AgentWorker
- WorkSession
- WorkSessionRun
- runtime/internal Session reference
- Request
- Review
- Contribution
- EvidenceManifest
- EvidenceItem
- event envelope
- trace context
- status transitions

Done when:

- WorkSession status transitions reject invalid transitions
- event envelopes require ids, sequence, timestamps, actor, trace context, and
  hash fields
- WorkSession remains the public primitive
- runtime/internal Session remains adapter-internal

### Milestone 3: Local Runtime Foundation

Owner: Runtime

Supports: Kernel, Policy And Safety, Developer Experience

Output:

- SQLite persistence
- local filesystem workspace
- `.jarvis` internal storage
- SSE event stream
- local runtime config loader
- run leases and lock epochs
- checkpoint store
- request store
- evidence store

Done when:

- local runtime starts without Cloudflare credentials
- WorkSession persists across process restart
- pending requests survive restart
- SSE stream replays missed events from `Last-Event-ID`
- mutating runtime commits verify active WorkSession lock epoch

### Milestone 4: Policy And Request Control Plane

Owner: Policy And Safety

Supports: Kernel, Runtime, Developer Experience

Output:

- autonomy levels
- risk classes
- capability grants
- grant vector resolution
- structured requests
- one-use approval tokens
- takeover lock epoch
- external-send outbox contracts
- credential broker contracts
- tamper-evident policy events

Done when:

- uncovered action dimensions deny execution
- conflicting grants deny and create a Request
- stale approval tokens fail
- takeover cancels, fences, or reconciles in-flight work
- degraded audit integrity blocks high-risk modes
- external send cannot bypass the outbox

### Milestone 5: Memory And Learning

Owner: Memory And Learning

Supports: Kernel, Policy And Safety, Developer Experience

Output:

- memory records
- memory scopes
- lifecycle states
- provenance
- trust labels
- memory write policy matrix
- context manifest
- memory selector
- learning proposals after WorkSession runs

v0.1 subset:

- seed memory files
- project memory scope
- shared memory scope
- context manifest
- memory proposal records
- manual confirmation through API/CLI test helper

Done when:

- model-derived memory cannot confirm itself
- untrusted tool output cannot become durable memory automatically
- project memory cannot leak into another project
- context manifests explain selected memories, skills, policy, and tool
  inventory
- learning pass proposes memory updates without mutating durable memory

### Milestone 6: Skills, Tools, MCP, And Sandbox Contracts

Owner: Skills And Tools

Supports: Policy And Safety, Runtime, Developer Experience

Output:

- skill manifest and bundle format
- skill inventory
- skill activation gates
- policy-wrapped tool registry
- MCP gateway contracts
- MCP capability inventory hashing and quarantine
- sandbox tool contract
- tool output trust labels
- tool failure records

v0.1 subset:

- local skill manifest loading
- skill activation gates
- one policy-wrapped sandbox command tool
- MCP inventory capture and quarantine
- no external MCP execution by default

Done when:

- unreviewed skill updates stay inactive
- raw tools cannot bypass policy wrappers
- changed MCP capability inventory enters quarantine
- MCP prompts/resources never become instruction authority
- sandbox execution produces evidence and policy decisions

### Milestone 7: Agent Loop And Golden Path

Owner: Runtime

Supports: Kernel, Policy And Safety, Memory And Learning, Skills And Tools,
Developer Experience

Output:

- `createJarvisLocalRuntime`
- `pairs.create`
- `workSessions.start`
- `workSessions.send`
- `workSessions.events`
- `requests.resolve`
- `workSessions.complete`
- CLI commands:
  - `jarvis:dev`
  - `jarvis:session`
  - `jarvis:requests`
  - `jarvis:approve`
  - `jarvis:evidence`

Done when:

- a fresh scaffold runs the golden path API
- CLI and TypeScript API operate on the same WorkSession contracts
- default network-denied policy creates a structured Request
- approval resumes the WorkSession
- final run exports an EvidenceManifest

### Milestone 8: v0.1 Alpha Hardening

Owner: Developer Experience

Supports: all lanes

Output:

- docs for install, concepts, local runtime, policy, memory, tools, and
  troubleshooting
- examples for research, coding-assistant, and local project assistant flows
- release acceptance tests
- API reference generated from public exports
- migration notes for future runtime adapters

Done when:

- all v0.1 acceptance tests pass
- scaffold installs from a clean machine
- no Cloudflare credentials are required for local alpha
- evidence export includes event-chain root, evidence item hashes,
  request/review records, policy decisions, context manifest ref, artifact
  refs, and limitations

## v0.2 Cloudflare Runtime Beta

Goal: make Cloudflare the first-class production runtime without moving Jarvis
semantics into Cloudflare-specific code.

Output:

- `@jarvis/runtime-cloudflare`
- `JarvisHost` mapped to a HumanWorker + AgentWorker relationship
- `JarvisWorkSessionActor` mapped to WorkSession or WorkSessionRun
- Think integration for low-level session/message persistence, streaming,
  model/tool loop mechanics, checkpoints, and recovery
- Durable Objects/Agents actor mapping
- Workspace integration
- Sandbox/Container execution
- R2 evidence/artifact storage
- alarms/background work
- service binding boundaries

Done when:

- Cloudflare adapter invokes Jarvis kernel services for context, policy, tools,
  events, evidence, and learning
- Cloudflare runtime passes the same WorkSession behavior tests as local runtime
- kernel packages still import no Cloudflare types
- runtime debug surfaces apply Jarvis redaction rules

## v0.3 Connector And Skill Ecosystem

Goal: make Jarvis extensible without weakening policy.

Output:

- skill package publishing format
- skill trust and review workflow
- MCP server registration workflow
- connector examples
- tool inventory diff UI/API hooks
- memory import/export contracts
- evidence export profiles
- runtime adapter authoring guide

Done when:

- external skills install but remain inactive until reviewed
- changed skills and MCP capabilities enter quarantine
- connector examples run through the same policy wrappers
- adapter authors can implement the required ports without reading runtime
  internals

## v1.0 Stable Protocol

Goal: stabilize the public contracts.

Output:

- stable package APIs
- stable WorkSession event schema
- stable memory schema
- stable policy/grant/request schema
- stable evidence manifest schema
- stable runtime adapter contract
- versioned migration path
- security review
- complete documentation set

Done when:

- v0.1 and v0.2 apps migrate without data loss
- runtime adapter contract is versioned
- evidence and policy schemas are versioned
- compatibility tests cover local and Cloudflare runtimes
- public docs define every stable primitive

## Team Lanes

### Kernel

Owns:

- `@jarvis/core`
- event contracts
- WorkSession lifecycle
- domain schemas
- status transitions

### Policy And Safety

Owns:

- `@jarvis/policy`
- grant resolver
- requests and approvals
- takeover lock epoch
- outbox
- credential broker
- audit events

### Memory And Learning

Owns:

- `@jarvis/memory`
- memory schema
- memory lifecycle
- context manifest
- learning proposals
- correction pipeline

### Skills And Tools

Owns:

- `@jarvis/skills`
- `@jarvis/tools`
- MCP gateway
- sandbox tool contract
- tool registry
- skill bundle format

### Runtime

Owns:

- `@jarvis/runtime-local`
- `@jarvis/runtime-cloudflare`
- runtime ports
- persistence
- streaming
- sandbox execution
- recovery

### Developer Experience

Owns:

- `create-jarvis`
- CLI
- examples
- docs
- acceptance tests
- release packaging

## Milestone Ownership Matrix

```txt
M0 Architecture Lock
  owner: Architecture
  supports: all lanes
  decision owner: architecture lead

M1 Repository And Package Scaffold
  owner: Developer Experience
  supports: Kernel, Runtime
  decision owner: DX lead

M2 Core Domain Kernel
  owner: Kernel
  supports: Policy And Safety, Runtime, Developer Experience
  decision owner: kernel lead

M3 Local Runtime Foundation
  owner: Runtime
  supports: Kernel, Policy And Safety, Developer Experience
  decision owner: runtime lead

M4 Policy And Request Control Plane
  owner: Policy And Safety
  supports: Kernel, Runtime, Developer Experience
  decision owner: safety lead

M5 Memory And Learning
  owner: Memory And Learning
  supports: Kernel, Policy And Safety, Developer Experience
  decision owner: memory lead

M6 Skills, Tools, MCP, And Sandbox Contracts
  owner: Skills And Tools
  supports: Policy And Safety, Runtime, Developer Experience
  decision owner: tools lead

M7 Agent Loop And Golden Path
  owner: Runtime
  supports: all implementation lanes
  decision owner: runtime lead

M8 v0.1 Alpha Hardening
  owner: Developer Experience
  supports: all lanes
  decision owner: release lead
```

## Suggested Execution Order

```txt
Week 0
  Milestone 0: architecture lock
  Gate A prerequisite: docs, package contracts, local runtime MVP, acceptance
  tests accepted

Week 1
  Milestone 1: repo/package scaffold
  Milestone 2 starts: core domain records and event envelope
  Continuous DX: create-jarvis skeleton and first acceptance fixture

Week 2
  Milestone 2 complete
  Milestone 3 starts: SQLite, workspace, event store, SSE
  Continuous DX: scaffold install test runs in CI

Week 3
  Milestone 3 complete
  Milestone 4 starts: policy, grants, requests, approvals
  Continuous DX: restart recovery fixture added

Week 4
  Milestone 4 complete
  Milestone 5 starts: memory, context manifest, learning proposals
  Continuous DX: request/approval fixture added

Week 5
  Milestone 5 complete
  Milestone 6 starts: skills, tools, MCP gateway, sandbox contracts
  Continuous DX: evidence manifest fixture added

Week 6
  Milestone 6 complete
  Milestone 7 starts: agent loop, CLI, golden path
  Continuous DX: CLI golden path fixture added

Week 7
  Milestone 7 complete
  Milestone 8 starts: hardening, docs, examples, acceptance tests
  Continuous DX: clean-machine scaffold test added

Week 8
  v0.1 alpha cut
  Cloudflare runtime beta starts
```

This schedule assumes focused execution by a small team. If one engineer owns
the full implementation, v0.1 becomes a 10-12 week target. If three engineers
work in parallel across kernel/policy, runtime, and developer experience, v0.1
is an 8 week target.

## Decision Gates

### Gate A: Start Implementation

Owner: Architecture

Required:

- architecture docs accepted
- package contracts accepted
- local runtime MVP accepted
- acceptance tests accepted
- Milestone 0 completed

### Gate B: v0.1 Alpha

Owner: Developer Experience

Required:

```txt
npm create jarvis@latest my-jarvis
cd my-jarvis
npm install
npm run test
```

Pass artifacts:

- scaffold installs without Cloudflare credentials
- `jarvis.config.ts` validates
- `.jarvis/local.db` is created during test setup
- package boundary tests pass

```txt
npm run jarvis:dev
```

Pass artifacts:

- local runtime URL is printed
- active policy profile is printed
- SSE stream is available
- no provider secret is required for runtime boot

```txt
npm run jarvis:session -- --objective "Inspect the scaffold and create a plan"
```

Pass artifacts:

- HumanWorker exists
- AgentWorker exists
- WorkSession exists
- runtime/internal Session ref exists below WorkSession
- `work_session_started` event exists
- context manifest exists

```txt
npm run jarvis:session -- --objective "Fetch example.com and summarize it"
npm run jarvis:requests
npm run jarvis:approve -- --request <id> --scope "network_fetch:example.com"
```

Pass artifacts:

- default network-denied policy creates a structured Request
- Request includes risk class, host, expected result, expiry, canonical action
  hash, and narrower alternative
- approval uses a one-use token
- stale approval replay fails
- WorkSession resumes
- policy decision records selected grant ids by dimension

```txt
npm run jarvis:evidence -- --work-session <id>
```

Pass artifacts:

- EvidenceManifest JSON exports
- manifest includes event-chain root, evidence item hashes, request/review
  records, policy decisions, context manifest ref, artifact refs, and known
  limitations
- redacted export is derived and raw immutable evidence remains unchanged

Restart fixture:

```txt
npm run jarvis:dev
npm run jarvis:session -- --objective "Trigger a blocked external send"
stop runtime
npm run jarvis:dev
npm run jarvis:requests
```

Pass artifacts:

- pending request survives restart
- WorkSession resumes from event log and checkpoint
- runtime/internal Session remains adapter-internal
- no outbox commit happens before approval

### Gate C: v0.2 Cloudflare Beta

Owner: Runtime

Required:

- Cloudflare runtime passes local runtime behavior tests
- Cloudflare adapter does not own Jarvis semantics
- sandbox, storage, streaming, recovery, and evidence work in production

### Gate D: v1.0

Owner: Release

Required:

- public contracts versioned
- security model reviewed
- migration path documented
- runtime adapter contract stable
- local and Cloudflare compatibility tests pass

## Risks And Controls

### Runtime Scope Creep

Risk: implementation moves Jarvis semantics into local or Cloudflare runtime.

Control: kernel packages own semantics. Runtime packages implement ports.

### Policy Bypass

Risk: raw tools, sandbox commands, MCP capabilities, or external sends bypass
policy.

Control: every tool is policy-wrapped. External effects pass through outbox.

### Memory Pollution

Risk: model-derived or tool-derived content becomes durable memory without
review.

Control: memory write policy matrix and lifecycle gates.

### Weak Local Runtime

Risk: local runtime becomes a demo instead of a real harness.

Control: local runtime must pass persistence, restart, request, evidence, and
policy tests.

### Cloudflare Lock-In

Risk: Cloudflare adapter shapes the public Jarvis API.

Control: kernel packages import no Cloudflare types. Cloudflare implements
runtime ports only.

## Immediate Next Actions

1. Complete Gate A with the team.
2. Create the Jarvis implementation repo.
3. Copy this design package into `/docs/design` or keep it as the planning
   source of truth.
4. Implement Milestone 1 package scaffold.
5. Add package boundary tests before writing runtime code.
6. Implement `@jarvis/core` WorkSession, event, request, review, contribution,
   and evidence contracts.
7. Implement the local runtime only after the kernel contracts compile.
