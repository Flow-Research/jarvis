# Jarvis SDK Helper Packages

This directory contains package foundations for Jarvis protocol helper
tooling.

The packages help compatible implementations create, validate, hash, export,
and test Jarvis protocol records.

The packages do not run agents, call models, execute tools, own memory
engines, render UI, authenticate callers, store records, route work, score
work, route payments, monitor hosts, integrate host systems, deploy services,
or own host workflow.

## Packages

- `packages/typescript`: TypeScript protocol helper package.
- `packages/python`: Python protocol helper package.
- `packages/cli`: protocol validation and conformance helper CLI.

## Boundary

Jarvis owns protocol helper contracts.

Hosts own execution, storage, auth, UI, model calls, tool execution, memory
engines, queues, billing, monitoring, deployment, host integrations, and host
workflow.
