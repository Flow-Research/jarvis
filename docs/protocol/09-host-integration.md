# Host Integration

Jarvis is implemented by a host.

A host is any implementation that produces and consumes Jarvis protocol
records. The host owns execution and infrastructure. Jarvis owns the protocol
records the host must produce.

## Host Responsibilities

A Jarvis-compatible host must:

- create HumanWorker records
- create AgentWorker records
- start and complete WorkSessions
- attach Policy to WorkSessions
- evaluate meaningful agent actions against Policy
- create Requests when action is blocked
- record Reviews from the HumanWorker
- enforce Takeover state
- record Contributions
- capture EvidenceManifest entries during work
- propose LearningRecords, MemoryProposals, and SkillProposals
- export portable Jarvis protocol records

## Host Freedom

A host owns these choices:

- UI
- auth
- model provider
- tool system
- MCP hosting
- sandbox
- storage
- queue
- cloud
- local execution
- deployment
- monitoring
- billing

None of these choices belong to Jarvis.

## Minimal Protocol Operation Sequence

A compatible host proves the minimal flow through OpenAPI protocol operations:

```txt
1. registerWorker and registerActor with non-WorkSession mutation headers.
2. createWorkSession with expected revision 0 and
   Jarvis-Previous-Event-Hash set to hash:protocol-genesis.
3. recordPolicyDecision before accepted AgentWorker protocol state.
4. appendJarvisEvent only after Actor authority, expected revision, and
   previous event hash pass.
5. createRequest for denied, blocked, or review-required scope.
6. recordReview or recordTakeover to resolve the Request.
7. recordContribution with attributable contributor refs.
8. exportEvidenceManifest only from a valid terminal WorkSession state.
9. createLearningRecord, MemoryProposal, or SkillProposal only through
   governed protocol records.
10. submitOutcomeReport as a non-WorkSession mutation.
```

This sequence is protocol shape only. Hosts own functions, storage, execution,
identity, UI, and deployment.

## Export Boundary

A host has private implementation fields. Those fields stay outside the
Jarvis export.

A portable Jarvis export contains:

- protocol_version
- WorkSession
- Workers
- Actors
- JarvisEvents
- PolicyDecisions
- Requests
- Reviews
- Takeovers
- Contributions
- EvidenceManifest
- LearningRecords
- MemoryProposals
- SkillProposals
- limitations

OutcomeReport is outside this sealed WorkSession export. When distributed,
OutcomeReport travels as a separate v0.1 extension record linked by
`work_session_id` and `learning_record_refs`.

## Compatibility

A host is Jarvis-compatible when it passes the conformance suite and exports
portable protocol records without requiring another host to understand its
private infrastructure.
