# Chunk 6: Existing-Agent Compatibility Proof Plan

Chunk 6 defines the existing-agent compatibility proof plan.

## Scope

This chunk proves protocol mapping on paper.

It does not add adapter code, wrapper code, integration code, runtime behavior,
model calls, tool execution, UI, storage, authentication backend, billing,
scoring, payment, or deployment behavior.

## Output

Chunk 6 creates:

```txt
docs/conformance/existing-agent-proof-plan.md
```

The proof plan is the source for Week 4 compatible examples.

## Required Proof

Chunk 6 proves:

```txt
existing human-agent interaction maps to Worker and Actor records
agent actions map to PolicyDecision and JarvisEvent records
PolicyDecision exists before accepted AgentWorker protocol state
blocked action maps to Request
human resolution maps to Review or Takeover
performed work maps to Contribution
artifacts and sources map to EvidenceManifest records with source_event_refs
confirmed improvement maps to LearningRecord, MemoryProposal, or SkillProposal
unsupported native concepts map to limitations or reject as unsupported_capability
two allowed host shapes produce equivalent Jarvis records
host-private fields stay outside portable protocol records
Review resolution equivalence is proven
Takeover resolution equivalence is proven
normalized Jarvis record graph equivalence is proven
```

## Proof Pair

Chunk 6 locks this v0.1 proof pair:

```txt
command_line_host_boundary
local_execution_host_boundary
```

Both host shapes MUST map the same collaboration loop into equivalent Jarvis
records.

## Required Gates

Existing-agent compatibility proof MUST preserve:

- WorkSession-scoped mutation headers
- non-WorkSession mutation headers
- WorkSession-scoped read and export read headers
- Actor authority checks
- WorkSession revision checks
- previous event hash linkage
- genesis WorkSession revision and genesis hash rules
- PolicyDecision before accepted AgentWorker state
- Request for blocked, denied, or review-required scope
- Review or Takeover for Request resolution
- bounded ApprovalScope for approve or narrow Review decisions
- Takeover lock_epoch and reconciliation_refs
- Contribution actor attribution
- EvidenceManifest event-chain refs and source_event_refs
- forbidden host-private export boundary
- governed LearningRecord, MemoryProposal, and SkillProposal states
- `limitations` or `unsupported_capability` for unsupported native concepts

## Done Criteria

Chunk 6 is complete when:

- two host shapes map to equivalent Jarvis records on paper
- neither host shape moves runtime behavior into Jarvis
- proof plan rejects host-private fields from portable records
- proof plan preserves zero-trust mutation gates
- proof plan preserves read and export header gates
- proof plan proves Review and Takeover resolution equivalence
- proof plan preserves evidence and governed learning gates
- local validation passes
- compatibility proof supports Week 4 compatible examples

## Local Check Sequence

Every Chunk 6 change MUST run:

```txt
python3 scripts/check_conformance_fixtures.py
python3 scripts/check_openapi_skeleton.py
python3 scripts/check_markdown_links.py
python3 scripts/check_week1_wording.py
git diff --check
```
