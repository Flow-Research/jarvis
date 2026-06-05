# Protocol Decisions

This document records decisions that are fixed for the Jarvis protocol.

## Settled Decisions

- Jarvis is a protocol, not an execution stack.
- Jarvis does not define cloud providers, local execution, databases, queues,
  sandboxes, deployment, or product UI.
- HumanWorker and AgentWorker are first-class participants.
- WorkSession is the source of truth.
- Every serious collaboration creates or resumes a WorkSession.
- Policy governs autonomous agent action.
- Action outside policy creates Request.
- Human Review or Takeover resolves Request.
- Human takeover is a protocol state, not a UI convention.
- Contributions are attributable to human, agent, service, tool, or shared
  work.
- Evidence is captured during work.
- Learning is proposed and governed.
- Memory and skill changes require proposal, provenance, scope, and review
  state.

## v0.1 Decisions

- Package families are `@jarvis/protocol`, `@jarvis/policy`,
  `@jarvis/memory`, `@jarvis/skills`, `@jarvis/evidence`, and
  `@jarvis/conformance`.
- Package contracts are defined in `08-package-contracts.md`.
- The public protocol starts with WorkSession.
- WorkSession status transitions are protocol-owned.
- Request decisions are protocol-owned.
- Review decisions are protocol-owned.
- EvidenceManifest export shape is protocol-owned.
- Conformance tests verify behavior, not infrastructure.

## Explicit Non-Decisions

Jarvis does not decide:

- where records are stored
- how events are streamed
- how an agent process runs
- which model is called
- which tool system is used
- which sandbox is used
- which cloud is used
- how a product authenticates users
- how a product displays inboxes or reviews
- how a product bills or operates

Those are host/product decisions.
