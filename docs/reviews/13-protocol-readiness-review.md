# Protocol Readiness Review

This review confirms Jarvis is ready to move from design into schemas,
examples, conformance tests, and host proofs.

## Review Baseline

Jarvis is the human-agent collaboration and learning-loop protocol. It defines
how a HumanWorker and AgentWorker coordinate under shared goals and policy,
produce reviewable Requests and Reviews, record Contributions, export
EvidenceManifest records, and govern LearningRecords, MemoryProposals, and
SkillProposals.

Jarvis is not a runtime, agent framework, product workspace, model provider,
task marketplace, or cloud stack.

## Protocol Patterns Reviewed

Jarvis follows proven protocol habits from existing standards:

- HTTP separates semantics from implementation and deployment.
- OAuth separates actors, grants, authorization, and resource access.
- Language Server Protocol uses initialization, capability negotiation, typed
  messages, and extension points.
- OpenAPI gives implementers machine-readable contracts.
- MCP standardizes tool/resource/prompt connectivity for LLM applications.
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
- request/response resolution rules
- portable export format
- extension points
- conformance tests
- compatibility language
- strict separation from implementation infrastructure

## What Jarvis Must Not Borrow

Jarvis must not become:

- MCP for tools
- A2A for agent-to-agent communication
- AG-UI for frontend streaming
- OpenAPI for generic HTTP APIs
- OAuth for identity and authorization
- an agent SDK runtime
- a product-specific workflow engine

Jarvis can integrate with all of these. It owns the collaboration and learning
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

## Corrections Made Before Implementation

The review tightened:

- duplicate core contract names in the README
- duplicate `JarvisEvent` entry in the roadmap
- stale agent-adapter wording in policy docs
- host integration pseudocode so actor ids and worker ids are not confused
- WorkSession evidence section headings
- roadmap wording that tied protocol explanation to named downstream systems
- canonical object spec with protocol-style normative language

## Remaining Gaps Before Schemas

These are the next protocol gaps to close:

1. Version negotiation: define `protocol_version`, supported versions, and
   compatibility behavior.
2. Capability negotiation: define how a host declares supported Jarvis features.
3. Extension model: define namespaced extension fields that do not break
   portability.
4. Error model: define protocol error codes for invalid transitions, missing
   review, stale takeover epoch, invalid export, and unsupported capability.
5. JSON examples: create one complete WorkSession export.
6. Conformance fixtures: create passing and failing examples.

## Readiness Judgment

The design is ready to start Week 1 execution.

The protocol thesis is stable. The boundaries are stable. The object set is
stable enough to begin schemas and examples.

The next work is the machine-readable contract, versioning, conformance tests,
and the first host proof mapping.
