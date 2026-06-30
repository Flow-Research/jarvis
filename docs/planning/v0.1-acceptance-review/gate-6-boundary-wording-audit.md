# Gate 6 Boundary And Wording Audit

Status: pass.

Review date: 2026-06-30.

Branch: `codex/v0.1-gate-6-boundary-wording-audit`.

Base commit audited: `e4cbcad`.

Working-tree audit state: Gate 6 diff on top of `e4cbcad`.

Decision: Gate 6 passes. Every required proof row passes and no blocker
remains.

## Scope

Audited sources:

- [../../../README.md](../../../README.md)
- [../../../AGENTS.md](../../../AGENTS.md)
- [../../protocol/](../../protocol/)
- [../../examples/](../../examples/)
- [../../conformance/](../../conformance/)
- [../../reviews/](../../reviews/)
- [../../planning/](../../planning/)
- [../../architecture_brief/jarvis_protocol_architecture_brief.md](../../architecture_brief/jarvis_protocol_architecture_brief.md)
- [../../../scripts/check_protocol_wording.py](../../../scripts/check_protocol_wording.py)

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

| Source group | Covered paths | Gate 6 check | Result |
| --- | --- | --- | --- |
| Wording guard | `scripts/check_protocol_wording.py` | Blocks soft protocol wording, advisory drift, stale host-implementation phrasing, and forbidden protocol ownership phrases | pass |
| Protocol docs | `docs/protocol/04-work-sessions.md`, `docs/protocol/13-contribution-evidence-learning.md`, `docs/protocol/16-positioning-adoption-lock.md` | Direct WorkSession state wording, export-read classification, optional host-owned AG-UI mapping | pass |
| Public examples | `docs/examples/protocol-records.md` | Host authentication examples do not prescribe token type or credential format | pass |
| Acceptance and review docs | `docs/planning/v0.1-acceptance-review/acceptance-spec.md`, `docs/reviews/acceptance-criteria.md` | Gate wording uses protocol-owned and host-owned language; export read header rule matches OpenAPI | pass |
| Planning docs | `docs/planning/12-30-day-roadmap.md`, `docs/planning/week-1/README.md`, `docs/planning/week-1/chunk-6-positioning-adoption-lock.md` | Older planning text preserves host-owned AG-UI mapping and avoids stale implementation-scope phrasing | pass |
| Architecture brief | `docs/architecture_brief/jarvis_protocol_architecture_brief.md` | Future work stays outside v0.1 object spine and preserves host-owned adapter boundary | pass |
| Acceptance audit artifact | `docs/planning/v0.1-acceptance-review/gate-6-boundary-wording-audit.md` | Gate proof matrix, blocker ledger, command evidence, changed-file coverage | pass |

Every changed file belongs to a coverage row:

| Changed file | Coverage row |
| --- | --- |
| `docs/architecture_brief/jarvis_protocol_architecture_brief.md` | Architecture brief |
| `docs/examples/protocol-records.md` | Public examples |
| `docs/planning/12-30-day-roadmap.md` | Planning docs |
| `docs/planning/v0.1-acceptance-review/acceptance-spec.md` | Acceptance and review docs |
| `docs/planning/week-1/README.md` | Planning docs |
| `docs/planning/week-1/chunk-6-positioning-adoption-lock.md` | Planning docs |
| `docs/protocol/04-work-sessions.md` | Protocol docs |
| `docs/protocol/13-contribution-evidence-learning.md` | Protocol docs |
| `docs/protocol/16-positioning-adoption-lock.md` | Protocol docs |
| `docs/reviews/acceptance-criteria.md` | Acceptance and review docs |
| `scripts/check_protocol_wording.py` | Wording guard |
| `docs/planning/v0.1-acceptance-review/gate-6-boundary-wording-audit.md` | Acceptance audit artifact |

## Required Proof Matrix

| ID | Required proof | Evidence | Result |
| --- | --- | --- | --- |
| G6-01 | Protocol statements use direct ownership language. | `README.md`, `AGENTS.md`, `docs/protocol/`, `docs/planning/v0.1-acceptance-review/acceptance-spec.md` | pass |
| G6-02 | Host-owned responsibilities stay outside Jarvis. | `docs/protocol/16-positioning-adoption-lock.md`, `docs/planning/12-30-day-roadmap.md`, `docs/planning/week-1/chunk-6-positioning-adoption-lock.md` | pass |
| G6-03 | SDK language stays limited to protocol implementation helpers. | `README.md`, `AGENTS.md`, `docs/protocol/08-package-contracts.md`, `docs/protocol/16-positioning-adoption-lock.md`, `docs/examples/existing-agent-compatibility.md`, `docs/conformance/existing-agent-proof-plan.md` | pass |
| G6-04 | Docs do not use soft wording for locked protocol rules. | `scripts/check_protocol_wording.py`, `python3 scripts/check_protocol_wording.py` | pass |
| G6-05 | Host authentication examples do not prescribe credential format or token type. | `docs/examples/protocol-records.md`, `docs/protocol/15-openapi-communication-binding.md` | pass |
| G6-06 | EvidenceManifest export remains an export read operation, not a six-header mutation. | `docs/protocol/13-contribution-evidence-learning.md`, `docs/reviews/acceptance-criteria.md`, `docs/conformance/checklist.md`, `docs/openapi/jarvis-openapi.yaml` | pass |

