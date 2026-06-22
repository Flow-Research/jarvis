# Chunk 2: Compatible Host Mapping Example

Chunk 2 creates the first public-compatible host mapping example.

## Scope

This chunk maps one native human-agent workflow into Jarvis records.

The example starts from the Week 3 proof plan and includes `host_shape_ref`
as descriptive metadata only. `host_shape_ref` names the host boundary shape; it
MUST NOT select behavior, change required records, change conformance results,
or imply a Jarvis-owned host adapter or runtime.

Allowed `host_shape_ref` values for this example are:

```txt
command_line_host_boundary
local_execution_host_boundary
```

This chunk does not build a host, adapter, wrapper, runtime, UI, model
integration, tool integration, storage backend, auth backend, SDK package, or
deployment path.

## Required Output

Chunk 2 creates or updates:

```txt
docs/examples/compatible-host-mapping.md
```

The mapping example records:

```txt
native human participant -> HumanWorker + Actor
native agent participant -> AgentWorker + Actor
native work objective -> WorkSession.objective
native policy boundary -> Policy
native agent action -> PolicyDecision + JarvisEvent
blocked native action -> Request
human judgment -> Review or Takeover
approved or narrowed authority -> ApprovalScope
performed work -> Contribution
source events and artifacts -> EvidenceManifest evidence refs
confirmed improvement -> LearningRecord
durable memory update -> MemoryProposal
reusable procedure update -> SkillProposal
post-session feedback -> OutcomeReport
```

## Required Invariants

The example preserves:

- WorkSession-scoped mutation headers: `Jarvis-Protocol-Version`,
  `Jarvis-Actor-Id`, `Jarvis-Idempotency-Key`,
  `Jarvis-Request-Timestamp`, `Jarvis-Expected-WorkSession-Revision`, and
  `Jarvis-Previous-Event-Hash`
- non-WorkSession protocol mutation headers: `Jarvis-Protocol-Version`,
  `Jarvis-Actor-Id`, `Jarvis-Idempotency-Key`, and
  `Jarvis-Request-Timestamp` only
- Actor authority verification before accepted protocol state
- WorkSession revision check for every WorkSession-scoped mutation
- previous event hash linkage for every WorkSession-scoped mutation
- PolicyDecision before accepted AgentWorker state
- Request for denied, blocked, or review-required scope
- Review or Takeover as the only human resolution path
- ApprovalScope bounds for approve or narrow Review decisions
- Takeover lock epoch and reconciliation refs
- attributable Contribution records
- EvidenceManifest source event refs
- forbidden host-private export exclusion
- governed LearningRecord, MemoryProposal, and SkillProposal records
- OutcomeReport as post-session feedback without sealed-record mutation

## Public Explanation

The example must answer:

```txt
What happened?
Who acted?
What did policy allow or block?
Where did the agent request human help?
What did the human review or take over?
What evidence proves the work?
What learning carries forward?
What stays host-owned?
```

## Review Focus

Review verifies:

- mapping uses protocol objects only
- host-owned execution stays outside records
- example fields exist in the OpenAPI contract
- example references Week 3 conformance gates
- wording stays direct and public-readable

## Done Criteria

Chunk 2 is complete when:

- compatible host mapping doc exists
- both host shapes map to equivalent Jarvis records
- no adapter or runtime behavior enters Jarvis
- all required invariants are represented
- local checks pass
- internal reviewer lanes have no valid unresolved findings
- CodeRabbit has no valid unresolved findings
