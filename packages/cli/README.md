# @jarvis-protocol/cli

Status: package foundation.

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
