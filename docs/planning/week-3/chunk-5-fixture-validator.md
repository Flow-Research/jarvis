# Chunk 5: Fixture Validator

Chunk 5 locks local validator checks for conformance fixtures.

## Scope

This chunk validates fixture structure and expected protocol outcomes.

The validator MUST NOT execute host behavior, runtime behavior, model calls,
tool calls, or adapter code.

## Validator Requirements

Conformance fixtures MUST satisfy:

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

Compatible implementations MUST run:

```txt
python3 scripts/check_conformance_fixtures.py
```

Jarvis defines the validator inputs as:

```txt
docs/openapi/jarvis-openapi.yaml
docs/conformance/fixtures/valid/*.json
docs/conformance/fixtures/invalid/*.json
```

The protocol rejects fixtures that do not satisfy:

```txt
valid fixtures MUST pass
invalid fixtures MUST reject with their locked expected_error_id
fixture operations MUST use OpenAPI operation ids, methods, paths, and statuses
fixture path ids MUST bind to operation ids and request body ids
mutation operations MUST carry the required Jarvis protocol headers
missing-header fixtures MUST omit the exact missing header
WorkSession mutation headers MUST bind to represented WorkSession revision and
  event hash state
read operations MUST exclude mutation-only headers
source_contract_refs MUST resolve to existing docs or OpenAPI components
host_shape_ref MUST stay fixture metadata only
EvidenceManifest records MUST exclude host-private export fields unless the
  fixture is the forbidden_host_private_field rejection case
JarvisEvent previous_hash values MUST point to represented event-chain state
accepted operation expected_event_ref values MUST bind to the operation previous
  hash
```

The validator MUST NOT execute host behavior, runtime behavior, model calls,
tool calls, adapter code, auth backend, storage, billing, scoring, payment, or
deployment behavior.

## Local Check Sequence

Every conformance-fixture change MUST run:

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
