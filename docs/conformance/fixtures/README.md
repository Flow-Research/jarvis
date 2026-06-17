# Conformance Fixtures

This directory contains Jarvis v0.1 conformance fixtures.

Fixtures are protocol proof records. They do not execute host behavior,
runtime behavior, model calls, tool calls, UI, storage, auth backend, billing,
scoring, payment, or deployment behavior.

## Layout

```txt
valid/
  golden-path.json

invalid/
  added in Week 3 Chunk 4
```

## Fixture Envelope

Every fixture uses this envelope:

```txt
fixture_id
protocol_version
kind
title
description
source_contract_refs
host_shape_ref
records
operations
assertions
expected_result
expected_error_id
expected_error_field
```

Valid fixtures omit `expected_error_id` and `expected_error_field`.
Invalid fixtures include one primary `expected_error_id`.

`host_shape_ref` is fixture metadata only. It MUST NOT appear inside records,
operation bodies, JarvisEvents, EvidenceManifest, or portable export payloads.

## Records

`records` contains protocol records only.

Fixture precondition records represent protocol authority that exists before
the operation sequence starts. They remain protocol records and do not define
host setup.

When a protocol object changes state during the fixture, records use named
snapshots:

```txt
genesis_request
created
pending
approved
completed
```

Named snapshots do not create host state. They preserve the protocol state that
operations and assertions reference.

## Operations

`operations` use OpenAPI operation ids from
`docs/openapi/jarvis-openapi.yaml`.

Operation entries record the OpenAPI `HostAuth` placeholder, Jarvis protocol
headers, and expected protocol outcomes. They do not define auth backend
behavior and do not execute host code.

Accepted mutation operations that produce a JarvisEvent record use
`expected_event_ref` with the produced JarvisEvent id. Fixtures MUST NOT
duplicate that produced event with a separate `appendJarvisEvent` operation.
`appendJarvisEvent` appears only when the operation under test directly appends
a JarvisEvent request body.

## Assertions

`assertions` record the protocol gates that a compatible implementation proves
or rejects.

Assertion classes come from
`docs/planning/week-3/chunk-1-fixture-architecture.md`.
