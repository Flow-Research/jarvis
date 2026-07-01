# Gate 2 OpenAPI Binding Audit

Status: pass.

Review date: 2026-06-30.

This is a historical Gate 2 audit record. It preserves acceptance evidence from
that gate and is not current normative protocol text.

Branch: `codex/v0.1-gate-2-openapi-binding-audit`.

Base commit audited: `35fd13f`.

Working-tree audit state: Gate 2 diff on top of `35fd13f`.

Decision: Gate 2 passes. Every required proof row passes and no blocker
remains.

## Scope

Audited sources:

- [../../openapi/jarvis-openapi.yaml](../../openapi/jarvis-openapi.yaml)
- [../../../scripts/check_openapi_contract.py](../../../scripts/check_openapi_contract.py)
- [../../protocol/11-core-protocol-objects.md](../../protocol/11-core-protocol-objects.md)
- [../../protocol/15-openapi-communication-binding.md](../../protocol/15-openapi-communication-binding.md)
- [../../conformance/checklist.md](../../conformance/checklist.md)
- [../../conformance/golden-path.md](../../conformance/golden-path.md)
- [../../conformance/failure-modes.md](../../conformance/failure-modes.md)
- [../../examples/protocol-records.md](../../examples/protocol-records.md)

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

| Source group | Covered paths | Gate 2 check | Result |
| --- | --- | --- | --- |
| Machine contract | `docs/openapi/jarvis-openapi.yaml` | OpenAPI 3.1 version, metadata, paths, schemas, parameters, request bodies, responses, security scheme, examples, operation descriptions, operation classes | pass |
| Validator | `scripts/check_openapi_contract.py` | Required schemas, required fields, enum values, forbidden fields, invariants, operation header classes, request bodies, success responses, error responses, examples, conformance entry refs | pass |
| Protocol source | `docs/protocol/11-core-protocol-objects.md`, `docs/protocol/15-openapi-communication-binding.md` | Object field lock, operation list, header matrix, security model, error model, forbidden export fields | pass |
| Conformance source | `docs/conformance/checklist.md`, `docs/conformance/golden-path.md`, `docs/conformance/failure-modes.md` | OpenAPI-backed rejection ids, mutation headers, read authority, evidence export, learning governance | pass |
| Example source | `docs/examples/protocol-records.md` | Example object shape alignment, OutcomeReport learning refs, EvidenceManifest export refs | pass |
| Acceptance audit artifact | `docs/planning/v0.1-acceptance-review/gate-2-openapi-binding-audit.md` | Gate proof matrix, blocker ledger, command evidence, changed-file coverage | pass |

Every changed file belongs to a coverage row:

| Changed file | Coverage row |
| --- | --- |
| `docs/openapi/jarvis-openapi.yaml` | Machine contract |
| `scripts/check_openapi_contract.py` | Validator |
| `docs/planning/v0.1-acceptance-review/gate-2-openapi-binding-audit.md` | Acceptance audit artifact |

## Required Proof Matrix

