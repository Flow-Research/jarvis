# Gate 3 Conformance Surface Audit

Status: pass.

Review date: 2026-06-30.

Branch: `codex/v0.1-gate-3-conformance-surface-audit`.

Base commit audited: `b093337`.

Working-tree audit state: Gate 3 diff on top of `b093337`.

Decision: Gate 3 passes. Every required proof row passes and no blocker
remains.

## Scope

Audited sources:

- [../../conformance/checklist.md](../../conformance/checklist.md)
- [../../conformance/golden-path.md](../../conformance/golden-path.md)
- [../../conformance/failure-modes.md](../../conformance/failure-modes.md)
- [../../conformance/fixtures/README.md](../../conformance/fixtures/README.md)
- [../../conformance/fixtures/valid/golden-path.json](../../conformance/fixtures/valid/golden-path.json)
- [../../conformance/fixtures/invalid/](../../conformance/fixtures/invalid/)
- [../../../scripts/check_conformance_fixtures.py](../../../scripts/check_conformance_fixtures.py)
- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)

Out of scope:

```txt
SDK implementation
adapter implementation
wrapper implementation
host runtime behavior
host UI behavior
model orchestration
tool execution
storage behavior
auth behavior
billing behavior
scoring behavior
payment behavior
deployment behavior
```

## Source Coverage

| Source group | Covered paths | Gate 3 check | Result |
| --- | --- | --- | --- |
| Public checklist | `docs/conformance/checklist.md` | Golden path, required headers, compatibility gates, fixture-backed rejection ids, non-fixture-backed error ids, error envelope, public compatibility claim | pass |
| Fixture entry | `docs/conformance/fixtures/README.md` | Fixture layout, envelope, operations, assertions, validator contract, host boundary | pass |
| Fixture records | `docs/conformance/fixtures/valid/golden-path.json`, `docs/conformance/fixtures/invalid/*.json` | Golden path and 24 invalid rejection fixtures | pass |
| Validator | `scripts/check_conformance_fixtures.py` | Required fixture set, OpenAPI operation binding, headers, revision/hash binding, forbidden export fields, event chain, golden-path semantics, invalid rejection semantics, assertion coverage | pass |
| OpenAPI source | `docs/openapi/jarvis-openapi.yaml` | Operation ids, protocol error ids, schema refs used by fixtures | pass |
| Acceptance audit artifact | `docs/planning/v0.1-acceptance-review/gate-3-conformance-surface-audit.md` | Gate proof matrix, blocker ledger, command evidence, changed-file coverage | pass |

Every changed file belongs to a coverage row:

| Changed file | Coverage row |
| --- | --- |
| `docs/conformance/fixtures/README.md` | Fixture entry |
| `docs/conformance/fixtures/valid/golden-path.json` | Fixture records |
| `docs/conformance/fixtures/invalid/*.json` | Fixture records |
| `scripts/check_conformance_fixtures.py` | Validator |
| `docs/planning/v0.1-acceptance-review/gate-3-conformance-surface-audit.md` | Acceptance audit artifact |

## Required Proof Matrix

