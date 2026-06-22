# Chunk 7: Week 4 Closeout

Chunk 7 closes Week 4 after compatibility examples, public conformance
checklist, protocol record examples, README updates, and simulation updates are
complete.

## Scope

This chunk records the Week 4 result.

It does not start SDK implementation, adapter implementation, host
implementation, runtime work, model orchestration, tool execution, UI work,
storage work, auth work, billing work, scoring work, payment work, or
deployment work.

## Required Closeout

Chunk 7 records:

- completed compatible host mapping example
- completed existing-agent compatibility example
- completed public conformance checklist
- completed protocol record examples
- completed public README tightening
- completed simulation proof-path update
- local validation output
- internal reviewer lane results
- CodeRabbit result
- remaining public-readiness gaps
- v0.1 acceptance status

## Required Output

Chunk 7 creates:

```txt
docs/planning/week-4/closeout.md
```

## v0.1 Readiness Gate

Week 4 closeout verifies:

- Jarvis remains protocol-only
- compatible examples preserve host-owned execution
- existing agents remain first-class
- SDK language stays limited to protocol implementation helpers
- required mutation headers remain visible by operation class
- accepted WorkSession-scoped state changes verify Actor authority
- WorkSession-scoped mutations check expected revision and previous event hash
- AgentWorker actions record PolicyDecision before accepted protocol state
- Requests resolve only through Review or Takeover
- Takeover resume requires reconciliation refs
- EvidenceManifest export excludes forbidden host-private fields
- public conformance checklist matches fixtures
- examples match OpenAPI field names
- README explains Jarvis without product-specific dependency
- simulation shows protocol proof path
- local checks pass
- automated and human review have no valid unresolved findings

## Done Criteria

Chunk 7 is complete when:

- Week 4 outputs are linked from the closeout
- v0.1 readiness gaps are explicit
- local checks pass
- internal reviewer lanes have no valid unresolved findings
- CodeRabbit has no valid unresolved findings
- roadmap status is ready for the next phase only after review approves it
