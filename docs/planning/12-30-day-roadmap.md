# 30-Day Roadmap

This roadmap turns Jarvis from design into a credible protocol proof.

Jarvis is not an agent framework, runtime, agent adapter package, cloud stack, or
product UI. Jarvis is the human-agent collaboration and learning-loop
protocol. The next 30 days prove that existing agents and products are
mapped into Jarvis protocol records without replacing their runtime.

## Thesis

The world already has agent runtimes, tools, UI protocols, and agent-to-agent
protocols. Jarvis must not compete with them.

Jarvis wins by defining the missing standard record for:

- HumanWorker and AgentWorker collaboration
- policy-governed autonomy
- Requests when the agent is blocked
- Reviews and Takeovers from the human
- attributable Contributions
- portable EvidenceManifest
- governed LearningRecords
- MemoryProposal and SkillProposal loops

The practical proof is simple: a human and an existing agent complete real
work through a WorkSession, produce evidence, record who did what, and leave
behind learning that improves the next WorkSession.

## Current Protocol Landscape

Jarvis sits beside existing standards:

- MCP standardizes how LLM apps connect to external tools, resources, and
  prompts. Jarvis records MCP tool use as protocol evidence, but Jarvis is
  not MCP.
- A2A standardizes agent-to-agent communication and delegation. Jarvis records
  A2A delegation inside a WorkSession, but Jarvis is not A2A.
- AG-UI standardizes agent-to-frontend interaction. Hosts may expose Jarvis
  WorkSession records to AG-UI clients, but Jarvis does not define frontend
  events, rendering, UI state, or UI transport.
- Agent SDKs, coding agents, local agents, and hosted agent products provide
  runtimes, tools, sessions, handoffs, tracing, or execution environments.
  Compatible adapters map their work into collaboration records instead of
  replacing them.

Protocol grounding:

- MCP: https://modelcontextprotocol.io/specification/
- A2A: https://a2a-protocol.org/latest/
- AGNTCY ACP: https://spec.acp.agntcy.org/
- AG-UI: https://docs.ag-ui.com/
- OpenAPI 3.1.1: https://spec.openapis.org/oas/v3.1.1.html
- RFC 8785 JSON Canonicalization Scheme:
  https://www.rfc-editor.org/rfc/rfc8785
- W3C PROV provenance model: https://www.w3.org/TR/prov-overview/

## North Star For The 30 Days

By the end of 30 days, we show:

```txt
Jarvis OpenAPI 3.1 contract
  -> protocol objects
  -> protocol operations
  -> zero-trust security requirements
  -> portable export
  -> conformance fixtures
  -> existing-agent adapter contract
  -> compatible example readiness
```

Compatible examples start after the protocol semantics, OpenAPI contract,
and conformance entry rules are stable.

## Week 1: Protocol Lock And Research Grounding

Status: complete.

Goal: freeze the core protocol vocabulary, communication strategy, and security
boundary.

Deliverables:

- finalize `11-core-protocol-objects.md`
- lock OpenAPI 3.1 as the machine-readable communication contract
- define required fields for each core object
- define WorkSession state transitions
- define Request, Review, and Takeover lifecycle
- define PolicyDecision semantics
- define EvidenceManifest minimum export shape
- define LearningRecord, MemoryProposal, and SkillProposal review states
- define OutcomeReport as an optional post-session feedback extension
- write the protocol positioning note against MCP, A2A, ACP, AG-UI, and agent
  SDKs
- define zero-trust OpenAPI headers, security schemes, and forbidden export
  fields

Done when:

- every document uses the same core object names
- no document describes Jarvis as a runtime, product, agent framework, or
  agent application
- every core object has a reason to exist
- OpenAPI 3.1 is the machine-readable communication contract
- host implementation work was not part of Week 1 active work
- Jarvis is explained in one paragraph without mentioning any host application
  or external evaluation

## Week 2: OpenAPI Contract And Conformance Entry

