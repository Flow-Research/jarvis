# Jarvis OpenAPI Contract

This directory contains the machine-readable OpenAPI 3.1 communication binding
for Jarvis v0.1.

Jarvis is the human-agent collaboration and learning-loop protocol. OpenAPI
defines how compatible hosts exchange Jarvis protocol records.

OpenAPI defines Jarvis protocol record exchange only.

## Files

- [jarvis-openapi.yaml](./jarvis-openapi.yaml) - v0.1 OpenAPI entry point.

## Contract Surface

The v0.1 OpenAPI contract defines:

- protocol object schemas
- protocol operations
- required Jarvis header parameters
- HostAuth placeholder security scheme
- protocol error envelope
- examples used by the conformance docs

Executable conformance fixtures live under
[../conformance/fixtures/](../conformance/fixtures/). Validate them with:

```txt
python3 scripts/check_conformance_fixtures.py
python3 scripts/check_openapi_contract.py
```

## Boundary

Compatible hosts publish their own server URLs. Jarvis defines protocol records
and conformance requirements only.
