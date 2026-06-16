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

## Done Criteria

Chunk 5 is complete when:

- validator script exists
- valid fixture passes
- invalid fixtures fail for their expected protocol error ids
- validator runs in the local check sequence
