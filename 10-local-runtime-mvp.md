# Local Runtime MVP

The local runtime proves that Jarvis is open-source usable without Cloudflare.
It is not the production reference. Cloudflare remains the first-class
production runtime.

## Defaults

```txt
storage
  SQLite

workspace
  local filesystem under ./workspace

internal data
  ./.jarvis

sandbox
  Docker or namespace isolation

streaming
  SSE

scheduler
  local process timers persisted through SQLite

model provider
  configured adapter, no default secret

network
  denied until policy grants hosts
```

Host shell execution is degraded mode. It runs only explicit human-run commands
with no credentials, no background execution, and no private workspace writes.

## Required Runtime Ports

```ts
export interface SessionStore {
  load(ref: RuntimeSessionRef): Promise<RuntimeSession | null>;
  save(session: RuntimeSession, expectedVersion: number): Promise<void>;
}

export interface EventStore {
  append(event: JarvisEvent, expectedSequence: number): Promise<void>;
  readWorkSession(workSessionId: string): AsyncIterable<JarvisEvent>;
}

export interface RequestStore {
  create(request: JarvisRequest): Promise<void>;
  resolve(input: ResolveRequestInput): Promise<JarvisRequest>;
  listPending(workSessionId: string): Promise<JarvisRequest[]>;
}

export interface WorkspaceStore {
  read(path: string): Promise<WorkspaceFile>;
  write(input: WorkspaceWrite, grant: GrantResolution): Promise<void>;
  list(prefix: string): Promise<WorkspaceEntry[]>;
}

export interface SandboxExecutor {
  start(input: SandboxStartInput): Promise<SandboxLease>;
  exec(input: SandboxExecInput): Promise<SandboxExecResult>;
  stop(leaseId: string): Promise<void>;
}

export interface LeaseManager {
  acquire(input: LeaseInput): Promise<Lease>;
  renew(leaseId: string, epoch: number): Promise<void>;
  release(leaseId: string): Promise<void>;
}

export interface StreamSink {
  publish(event: JarvisEvent): Promise<void>;
  subscribe(workSessionId: string): AsyncIterable<JarvisEvent>;
}

export interface ModelProvider {
  runTurn(input: ModelTurnInput): Promise<ModelTurnResult>;
}
```

Every mutating method receives idempotency keys through its input object. Every
commit verifies the active WorkSession lock epoch before persisting effects.

## Persistence Schema

SQLite stores:

```txt
human_profiles
agent_profiles
human_agent_pairs
work_sessions
runtime_sessions
work_session_runs
events
requests
reviews
contributions
evidence_items
evidence_manifests
memory_records
memory_versions
skill_records
tool_inventory
policy_grants
policy_decisions
leases
checkpoints
outbox_drafts
outbox_authorizations
outbox_receipts
```

All event, evidence, policy, and outbox tables store hash fields for audit
chains. Tables with user-visible records store `created_at`, `updated_at`, and
`version`.

## Stream Protocol

SSE events use the Jarvis event envelope:

```txt
id
sequence
type
work_session_id
run_id
actor_id
timestamp
trace_context
payload
previous_hash
event_hash
```

The stream replays missed events from `Last-Event-ID`.

## WorkSession Schema Floor

```txt
id
version
status
title
objective
human_agent_pair_id
human_actor_id
agent_actor_id
interface_source
active_run_id
autonomy_level
policy_profile_id
created_at
updated_at
completed_at
lock_epoch
```

Statuses:

```txt
created
active
waiting_on_human
takeover
reconciling
completed
failed
closed
```

Status transitions are validated by `@jarvis/core`. Runtime adapters cannot
write arbitrary statuses.

## Deferred Ports

These ports are outside v0.1 local runtime:

```txt
BackgroundJobRunner for recurring work
multi-user NotificationSink
remote artifact replication
distributed lease manager
```

The interfaces exist only when an implementation uses them. The v0.1 scaffold
does not depend on them.
