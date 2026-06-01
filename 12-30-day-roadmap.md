# 30-Day Roadmap

This roadmap turns Jarvis from design into a credible protocol proof.

Jarvis is not an agent framework, runtime, agent harness, cloud stack, or
product UI. Jarvis is the human-agent collaboration and learning-loop
protocol. The next 30 days must prove that existing agents and products can be
wrapped with Jarvis contracts without replacing their runtime.

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

The practical proof is simple: a human and an existing agent should complete
real work through a WorkSession, produce evidence, record who did what, and
leave behind learning that improves the next WorkSession.

## Current Protocol Landscape

Jarvis should position itself beside existing standards:

- MCP standardizes how LLM apps connect to external tools, resources, and
  prompts. Jarvis can record MCP tool use as protocol evidence, but Jarvis is
  not MCP.
- A2A standardizes agent-to-agent communication and delegation. Jarvis can
  record A2A delegation inside a WorkSession, but Jarvis is not A2A.
- AG-UI standardizes agent-to-frontend interaction. Jarvis can feed AG-UI
  interfaces with WorkSession state, Requests, Reviews, and EvidenceManifest
  data, but Jarvis is not a frontend protocol.
- Agent SDKs and agent products such as OpenAI Agents SDK, Claude Code, Hermes,
  and OpenClaw provide runtimes, tools, sessions, handoffs, tracing, or
  execution environments. Jarvis wraps their work into collaboration records
  instead of replacing them.

Protocol grounding:

- MCP: https://modelcontextprotocol.io/specification/
- A2A: https://a2a-protocol.org/latest/
- AG-UI: https://docs.ag-ui.com/
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/

## North Star For The 30 Days

By the end of 30 days, we must be able to show:

```txt
Existing agent or Garden POC
  -> wrapped by Jarvis protocol adapter
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
- write a short protocol positioning note against MCP, A2A, AG-UI, and agent
  SDKs

Done when:

- every document uses the same core object names
- no document describes Jarvis as a runtime, product, agent framework, or
  personal agent
- every core object has a reason to exist
- we can explain Jarvis in one paragraph without mentioning any host product
  or downstream evaluation system

## Week 2: Schemas, Conformance, And Adapter Surface

Goal: make Jarvis implementable by another product or agent wrapper.

Deliverables:

- JSON schemas for core protocol objects
- event envelope schema
- portable export schema
- golden-path conformance checklist
- failure-mode conformance checklist
- adapter contract for wrapping existing agents
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

- a developer can implement a minimal Jarvis-compatible host from the schemas
- conformance can reject a fake implementation that skips policy, review,
  evidence, or learning
- adapters do not require the agent runtime to be rewritten

## Week 3: Garden POC End-To-End Integration

Goal: use the existing Garden POC as the first host proof, without making
Jarvis depend on Garden.

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

- Garden can demonstrate the Jarvis loop end to end
- Jarvis protocol records can be exported from the Garden POC
- the exported records do not contain Garden-private assumptions
- the demo proves human and agent both improve, not only agent memory

## Week 4: Interoperability Demo And Public Story

Goal: prove Jarvis works with existing agents and is worth discussing publicly.

Deliverables:

- one Garden POC demo
- one CLI-agent wrapper demo
- one external-agent or simulated-agent wrapper demo
- public README tightened around protocol positioning
- protocol examples for WorkSession, Request, Review, EvidenceManifest, and
  LearningRecord
- conformance checklist published
- GitHub Pages simulation updated to show the 30-day proof path
- short public narrative: why Jarvis exists and what it does not replace

Candidate wrappers:

- Claude Code-style CLI wrapper
- Hermes/OpenClaw-style local agent wrapper
- OpenAI Agents SDK-style runtime wrapper
- MCP tool-use wrapper

Done when:

- at least two different host shapes can produce the same Jarvis protocol
  records
- the Garden POC is one host, not the protocol itself
- the team can share one URL and one README that explain the point clearly
- the protocol can be discussed as a standard, not an internal app feature

## Daily Operating Rhythm

Every day should produce one visible artifact:

- spec page
- schema
- JSON example
- conformance test/checklist
- adapter note
- Garden POC mapping
- demo screenshot
- public docs update

Daily review questions:

1. Did we strengthen the protocol or drift into building a runtime?
2. Can this work with an existing agent without rewriting the agent?
3. Did we capture human judgment, agent action, contribution, evidence, and
   learning?
4. Can another host implement this without Garden?
5. Does this improve the next WorkSession?

## Non-Negotiables

- Jarvis remains protocol-only.
- Garden is only the first proof host.
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
3. Draft the adapter contract for wrapping an existing agent.
4. Map Garden POC concepts to Jarvis objects.
5. Decide the first two proof hosts: Garden POC plus one CLI/external-agent
   wrapper.

If these are clear, the rest of the 30 days becomes execution rather than
debate.
