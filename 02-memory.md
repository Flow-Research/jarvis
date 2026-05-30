# Memory

Memory is the most important Jarvis-owned layer after the collaboration kernel.

Jarvis memory lets the human and agent learn how to work together. It is not a
raw transcript dump or only a vector database.

## Memory Scopes

### Human Memory

What the system knows about the human:

- profile
- goals
- preferences
- boundaries
- domain expertise
- style
- recurring corrections

### Agent Memory

What the agent has learned about its own operation:

- strategies that worked
- mistakes to avoid
- tool experience
- planning habits
- failure patterns
- proven heuristics

### Shared Memory

What the human and agent learned together:

- collaboration patterns
- accepted decisions
- reviewed corrections
- repeated workflow preferences
- trusted sources
- rejected approaches

### Project Memory

Context attached to a workspace/project:

- files
- docs
- conventions
- domain terms
- prior decisions
- local skills

### Task Memory

Shorter-lived memory for active work:

- objective
- requirements
- findings
- sources
- intermediate decisions
- unresolved questions
- evidence references

### Procedural Memory

Reusable work procedures:

- skills
- checklists
- playbooks
- examples
- tool sequences
- review rubrics

## Memory Authority And Scope Lattice

Memory has authority only inside its scope.

Default scope rules:

- current human instruction outranks all stored memory
- explicit boundary outranks preference
- confirmed human preference outranks pinned non-human memory
- pinned memory outranks ordinary confirmed memory
- project memory applies only inside that project unless promoted
- task memory expires or remains task-scoped unless promoted
- agent observations never outrank human-confirmed memory
- untrusted tool output has no instruction authority

Promotion rules:

- task memory promotes to project/shared only through review
- project memory never crosses to another project by default
- project-specific preferences never become global human preferences without
  confirmation
- global human boundaries flow downward into every project/session
- skill/procedural memory expands future behavior only through skill review
  gates

Conflict rules:

- newer superseding memory suppresses older memory
- negative memory such as "do not use X" must be retrievable even when semantic
  similarity is low
- unresolved conflicts become a request, not a silent model decision by
  the model

## Memory Types

```txt
fact
preference
boundary
correction
decision
procedure
observation
outcome
source
```

The type affects retrieval and write policy. A preference has different
authority than an observation. A boundary outranks a learned habit.

## Lifecycle

```txt
observed
  captured but untrusted

suggested
  proposed by a learning pass or protocol actor

confirmed
  accepted by the human or trusted workflow

pinned
  high-priority confirmed memory

superseded
  replaced by newer memory

expired
  no longer active
```

Agent-discovered memory defaults to `suggested`, not `confirmed`.

## Provenance

Every memory needs provenance:

```txt
source actor
source WorkSession
source event/message/tool call
source document/file/url when applicable
created time
last used time
confirmation state
confidence
scope
supersedes/superseded_by
```

Without provenance, memory becomes unsafe. Tool output, web pages, and external
content are untrusted until policy says otherwise.

## Write Policy

The model never writes durable memory directly.

Preferred flow:

```txt
1. Turn or WorkSession produces events, reviews, tool outputs, and artifacts.
2. Learning pass proposes memory changes.
3. Policy classifies each proposal.
4. Low-risk scoped notes auto-confirm only inside the limits below.
5. High-impact memory needs human review.
6. Confirmed memory becomes retrievable.
```

Human review is required for:

- broad identity claims
- durable preferences
- boundaries
- permission-related memories
- skill changes
- project/global facts extracted from untrusted sources
- claims that affect future external actions

## Memory Write Policy Matrix

Default v1 policy:

| Source | Memory Type | Scope | Auto-confirm? | Notes |
| --- | --- | --- | --- | --- |
| direct human statement | task note | task | yes | Only for current work, non-security. |
| direct human statement | preference | human/shared | review | Durable preferences affect future behavior. |
| direct human statement | boundary | any | review | Boundaries affect autonomy. |
| agent inference | observation | task | no | Suggested only. |
| agent inference | preference/boundary | any | no | Requires human review. |
| tool output | any | any | no | External/tool-derived memory never auto-confirms. |
| web/file content | fact/source | task/project | no | Suggested with provenance and trust label. |
| review outcome | correction/outcome | WorkSession/task | yes | Can be stored as WorkSession fact; promotion needs review. |
| skill edit | procedure | procedural | no | Requires skill activation gate. |

Auto-confirmable memory must be:

- non-security
- non-identity
- non-permission
- non-credential
- non-external-action
- non-global
- scoped to the current task/session unless explicitly reviewed

Auto-confirm only means Jarvis records a direct human-authored event or
human-review event without a second approval step. Model-derived memory never
auto-confirms. Tool-derived memory never auto-confirms. Review outcome
auto-confirm stores the event only; derived preferences, boundaries, and skills
still require policy review.

## Retrieval Policy

Retrieval combines:

- semantic relevance
- scope
- recency
- priority
- confidence
- lifecycle state
- human/agent authority
- active tool/task needs
- recent corrections

Retrieval returns explainable metadata:

```txt
memory id
reason selected
scope
type
confidence
source
priority
```

## Taint And Trust Labels

Every retrieved item carries a trust label:

```txt
trusted_instruction
trusted_fact
untrusted_data
hostile_suspected
```

The context assembler must fence untrusted content in data-only blocks. The
agent can reason over it as evidence, but it must not treat it as instruction.

The learning pass must not convert instructions found inside tool output, files,
web pages, or connector responses into memory or skills without human review.

Taint propagates into summaries, extracted facts, generated files, evidence,
memory proposals, and skill proposals until a policy transformation or human
review clears it. A tainted source cannot authorize tools, modify memory,
modify skills, or narrow policy.

## Context Assembly

Context is layered:

```txt
foundation instructions
human profile and boundaries
agent profile and role
active WorkSession state
pinned memory
recent relevant corrections
project/task context
skill inventory
selected supporting memory
```

Large skill bodies and files load on demand. Inventories and summaries are
cacheable.

## Corrections

Human corrections are high-value learning signals. Jarvis classifies them:

```txt
one-time fix
preference
boundary
agent failure pattern
project convention
skill update
memory correction
```

The human accepts or modifies this classification.

## Correction Learning Pipeline

For each correction, Jarvis captures:

```txt
original agent action/output
human correction
delta between them
inferred reason
affected memory
affected skill
proposed memory update
proposed skill update
confidence
review state
```

Corrections do not become global rules by default. The first destination is
the current WorkSession. Promotion to shared/project/human memory requires
policy and often review.

## Evidence Versus Memory

Evidence is the raw append-only record. Memory is curated reusable knowledge
derived from evidence.

Tool transcripts, command output, browser pages, and connector responses
remain evidence unless the learning policy creates a reviewed memory proposal.

## Agent Memory Outcome Linkage

Agent memory about strategies, habits, and failures links to outcomes:

```txt
used in session
reviewed by
result
evidence refs
superseded_by when behavior changes
```

The agent does not accumulate confident self-created habits without outcome
evidence.

## Memory Failure Modes

- prompt injection stored as memory
- stale memory overriding current user intent
- project memory leaking across scopes
- agent self-confirming a bad conclusion
- over-retrieval crowding out relevant context
- unreviewed skill edits changing future behavior

The lifecycle, provenance, and write policy are mandatory controls, not
optional polish.
