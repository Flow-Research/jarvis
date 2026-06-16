# Chunk 3: Golden-Path Fixture

Chunk 3 adds the valid golden-path fixture.

## Scope

This chunk creates the fixture files required for a passing WorkSession proof.

It does not build a host, adapter, runtime, UI, model integration, or tool
integration.

## Required Fixture

Chunk 3 adds:

```txt
docs/conformance/fixtures/README.md
docs/conformance/fixtures/valid/golden-path.json
```

## Required Proof

The golden-path fixture records:

- Worker and Actor records for HumanWorker and AgentWorker
- WorkSession creation with genesis revision and event hash
- PolicyDecision before AgentWorker action
- Request for blocked work
- Review approval or narrowing resolving Request
- ApprovalScope for approved or narrowed authority
- Contribution records
- EvidenceManifest export
- LearningRecord
- MemoryProposal or SkillProposal
- OutcomeReport hook

The golden-path fixture resolves the Request through Review approval or
narrowing. The stale Takeover fixture proves Takeover lock epoch rejection. A
valid Takeover path requires a separate fixture or an explicit golden-path
branch with reconciliation refs before AgentWorker continuation.

## Done Criteria

Chunk 3 is complete when:

- the valid fixture follows the Chunk 1 envelope
- the fixture references OpenAPI components by name
- the fixture proves the golden-path conformance entry
- local checks pass
