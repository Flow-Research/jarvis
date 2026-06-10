# Chunk 6: Positioning And Adoption Lock

Chunk 6 closes Week 1 by locking why Jarvis exists beside existing agents,
agent frameworks, agent protocols, and product hosts.

This chunk does not create adapters, OpenAPI YAML, conformance fixtures,
runtime code, product UI, or host implementation behavior. It locks the adoption
argument that Week 2 OpenAPI drafting must preserve.

## Scope

Chunk 6 locks:

```txt
one-paragraph Jarvis explanation
positioning against MCP
positioning against A2A
positioning against AGNTCY ACP
positioning against AG-UI
positioning against agent SDKs
positioning against coding agents
positioning against personal agents
existing-agent adoption rule
non-replacement rule
Week 1 closeout state
```

## Non-Goals

Chunk 6 does not:

- create an adapter
- create OpenAPI YAML
- create conformance fixtures
- define runtime execution
- define product UI
- define host implementation behavior
- define task marketplace behavior
- define auth provider behavior
- replace MCP, A2A, ACP, AG-UI, agent SDKs, coding agents, or personal agents

## Locked Position

Jarvis is the human-agent collaboration and learning-loop protocol.

Jarvis defines how HumanWorkers and AgentWorkers collaborate inside
WorkSessions under policy, ask for help through Requests, capture human
judgment through Reviews and Takeovers, record attributable Contributions,
export portable EvidenceManifest records, and carry governed LearningRecords,
MemoryProposals, and SkillProposals into future work.

Jarvis does not run the agent. Jarvis records the collaboration.

## One-Paragraph Explanation

Jarvis is the protocol for governed human-agent collaboration and shared
learning. It defines how a HumanWorker and an AgentWorker coordinate inside a
WorkSession under shared goals and human-defined Policy, create Requests when
the AgentWorker is blocked, record Reviews and Takeovers from human judgment,
preserve attributable Contributions, export portable EvidenceManifest records,
and carry governed LearningRecords, MemoryProposals, and SkillProposals into
future WorkSessions.

## Adjacent Protocol Positioning

MCP standardizes how agent applications connect to tools, prompts, resources,
and context servers. Jarvis records MCP use inside WorkSessions when MCP is
used. Jarvis does not define MCP transports, MCP tools, MCP resources, or MCP
server behavior.

A2A standardizes communication and interoperability between independent agent
systems. Jarvis records agent delegation or agent-to-agent coordination as
WorkSession events, Contributions, and Evidence when A2A is used. Jarvis does
not define A2A discovery, tasks, messages, artifacts, or protocol bindings.

AGNTCY ACP defines a remote-agent interface with an OpenAPI contract. Jarvis
uses the OpenAPI lesson for its own host-facing communication binding. Jarvis
does not define remote-agent run execution, thread execution, output retrieval,
or ACP agent interfaces.

AG-UI standardizes how agents connect to user-facing applications through
event-based frontend interaction. Hosts may expose Jarvis WorkSession state,
Requests, Reviews, Takeovers, Contributions, and Evidence to AG-UI clients.
Jarvis does not define frontend events, frontend rendering, user interface
state, or UI transport.

## Agent Product Positioning

Agent SDKs provide execution primitives, model calls, tool calls, tracing,
handoffs, and runtime behavior. Jarvis records the human-agent collaboration
around that execution. Jarvis does not replace an SDK.

Coding agents perform software work through terminals, editors, repositories,
tools, sandboxes, and review loops. Jarvis records the WorkSession, Policy,
Requests, Reviews, Takeovers, Contributions, Evidence, and Learning around that
work. Jarvis does not replace the coding agent.

Personal agents provide a product or assistant experience for a person. Jarvis
defines the collaboration protocol that a personal agent may implement. Jarvis
is not the personal agent product.

## Adoption Rule

Existing agents remain first-class.

A compatible host or adapter maps existing agent work into Jarvis records
without rewriting the agent runtime. The adapter records who acted, what Policy
allowed, what was blocked, what the human reviewed, what evidence was captured,
what contribution was made, and what learning was accepted.

Adoption fails if the implementation requires a developer to abandon their
agent, runtime, product UI, model provider, sandbox, database, or cloud.

Adoption succeeds when different agents and products produce the same
WorkSession, Request, Review, Takeover, Contribution, EvidenceManifest,
LearningRecord, MemoryProposal, and SkillProposal semantics.

## Why Jarvis Exists

Existing systems answer different questions:

```txt
MCP answers: how does an agent use tools and resources?
A2A answers: how do agents communicate and delegate?
ACP answers: how does a remote agent expose a standard interface?
AG-UI answers: how does an agent interact with a frontend?
Agent SDKs answer: how does an agent execute?
Coding agents answer: how does an agent work inside a codebase?
Personal agents answer: how does a person experience an assistant?
Jarvis answers: how do a human and an agent collaborate, produce evidence,
record contribution, and learn together across WorkSessions?
```

That is the adoption point.

## Done Criteria

Chunk 6 is complete when:

- [16-positioning-adoption-lock.md](../../protocol/16-positioning-adoption-lock.md)
  locks the positioning argument
- [14-protocol-lock.md](../../protocol/14-protocol-lock.md) no longer carries
  stale Week 1 lock status
- [week-1/README.md](./README.md) uses the final Week 1 header and positioning
  wording
- README and docs index point to the positioning lock
- local checks pass
- at least four reviewer lanes pass, including the Protocol Thesis Reviewer and
  Conformance And Interop Reviewer
- valid findings are integrated
- rejected findings are recorded with concrete reasons
- PR is opened