| ID | Required proof | Evidence | Result |
| --- | --- | --- | --- |
| G3-01 | golden-path fixture validates | `docs/conformance/fixtures/valid/golden-path.json`, `scripts/check_conformance_fixtures.py:1034`, `scripts/check_conformance_fixtures.py:1639` | pass |
| G3-02 | invalid fixtures validate | `docs/conformance/fixtures/invalid/`, `scripts/check_conformance_fixtures.py:99`, `scripts/check_conformance_fixtures.py:1643` | pass |
| G3-03 | fixture-backed rejection ids match checklist | `docs/conformance/checklist.md:387`, `scripts/check_conformance_fixtures.py:99`, `scripts/check_conformance_fixtures.py:1651` | pass |
| G3-04 | unsupported non-fixture rejection ids remain documented without claiming fixture coverage | `docs/conformance/checklist.md:418`, `docs/conformance/checklist.md:423` | pass |
| G3-05 | validator checks required headers | `scripts/check_conformance_fixtures.py:130`, `scripts/check_conformance_fixtures.py:140`, `scripts/check_conformance_fixtures.py:148`, `scripts/check_conformance_fixtures.py:765` | pass |
| G3-06 | validator checks expected revision and previous event hash | `scripts/check_conformance_fixtures.py:424`, `scripts/check_conformance_fixtures.py:915`, `scripts/check_conformance_fixtures.py:1007` | pass |
| G3-07 | validator checks Actor authority fixture semantics | `scripts/check_conformance_fixtures.py:369`, `scripts/check_conformance_fixtures.py:1481` | pass |
| G3-08 | validator checks PolicyDecision ordering semantics | `scripts/check_conformance_fixtures.py:1080`, `scripts/check_conformance_fixtures.py:1249` | pass |
| G3-09 | validator checks Request resolution semantics | `scripts/check_conformance_fixtures.py:1088`, `scripts/check_conformance_fixtures.py:1266`, `scripts/check_conformance_fixtures.py:1290` | pass |
| G3-10 | validator checks Takeover epoch semantics | `scripts/check_conformance_fixtures.py:1377`, `scripts/check_conformance_fixtures.py:1394`, `docs/conformance/checklist.md:230` | pass |
| G3-11 | validator checks forbidden host-private export fields | `scripts/check_conformance_fixtures.py:172`, `scripts/check_conformance_fixtures.py:549`, `docs/conformance/checklist.md:44` | pass |
| G3-12 | validator checks sealed WorkSession and sealed EvidenceManifest mutation | `scripts/check_conformance_fixtures.py:1434`, `scripts/check_conformance_fixtures.py:1447`, `docs/conformance/checklist.md:157`, `docs/conformance/checklist.md:291` | pass |
| G3-13 | public checklist covers ApprovalScope bounds | `docs/conformance/checklist.md:212`, `docs/conformance/checklist.md:219` | pass |
| G3-14 | public checklist covers Contribution attribution | `docs/conformance/checklist.md:248`, `docs/conformance/checklist.md:252` | pass |
| G3-15 | public checklist covers EvidenceManifest completeness and capture timing | `docs/conformance/checklist.md:268`, `docs/conformance/checklist.md:272`, `docs/conformance/checklist.md:275` | pass |
| G3-16 | public checklist covers MemoryProposal and SkillProposal governance | `docs/conformance/checklist.md:317`, `docs/conformance/checklist.md:334` | pass |
| G3-17 | public checklist covers OutcomeReport learning hook | `docs/conformance/checklist.md:349`, `docs/conformance/checklist.md:358` | pass |
| G3-18 | public checklist covers protocol error envelope | `docs/conformance/checklist.md:463`, `docs/conformance/checklist.md:465` | pass |
| G3-19 | public checklist covers capability negotiation and extension rejection | `docs/conformance/checklist.md:370`, `docs/conformance/checklist.md:374`, `docs/conformance/checklist.md:381` | pass |
| G3-20 | validator checks global assertion-class coverage | `scripts/check_conformance_fixtures.py:90`, `scripts/check_conformance_fixtures.py:1526`, `scripts/check_conformance_fixtures.py:1691` | pass |

## Source Findings

