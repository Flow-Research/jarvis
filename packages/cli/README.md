# @jarvis-protocol/cli

Status: Protocol Alpha helper tooling.

This package provides a command-line helper for Jarvis v0.1 protocol record
validation and conformance fixture execution.

Accepted command surfaces:

- `jarvis validate fixture <file>`
- `jarvis validate fixtures <directory>`
- `jarvis validate record <file>`
- `jarvis validate evidence-manifest <file>`
- `jarvis check headers <file> --operation-id <operation_id>`
- `jarvis check headers <file> --operation-class <operation_class>`
- `jarvis check hash-chain <file>`
- `jarvis list rejection-ids`
- `jarvis print compatibility-claim`

## Examples

From the repository root, run one fixture expectation:

```bash
jarvis validate fixture packages/cli/fixtures/v0.1/valid/golden-path.json
```

From the repository root, run the full fixture snapshot:

```bash
jarvis validate fixtures packages/cli/fixtures/v0.1
```

Installed package consumers pass the path to the installed
`@jarvis-protocol/cli/fixtures/v0.1` directory.

Validate one protocol record file:

```bash
jarvis validate record record.json
```

The record file MUST use this envelope:

```json
{
  "object_type": "Request",
  "record": {}
}
```

Validate an EvidenceManifest export:

```bash
jarvis validate evidence-manifest evidence-manifest.json
```

Check operation headers:

```bash
jarvis check headers headers.json --operation-id createWorkSession
jarvis check headers headers.json --operation-class non_worksession_mutation
```

Check an event hash chain:

```bash
jarvis check hash-chain events.json
```

List protocol rejection ids:

```bash
jarvis list rejection-ids
```

Print a compatibility claim template:

```bash
jarvis print compatibility-claim
```

## Exit Status

Validation commands return `0` when the requested protocol check passes.

Record, header, EvidenceManifest, and hash-chain commands return non-zero when
the protocol record is invalid.

Fixture commands return `0` when the fixture outcome matches its
`expected_result`. Invalid fixtures pass the command when they reject with the
expected protocol error id.

All validation and error output is JSON. Error output uses the Jarvis
`ProtocolError` envelope.

The compatibility claim output is an implementation claim template. It is not a
Jarvis certification.

Rejected surfaces:

- agent runtime
- model router
- tool executor
- host adapter
- wrapper
- UI kit
- auth provider
- storage backend
- memory engine
- sandbox
- billing system
- scoring system
- payment system
- deployment system
- host workflow engine

The CLI validates Jarvis protocol records. The CLI does not certify
implementations.

## Local Validation

Run CLI tests from the repository root:

```bash
npm --workspace @jarvis-protocol/cli test
```
