# Positioning And Adoption Lock

Jarvis is the human-agent collaboration and learning-loop protocol.

Jarvis defines the protocol record that makes human-agent work reviewable,
attributable, portable, and able to improve across WorkSessions.

## One-Paragraph Definition

Jarvis is the protocol for governed human-agent collaboration and shared
learning. It defines how a HumanWorker and an AgentWorker coordinate inside a
WorkSession under shared goals and human-defined Policy, create Requests when
the AgentWorker is blocked, record Reviews and Takeovers from human judgment,
preserve attributable Contributions, export portable EvidenceManifest records,
and carry governed LearningRecords, MemoryProposals, and SkillProposals into
future WorkSessions.

## The Category

Jarvis is not an agent protocol in the narrow sense.

Jarvis is the human-agent collaboration and learning-loop protocol.

The primitive is:

```txt
HumanWorker + AgentWorker + WorkSession + Policy + Evidence + Learning
```

The primitive is not:

```txt
User -> Assistant -> Answer
```

Jarvis exists because useful work requires more than agent execution. Useful
work needs human judgment, policy, review, takeover, attribution, evidence, and
learning that survives the current task.

## Adjacent Protocols

MCP standardizes how LLM applications connect to tools, prompts, resources, and
context servers. MCP uses JSON-RPC messages over transports such as Streamable
HTTP, where clients send JSON-RPC messages to an MCP endpoint and servers use
SSE for streaming when that transport is active. Jarvis records tool and resource use as WorkSession
events, PolicyDecisions, Contributions, and Evidence when MCP is used. Jarvis
does not define MCP transports, MCP tools, MCP resources, MCP prompts, or MCP
server behavior.

A2A standardizes communication and interoperability between independent agent
systems. A2A separates data model, abstract operations, and protocol bindings,
including JSON-RPC, gRPC, and HTTP+JSON/REST. Jarvis records agent delegation
or agent-to-agent coordination as WorkSession events, Contributions, and
Evidence when A2A is used. Jarvis does not define A2A discovery, tasks,
messages, artifacts, agent cards, or A2A protocol bindings.

AGNTCY ACP defines a standard remote-agent interface and publishes an OpenAPI
contract. Jarvis uses the same discipline of a discoverable host-facing
contract. Jarvis does not define remote-agent execution, thread execution,
interrupt delivery, output retrieval, or ACP agent interfaces.

AG-UI standardizes how AI agents connect to user-facing applications through an
open, lightweight, event-based protocol. AG-UI focuses on agent state, UI
intents, user interactions, frontend tools, streaming, and interactive
frontends. A Jarvis-compatible host exposes WorkSession state,
Requests, Reviews, Takeovers, Contributions, Evidence, and Learning to AG-UI
clients. Jarvis does not define frontend events, rendering, UI state, or
user-interface transport.

## Host Boundary

Hosts provide UI, auth, storage, execution, connectors, notifications,
monitoring, support, and deployment. Jarvis defines the records that hosts
exchange. Jarvis does not become the host.

## SDK Boundary

A Jarvis SDK is a protocol implementation kit.

A Jarvis SDK provides protocol helpers for compatible implementations to create,
validate, export, and test Jarvis records. It does not run agents, orchestrate
models, execute tools, own memory engines, provide UI, manage auth, store
records, run sandboxes, schedule work, or become a host adapter.

SDK support does not change the category. Jarvis remains the human-agent
collaboration and learning-loop protocol.

## Non-Replacement Rule

Compatible implementations MUST NOT require developers to abandon their
existing execution systems, UI, model providers, isolation mechanisms, storage,
or deployment.

Compatible implementations map existing work into Jarvis records:

```txt
human participant -> HumanWorker + Actor
agent participant -> AgentWorker + Actor
agent action affecting a WorkSession -> PolicyDecision + JarvisEvent
blocked action -> Request
human judgment -> Review or Takeover
work performed -> Contribution
trace/artifact/source/output -> EvidenceManifest evidence_item_refs
confirmed improvement -> LearningRecord
memory update proposal -> MemoryProposal
reusable process proposal -> SkillProposal
```

Host mappings preserve host-owned execution. Protocol records remain complete.

## Adoption Argument

Jarvis adoption centers on:

```txt
policy
requests
reviews and takeovers
contribution attribution
evidence
governed learning
memory and skill proposals
```

Jarvis answers these protocol accountability questions:

```txt
What work happened?
Who acted?
What did policy allow?
Where did the agent ask for help?
What did the human review or take over?
What evidence proves the work?
What contribution belongs to the human, agent, pair, or service?
What learning carries into the next WorkSession?
What memory or skill change was proposed, reviewed, accepted, rejected, or
carried forward?
```

Those questions require the Jarvis collaboration record.

## Compatibility Rule

Compatible implementations preserve host-owned execution while recording
Jarvis protocol semantics around it. Jarvis records the collaboration loop that
makes the work governed, reviewable, attributable, evidence-backed, and able to
improve.

## Source References

- MCP specification: https://modelcontextprotocol.io/specification/
- A2A specification: https://a2a-protocol.org/latest/specification/
- AGNTCY ACP specification: https://spec.acp.agntcy.org/
- AG-UI documentation: https://docs.ag-ui.com/
- OpenAPI 3.1.1: https://spec.openapis.org/oas/v3.1.1.html
