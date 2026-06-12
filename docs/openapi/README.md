# Jarvis OpenAPI Contract

This directory contains the machine-readable OpenAPI 3.1 communication binding
for Jarvis v0.1.

Jarvis is the human-agent collaboration and learning-loop protocol. OpenAPI
defines how compatible hosts exchange Jarvis protocol records. OpenAPI does not
make Jarvis a runtime, host implementation, auth system, storage system, cloud stack, tool
protocol, frontend protocol, or agent framework.

## Files

- [jarvis-openapi.yaml](./jarvis-openapi.yaml) - v0.1 OpenAPI entry point.

## Chunk Locks

Chunk 1 locks the OpenAPI document skeleton:

```txt
openapi
jsonSchemaDialect
info
servers
security
tags
paths
components.schemas
components.parameters
components.headers
components.requestBodies
components.responses
components.securitySchemes
components.examples
x-jarvis-protocol
```

Chunk 1 defines the global HostAuth baseline. Later chunks define
operation-specific Jarvis header requirements from the locked protocol docs.

Chunk 2 defines shared schema primitives and the participant schemas:

```txt
Worker
Actor
HumanWorker
AgentWorker
```

Chunk 2 does not define path operation bodies, operation-specific security
requirements, WorkSession schema, control-plane schemas, evidence and learning
schemas, examples, or conformance fixtures. Later chunks define those sections
from the locked protocol docs.

Chunk 3 defines the WorkSession, event, Policy, and PolicyDecision schema
spine:

```txt
WorkSession
JarvisEvent
Policy
PolicyDecision
```

Chunk 3 does not define Request, Review, Takeover, Contribution,
EvidenceManifest, learning schemas, path operation bodies, examples, or
conformance fixtures.

Chunk 4 defines the control-plane schemas:

```txt
Request
Review
ApprovalScope
Takeover
```

Chunk 4 does not define Contribution, EvidenceManifest, learning schemas, path
operation bodies, examples, or conformance fixtures.

## Boundary

Compatible hosts publish their own server URLs, identity providers, credential
handling, storage, execution, deployment, billing, and UI. Jarvis defines
protocol records and conformance requirements only.
