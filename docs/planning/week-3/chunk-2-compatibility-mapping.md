# Chunk 2: Compatibility Mapping Rules

Chunk 2 defines how existing human-agent work maps into Jarvis protocol
records.

## Scope

This chunk defines protocol mapping rules only.

It does not add adapter code, wrapper code, runtime behavior, host workflow, UI,
storage, auth, model calls, or tool execution.

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

## Done Criteria

Chunk 2 is complete when:

- every required mapping has a protocol object target
- unsupported native host concepts map to explicit limitations
- host-owned execution remains outside Jarvis records
- mapping rules support the Week 3 fixtures
