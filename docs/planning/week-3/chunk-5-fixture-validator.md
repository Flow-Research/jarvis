# Chunk 5: Fixture Validator

Chunk 5 adds local validator checks for conformance fixtures.

## Scope

This chunk validates fixture structure and expected protocol outcomes.

It does not execute host behavior, runtime behavior, model calls, tool calls, or
adapter code.

## Validator Requirements

The validator checks:

- fixture envelope fields
- fixture id format
- protocol version
- valid versus invalid fixture kind
- expected result
- expected error id for invalid fixtures
- required operation headers
- required assertion classes
- forbidden host-private export fields
- OpenAPI component references

The validator is:

```txt
python3 scripts/check_conformance_fixtures.py
```

The validator reads:

```txt
docs/openapi/jarvis-openapi.yaml
docs/conformance/fixtures/valid/*.json
docs/conformance/fixtures/invalid/*.json
```

The validator enforces:

```txt
valid fixtures pass
invalid fixtures reject with their locked expected_error_id
fixture operations use OpenAPI operation ids, methods, paths, and statuses
fixture path ids bind to operation ids and request body ids
mutation operations carry the required Jarvis protocol headers
missing-header fixtures omit the exact missing header
WorkSession mutation headers bind to represented WorkSession revision and event
  hash state
read operations exclude mutation-only headers
source_contract_refs resolve to existing docs or OpenAPI components
host_shape_ref stays fixture metadata only
EvidenceManifest records exclude host-private export fields unless the fixture
  is the forbidden_host_private_field rejection case
JarvisEvent previous_hash values point to represented event-chain state
accepted operation expected_event_ref values bind to the operation previous hash
```

The validator does not execute host behavior, runtime behavior, model calls,
tool calls, adapter code, auth backend, storage, billing, scoring, payment, or
deployment behavior.

## Local Check Sequence

Every chunk that changes conformance fixtures runs:

```txt
python3 scripts/check_conformance_fixtures.py
python3 scripts/check_openapi_skeleton.py
python3 scripts/check_markdown_links.py
python3 scripts/check_week1_wording.py
git diff --check
```

## Done Criteria

Chunk 5 is complete when:

- validator script exists
- valid fixture passes
- invalid fixtures fail for their expected protocol error ids
- validator runs in the local check sequence
