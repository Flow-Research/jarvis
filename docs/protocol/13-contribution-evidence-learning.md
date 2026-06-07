# Contribution, Evidence, And Learning

Jarvis records attributable work, portable evidence, and governed learning.

This document locks how Contribution, EvidenceManifest, LearningRecord,
MemoryProposal, SkillProposal, and OutcomeReport behave.

Jarvis does not define payment, scoring, task evaluation, model training,
product analytics, or storage implementation.

## Contribution

Contribution records who did what inside a WorkSession.

Contribution is not compensation. Contribution is not payment. Contribution is
not score. Downstream systems may evaluate Contribution records, but Jarvis does
not own that evaluation.

Every Contribution records:

```txt
id
work_session_id
contributor_refs
contributor_type
contribution_type
event_refs
created_at
```

Optional Contribution fields:

```txt
artifact_refs
review_refs
evidence_refs
confidence
limitations
```

`contributor_refs` contains one or more `{worker_id, actor_id,
contribution_role}` references.

Contributor types:

```txt
human
agent
service
tool
shared
```

Contribution types:

```txt
intent
instruction
plan
research
execution
artifact
review
correction
decision
evidence_capture
memory_proposal
skill_proposal
submission
```

Rules:

- Human, agent, service, tool, and shared contributions remain distinguishable.
- Shared contribution MUST preserve individual contributor refs.
- Contribution MUST reference WorkSession events or artifacts.
- Contribution MUST NOT contain payment, compensation, private score, or
  settlement fields.

Rejections:

```txt
missing_contribution_actor
invalid_contributor_refs
shared_contribution_without_individual_refs
```

## Evidence Capture

Evidence is captured during work.

Evidence is not reconstructed only at the end.

Evidence item refs record portable proof pointers:

```txt
id
work_session_id
source_event_refs
captured_by_actor_id
evidence_type
artifact_ref
content_hash
trust_label
redaction_state
captured_at
limitation_refs
```

Evidence item refs may point to host-held artifacts, source snapshots, command
outputs, tool results, review records, request records, policy decisions, or
export receipts. The refs are portable protocol pointers, not host-private
database ids.

Rules:

- Evidence item refs MUST link to source JarvisEvents.
- Evidence item refs MUST record who captured them.
- Evidence item refs MUST record capture time.
- Evidence item refs MUST NOT expose credentials, secrets, raw runtime state,
  host-only database ids, deployment details, billing data, private scores, or
  product UI state.
- Evidence captured after the fact MUST be marked as limitation or
  post-session feedback, not presented as during-work evidence.

Rejections:

```txt
evidence_after_the_fact
missing_evidence_event_refs
forbidden_export_field
```

## EvidenceManifest

EvidenceManifest is the portable proof package for a WorkSession.

Minimum export shape:

```txt
id
work_session_id
generated_by_actor_id
objective
event_chain_root
evidence_item_refs
policy_decision_refs
request_refs
review_refs
takeover_refs
contribution_refs
export_profile
generated_at
```

Optional export refs:

```txt
artifact_refs
limitation_refs
redaction_refs
```

Rules:

- EvidenceManifest references the WorkSession event chain.
- EvidenceManifest references policy decisions, requests, reviews, takeovers,
  contributions, artifacts, evidence items, and limitations when present.
- Final EvidenceManifest export is valid only from completed, failed,
  cancelled, or closed WorkSession state.
- Redacted exports are derived artifacts.
- Redaction never replaces the source evidence record.
- EvidenceManifest MUST exclude product-private fields, credentials, secrets,
  raw runtime state, host-only database ids, deployment details, billing data,
  private scores, and product UI state.

Rejections:

```txt
invalid_evidence_export_state
forbidden_export_field
sealed_evidence_mutation
```

## LearningRecord

LearningRecord records what improved because of a WorkSession or accepted
OutcomeReport.

LearningRecord subject types:

```txt
human
agent
pair
```

LearningRecord review states:

```txt
proposed
accepted
rejected
superseded
```

Rules:

- Learning is not only agent memory.
- Jarvis records human learning, agent learning, and pair learning.
- LearningRecord references source events. OutcomeReport-backed
  LearningRecords use the OutcomeReport acceptance JarvisEvent as
  `source_event_refs` and may also record `outcome_report_refs`.
- LearningRecord may reference MemoryProposal or SkillProposal.
- LearningRecord does not create durable memory or active skill behavior by
  itself.

## MemoryProposal

MemoryProposal records a proposed durable memory change.

MemoryProposal states:

```txt
proposed
pending_review
accepted
rejected
superseded
expired
```

Rules:

- Memory does not silently mutate.
- Model-derived memory cannot confirm itself.
- Tool-derived memory cannot confirm itself.
- Durable preferences, boundaries, permissions, broad facts, and
  cross-session behavior require review.
- Accepted MemoryProposal creates durable memory only inside its declared
  memory_scope.
- Accepted MemoryProposal requires review_refs.
- Rejected, superseded, or expired MemoryProposal does not affect retrieval.

Rejections:

```txt
silent_memory_mutation
model_self_confirmed_memory
tool_self_confirmed_memory
```

## SkillProposal

SkillProposal records a proposed reusable way of working.

SkillProposal states:

```txt
proposed
pending_review
accepted
rejected
superseded
archived
```

Rules:

- Skills are procedural memory.
- Unreviewed skill changes do not become active.
- Accepted SkillProposal creates active skill behavior only inside its declared
  skill_scope.
- Skill changes cannot expand tool access without separate policy review.
- Accepted SkillProposal requires review_refs.
- Rejected, superseded, or archived SkillProposal does not affect active skill
  behavior.

Rejections:

```txt
silent_skill_activation
skill_expands_tool_access_without_policy_review
```

## OutcomeReport

OutcomeReport is an optional post-session feedback extension.

OutcomeReport records attributable feedback that arrives after a WorkSession
export. It closes the learning loop without rewriting completed work.

Rules:

- OutcomeReport arrives after a WorkSession is completed, failed, cancelled, or
  closed.
- OutcomeReport does not mutate the sealed WorkSession.
- OutcomeReport does not mutate the sealed EvidenceManifest.
- OutcomeReport creates or references governed LearningRecord.
- OutcomeReport is not an evaluation system.
- OutcomeReport is not payment, scoring, settlement, or marketplace logic.
- OutcomeReport remains an extension and does not change the v0 core object
  list.

Rejections:

```txt
sealed_work_session_mutation
sealed_evidence_mutation
outcome_report_without_learning_record
```

## Conformance

A compatible implementation proves:

```txt
Mutating attribution, evidence, learning, proposal, export, and OutcomeReport
operations require Jarvis-Protocol-Version, Jarvis-Actor-Id,
Jarvis-Idempotency-Key, Jarvis-Request-Timestamp,
Jarvis-Expected-WorkSession-Revision, and Jarvis-Previous-Event-Hash.
Contribution preserves contributor refs.
Shared Contribution preserves individual contributors.
Evidence item refs link to source JarvisEvents.
EvidenceManifest export only happens from valid WorkSession states.
EvidenceManifest excludes forbidden export fields.
LearningRecord subject_type is human, agent, or pair.
MemoryProposal cannot self-confirm from model or tool output.
SkillProposal cannot activate without review.
SkillProposal cannot expand tool access without policy review.
OutcomeReport creates or references LearningRecord.
OutcomeReport does not mutate sealed WorkSession or EvidenceManifest.
```