| Finding ID | Blocker ID | Severity | Source | Gate proof affected | Finding | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G3-F1 | G3-B1 | blocker | `scripts/check_conformance_fixtures.py` | G3-07, G3-08, G3-09, G3-10, G3-12, G3-20 | The validator checked fixture envelopes, operation binding, header classes, event hash shape, and assertion labels, but it did not prove several semantic rejection shapes. A fixture label alone did not prove invalid Request, PolicyDecision, Takeover, sealed mutation, or learning-governance rejection state. | Added golden-path semantic checks, invalid rejection semantic checks, and global assertion-class coverage checks. The validator now rejects fake semantic fixtures for Actor authority, missing Policy, missing PolicyDecision, Request resolution, ApprovalScope, Takeover epoch, evidence export state, sealed WorkSession mutation, sealed EvidenceManifest mutation, silent memory mutation, silent skill activation, OutcomeReport learning refs, and golden-path proof. | resolved |
| G3-F2 | G3-B2 | blocker | `docs/conformance/fixtures/README.md` | G3-03, G3-20 | The fixture README described envelope, operation, header, and host-private validation but did not state the full semantic validator contract. | Updated the fixture README to name global assertion-class coverage, golden-path semantic coverage, invalid rejection semantics, WorkSession revision and previous-hash binding, and host-private export boundaries. | resolved |
| G3-F3 | G3-B3 | blocker | `scripts/check_conformance_fixtures.py` | G3-01, G3-09, G3-13, G3-15, G3-17 | Golden-path checks proved object presence but did not bind `PolicyDecision -> Request -> Review -> ApprovalScope -> EvidenceManifest -> LearningRecord -> OutcomeReport` by protocol ids. | Added cross-object golden-path binding for PolicyDecision, Request, Review, ApprovalScope, Contribution, EvidenceManifest, LearningRecord, MemoryProposal, SkillProposal, and OutcomeReport. | resolved |
| G3-F4 | G3-B4 | blocker | `scripts/check_conformance_fixtures.py` | G3-09, G3-10, G3-12 | Several invalid fixture checks accepted unrelated records instead of the rejecting operation body, Actor, WorkSession, and scope. | Bound `request_unresolved`, `stale_takeover_epoch`, `invalid_evidence_export_state`, `sealed_work_session_mutation`, and `sealed_evidence_mutation` to the rejecting operation and target WorkSession. | resolved |
| G3-F5 | G3-B5 | blocker | `scripts/check_conformance_fixtures.py` | G3-05 | `stale_request_timestamp` checked timestamp format but did not prove stale time. | Added timestamp comparison between `Jarvis-Request-Timestamp` and the submitted protocol body timestamp. | resolved |
| G3-F6 | G3-B6 | blocker | `scripts/check_conformance_fixtures.py` | G3-09 | Request review-resolution status coverage omitted `needs_revision`. | Added `needs_revision` to review-resolved Request status validation. | resolved |
| G3-F7 | G3-B7 | blocker | `docs/conformance/fixtures/README.md`, `docs/conformance/fixtures/**/*.json` | G3-03, G3-15 | Public fixture docs and fixture source refs contained week-planning references, and the invalid EvidenceManifest fixture used stale `externally_submitted` wording. | Replaced planning references with stable conformance, protocol, and validator sources, and changed final export wording to `completed`, `failed`, `cancelled`, or `closed`. | resolved |

## Blocker List

No blocker remains.

| Blocker ID | Source | Gate proof failed | Resolution evidence | Status |
| --- | --- | --- | --- | --- |
| G3-B1 | Conformance validator semantic coverage | G3-07, G3-08, G3-09, G3-10, G3-12, G3-20 | `scripts/check_conformance_fixtures.py:1034`, `scripts/check_conformance_fixtures.py:1227`, `scripts/check_conformance_fixtures.py:1526`, `scripts/check_conformance_fixtures.py:1639` | resolved |
| G3-B2 | Fixture README validator contract | G3-03, G3-20 | `docs/conformance/fixtures/README.md:121` | resolved |
| G3-B3 | Golden-path cross-object binding | G3-01, G3-09, G3-13, G3-15, G3-17 | `scripts/check_conformance_fixtures.py:1080`, `scripts/check_conformance_fixtures.py:1088`, `scripts/check_conformance_fixtures.py:1104`, `scripts/check_conformance_fixtures.py:1175`, `scripts/check_conformance_fixtures.py:1210` | resolved |
| G3-B4 | Invalid fixture rejecting-operation binding | G3-09, G3-10, G3-12 | `scripts/check_conformance_fixtures.py:1301`, `scripts/check_conformance_fixtures.py:1377`, `scripts/check_conformance_fixtures.py:1417`, `scripts/check_conformance_fixtures.py:1434`, `scripts/check_conformance_fixtures.py:1447` | resolved |
| G3-B5 | Stale request timestamp proof | G3-05 | `scripts/check_conformance_fixtures.py:97`, `scripts/check_conformance_fixtures.py:1236` | resolved |
| G3-B6 | Request `needs_revision` resolution coverage | G3-09 | `scripts/check_conformance_fixtures.py:89`, `scripts/check_conformance_fixtures.py:1277` | resolved |
| G3-B7 | Public fixture source wording | G3-03, G3-15 | `docs/conformance/fixtures/README.md:110`, `docs/conformance/fixtures/valid/golden-path.json:10`, `docs/conformance/fixtures/invalid/invalid-evidence-export-state.json:254` | resolved |

