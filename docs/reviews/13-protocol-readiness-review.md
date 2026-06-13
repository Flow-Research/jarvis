# Protocol Readiness Lock

Jarvis moved from design into the OpenAPI 3.1 contract, examples, and
conformance entry.

## Baseline

Jarvis is the human-agent collaboration and learning-loop protocol. It defines
how a HumanWorker and AgentWorker coordinate under shared goals and policy,
produce reviewable Requests and Reviews, record Contributions, export
EvidenceManifest records, and govern LearningRecords, MemoryProposals, and
SkillProposals.

Jarvis is not a runtime, agent framework, host workspace, model provider,
task marketplace, or cloud stack.

## Protocol Habits We Use

Jarvis follows proven protocol habits from existing standards:

- HTTP separates semantics from implementation and deployment.
- OAuth separates actors, grants, authorization, and resource access.
- Language Server Protocol uses initialization, capability negotiation, typed
  messages, and extension points.
- OpenAPI gives implementers machine-readable contracts.
- MCP standardizes tool, resource, and prompt connectivity for LLM
  applications through JSON-RPC message encoding.
- A2A standardizes agent-to-agent discovery, tasks, messages, and artifacts.
- A2A separates canonical model, abstract operations, and protocol bindings.
- AGNTCY ACP specifies a REST-based remote-agent interface with OpenAPI.
- AG-UI standardizes agent-to-frontend event streams.

References:

- HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110
- OAuth 2.0: https://www.rfc-editor.org/rfc/rfc6749
- Language Server Protocol: https://microsoft.github.io/language-server-protocol/
- OpenAPI Specification: https://spec.openapis.org/oas/latest.html
- MCP: https://modelcontextprotocol.io/specification/
- A2A: https://a2a-protocol.org/latest/
- AGNTCY ACP: https://spec.acp.agntcy.org/
- AG-UI: https://docs.ag-ui.com/

## Protocol Disciplines

Jarvis uses these protocol disciplines:

- explicit actors and roles
- lifecycle states
- versioned records
- capability negotiation
- typed events
- request and response resolution rules
- portable export format
- extension points
- conformance tests
- compatibility language
- strict separation from implementation infrastructure

## Communication Binding Decision

Jarvis uses OpenAPI 3.1 as the primary machine-readable communication
contract.

Jarvis does not use JSON-RPC as its default host-facing binding. JSON-RPC fits
tool sessions and bidirectional method calls. Jarvis needs a host-facing
contract for WorkSessions, Requests, Reviews, Takeovers, Contributions,
EvidenceManifest exports, LearningRecords, and OutcomeReports.

Jarvis follows the A2A discipline: protocol semantics, operations, and
bindings stay separate. Jarvis follows the ACP lesson: an agent-facing protocol
benefits from a discoverable REST/OpenAPI contract.

## Boundaries We Keep

Jarvis does not become:

- MCP for tools
- A2A for agent-to-agent communication
- AG-UI for frontend streaming
- OpenAPI for generic HTTP APIs
- OAuth for identity and authorization
- an agent SDK runtime
- a host-specific workflow engine

Jarvis integrates with all of these. It owns the collaboration and learning
record they do not define.

## Current Alignment

The repo is aligned on the main thesis:

- HumanWorker and AgentWorker are first-class.
- WorkSession is the source of truth.
- Policy bounds autonomous action.
- blocked action becomes Request.
- human judgment is captured through Review and Takeover.
- Contribution keeps attribution visible.
- EvidenceManifest provides portable proof.
- LearningRecord captures human, agent, and pair learning.
- MemoryProposal and SkillProposal prevent silent learning mutation.
- hosts own execution, storage, UI, deployment, and model choice.

## Locked Before OpenAPI Contract

The docs locked these points before Week 2 converted them into the OpenAPI
contract:

- README uses one direct protocol definition.
- roadmap uses one object vocabulary.
- policy docs keep Jarvis out of runtime ownership.
- host integration keeps actor ids and worker ids separate.
- WorkSession evidence terms stay consistent.
- roadmap wording stays independent from external systems.
- core object spec uses protocol-style normative language.

## Week 1 Closeout State

Week 1 locked the OpenAPI entry decisions that Week 2 encoded:

1. Version negotiation uses `Jarvis-Protocol-Version`.
2. Capability negotiation uses `Jarvis-Host-Capabilities` and
   `Jarvis-Required-Capabilities`.
3. Extensions are namespaced and cannot override core fields.
4. Protocol errors use structured error ids and a required error envelope.
5. WorkSession-scoped mutations require protocol version, Actor id,
   idempotency key, timestamp, expected WorkSession revision, and previous
   event hash.
6. Worker registration, Actor registration, and OutcomeReport submission use
   the non-WorkSession mutation header set.
7. WorkSession-scoped and export reads require protocol version, caller
   authentication, and Actor authority.
8. Portable exports and error responses exclude forbidden host-private fields.
9. Positioning is locked: Jarvis records collaboration around host-owned
   execution and external protocol participation without replacing them.

Week 2 converted these locked decisions into OpenAPI component syntax, path
syntax, examples, and conformance entry documents.

## Readiness State

The protocol thesis is stable. The boundaries are stable. The object set,
lifecycle, control plane, evidence model, learning model, OpenAPI security
entry, and positioning boundary are encoded in the OpenAPI contract and
conformance entry.

Compatible examples start only after the OpenAPI contract and conformance
entry rules are stable.
