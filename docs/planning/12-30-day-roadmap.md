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
- AG-UI standardizes agent-to-frontend interaction. Jarvis feeds AG-UI
  interfaces with WorkSession state, Requests, Reviews, and EvidenceManifest
  data, but Jarvis is not a frontend protocol.
- Agent SDKs, coding agents, local agents, and hosted agent products provide
  runtimes, tools, sessions, handoffs, tracing, or execution environments.
  Compatible adapters map their work into collaboration records instead of
  replacing them.

Protocol grounding:

- MCP: https://modelcontextprotocol.io/specification/
- A2A: https://a2a-protocol.org/latest/
- AG-UI: https://docs.ag-ui.com/
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
- RFC 8785 JSON Canonicalization Scheme:
  https://www.rfc-editor.org/rfc/rfc8785
- W3C PROV provenance model: https://www.w3.org/TR/prov-overview/

## North Star For The 30 Days

By the end of 30 days, we show:

```txt
Garden POC plus one real existing-agent adapter
  -> map HumanWorker + AgentWorker work into Jarvis protocol records
  -> HumanWorker starts WorkSession
  -> AgentWorker acts inside Policy
  -> blocked action creates Request
  -> HumanWorker reviews or takes over
  -> Contribution ledger records who did what
  -> EvidenceManifest exports portable proof
  -> LearningRecord captures human, agent, and pair learning
  -> next WorkSession starts with governed improvements
```

The demo does not need a perfect platform. It needs a real end-to-end protocol
proof.

## Week 1: Protocol Lock And Research Grounding

Goal: freeze the core protocol vocabulary and remove ambiguity.

Deliverables:

- finalize `11-core-protocol-objects.md`
- define required fields for each core object
- define WorkSession state transitions
- define Request, Review, and Takeover lifecycle
- define PolicyDecision semantics
- define EvidenceManifest minimum export shape
- define LearningRecord, MemoryProposal, and SkillProposal review states
- define OutcomeReport as an optional post-session feedback extension
- write a short protocol positioning note against MCP, A2A, AG-UI, and agent
  SDKs

Done when:

- every document uses the same core object names
- no document describes Jarvis as a runtime, product, agent framework, or
  agent application
- every core object has a reason to exist
- Jarvis is explained in one paragraph without mentioning any host product
  or downstream evaluation system

## Week 2: Schemas, Conformance, And Adapter Surface

Goal: make Jarvis implementable by another product or agent adapter.

Deliverables:

- JSON schemas for core protocol objects
- event envelope schema
- portable export schema
- golden-path conformance checklist
- failure-mode conformance checklist
- adapter contract for mapping existing agents into Jarvis protocol records
- first JSON example WorkSession

Adapter contract must answer:

- how an existing agent becomes an `AgentWorker`
- how a human becomes a `HumanWorker`
- how agent actions become `JarvisEvent`
- how tool calls become `PolicyDecision` and `EvidenceManifest` entries
- how a blocked action becomes `Request`
- how a human response becomes `Review` or `Takeover`
- how corrections become `LearningRecord`, `MemoryProposal`, or
  `SkillProposal`

Done when:

- a developer implements a minimal Jarvis-compatible host from the schemas
- conformance rejects a fake implementation that skips policy, review,
  evidence, or learning
- adapters do not require the agent runtime to be rewritten

## Week 3: Garden POC Product Proof

Goal: use Garden POC as the first product proof without making Jarvis depend on
Garden. The POC proves the protocol before main Garden adopts it.

Deliverables:

- map Garden POC concepts to Jarvis objects
- create one Garden-backed WorkSession flow
- show HumanWorker objective entry
- show AgentWorker execution inside policy
- show Request inbox when the agent needs permission or judgment
- show Review decision and optional Takeover
- record Contribution entries
- produce EvidenceManifest export
- produce LearningRecord and MemoryProposal after review
- document what belongs to Garden and what belongs to Jarvis

Done when:

- Garden POC demonstrates the Jarvis loop end to end
- Jarvis protocol records export from Garden POC
- the exported records do not contain Garden-private assumptions
- the demo proves human and agent both improve, not only agent memory

## Week 4: Interoperability Demo And Public Story

Goal: prove Jarvis works with existing agents and is worth discussing publicly.

Deliverables:

- one Garden POC demo
- one CLI-agent adapter demo
- one real external-agent or SDK-agent adapter demo
- public README tightened around protocol positioning
- protocol examples for WorkSession, Request, Review, EvidenceManifest, and
  LearningRecord
- conformance checklist published
- GitHub Pages simulation updated to show the 30-day proof path
- short public narrative: why Jarvis exists and what it does not replace

First Adapter Targets:

- Claude Code-style CLI adapter
- Hermes/OpenClaw-style local agent adapter
- OpenAI Agents SDK-style runtime adapter
- MCP tool-use adapter

Done when:

- at least two different host or adapter shapes produce the same Jarvis protocol
  records
- Garden POC is one product proof, not the protocol itself
- the team shares one URL and one README that explain the point clearly
- the protocol is discussed as a standard, not an internal app feature

## Daily Operating Rhythm

Every day produces one visible artifact:

- spec page
- schema
- JSON example
- conformance test/checklist
- adapter note
- Garden POC mapping
- demo screenshot
- public docs update

Daily checks:

1. Did we strengthen the protocol or drift into building a runtime?
2. Does this work with an existing agent without rewriting the agent?
3. Did we capture human judgment, agent action, contribution, evidence, and
   learning?
4. Does another product implement this without Garden-specific assumptions?
5. Does this improve the next WorkSession?

## Non-Negotiables

- Jarvis remains protocol-only.
- Garden POC is only the first product proof.
- Existing agents remain first-class.
- HumanWorker and AgentWorker are both actors.
- Learning belongs to the human, agent, and pair.
- Evidence is captured during work.
- Contributions remain attributable.
- Memory and skills do not silently mutate.
- Compatibility matters more than owning the runtime.

## First 72 Hours

1. Freeze the object model in `11-core-protocol-objects.md`.
2. Create JSON examples for one complete WorkSession.
3. Draft the adapter contract for mapping an existing agent.
4. Map Garden POC concepts to Jarvis objects.
5. Decide the first two proof paths: Garden POC plus one CLI/external-agent
   adapter.

Once these are clear, the rest of the 30 days becomes execution rather than
debate.