| ID | Required proof | Evidence | Result |
| --- | --- | --- | --- |
| G2-01 | all core schemas exist | `scripts/check_openapi_contract.py:46`, `docs/openapi/jarvis-openapi.yaml:1232`, `docs/openapi/jarvis-openapi.yaml:2467` | pass |
| G2-02 | required fields match core object field locks | `scripts/check_openapi_contract.py:453`, `scripts/check_openapi_contract.py:1862` | pass |
| G2-03 | core operations exist for Worker, Actor, WorkSession, event, PolicyDecision, Request, Review, Takeover, Contribution, LearningRecord, MemoryProposal, SkillProposal, EvidenceManifest export, and OutcomeReport | `scripts/check_openapi_contract.py:300`, `docs/openapi/jarvis-openapi.yaml:37`, `docs/openapi/jarvis-openapi.yaml:438` | pass |
| G2-04 | every mutating operation requires HostAuth | `scripts/check_openapi_contract.py:2323`, `docs/openapi/jarvis-openapi.yaml:50`, `docs/openapi/jarvis-openapi.yaml:452` | pass |
| G2-05 | WorkSession-scoped mutations require six Jarvis mutation headers | `scripts/check_openapi_contract.py:279`, `scripts/check_openapi_contract.py:2325`, `docs/openapi/jarvis-openapi.yaml:162` | pass |
| G2-06 | non-WorkSession mutations require four Jarvis mutation headers and do not require fake WorkSession revision or previous hash | `scripts/check_openapi_contract.py:288`, `scripts/check_openapi_contract.py:2304`, `docs/openapi/jarvis-openapi.yaml:46`, `docs/openapi/jarvis-openapi.yaml:448` | pass |
| G2-07 | WorkSession-scoped reads and export reads require HostAuth, protocol version, Actor, and Actor read authority | `scripts/check_openapi_contract.py:295`, `scripts/check_openapi_contract.py:2296`, `docs/openapi/jarvis-openapi.yaml:128`, `docs/openapi/jarvis-openapi.yaml:130`, `docs/openapi/jarvis-openapi.yaml:132`, `docs/openapi/jarvis-openapi.yaml:418`, `docs/openapi/jarvis-openapi.yaml:419`, `docs/openapi/jarvis-openapi.yaml:422` | pass |
| G2-08 | Worker registration, Actor registration, and OutcomeReport submission stay non-WorkSession mutations | `docs/openapi/jarvis-openapi.yaml:46`, `docs/openapi/jarvis-openapi.yaml:75`, `docs/openapi/jarvis-openapi.yaml:448`, `scripts/check_openapi_contract.py:303`, `scripts/check_openapi_contract.py:313`, `scripts/check_openapi_contract.py:443` | pass |
| G2-09 | protocol errors expose public error fields only | `docs/openapi/jarvis-openapi.yaml:2528`, `docs/openapi/jarvis-openapi.yaml:2559`, `scripts/check_openapi_contract.py:693`, `scripts/check_openapi_contract.py:1271` | pass |
| G2-10 | portable protocol records reject host-private fields | `scripts/check_openapi_contract.py:1185`, `scripts/check_openapi_contract.py:1881`, `scripts/check_openapi_contract.py:1888`, `docs/openapi/jarvis-openapi.yaml:1153`, `docs/openapi/jarvis-openapi.yaml:2196` | pass |
| G2-11 | examples exist and avoid host-private fields | `scripts/check_openapi_contract.py:1771`, `scripts/check_openapi_contract.py:1789`, `scripts/check_openapi_contract.py:1796`, `docs/openapi/jarvis-openapi.yaml:2828` | pass |
| G2-12 | operation descriptions make the spec implementable without guessing authority or header class | `docs/openapi/jarvis-openapi.yaml:39`, `docs/openapi/jarvis-openapi.yaml:46`, `docs/openapi/jarvis-openapi.yaml:127`, `docs/openapi/jarvis-openapi.yaml:132`, `docs/openapi/jarvis-openapi.yaml:440`, `docs/openapi/jarvis-openapi.yaml:448`, `scripts/check_openapi_contract.py:2279`, `scripts/check_openapi_contract.py:2287` | pass |

## Source Findings

| Finding ID | Blocker ID | Severity | Source | Gate proof affected | Finding | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G2-F1 | G2-B1 | blocker | `docs/openapi/jarvis-openapi.yaml`, `scripts/check_openapi_contract.py` | G2-03, G2-05, G2-06, G2-07, G2-12 | OpenAPI operations had correct parameters and responses, but no summaries, descriptions, or operation-class metadata. A developer reading the OpenAPI had to infer authority semantics and mutation/read class from parameter lists. | Added operation summaries, direct descriptions, and `x-jarvis-operation-class` to every operation. Updated `check_openapi_contract.py` to require operation summaries, descriptions, operation class, read-authority wording, non-WorkSession mutation exclusions, and genesis revision wording. | resolved |
| G2-F2 | G2-B2 | blocker | `docs/openapi/jarvis-openapi.yaml`, `scripts/check_openapi_contract.py` | G2-05, G2-11 | `WorkSessionCreateExample` represented an accepted WorkSession response with revision `0` and `last_event_hash: hash:genesis`, which conflicted with the WorkSession hash-chain rule. | Changed the accepted example to revision `1` and `last_event_hash: hash:event-worksession-created`. Updated `check_openapi_contract.py` to require those accepted response values and require the create operation description to name `hash:protocol-genesis` for the genesis request header. | resolved |
| G2-F3 | G2-B3 | blocker | `docs/openapi/jarvis-openapi.yaml`, `scripts/check_openapi_contract.py` | G2-10 | Export-related forbidden-field metadata omitted `session_cookie` and `private_key` even though the locked OpenAPI binding forbids session cookies and private keys in exports. | Added `session_cookie` and `private_key` to `ExportProfile`, `EvidenceItemRef`, and `EvidenceManifest` forbidden-field metadata and to validator-required forbidden metadata. | resolved |

