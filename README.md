# Jarvis Human-Agent Collaboration Harness

Jarvis is the open-source harness where a human and an autonomous agent share
memory, skills, tools, context, policy, and learning over time.

## Interactive Simulation

Open the live simulation here:

https://flow-research.github.io/jarvis_human_agent/

The page is served directly by GitHub Pages from this repository.

Jarvis is the durable operating layer for collaboration:

```txt
human judgment + agent execution + shared memory + safe autonomy + evidence
```

The agent works independently inside predefined boundaries.
The human does not babysit every action. When the agent needs missing
permission, missing context, or human judgment, it creates a request that the
human approves, denies, narrows, answers, or takes over.

## Scope

This design is only about Jarvis.

Jarvis does not define product interface ownership, external work ownership,
external identity ownership, or enterprise workspace ownership. Those systems
integrate with Jarvis through interfaces and adapters. Jarvis stands alone as
the harness.

## Thesis

An autonomous agent still needs an operating environment:

- durable sessions
- durable files and state
- model calls
- context assembly
- memory retrieval
- tool execution
- sandboxed command/code execution
- scheduling/background work
- policy and approvals
- event/evidence capture
- recovery after failure

Cloudflare provides the first Jarvis runtime substrate:
Agents, Think, Durable Objects, Workspace, Sandbox, Containers, R2, Worker
Loader, service bindings, alarms, and durable execution patterns.

Jarvis owns the layer above that substrate:

- human-agent collaboration semantics
- structured memory and learning
- autonomy policy
- request/review/takeover flows
- skills as procedural memory
- policy-wrapped tools
- evidence and contribution records
- runtime adapter contracts

## Document Map

- [00-principles.md](./00-principles.md) - first principles, non-goals, and
  design constraints.
- [01-architecture.md](./01-architecture.md) - system layers, kernel
  primitives, and boundaries.
- [02-memory.md](./02-memory.md) - memory taxonomy, lifecycle, provenance,
  retrieval, and write policy.
- [03-autonomy-policy.md](./03-autonomy-policy.md) - autonomy levels,
  capability grants, requests, inbox, and takeover.
- [04-work-sessions.md](./04-work-sessions.md) - collaboration records,
  events, reviews, evidence, and learning loops.
- [05-skills-tools.md](./05-skills-tools.md) - skills, tools, MCP, sandbox
  policy, and tool wrapping.
- [06-runtime-adapters.md](./06-runtime-adapters.md) - Cloudflare-first runtime
  adapter and local/runtime-neutral boundaries.
- [07-implementation-decisions.md](./07-implementation-decisions.md) -
  implementation choices that remain below the architecture layer.
- [08-package-contracts.md](./08-package-contracts.md) - package graph,
  exports, ownership, forbidden imports, and release tests.
- [09-default-project.md](./09-default-project.md) - `create-jarvis`
  scaffold, config, CLI flow, and golden path API.
- [10-local-runtime-mvp.md](./10-local-runtime-mvp.md) - local runtime
  defaults, required ports, persistence schema, and stream protocol.
- [ROADMAP.md](./ROADMAP.md) - release roadmap, milestones, team workstreams,
  decision gates, risks, and immediate next actions.

## Architecture Contract

Jarvis core is runtime-neutral. Runtime adapters implement infrastructure ports.
Jarvis kernel services own collaboration, policy, memory, learning, skills,
tools, requests, reviews, and evidence.

Cloudflare is not the public identity of Jarvis. Cloudflare is the first-class
runtime implementation because it provides the primitives Jarvis requires.

The local development runtime is included for open-source adoption and
testability.

## First Usable Jarvis

The first open-source release contains a buildable Jarvis harness, not a
reference essay.

The initial distribution is:

```txt
@jarvis/core
  actors, HumanAgentPair, WorkSession, Run, Request, Review, Contribution,
  EvidenceManifest, memory records, policy records, and event contracts

@jarvis/memory
  scoped memory store, retrieval policy, provenance, lifecycle, correction
  learning pipeline, and context manifest support

@jarvis/policy
  autonomy levels, grants, risk classes, grant resolution, request creation,
  takeover locks, outbox protocol, credential broker contracts, and audit events

@jarvis/skills
  skill manifest, skill inventory, skill activation gates, skill versioning,
  and skill loading contracts

@jarvis/tools
  policy-wrapped tool registry, MCP gateway contracts, sandbox tool contracts,
  trust labels, and tool failure records

@jarvis/runtime-cloudflare
  first-class Cloudflare adapter using Agents, Think, Durable Objects,
  Workspace, Sandbox/Containers, R2, Worker Loader, alarms, and service bindings

@jarvis/runtime-local
  local development adapter using SQLite, local filesystem workspace, local
  Docker or namespace-isolated sandbox behind policy, local scheduler, and SSE
  streaming
```

The first usable flow is:

```txt
create HumanAgentPair
start WorkSession
attach memory store
attach policy profile
attach skills and policy-wrapped tools
send human intent
run agent inside policy
create Request when permission/context/judgment is missing
review, approve, deny, narrow, or take over
record events, contributions, and evidence
run learning pass
persist confirmed memory and skill updates
resume the WorkSession later
```

The public harness starts with WorkSession. Low-level runtime sessions remain
internal unless an advanced runtime integration explicitly exposes them.

## Jarvis Spine

Jarvis is built around these primitives:

```txt
HumanAgentPair
  durable relationship between one human and one agent

WorkSession
  public collaboration record, not just chat

Request/Review/Takeover
  control plane for safe autonomy

Contribution Ledger
  inspectable record of human, agent, and service actions

Evidence Manifest
  exportable package of artifacts, traces, reviews, and limitations

Governed Learning
  memory and skill changes flow through policy and review gates
```

## Design Constraints

Jarvis incorporates these constraints:

- durable sessions, files, tools, sandbox execution, streaming, and recovery
- structured memory with provenance, lifecycle, scope, and review state
- connector and tool execution through policy wrappers
- untrusted external content fenced as data, not instruction
- agent identity, human review, authorization, and evidence capture
- inspectable long-running work with resumable state

These constraints are part of the Jarvis architecture.
