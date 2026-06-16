# Chunk 6: Existing-Agent Compatibility Proof Plan

Chunk 6 defines the existing-agent compatibility proof plan.

## Scope

This chunk proves protocol mapping on paper.

It does not add adapter code, wrapper code, integration code, runtime behavior,
model calls, tool execution, UI, storage, auth, billing, scoring, or deployment
behavior.

## Required Proof

Chunk 6 proves:

- an existing agent interaction maps to Worker and Actor records
- agent actions map to PolicyDecision and JarvisEvent records
- blocked action maps to Request
- human answer maps to Review or Takeover
- performed work maps to Contribution
- artifacts and sources map to EvidenceManifest records
- confirmed improvement maps to LearningRecord, MemoryProposal, or SkillProposal
- unsupported host concepts map to limitations

## Done Criteria

Chunk 6 is complete when:

- two host shapes map to equivalent Jarvis records on paper
- neither host shape requires Jarvis-owned runtime behavior
- compatibility proof supports Week 4 compatible examples
