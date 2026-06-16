# Protocol Decisions

This document records decisions that are fixed for the Jarvis protocol.

## Settled Decisions

- Jarvis is a protocol, not an execution stack.
- Jarvis does not define cloud providers, local execution, databases, queues,
  sandboxes, deployment, or UI.
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
- OpenAPI 3.1 is the primary host-facing communication binding.
- Every WorkSession-scoped mutating operation requires
  `Jarvis-Protocol-Version`,
  `Jarvis-Actor-Id`, `Jarvis-Idempotency-Key`,
  `Jarvis-Request-Timestamp`, `Jarvis-Expected-WorkSession-Revision`, and
  `Jarvis-Previous-Event-Hash`.
- Non-WorkSession protocol mutations require `Jarvis-Protocol-Version`,
  `Jarvis-Actor-Id`, `Jarvis-Idempotency-Key`, and
  `Jarvis-Request-Timestamp`.
- Worker and Actor registration records protocol references. It does not create
  accounts, authenticate callers, issue credentials, or own identity storage.
- OutcomeReport submission does not mutate sealed WorkSession or
  EvidenceManifest records.
- Security schemes define protocol entry requirements without owning host auth.
- Capability and extension negotiation are protocol-owned.
- Extension fields must be namespaced and cannot override core fields.
- Compatible implementations MUST NOT silently downgrade a request.
- Protocol errors use a structured error envelope.
- WorkSession-scoped and export read operations require protocol version,
  host authentication, and Actor authority. They do not require mutation-only
  idempotency, expected revision, or previous event hash headers.

## Explicit Non-Decisions

Jarvis does not decide:

- where records are stored
- how events are streamed
- how an agent process runs
- which model is called
- which tool system is used
- which isolation mechanism is used
- which cloud is used
- how a host authenticates users
- how a host displays inboxes or reviews
- how a host bills or operates

Hosts own those decisions.
