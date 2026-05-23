# Architecture

Jarvis coordinates a human and an autonomous agent across memory, work
sessions, tools, policy, reviews, and learning.

## Layer Model

```txt
Interface layer
  chat, CLI, desktop, mobile, browser, messaging, custom apps

Jarvis collaboration layer
  work sessions, requests, reviews, takeover, evidence, contributions

Jarvis context and learning layer
  memory retrieval, context assembly, skill loading, learning proposals

Jarvis capability layer
  tools, MCP servers, sandbox actions, files, browser, shell, connectors

Jarvis policy layer
  autonomy levels, grants, risk classes, request rules, audit decisions

Runtime substrate
  durable actors, sessions, files, tool loop, sandbox, scheduling, streaming
```

The interface is replaceable. The runtime is replaceable by contract. Jarvis is
the collaboration, context, learning, and policy layer in the middle.

## Kernel Primitives

### Actor

An entity that can contribute to a session.

```txt
human | agent | service
```

### HumanProfile

Durable human context:

- name/handle
- role/domain
- goals
- preferences
- boundaries
- communication style
- correction history

### AgentProfile

Durable agent context:

- persona
- role
- instructions
- autonomy defaults
- capability defaults
- skill inventory
- learned behavior notes

### HumanAgentPair

The durable collaboration relationship between one human and one agent.

This is the central Jarvis primitive. It captures how this human and this agent
work together:

- trust level
- default autonomy profile
- shared preferences
- correction history
- review patterns
- learned working style
- common tools and skills
- escalation/takeover preferences

HumanProfile describes the human. AgentProfile describes the agent.
HumanAgentPair describes the partnership.

### Session

Durable conversational and turn state. Session is runtime/internal by default.
Developers work with WorkSession.

### WorkSession

The durable collaboration record for one focused unit of work.

`WorkSession` is the default public Jarvis primitive. Every developer-facing
Jarvis flow starts or resumes a `WorkSession`.

A `WorkSession` owns the collaboration record: messages, actions, file and
artifact references, requests, reviews, evidence, runtime runs, and learning
proposals.

`Session` is a runtime persistence primitive. It stores and resumes
message/turn state for an adapter. `Session` is not the default developer API.

### Run

One execution attempt inside a WorkSession. A WorkSession has one or more runs,
and each run has one or more turns. Runs bind to runtime execution references,
leases, checkpoints, and recovery state.

### Memory

Structured knowledge with type, scope, provenance, lifecycle state, confidence,
priority, and retrieval metadata.

### Skill

Procedural memory. A reusable, inspectable way of performing work.

### Tool

Executable capability with schema, risk class, scope, provenance, and policy
wrapper.

### Policy

Rules that decide permitted autonomous actions and required human input.

### Request

Agent-created ask for missing permission, context, decision, review, or human
takeover.

### Review

Human judgment over a plan, action, artifact, memory update, or skill update.

### Contribution

Traceable action by a human, agent, or service inside a WorkSession.

### Evidence

Artifacts and observations that support what happened during work.

## Agent Operating Environment

For an agent to work seriously, Jarvis needs:

```txt
model adapter
foundation prompt
session history
context assembler
memory retriever
skill inventory/loader
tool registry
policy engine
workspace/files
sandbox executor
request sink
event store
learning worker
runtime health surface
```

The runtime supplies mechanics. Jarvis supplies meaning and policy.

## Standard Work Flow

```txt
1. Interface starts or resumes a WorkSession for a HumanAgentPair.
2. Runtime restores durable run/session state.
3. Jarvis assembles context from human, agent, pair, memory, skills, and active
   work.
4. Policy selects visible tools and autonomy limits.
5. Agent plans and executes within allowed boundaries.
6. Policy wraps every tool/action.
7. Missing permission or context becomes a Request.
8. Events, contributions, and evidence are recorded.
9. Human reviews when policy requires it or chooses takeover.
10. Learning worker proposes memory/skill changes.
11. Confirmed learning affects future WorkSessions.
```

## Ownership Boundary

Jarvis owns:

- memory semantics
- session/work semantics
- collaboration events
- request/review semantics
- policy evaluation
- skill lifecycle
- tool wrapping
- evidence capture
- learning proposals
- context assembly
- memory selection

Runtime owns:

- durable actors
- storage primitives
- streaming transport
- sandbox mechanics
- scheduling/recovery
- model/tool loop mechanics
- run leases and checkpoints
- idempotent execution support

Interface owns:

- visual layout
- notifications
- user interaction controls
- local input/output conventions

## Important Design Tension

Jarvis is powerful enough to support products and small enough to be usable as
open-source infrastructure.

The kernel excludes product-specific concepts. Product-specific behavior enters
through adapters, policies, tools, and interfaces.

## Minimum Developer Entry Point

The public API flow is:

```txt
create or load HumanAgentPair
start WorkSession
attach tools/skills/policy
send human intent
observe events/requests/evidence
review or take over when needed
complete session
inspect learning proposals
```

Low-level runtime sessions, model turns, context snapshots, and adapter-specific
actors remain below this surface unless the developer asks for advanced
runtime control.
