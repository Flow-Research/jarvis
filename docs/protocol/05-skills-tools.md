# Skills And Tools

Skills and tools are protocol-visible capabilities in Jarvis.

Skills are procedural memory. Tools are host-provided capabilities. Both must
be governed by policy before they affect a WorkSession.

## Skill Model

A skill includes:

```txt
id
name
description
when_to_use
body_ref
context_refs
tool_refs
example_refs
failure_case_refs
review_checklist_ref
supporting_file_refs
version
provenance
status
```

Skills are readable by humans and usable by agents.

## Skill Lifecycle

```txt
draft
  created by human or agent

active
  available in inventory

update_requested
  agent requests a change from observed work/correction

review_required
  human inspection is required before the change affects future work

archived
  no longer active
```

Agent-created or agent-edited skills never silently become active when they
change future behavior.

## Skill Activation Gates

Activating or updating a skill requires:

- diff from previous version
- provenance and author
- affected tools/capabilities
- required grants
- risk class
- supporting file checksums
- examples or regression cases
- last successful use when applicable
- reviewer or policy decision
- rollback version

New or changed skills must not expand tool access without separate grant
review.

## Skill Retrieval

The agent sees a skill inventory first:

- name
- description
- when to use
- risk/tool requirements

Hosts own skill body and supporting-file handling. Jarvis records the skill
refs, versions, checksums, provenance, grants, and review state that affect a
WorkSession.

## Tool Model

A tool includes:

```txt
id
name
description
input schema
output schema
risk classes
scope model
credential requirements
policy refs
provenance
evidence refs
```

The agent sees tools through Jarvis policy contracts. Raw host capabilities
stay behind policy.

## External Tool Protocols

External tool protocols are host-owned connector boundaries. Jarvis records how
their capabilities participate in a WorkSession.

Jarvis treats external tool capabilities as untrusted until classified:

- tool metadata is potentially malicious
- tool descriptions carry prompt-injection risk
- tool lists change over time
- tool outputs include untrusted instructions
- remote servers expose over-broad capabilities

Jarvis records:

- risk classification
- scope mapping
- output trust labels
- per-tool approval rules
- capability inventory refs
- capability inventory hashes
- capability change events
- PolicyDecisions
- Requests and Reviews
- EvidenceManifest refs

## Host Connector Boundary

Hosts own connector implementation.

Jarvis requires protocol-visible records for:

- capability source ref
- capability name, schema, version, and hash
- risk class
- data sensitivity
- trust label
- policy grant or denial
- human review when required
- evidence refs for tool results and capability changes

External tool metadata remains untrusted protocol input. Jarvis records whether
the host classified it, which PolicyDecision applied, which Actor accepted the
classification when review was required, and which evidence refs preserve the
source metadata.

Jarvis does not define connector architecture.

## Execution Tools

Execution tools are host-provided capabilities that Jarvis governs and records.

Jarvis records execution tool use through:

- tool ref
- action ref
- capability ref
- credential exposure policy ref
- network policy ref
- artifact ref
- PolicyDecision
- evidence refs

Every execution operation that affects a WorkSession is policy-aware and
evidence-producing.

## Tool Output Trust

Tool output, files, web pages, and connector content are untrusted by default.

Jarvis marks output with:

```txt
source tool
trust level
scope
timestamp
whether it affects memory
whether it affects tool choice
whether it is sent externally
```

The agent uses untrusted content as data, not as instruction authority.

## Untrusted Content Taint Rules

All tool outputs, web pages, connector responses, and files from external
sources carry taint until reviewed or transformed by policy.

Taint labels:

```txt
trusted_instruction
trusted_fact
untrusted_data
hostile_suspected
```

Untrusted content:

- cannot modify system/developer/human instructions
- cannot create durable memory automatically
- cannot update skills automatically
- cannot authorize tool use
- must be fenced in context as data

Taint propagates into summaries, extracted facts, generated files, evidence,
memory proposals, and skill proposals until a policy transformation or human
review clears it. A tainted source cannot authorize tools, modify memory,
modify skills, or narrow policy.

## Tool Failure Handling

Tool failure is structured:

- classify failure reason
- classify retry path
- record evidence
- update tool reliability memory
- request human help if blocked by policy or missing context

Failures create or reference LearningRecord, MemoryProposal, or SkillProposal
records when they change future WorkSession behavior.