## Command Evidence

Commands run after Gate 3 fixes:

| Command | Exit status | Output summary |
| --- | --- | --- |
| `python3 scripts/check_conformance_fixtures.py` | 0 | `conformance fixtures ok` |
| `python3 scripts/check_protocol_wording.py` | 0 | `protocol wording ok` |
| `python3 scripts/check_markdown_links.py` | 0 | `markdown links ok` |
| `python3 scripts/check_openapi_contract.py` | 0 | `openapi contract ok` |
| `git diff --check` | 0 | no output |
| `node --check demo/assets/app.js` | 0 | no output |

Pre-stage working-tree state at audit time:

```txt
 M docs/conformance/fixtures/README.md
 M docs/conformance/fixtures/invalid/forbidden-host-private-export-field.json
 M docs/conformance/fixtures/invalid/invalid-approval-scope.json
 M docs/conformance/fixtures/invalid/invalid-evidence-export-state.json
 M docs/conformance/fixtures/invalid/invalid-previous-event-hash.json
 M docs/conformance/fixtures/invalid/missing-actor.json
 M docs/conformance/fixtures/invalid/missing-expected-work-session-revision.json
 M docs/conformance/fixtures/invalid/missing-idempotency-key.json
 M docs/conformance/fixtures/invalid/missing-policy-decision.json
 M docs/conformance/fixtures/invalid/missing-policy.json
 M docs/conformance/fixtures/invalid/missing-previous-event-hash.json
 M docs/conformance/fixtures/invalid/missing-protocol-version.json
 M docs/conformance/fixtures/invalid/missing-request-timestamp.json
 M docs/conformance/fixtures/invalid/missing-review-resolution.json
 M docs/conformance/fixtures/invalid/missing-takeover-resolution.json
 M docs/conformance/fixtures/invalid/outcome-report-without-learning-record.json
 M docs/conformance/fixtures/invalid/sealed-evidence-mutation.json
 M docs/conformance/fixtures/invalid/sealed-work-session-mutation.json
 M docs/conformance/fixtures/invalid/silent-memory-mutation.json
 M docs/conformance/fixtures/invalid/silent-skill-activation.json
 M docs/conformance/fixtures/invalid/stale-request-timestamp.json
 M docs/conformance/fixtures/invalid/stale-takeover-continuation.json
 M docs/conformance/fixtures/invalid/stale-work-session-revision.json
 M docs/conformance/fixtures/invalid/unauthorized-actor.json
 M docs/conformance/fixtures/invalid/unresolved-request.json
 M docs/conformance/fixtures/valid/golden-path.json
 M scripts/check_conformance_fixtures.py
?? docs/planning/v0.1-acceptance-review/gate-3-conformance-surface-audit.md
```

Tracked diff stat before staging:

