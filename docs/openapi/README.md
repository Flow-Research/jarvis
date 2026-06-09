# Jarvis OpenAPI Contract

This directory contains the machine-readable OpenAPI 3.1 communication binding
for Jarvis v0.1.

Jarvis is the human-agent collaboration and learning-loop protocol. OpenAPI
defines how compatible hosts exchange Jarvis protocol records. OpenAPI does not
make Jarvis a runtime, product, auth system, database, cloud stack, tool
protocol, frontend protocol, or agent framework.

## Files

- [jarvis-openapi.yaml](./jarvis-openapi.yaml) - v0.1 OpenAPI entry point.

## Chunk 1 Lock

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

Chunk 1 does not define component field schemas, path operation bodies,
operation-specific security requirements, examples, or conformance fixtures.
Later chunks define those sections from the locked protocol docs.

## Boundary

Compatible hosts publish their own server URLs, identity providers, credential
handling, storage, execution, deployment, billing, and UI. Jarvis defines
protocol records and conformance requirements only.