## Blocker List

No blocker remains.

| Blocker ID | Source | Gate proof failed | Resolution evidence | Status |
| --- | --- | --- | --- | --- |
| G2-B1 | OpenAPI operation semantics | G2-03, G2-05, G2-06, G2-07, G2-12 | `docs/openapi/jarvis-openapi.yaml:39`, `docs/openapi/jarvis-openapi.yaml:46`, `docs/openapi/jarvis-openapi.yaml:127`, `docs/openapi/jarvis-openapi.yaml:132`, `docs/openapi/jarvis-openapi.yaml:440`, `docs/openapi/jarvis-openapi.yaml:448`, `scripts/check_openapi_contract.py:2279`, `scripts/check_openapi_contract.py:2287` | resolved |
| G2-B2 | WorkSession creation example | G2-05, G2-11 | `docs/openapi/jarvis-openapi.yaml:102`, `docs/openapi/jarvis-openapi.yaml:2836`, `docs/openapi/jarvis-openapi.yaml:2837`, `scripts/check_openapi_contract.py:256`, `scripts/check_openapi_contract.py:257`, `scripts/check_openapi_contract.py:2317` | resolved |
| G2-B3 | Export forbidden-field metadata | G2-10 | `docs/openapi/jarvis-openapi.yaml:1157`, `docs/openapi/jarvis-openapi.yaml:1221`, `docs/openapi/jarvis-openapi.yaml:2200`, `scripts/check_openapi_contract.py:1185` | resolved |

## Command Evidence

Commands run after Gate 2 fixes:

| Command | Exit status | Output summary |
| --- | --- | --- |
| `python3 scripts/check_openapi_contract.py` | 0 | `openapi contract ok` |
| `python3 scripts/check_protocol_wording.py` | 0 | `protocol wording ok` |
| `python3 scripts/check_markdown_links.py` | 0 | `markdown links ok` |
| `python3 scripts/check_conformance_fixtures.py` | 0 | `conformance fixtures ok` |
| `git diff --check` | 0 | no output |
| `node --check demo/assets/app.js` | 0 | no output |

Pre-stage working-tree state at audit time:

```txt
 M docs/openapi/jarvis-openapi.yaml
 M scripts/check_openapi_contract.py
?? docs/planning/v0.1-acceptance-review/gate-2-openapi-binding-audit.md
```

Tracked diff stat before staging:

```txt
 docs/openapi/jarvis-openapi.yaml  | 130 +++++++++++++++++++++++++++++++++++++-
 scripts/check_openapi_contract.py |  67 ++++++++++++++++++++
 2 files changed, 195 insertions(+), 2 deletions(-)
```

Tracked diff name-only before staging:

```txt
docs/openapi/jarvis-openapi.yaml
scripts/check_openapi_contract.py
```

## Gate 2 Decision

Gate 2 status: pass.

Accepted proof rows: G2-01 through G2-12.

Resolved blockers: G2-B1, G2-B2, G2-B3.

Remaining blockers: none.

Decision rationale:

```txt
Jarvis v0.1 OpenAPI now carries the machine-readable schema contract, operation
contract, security header contract, error contract, forbidden-field boundary,
examples, operation class metadata, and operation descriptions required for a
compatible implementation to implement protocol record exchange without
guessing Jarvis-owned semantics or adopting host-owned runtime behavior.
```
