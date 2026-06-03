# Protocol Readiness Lock

Jarvis is ready to move from design into schemas, examples, conformance tests,
and host proofs.

## Baseline

Jarvis is the human-agent collaboration and learning-loop protocol. It defines
how a HumanWorker and AgentWorker coordinate under shared goals and policy,
produce reviewable Requests and Reviews, record Contributions, export
EvidenceManifest records, and govern LearningRecords, MemoryProposals, and
SkillProposals.

Jarvis is not a runtime, agent framework, product workspace, model provider,
task marketplace, or cloud stack.

## Protocol Habits We Use

Jarvis follows proven protocol habits from existing standards:

- HTTP separates semantics from implementation and deployment.
- OAuth separates actors, grants, authorization, and resource access.
- Language Server Protocol uses initialization, capability negotiation, typed
  messages, and extension points.
- OpenAPI gives implementers machine-readable contracts.
- MCP standardizes tool, resource, and prompt connectivity for LLM
  applications.
- A2A standardizes agent-to-agent discovery, tasks, messages, and artifacts.
- AG-UI standardizes agent-to-frontend event streams.

References:

- HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110
- OAuth 2.0: https://www.rfc-editor.org/rfc/rfc6749
- Language Server Protocol: https://microsoft.github.io/language-server-protocol/
- OpenAPI Specification: https://spec.openapis.org/oas/latest.html
- MCP: https://modelcontextprotocol.io/specification/
- A2A: https://a2a-protocol.org/latest/
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

## Boundaries We Keep

Jarvis does not become:

- MCP for tools
- A2A for agent-to-agent communication
- AG-UI for frontend streaming
- OpenAPI for generic HTTP APIs
- OAuth for identity and authorization
- an agent SDK runtime
- a product-specific workflow engine

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
- products and hosts own execution, storage, UI, deployment, and model choice.

## Locked Before Implementation

The docs now lock these points before schema work starts:

- README uses one direct protocol definition.
- roadmap uses one object vocabulary.
- policy docs keep Jarvis out of runtime ownership.
- host integration keeps actor ids and worker ids separate.
- WorkSession evidence terms stay consistent.
- roadmap wording stays independent from downstream products.
- core object spec uses protocol-style normative language.

## Schema Entry Gaps

Schema work starts by closing these protocol gaps:

1. Version negotiation: define `protocol_version`, supported versions, and
   compatibility behavior.
2. Capability negotiation: define how a host declares supported Jarvis features.
3. Extension model: define namespaced extension fields that preserve
   portability.
4. Error model: define protocol error codes for invalid transitions, missing
   review, stale takeover epoch, invalid export, and unsupported capability.
5. JSON examples: create one complete WorkSession export.
6. Conformance fixtures: create passing and failing examples.

## Readiness State

The protocol thesis is stable. The boundaries are stable. The object set is
stable enough to begin schemas and examples.

Week 1 starts with the machine-readable contract, versioning, conformance tests,
and the first host proof mapping.