## Source Findings

| Finding ID | Blocker ID | Severity | Source | Gate proof affected | Finding | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G6-F1 | G6-B1 | blocker | `docs/examples/protocol-records.md` | G6-02, G6-05 | Public protocol examples used `Authorization: Bearer host-auth-ref`, which prescribed a token type even though Jarvis does not own credential format. | Replaced public header examples with `Authorization: HostAuth fixture`. | resolved |
| G6-F2 | G6-B2 | blocker | `docs/protocol/16-positioning-adoption-lock.md`, `docs/planning/12-30-day-roadmap.md`, `docs/planning/week-1/chunk-6-positioning-adoption-lock.md` | G6-02 | AG-UI positioning made compatible hosts appear to expose Jarvis records to AG-UI clients as a required integration surface. | Rewrote AG-UI language so host-owned code maps Jarvis records only when the host chooses AG-UI integration. Jarvis does not require or define AG-UI integration. | resolved |
| G6-F3 | G6-B3 | blocker | `docs/reviews/acceptance-criteria.md`, `docs/protocol/13-contribution-evidence-learning.md` | G6-06 | EvidenceManifest export was grouped with six-header mutating WorkSession-scoped operations. OpenAPI defines export as an export read. | Split state-changing attribution, evidence, learning, and proposal operations from EvidenceManifest export. Export read now requires host authentication, protocol version, Actor id, and Actor read authority only. | resolved |
| G6-F4 | G6-B4 | blocker | `docs/planning/v0.1-acceptance-review/acceptance-spec.md` | G6-01, G6-02 | Acceptance spec used product-shaped wording in a Gate 4 failure rule and used advisory wording in the Gate 6 failure rule. | Replaced the product-shaped phrase with `host-product behavior` and replaced advisory-language wording with direct protocol failure language. | resolved |
| G6-F5 | G6-B5 | blocker | `scripts/check_protocol_wording.py`, `docs/architecture_brief/jarvis_protocol_architecture_brief.md` | G6-04 | The wording guard missed an advisory drift term, and the architecture brief used that term in a future-area label. | Added the advisory drift term to the wording guard and changed the architecture brief label to `Compatibility rules`. | resolved |
| G6-F6 | G6-B6 | blocker | `docs/protocol/04-work-sessions.md`, `docs/planning/week-1/README.md` | G6-01, G6-04 | WorkSession state text used softer `intended outcome` wording, explanatory `supports` wording, and old implementation-concern phrasing. | Replaced those lines with declared objective, declared completion, protocol basis, preserved resumption basis, and host implementation scope wording. | resolved |
| G6-F7 | G6-B7 | blocker | `docs/architecture_brief/jarvis_protocol_architecture_brief.md` | G6-02, G6-03 | Future work listed `full host adapters` and grouped future work as adapters. | Replaced with host-owned adapter examples and future extension contracts or conformance fixtures. | resolved |
| G6-F8 | G6-B8 | blocker | `docs/planning/v0.1-acceptance-review/gate-4-compatibility-examples-audit.md` | G6-01 | Gate 4 blocker bookkeeping omitted `G4-B4` from the final resolved-blocker list. | Added `G4-B4` to the final resolved-blocker list. | resolved |

## Blocker List

No blocker remains.

| Blocker ID | Source | Gate proof failed | Resolution evidence | Status |
| --- | --- | --- | --- | --- |
| G6-B1 | Host auth examples prescribed Bearer token format | G6-02, G6-05 | `docs/examples/protocol-records.md` | resolved |
| G6-B2 | AG-UI wording implied required host UI integration | G6-02 | `docs/protocol/16-positioning-adoption-lock.md`, `docs/planning/12-30-day-roadmap.md`, `docs/planning/week-1/chunk-6-positioning-adoption-lock.md` | resolved |
| G6-B3 | Export read misclassified as six-header mutation | G6-06 | `docs/reviews/acceptance-criteria.md`, `docs/protocol/13-contribution-evidence-learning.md` | resolved |
| G6-B4 | Acceptance spec carried product-shaped and advisory wording | G6-01, G6-02 | `docs/planning/v0.1-acceptance-review/acceptance-spec.md` | resolved |
| G6-B5 | Wording guard missed advisory drift term | G6-04 | `scripts/check_protocol_wording.py`, `docs/architecture_brief/jarvis_protocol_architecture_brief.md` | resolved |
| G6-B6 | WorkSession and old planning wording needed direct state language | G6-01, G6-04 | `docs/protocol/04-work-sessions.md`, `docs/planning/week-1/README.md` | resolved |
| G6-B7 | Future work wording blurred host-owned adapter boundary | G6-02, G6-03 | `docs/architecture_brief/jarvis_protocol_architecture_brief.md` | resolved |
| G6-B8 | Gate 4 final blocker list missed resolved blocker | G6-01 | `docs/planning/v0.1-acceptance-review/gate-4-compatibility-examples-audit.md` | resolved |

