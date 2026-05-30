# Design Acceptance Criteria

Jarvis architecture is accepted only when these criteria hold.

Each criterion maps to a buildable part of the harness.

## Scope

- The design stays focused on Jarvis.
- Jarvis does not define product interface ownership, external work ownership,
  or external identity ownership.
- Cloudflare is first-class runtime substrate, not the public identity.

## Human-Agent Collaboration

- The human is an active contributor, reviewer, and teacher.
- The agent is autonomous and bounded.
- The human takes over and hands work back through a defined state machine.
- Corrections become structured learning signals.

## Memory

- Memory scopes are explicit.
- Memory has lifecycle and provenance.
- Untrusted sources never become durable memory automatically.
- Conflicts, stale memory, and project leakage have defined controls.

## Autonomy And Policy

- The agent works without babysitting inside predefined policy.
- Capability grants and risk classes are enforceable.
- Requests are structured and reviewable.
- Sandbox, network, filesystem, credential, and external-send risks are covered.
- Allow/deny decisions are inspectable and auditable.

## Work Sessions

- WorkSession captures more than chat.
- Events, contributions, requests, reviews, and evidence are represented.
- Evidence is inspectable without turning Jarvis into accounting software.
- WorkSessions resume after human delay or runtime recovery; runtime Sessions
  remain adapter-internal.

## Skills And Tools

- Skills are procedural memory.
- Skill updates are governed.
- Tools are policy-wrapped.
- MCP and tool poisoning risks are addressed.
- Tool outputs are untrusted data by default.

## Runtime

- Cloudflare is used deeply where it is strong.
- Kernel primitives do not import Cloudflare types.
- Local development runtime runs the core harness without Cloudflare setup.
- Observability is sufficient for debugging agent behavior.

## v0.1 Acceptance Tests

The first build passes these checks:

```txt
npm create jarvis@latest my-jarvis
cd my-jarvis
npm install
npm run test
```

Expected result:

- scaffold installs without Cloudflare credentials
- `jarvis.config.ts` validates
- `src/agent.ts`, `src/policy.ts`, `src/tools.ts`, `src/skills.ts`, and
  `src/memory.ts` compile
- `.jarvis/local.db` is created during test setup

```txt
npm run jarvis:dev
```

Expected result:

- local runtime starts with SQLite, local filesystem workspace, isolated
  sandbox, and SSE stream
- startup prints the local runtime URL and active policy profile
- no secret or provider key is required for runtime boot

```txt
npm run jarvis:session -- --objective "Inspect the scaffold and create a plan"
```

Expected result:

- a HumanWorker exists
- an AgentWorker exists
- a WorkSession is created
- a runtime/internal Session reference is created below the WorkSession
- the event stream emits `work_session_started`
- a context manifest is persisted

```txt
npm run jarvis:session -- --objective "Fetch example.com and summarize it"
```

Expected result:

- default network-denied policy blocks the fetch
- Jarvis creates a structured request
- request contains risk class, requested host, expected result, expiry,
  canonical action hash, and narrower alternative

```txt
npm run jarvis:requests
npm run jarvis:approve -- --request <id> --scope "network_fetch:example.com"
```

Expected result:

- request resolves with a one-use approval token
- stale approval replay fails
- WorkSession resumes
- policy decision event records selected grant ids by dimension

```txt
npm run jarvis:evidence -- --work-session <id>
```

Expected result:

- EvidenceManifest JSON exports
- manifest includes event-chain root, evidence item hashes, request/review
  records, policy decisions, context manifest ref, artifact refs, and known
  limitations
- redacted export is a derived artifact and raw immutable evidence remains
  unchanged

Restart test:

```txt
npm run jarvis:dev
npm run jarvis:session -- --objective "Trigger a blocked external send"
stop runtime
npm run jarvis:dev
npm run jarvis:requests
```

Expected result:

- pending request survives restart
- WorkSession resumes from event log and checkpoint
- runtime/internal Session remains adapter-internal
- no outbox commit happens before approval
