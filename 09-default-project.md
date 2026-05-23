# Default Project

`create-jarvis` creates a complete local Jarvis project. The scaffold runs
without Cloudflare and keeps Cloudflare as the production runtime path.

## Scaffold Tree

```txt
my-jarvis/
  package.json
  jarvis.config.ts
  src/
    agent.ts
    human-agent-pair.ts
    policy.ts
    tools.ts
    skills.ts
    memory.ts
  skills/
    research.skill.md
    coding-assistant.skill.md
  memory/
    README.md
    seeds/
      human.md
      agent.md
      shared.md
  workspace/
    .gitkeep
  .jarvis/
    local.db
    events/
    evidence/
    artifacts/
    checkpoints/
    requests/
    context-manifests/
  scripts/
    export-evidence.ts
```

## `package.json` Scripts

```txt
jarvis:dev
  starts the local runtime and SSE stream

jarvis:session
  starts a WorkSession from the CLI

jarvis:requests
  lists pending requests

jarvis:approve
  resolves a request with an approval token

jarvis:evidence
  exports an EvidenceManifest

test
  runs scaffold acceptance tests
```

## Config Contract

`jarvis.config.ts` declares:

```txt
project id
runtime profile
model provider
memory stores
skill directories
tool registry
policy profile
sandbox profile
event stream
evidence retention
```

The config is data-first. Runtime adapters load it and produce ports. Kernel
packages do not import adapter config types.

## Default Policy

The scaffold starts with `local_dev_safe`:

```txt
autonomy
  bounded_autonomy inside workspace scratch paths

read
  project files and memory seeds

write
  workspace/**
  .jarvis/artifacts/**

execute
  Docker or namespace-isolated sandbox only

network
  denied by default

external send
  denied by default

credentials
  denied by default

command timeout
  120 seconds

grant expiry
  current WorkSession

pending request limit
  20 per WorkSession
```

Equivalent blocked actions coalesce into one pending request with multiple
evidence references.

## Golden Path API

The scaffold exposes one direct TypeScript flow:

```ts
import { createJarvisLocalRuntime } from "@jarvis/runtime-local";

const jarvis = await createJarvisLocalRuntime({
  config: "./jarvis.config.ts"
});

const pair = await jarvis.pairs.create({
  human: { handle: "abi" },
  agent: { handle: "jarvis" }
});

const work = await jarvis.workSessions.start({
  humanAgentPairId: pair.id,
  objective: "Inspect the repo and propose the next implementation step"
});

await jarvis.workSessions.send(work.id, {
  actor: "human",
  content: "Start with the README and package layout."
});

for await (const event of jarvis.workSessions.events(work.id)) {
  if (event.type === "request_created") {
    await jarvis.requests.resolve(event.request_id, {
      decision: "approve_with_narrower_scope",
      scope: "read-only project files"
    });
  }
}
```

These names define the v0.1 public API contract.

## CLI Path

The scaffold exposes the same flow through CLI:

```txt
npm run jarvis:dev
npm run jarvis:session -- --objective "Inspect the repo and propose next step"
npm run jarvis:requests
npm run jarvis:approve -- --request <id> --scope "read-only project files"
npm run jarvis:evidence -- --work-session <id>
```

The CLI talks to the same WorkSession, Request, Review, Event, and Evidence
contracts as the TypeScript API.