Status: active.

Goal: produce the first OpenAPI 3.1 contract shape and conformance entry rules.

Deliverables:

- OpenAPI 3.1 document skeleton
- `components.schemas` for core protocol objects
- path layout for core protocol operations
- event envelope component
- portable export component
- security schemes and required protocol headers
- protocol error model
- golden-path conformance checklist
- failure-mode conformance checklist
- first OpenAPI examples for WorkSession, Request, Review, and export

OpenAPI contract must answer:

- how a host creates a WorkSession
- how a host appends JarvisEvent records
- how AgentWorker actions record PolicyDecision
- how blocked action creates Request
- how HumanWorker response records Review or Takeover
- how Contribution and EvidenceManifest records are exported
- how OutcomeReport feeds post-session learning

Done when:

- a developer reads the OpenAPI contract and implements a minimal
  Jarvis-compatible host
- conformance rejects a fake implementation that skips policy, review,
  evidence, or learning
- host implementation work is still out of scope

## Week 3: Adapter Contract And Conformance Fixtures

Goal: prove the OpenAPI contract against examples, fixtures, and one
existing-agent adapter contract.

Deliverables:

- adapter contract for mapping existing agents into Jarvis protocol records
- valid and invalid OpenAPI examples
- golden-path fixture
- stale takeover fixture
- missing policy fixture
- unresolved Request fixture
- forbidden host-private export fixture
- CLI/existing-agent adapter plan

Done when:

- two host shapes produce equivalent Jarvis protocol records on paper
- conformance fixtures catch unsafe or incomplete implementations
- adapter work does not require rewriting the agent runtime
- compatible examples start only after the conformance gate

## Week 4: Compatible Examples And Public Story

Goal: prepare compatible examples after the protocol contract and
conformance gate are credible.

Deliverables:

- compatible host mapping example
- one CLI-agent adapter proof plan
- one real external-agent or SDK-agent adapter proof plan
- public README tightened around protocol positioning
- protocol examples for WorkSession, Request, Review, EvidenceManifest, and
  LearningRecord
- conformance checklist published
- GitHub Pages simulation updated to show the OpenAPI proof path
- short public narrative: why Jarvis exists and what it does not replace

First Adapter Targets:

- Claude Code-style CLI adapter
- Hermes/OpenClaw-style local agent adapter
- OpenAI Agents SDK-style runtime adapter
- MCP tool-use adapter

Done when:

- at least two different host or adapter shapes have a credible implementation
  plan against the same OpenAPI contract
- a compatible host example maps real work into Jarvis records without becoming the
  protocol itself
- the team shares one URL and one README that explain the point clearly
- the protocol is discussed as a standard, not an internal app feature

## Daily Operating Rhythm

Every day produces one visible artifact:

- spec page
- OpenAPI section
- OpenAPI example
- conformance test/checklist
- adapter note
- security note
- protocol diagram or conformance output
- public docs update

Daily checks:

1. Did we strengthen the protocol or drift into building a runtime?
2. Does this work with an existing agent without rewriting the agent?
3. Did we capture human judgment, agent action, contribution, evidence, and
   learning?
4. Does another product implement this without host-application-specific assumptions?
5. Does this improve the next WorkSession?

## Non-Negotiables

- Jarvis remains protocol-only.
- Compatible examples stay outside the protocol core.
- Existing agents remain first-class.
- HumanWorker and AgentWorker are both actors.
- Learning belongs to the human, agent, and pair.
- Evidence is captured during work.
- Contributions remain attributable.
- Memory and skills do not silently mutate.
- Compatibility matters more than owning the runtime.

## First 72 Hours

1. Freeze the object model in `11-core-protocol-objects.md`.
2. Lock OpenAPI 3.1 as the communication contract.
3. Define core operations and zero-trust headers.
4. Define OpenAPI component layout.
5. Define conformance entry rules.

Once these are clear, the rest of the 30 days becomes execution rather than
debate.
