# Chunk 3: Existing-Agent Compatibility Example

Chunk 3 proves that an existing agent participates in Jarvis without becoming a
Jarvis-owned agent.

## Scope

This chunk defines a public example for an existing native agent boundary.
When the example mentions a Jarvis SDK, the SDK appears only as a protocol
implementation helper around that native agent.

The native agent keeps its own runtime, model calls, tool calls, memory,
skills, tracing, session handling, and execution flow. Jarvis records the
human-agent collaboration loop around that native work.

This chunk does not build adapter code, wrapper code, SDK code, integration
code, runtime behavior, host workflow, UI, model routing, tool execution,
storage, auth, billing, scoring, payment, or deployment behavior.

## Required Output

Chunk 3 creates or updates:

```txt
docs/examples/existing-agent-compatibility.md
```

The example records:

```txt
WorkSession-scoped mutation headers -> Jarvis-Protocol-Version, Jarvis-Actor-Id, Jarvis-Idempotency-Key, Jarvis-Request-Timestamp, Jarvis-Expected-WorkSession-Revision, Jarvis-Previous-Event-Hash
non-WorkSession protocol mutation headers -> Jarvis-Protocol-Version, Jarvis-Actor-Id, Jarvis-Idempotency-Key, Jarvis-Request-Timestamp only
Actor authority verification -> before accepted protocol state
WorkSession revision check -> every WorkSession-scoped mutation
previous event hash linkage -> every WorkSession-scoped mutation
existing agent identity -> AgentWorker + Actor
human operator -> HumanWorker + Actor
task intent -> WorkSession
agent action affecting protocol state -> PolicyDecision
blocked action -> Request
human resolution -> Review or Takeover
agent continuation -> JarvisEvent inside approved scope
work performed -> Contribution
evidence captured during work -> EvidenceManifest
confirmed learning -> LearningRecord
future behavior change -> MemoryProposal or SkillProposal
external result -> OutcomeReport
```

## Non-Rewrite Rule

The example rejects compatibility claims that require:

- rewriting the existing agent as a Jarvis agent
- moving native runtime behavior into Jarvis
- moving model orchestration into Jarvis
- moving tool execution into Jarvis
- moving native memory into Jarvis
- making Jarvis own host storage, auth, UI, or deployment

## SDK Boundary

The example treats a Jarvis SDK as a protocol implementation kit only.

Allowed SDK use:

```txt
create protocol records
validate records
attach required headers
preserve event hash chain
export EvidenceManifest
run conformance checks
map example records
```

Rejected SDK use:

```txt
run agent
plan task
route model
execute tool
own memory
own host adapter
own UI
own auth
own storage
```

## Review Focus

Review verifies:

- existing agent remains native
- Jarvis records collaboration only
- compatibility proof references Week 3 gates
- SDK boundary stays protocol-only
- public wording explains why existing agents still need Jarvis records

## Done Criteria

Chunk 3 is complete when:

- existing-agent compatibility doc exists
- the example preserves native execution
- the example maps the full collaboration loop into protocol records
- SDK language stays limited to protocol implementation helpers
- local checks pass
- internal reviewer lanes have no valid unresolved findings
- CodeRabbit has no valid unresolved findings
