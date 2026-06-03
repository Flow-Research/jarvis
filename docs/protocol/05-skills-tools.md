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
instructions
required_context
required_tools
examples
failure_cases
review_checklist
supporting_files
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

Full skill bodies and supporting files load on demand. This preserves context
budget and lets the host cache stable inventories.

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
policy wrapper
provenance
observability hooks
```

The agent sees tools through Jarvis policy contracts. Raw host capabilities
stay behind policy.

## MCP Tools

MCP is the connector boundary. MCP servers remain untrusted until Jarvis
classifies them.

Jarvis treats MCP tools as untrusted until classified:

- tool metadata is potentially malicious
- tool descriptions carry prompt-injection risk
- tool lists change over time
- tool outputs include untrusted instructions
- remote servers expose over-broad capabilities

Compatible hosts support:

- MCP server allowlists
- tool filtering
- risk classification
- scope mapping
- output trust labels
- per-tool approval rules
- tool inventory diffing

## Host MCP Gateway

A compatible host routes MCP through a gateway when MCP is used. Jarvis defines
the classification, policy, evidence, and trust records:

- pins server identity
- records full capability inventory name/schema/version/hash
- quarantines changed capability inventories
- disables new or changed capabilities until reviewed or classified
- strips tool, prompt, and resource descriptions from instruction authority
- classifies every tool, resource, prompt, sampling, elicitation, and roots
  capability by risk and sensitivity
- labels outputs as untrusted data
- brokers OAuth and delegated identity scopes
- records inventory diffs as events

MCP is a connector protocol, not a trust boundary.

Raw MCP tool, prompt, and resource descriptions are never inserted as
instructions. The host stores raw metadata as untrusted evidence, then exposes
a sanitized capability summary after classification. New, removed, or changed
capability schema/hash enters quarantine until reviewed or policy-classified.

MCP prompts and resources are untrusted data. Server-initiated sampling,
elicitation, roots changes, and capability changes are denied unless explicitly
granted. The host gateway hashes and diffs the full MCP capability surface. Any
changed resource, prompt, tool, sampling, elicitation, or roots surface enters
quarantine before exposure.

## Execution Tools

Execution tools are host-provided capabilities that Jarvis governs and records.

Execution tools support:

- command execution
- file read/write
- package installation when permitted
- artifact creation
- broker handle or tool-bound token injection under policy
- network egress controls
- process/session inspection

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

Failures are learning signals, not just errors.