## Reviewer Evidence

| Reviewer | Focus | Initial finding | Resolution | Final status |
| --- | --- | --- | --- | --- |
| Godel | protocol boundary drift | public examples prescribed Bearer auth format | replaced examples with `Authorization: HostAuth fixture` | no findings |
| Boyle | direct wording and soft language | architecture brief label, WorkSession wording, and old planning phrase needed direct protocol language | added guard coverage and replaced wording with direct state language | no findings |
| Pasteur | SDK/helper and adoption boundary | AG-UI wording implied required host-owned UI integration surface | made AG-UI mapping conditional and host-owned across protocol and planning docs | no findings |
| Linnaeus | OpenAPI, conformance, and review consistency | EvidenceManifest export was misclassified as six-header mutation; Gate 4 blocker bookkeeping missed `G4-B4` | separated export read headers from mutation headers and corrected Gate 4 resolved-blocker list | no findings |

## Command Evidence

Commands run after Gate 6 fixes:

| Command | Exit status | Output summary |
| --- | --- | --- |
| `python3 scripts/check_conformance_fixtures.py` | 0 | `conformance fixtures ok` |
| `python3 scripts/check_openapi_contract.py` | 0 | `openapi contract ok` |
| `python3 scripts/check_markdown_links.py` | 0 | `markdown links ok` |
| `python3 scripts/check_protocol_wording.py` | 0 | `protocol wording ok` |
| `git diff --check` | 0 | no output |
| `node --check demo/assets/app.js` | 0 | no output |

Pre-stage working-tree state at audit time:

```txt
 M docs/architecture_brief/jarvis_protocol_architecture_brief.md
 M docs/examples/protocol-records.md
 M docs/planning/12-30-day-roadmap.md
 M docs/planning/v0.1-acceptance-review/acceptance-spec.md
 M docs/planning/week-1/README.md
 M docs/planning/week-1/chunk-6-positioning-adoption-lock.md
 M docs/protocol/04-work-sessions.md
 M docs/protocol/13-contribution-evidence-learning.md
 M docs/protocol/16-positioning-adoption-lock.md
 M docs/reviews/acceptance-criteria.md
 M scripts/check_protocol_wording.py
?? docs/planning/v0.1-acceptance-review/gate-6-boundary-wording-audit.md
```

Final branch diff stat against `main`:

```txt
 .../jarvis_protocol_architecture_brief.md          |   8 +-
 docs/examples/protocol-records.md                  |   6 +-
 docs/planning/12-30-day-roadmap.md                 |   5 +-
 .../v0.1-acceptance-review/acceptance-spec.md      |   7 +-
 .../gate-4-compatibility-examples-audit.md         |   2 +-
 .../gate-6-boundary-wording-audit.md               | 212 +++++++++++++++++++++
 docs/planning/week-1/README.md                     |   4 +-
 .../week-1/chunk-6-positioning-adoption-lock.md    |   9 +-
 docs/protocol/04-work-sessions.md                  |  19 ++-
 docs/protocol/13-contribution-evidence-learning.md |   8 +-
 docs/protocol/16-positioning-adoption-lock.md      |   8 +-
 docs/reviews/acceptance-criteria.md                |   8 +-
 scripts/check_protocol_wording.py                  |   1 +
 13 files changed, 261 insertions(+), 36 deletions(-)
```

Final branch diff name-only against `main`:

```txt
docs/architecture_brief/jarvis_protocol_architecture_brief.md
docs/examples/protocol-records.md
docs/planning/12-30-day-roadmap.md
docs/planning/v0.1-acceptance-review/acceptance-spec.md
docs/planning/v0.1-acceptance-review/gate-4-compatibility-examples-audit.md
docs/planning/v0.1-acceptance-review/gate-6-boundary-wording-audit.md
docs/planning/week-1/README.md
docs/planning/week-1/chunk-6-positioning-adoption-lock.md
docs/protocol/04-work-sessions.md
docs/protocol/13-contribution-evidence-learning.md
docs/protocol/16-positioning-adoption-lock.md
docs/reviews/acceptance-criteria.md
scripts/check_protocol_wording.py
```

## Gate 6 Decision

Gate 6 status: pass.

Accepted proof rows: G6-01 through G6-06.

Resolved blockers: G6-B1, G6-B2, G6-B3, G6-B4, G6-B5, G6-B6, G6-B7, G6-B8.

Remaining blockers: none.

Decision rationale:

```txt
Jarvis v0.1 boundary and wording now preserve direct protocol ownership.
Protocol docs, public examples, planning docs, review docs, and the
architecture brief keep host implementation outside Jarvis. SDK language stays
limited to protocol implementation helpers. Host authentication examples do not
prescribe credential format. AG-UI mapping is optional and host-owned.
EvidenceManifest export remains an export read operation. The wording guard
blocks soft protocol wording and advisory drift terms.
```