```txt
 docs/conformance/fixtures/README.md                |  11 +-
 .../forbidden-host-private-export-field.json       |   4 +-
 .../fixtures/invalid/invalid-approval-scope.json   |   4 +-
 .../invalid/invalid-evidence-export-state.json     |   6 +-
 .../invalid/invalid-previous-event-hash.json       |   4 +-
 .../fixtures/invalid/missing-actor.json            |   4 +-
 .../missing-expected-work-session-revision.json    |   4 +-
 .../fixtures/invalid/missing-idempotency-key.json  |   4 +-
 .../fixtures/invalid/missing-policy-decision.json  |   4 +-
 .../fixtures/invalid/missing-policy.json           |   4 +-
 .../invalid/missing-previous-event-hash.json       |   4 +-
 .../fixtures/invalid/missing-protocol-version.json |   4 +-
 .../invalid/missing-request-timestamp.json         |   4 +-
 .../invalid/missing-review-resolution.json         |   4 +-
 .../invalid/missing-takeover-resolution.json       |   4 +-
 .../outcome-report-without-learning-record.json    |   4 +-
 .../fixtures/invalid/sealed-evidence-mutation.json |   4 +-
 .../invalid/sealed-work-session-mutation.json      |   4 +-
 .../fixtures/invalid/silent-memory-mutation.json   |   4 +-
 .../fixtures/invalid/silent-skill-activation.json  |   4 +-
 .../fixtures/invalid/stale-request-timestamp.json  |   4 +-
 .../invalid/stale-takeover-continuation.json       |   5 +-
 .../invalid/stale-work-session-revision.json       |   4 +-
 .../fixtures/invalid/unauthorized-actor.json       |   4 +-
 .../fixtures/invalid/unresolved-request.json       |   4 +-
 docs/conformance/fixtures/valid/golden-path.json   |   2 +-
 scripts/check_conformance_fixtures.py              | 721 ++++++++++++++++++++-
 27 files changed, 775 insertions(+), 58 deletions(-)
```

Tracked diff name-only before staging:

```txt
docs/conformance/fixtures/README.md
docs/conformance/fixtures/invalid/forbidden-host-private-export-field.json
docs/conformance/fixtures/invalid/invalid-approval-scope.json
docs/conformance/fixtures/invalid/invalid-evidence-export-state.json
docs/conformance/fixtures/invalid/invalid-previous-event-hash.json
docs/conformance/fixtures/invalid/missing-actor.json
docs/conformance/fixtures/invalid/missing-expected-work-session-revision.json
docs/conformance/fixtures/invalid/missing-idempotency-key.json
docs/conformance/fixtures/invalid/missing-policy-decision.json
docs/conformance/fixtures/invalid/missing-policy.json
docs/conformance/fixtures/invalid/missing-previous-event-hash.json
docs/conformance/fixtures/invalid/missing-protocol-version.json
docs/conformance/fixtures/invalid/missing-request-timestamp.json
docs/conformance/fixtures/invalid/missing-review-resolution.json
docs/conformance/fixtures/invalid/missing-takeover-resolution.json
docs/conformance/fixtures/invalid/outcome-report-without-learning-record.json
docs/conformance/fixtures/invalid/sealed-evidence-mutation.json
docs/conformance/fixtures/invalid/sealed-work-session-mutation.json
docs/conformance/fixtures/invalid/silent-memory-mutation.json
docs/conformance/fixtures/invalid/silent-skill-activation.json
docs/conformance/fixtures/invalid/stale-request-timestamp.json
docs/conformance/fixtures/invalid/stale-takeover-continuation.json
docs/conformance/fixtures/invalid/stale-work-session-revision.json
docs/conformance/fixtures/invalid/unauthorized-actor.json
docs/conformance/fixtures/invalid/unresolved-request.json
docs/conformance/fixtures/valid/golden-path.json
scripts/check_conformance_fixtures.py
```

## Gate 3 Decision

Gate 3 status: pass.

Accepted proof rows: G3-01 through G3-20.

Resolved blockers: G3-B1, G3-B2, G3-B3, G3-B4, G3-B5, G3-B6, G3-B7.

Remaining blockers: none.

Decision rationale:

```txt
Jarvis v0.1 conformance now has public checklist coverage, fixture-backed
golden-path and invalid rejection proof, OpenAPI-bound operation validation,
zero-trust header checks, revision and previous-hash checks, cross-object
protocol id binding, rejecting-operation semantic checks, host-private export
rejection, sealed-record mutation rejection, stale timestamp rejection,
learning-governance checks, and global assertion-class coverage without
executing host-owned runtime behavior.
```
