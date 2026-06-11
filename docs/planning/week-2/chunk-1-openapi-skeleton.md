# Week 2 Chunk 1: OpenAPI Skeleton

## Goal

Create the v0.1 OpenAPI 3.1 entry point without reopening protocol semantics.

## Scope

This chunk locks:

- OpenAPI 3.1.1 document entry
- v0.1 protocol metadata
- top-level OpenAPI buckets
- tag taxonomy
- global HostAuth baseline
- source document references
- host-owned server boundary
- skeleton validation script

This chunk does not define:

- component field schemas
- path operation request bodies
- path operation response bodies
- operation-specific security requirements
- examples
- conformance fixtures
- adapter behavior
- host implementation behavior
- runtime execution

## Files

- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../openapi/README.md](../../openapi/README.md)
- [../../../scripts/check_openapi_skeleton.py](../../../scripts/check_openapi_skeleton.py)

## Acceptance

Chunk 1 is complete when:

- the OpenAPI file parses as YAML
- `openapi` is `3.1.1`
- `info.version` is `0.1.0`
- `x-jarvis-protocol.version` is `v0.1`
- required OpenAPI buckets exist
- required tags exist
- global security requires `HostAuth`
- `HostAuth` is defined without making Jarvis an identity provider
- the document states that hosts own server URLs and implementation details
- local validation passes

## Boundary

Jarvis owns the OpenAPI communication binding. Hosts own implementation.
