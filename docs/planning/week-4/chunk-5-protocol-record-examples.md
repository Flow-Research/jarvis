# Chunk 5: Protocol Record Examples

Chunk 5 adds concrete protocol record examples for the core collaboration
loop.

## Scope

This chunk creates public examples for the protocol records developers need to
understand first.

This chunk does not create a runtime, host, adapter, SDK package, UI, model
integration, tool integration, database, auth system, billing system, scoring
system, payment system, or deployment path.

## Required Output

Chunk 5 creates or updates:

```txt
docs/examples/protocol-records.md
```

The examples cover:

```txt
Worker
Actor
HumanWorker
AgentWorker
WorkSession
JarvisEvent
Policy
PolicyDecision
Request
Review
Takeover
ApprovalScope
Contribution
EvidenceManifest
LearningRecord
MemoryProposal
SkillProposal
OutcomeReport
```

## Example Requirements

Every example record:

- uses fields from the OpenAPI contract
- avoids host-private fields
- uses stable ids and refs
- preserves event ordering where relevant
- includes required mutation headers when the example describes a mutation
- links to the conformance gate it demonstrates
- stays small enough for public readers

## Required Narrative Flow

The examples follow one loop:

```txt
1. HumanWorker and AgentWorker exist.
2. WorkSession starts under Policy.
3. AgentWorker action records PolicyDecision before accepted protocol state.
4. Blocked action creates Request.
5. HumanWorker resolves Request through Review or Takeover.
6. Review approve or narrow creates bounded ApprovalScope.
7. Takeover records lock epoch and resumed Takeover requires reconciliation refs.
8. Work creates Contribution.
9. EvidenceManifest exports proof.
10. LearningRecord captures pair learning.
11. MemoryProposal or SkillProposal stays governed.
12. OutcomeReport carries post-session feedback.
```

## Review Focus

Review verifies:

- examples match OpenAPI field names
- references are coherent
- required gates remain visible
- examples do not invent host behavior
- examples teach protocol records without becoming implementation docs

## Done Criteria

Chunk 5 is complete when:

- protocol record examples exist
- examples cover the required records
- examples link to conformance expectations
- local checks pass
- internal reviewer lanes have no valid unresolved findings
- CodeRabbit has no valid unresolved findings
