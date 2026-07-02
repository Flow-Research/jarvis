# Chunk 4: Conformance Runner And Protocol Helper CLI

Issue: #67.

Status: implemented.

Chunk 4 defines the conformance runner and protocol helper CLI.

## Scope

This chunk creates a command-line helper for protocol record validation and
fixture execution.

It includes commands for:

- validating one fixture file
- validating a directory of fixtures
- validating one protocol record file
- validating an EvidenceManifest export
- checking required mutation headers
- checking required read headers
- checking event hash-chain continuity
- listing v0.1 rejection ids
- printing a public compatibility claim template

It does not connect to host storage, mutate host state, call models, run
agents, execute tools, own auth, render UI, schedule work, score work, route
payments, deploy services, or certify implementations.

## Required Inputs

Chunk 4 starts after Chunk 1 locks the SDK boundary and after at least one
validator package proves the shared validation shape.

Required inputs:

- [chunk-1-sdk-boundary-package-plan.md](./chunk-1-sdk-boundary-package-plan.md)
- [../../conformance/checklist.md](../../conformance/checklist.md)
- [../../conformance/fixtures/README.md](../../conformance/fixtures/README.md)
- [../../conformance/fixtures/valid/golden-path.json](../../conformance/fixtures/valid/golden-path.json)
- [../../conformance/fixtures/invalid/](../../conformance/fixtures/invalid/)
- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)

## Command Surface

The CLI MUST expose:

```txt
jarvis validate fixture <file>
jarvis validate fixtures <directory>
jarvis validate record <file>
jarvis validate evidence-manifest <file>
jarvis check headers <file> --operation-id <operation_id>
jarvis check headers <file> --operation-class <operation_class>
jarvis check hash-chain <file>
jarvis list rejection-ids
jarvis print compatibility-claim
```

Command names are normative for this plan and change only through a follow-up
doc update.

## Header Check Input

`jarvis check headers` requires operation context because Jarvis header
requirements differ by operation class.

The command MUST receive either:

```txt
--operation-id <operation_id>
```

or:

```txt
--operation-class <operation_class>
```

Accepted operation classes:

```txt
worksession_scoped_mutation
worksession_genesis_mutation
non_worksession_mutation
worksession_scoped_read
export_read
```

Header input files MUST contain:

```txt
headers
body_ref or body
operation_id or operation_class
```

The CLI maps operation id to header requirements through
`docs/openapi/jarvis-openapi.yaml` and
`docs/protocol/15-openapi-communication-binding.md`.

## Error Surface

CLI errors MUST include:

- error id
- protocol version
- object type
- field
- reason
- remediation
- trace id

The CLI MUST NOT expose credentials, provider secrets, raw auth tokens, session
cookies, private keys, deployment details, billing data, private scores, host
database ids, raw runtime state, or UI state.

## Test Requirements

Chunk 4 tests MUST include:

- valid fixture run
- invalid fixture run
- WorkSession genesis mutation header check
- missing mutation header
- missing read header
- unauthorized Actor
- previous event hash mismatch
- stale WorkSession revision
- forbidden host-private export field
- sealed WorkSession mutation
- sealed EvidenceManifest export rejection
- compatibility claim output
- machine-readable error output

## Acceptance Criteria

Chunk 4 is complete when:

- CLI runs against the existing fixture set.
- CLI returns stable machine-readable protocol errors.
- CLI emits non-zero exit status for invalid records.
- CLI emits zero exit status for valid records.
- CLI docs include command examples and exit status rules.
- CLI docs state that the CLI does not certify implementations.
- local protocol validation passes.
- CLI tests pass.
- review lanes have no valid unresolved findings.

## Boundary

The CLI validates Jarvis protocol records.

The CLI does not implement host behavior, certify implementations, run agents,
call models, execute tools, store records, authenticate callers, render host UI,
route tasks, score work, route payments, or deploy services.
