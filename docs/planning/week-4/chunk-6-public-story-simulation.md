# Chunk 6: Public Story And Simulation Proof Path

Chunk 6 tightens the public story and updates the simulation to show the
OpenAPI proof path.

## Scope

This chunk updates public-facing explanation and the existing GitHub Pages
simulation.

This chunk does not build product UI, host UI, runtime behavior, adapter code,
SDK code, model orchestration, tool execution, storage, auth, billing, scoring,
payment, or deployment behavior.

## Required Output

Chunk 6 updates:

```txt
README.md
demo/index.html
demo/assets/*
```

Only simulation assets that already belong to the public demo are in scope.

## Public Story

The public story states:

```txt
MCP connects agents to tools.
A2A connects agents to agents.
AG-UI connects agents to UI.
Jarvis records how humans and agents collaborate, produce evidence, and learn.
```

The README explains:

```txt
what Jarvis is
why Jarvis exists
what Jarvis does not replace
how existing agents participate
what compatible implementations prove
what SDK helpers are allowed to do
```

## Simulation Proof Path

The simulation shows:

```txt
WorkSession-scoped mutation carries required headers
Actor authority verified
WorkSession revision checked
previous event hash linked
WorkSession created
Policy attached
AgentWorker action checked
PolicyDecision recorded before accepted action
Request created for blocked or review-required scope
Review or Takeover resolves Request
ApprovalScope bounds Review-approved continuation
Takeover lock epoch and reconciliation refs bound Takeover continuation
Contribution recorded
EvidenceManifest exported without host-private fields
LearningRecord operation recorded
MemoryProposal or SkillProposal remains governed
OutcomeReport enters post-session feedback without sealed-record mutation
```

The simulation must not present Jarvis as a workspace product, runtime,
personal agent, agent framework, scheduler, router, or host UI.

## Review Focus

Review verifies:

- public wording stays protocol-only
- simulation matches protocol objects and OpenAPI proof path
- visual copy avoids product-specific claims
- no new host behavior enters the repo
- README and simulation tell the same story

## Done Criteria

Chunk 6 is complete when:

- README public story is tighter
- simulation shows the OpenAPI proof path
- demo assets render locally or as static files
- local checks pass
- internal reviewer lanes have no valid unresolved findings
- CodeRabbit has no valid unresolved findings
