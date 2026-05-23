# Implementation Decisions

This document records implementation decisions that complete the Jarvis v1
boundary. Deferred items are excluded from v1 and never reopen the core Jarvis
model.

## Settled Architectural Decisions

- WorkSession is the public developer-facing primitive.
- Session is runtime/internal by default.
- HumanAgentPair is the durable relationship between one human and one agent.
- Every serious interaction creates a WorkSession.
- Casual chat creates a lightweight WorkSession with reduced transcript detail.
- Requests, approvals, grants, policy decisions, tool calls, memory proposals,
  skill proposals, memory confirmations, skill confirmations, credential use,
  external-send drafts, external-send commits, external-send receipts,
  takeover, and reconciliation events are never reduced.
- Jarvis owns policy, context assembly, memory selection, learning, requests,
  reviews, evidence, and skill lifecycle.
- Runtime adapters own infrastructure: persistence, execution, streaming,
  leases, checkpoints, sandboxing, scheduling, model delivery, and recovery.
- Cloudflare is the production reference runtime.
- A minimal local development runtime exists for adoption and testing.

## v0.1 Decisions

- Package families are `@jarvis/core`, `@jarvis/memory`, `@jarvis/policy`,
  `@jarvis/skills`, `@jarvis/tools`, `@jarvis/runtime-local`, and
  `@jarvis/runtime-cloudflare`.
- Package contracts are defined in `08-package-contracts.md`.
- The local development runtime uses SQLite, a local filesystem workspace,
  Docker or namespace-isolated sandbox execution, file-backed config, and SSE
  streaming.
- The public WorkSession API uses `workSessions.start`,
  `workSessions.resume`, `workSessions.send`, `workSessions.events`,
  `requests.resolve`, and `workSessions.complete`.
- Memory editing in v0.1 is API-only through propose, confirm, reject,
  supersede, and revoke operations. Memory UI is outside Jarvis core.
- Default grant duration is one WorkSession unless a shorter expiry is set.
- Request limit is 20 pending requests per WorkSession. Equivalent blocked
  actions coalesce into one request with multiple evidence refs.
- Skill bundles are directories with a `skill.md` manifest, optional examples,
  optional fixtures, content hash, version, and review state.
- MCP gateway lives in `@jarvis/tools`.
- Evidence retention default is local-only until the runtime sets a retention
  policy.
- Evidence export format is JSON manifest plus referenced artifacts.
- Project scaffold contents are defined in `09-default-project.md`.
