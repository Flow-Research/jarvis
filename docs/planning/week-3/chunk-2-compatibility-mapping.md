# Chunk 2: Compatibility Mapping Rules

Chunk 2 defines how existing human-agent work maps into Jarvis protocol
records.

## Scope

This chunk defines protocol mapping rules only.

It does not add adapter code, wrapper code, runtime behavior, host workflow, UI,
storage, authentication backend, model calls, or tool execution.

## Output

Chunk 2 creates:

```txt
docs/conformance/compatibility-mapping.md
```

The conformance mapping document is the source for Week 3 fixture mapping.

## Required Mapping Surface

Chunk 2 maps:

```txt
human participant              -> HumanWorker + Actor
agent participant              -> AgentWorker + Actor
work objective                 -> WorkSession.objective
agent action                   -> PolicyDecision + JarvisEvent
blocked action                 -> Request
human approval or correction   -> Review
human direct control           -> Takeover
work performed                 -> Contribution
source, artifact, output       -> EvidenceManifest item
confirmed improvement          -> LearningRecord / MemoryProposal / SkillProposal
post-session feedback          -> OutcomeReport
```

## Host Shape References

Chunk 2 locks these fixture shape refs:

```txt
command_line_host_boundary
local_execution_host_boundary
hosted_execution_host_boundary
tool_use_protocol_boundary
```

Each `host_shape_ref` identifies the native execution boundary only. It never
records host-private behavior and never changes a Jarvis object meaning.

## Required Protocol Gates

Compatibility mapping MUST preserve these gates:

- WorkSession-scoped mutations MUST carry all six zero-trust headers
- non-WorkSession protocol mutations MUST carry the non-WorkSession mutation
  headers
- Worker registration, Actor registration, and OutcomeReport submission MUST NOT
  require fake WorkSession revision or previous event hash values
- AgentWorker action affecting WorkSession MUST record PolicyDecision before
  accepted protocol state
- Request MUST be scoped deferral, not chat, notification, or authority
- Review or Takeover MUST resolve human-resolved Request states
- Contribution MUST record actor attribution
- EvidenceManifest MUST exclude forbidden host-private fields
- LearningRecord MUST capture human, agent, or pair learning
- MemoryProposal and SkillProposal MUST stay governed until review

## Done Criteria

Chunk 2 is complete when:

- every required mapping has a protocol object target
- every unsupported native concept records `limitations` or rejects as
  `unsupported_capability`
- host-owned execution remains outside Jarvis records
- fixture `host_shape_ref` values are locked
- mapping rules support the Week 3 fixtures
