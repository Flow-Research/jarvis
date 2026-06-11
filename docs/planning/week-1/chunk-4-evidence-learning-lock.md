# Chunk 4: Contribution, Evidence, And Learning Lock

Chunk 4 locks attribution, portable proof, and governed learning.

This chunk defines how Jarvis records who contributed, what evidence was
captured, what the human-agent pair learned, and how memory or skill changes
become governed proposals instead of silent durable behavior.

This chunk does not define payment, scoring, task evaluation, external evaluation
behavior, model training, host analytics, storage implementation, or host
implementation behavior.

## Scope

Chunk 4 locks:

```txt
Contribution minimum shape
Contribution ledger rules
EvidenceManifest minimum export shape
evidence capture timing rules
evidence item reference rules
LearningRecord semantics
MemoryProposal review states
SkillProposal review states
OutcomeReport extension semantics
post-session feedback learning boundary
forbidden export fields
conformance checks for attribution, evidence, and governed learning
```

## Non-Goals

Chunk 4 does not:

- define compensation
- define marketplace scoring
- define reviewer payout
- define external evaluation
- define host analytics
- define model fine-tuning
- define vector database behavior
- define storage tables
- define host implementation behavior

## Attribution Thesis

Jarvis records work as attributable collaboration.

HumanWorker, AgentWorker, service, tool, and shared contributions remain
distinguishable.

Shared contribution never erases the individual contributing actors.

Contribution is not payment. Contribution is the protocol record external
systems inspect.

## Evidence Thesis

Evidence is captured during work.

Evidence is not reconstructed only at the end.

EvidenceManifest is the portable proof package for a WorkSession. It references
the event chain, policy decisions, requests, reviews, takeovers, contributions,
artifacts, evidence item refs, limitations, and export profile.

## Learning Thesis

Learning belongs to the human, the agent, and the pair.

LearningRecord records what improved.

MemoryProposal and SkillProposal record proposed durable changes.

Durable memory and active skill behavior require governed review.

OutcomeReport closes the post-session feedback loop without mutating the sealed
WorkSession or EvidenceManifest.

## Locked Invariants

Compatible implementations MUST enforce these invariants:

```txt
Every Contribution references WorkSession and contributing actor or worker refs.
Contribution with contributor_type shared preserves individual contributor refs.
Contribution is not compensation, payment, score, or settlement.
Evidence is captured during work and linked to JarvisEvents.
EvidenceManifest exports only from completed, failed, cancelled, or closed WorkSession.
EvidenceManifest excludes host-private fields and secrets.
Redaction creates derived export artifacts and never replaces source evidence.
LearningRecord subject_type is human, agent, or pair.
MemoryProposal and SkillProposal start as proposed or pending review states.
Model-derived memory cannot confirm itself.
Tool-derived memory cannot confirm itself.
Unreviewed skill changes do not become active behavior.
Skill changes cannot expand tool access without separate policy review.
OutcomeReport does not mutate sealed WorkSession or EvidenceManifest.
OutcomeReport creates or references governed LearningRecord.
```

## Required Review States

LearningRecord review states:

```txt
proposed
accepted
rejected
superseded
```

MemoryProposal states:

```txt
proposed
pending_review
accepted
rejected
superseded
expired
```

SkillProposal states:

```txt
proposed
pending_review
accepted
rejected
superseded
archived
```

Accepted MemoryProposal creates durable memory only inside its declared scope.

Accepted SkillProposal creates active skill behavior only inside its declared
scope and only when required policy review has also approved needed tool access.

## Required Rejection Reasons

Compatible implementations reject:

```txt
missing_contribution_actor
invalid_contributor_refs
shared_contribution_without_individual_refs
evidence_after_the_fact
missing_evidence_event_refs
invalid_evidence_export_state
forbidden_export_field
silent_memory_mutation
silent_skill_activation
model_self_confirmed_memory
tool_self_confirmed_memory
skill_expands_tool_access_without_policy_review
sealed_work_session_mutation
sealed_evidence_mutation
outcome_report_without_learning_record
```

## Reviewer Focus

Reviewers must verify:

- Contribution distinguishes human, agent, service, tool, and shared work
- EvidenceManifest is portable proof, not host analytics
- evidence is captured during work
- learning records human, agent, and pair improvement
- memory and skill proposals cannot silently mutate durable behavior
- OutcomeReport remains an extension and does not become evaluation ownership
- export boundaries exclude host-private and secret fields

## Done Criteria

Chunk 4 is complete when:

- [13-contribution-evidence-learning.md](../../protocol/13-contribution-evidence-learning.md)
  locks attribution, evidence, and governed learning semantics
- [11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
  matches the locked Contribution, EvidenceManifest, LearningRecord,
  MemoryProposal, SkillProposal, and OutcomeReport states
- [14-protocol-lock.md](../../protocol/14-protocol-lock.md) states the same
  attribution, evidence, and learning invariants
- conformance and package docs mention contribution attribution, evidence
  timing, export state, proposal review states, and OutcomeReport boundaries
- local checks pass
- Zero-Trust Security Reviewer plus at least three other reviewer lanes pass
- valid findings are integrated
- rejected findings are recorded with concrete reasons
- PR is opened
