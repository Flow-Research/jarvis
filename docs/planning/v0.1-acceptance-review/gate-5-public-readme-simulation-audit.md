# Gate 5 Public README And Non-Normative Simulation Audit

Status: pass.

Review date: 2026-06-30.

Branch: `codex/v0.1-gate-5-public-readme-simulation-audit`.

Base commit audited: `3b62951`.

Working-tree audit state: Gate 5 diff on top of `3b62951`.

Decision: Gate 5 passes. Every required proof row passes and no blocker
remains.

## Scope

Audited sources:

- [../../../README.md](../../../README.md)
- [../../../demo/index.html](../../../demo/index.html)
- [../../../demo/assets/app.js](../../../demo/assets/app.js)
- [../../../demo/assets/styles.css](../../../demo/assets/styles.css)
- [acceptance-spec.md](./acceptance-spec.md)

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

| Source group | Covered paths | Gate 5 check | Result |
| --- | --- | --- | --- |
| Public README | `README.md` | Protocol-only definition, MCP/A2A/AG-UI positioning, host-owned responsibilities, compatible implementation proof language | pass |
| Demo HTML | `demo/index.html` | Visible non-normative boundary, walkthrough labels, no host UI claim, no extra protocol object or operation names | pass |
| Demo script | `demo/assets/app.js` | Canonical OpenAPI operation naming, host-auth fixture wording, protocol record sequence, no conformance-proof claim | pass |
| Demo styles | `demo/assets/styles.css` | Presentation only, no protocol rule or host behavior | pass |
| Acceptance spec | `docs/planning/v0.1-acceptance-review/acceptance-spec.md` | Gate 5 proof rows and failure conditions | pass |
| Acceptance audit artifact | `docs/planning/v0.1-acceptance-review/gate-5-public-readme-simulation-audit.md` | Gate proof matrix, blocker ledger, command evidence, changed-file coverage | pass |

Every changed file belongs to a coverage row:

| Changed file | Coverage row |
| --- | --- |
| `README.md` | Public README |
| `demo/assets/app.js` | Demo script |
| `demo/assets/styles.css` | Demo styles |
| `demo/index.html` | Demo HTML |
| `docs/planning/v0.1-acceptance-review/gate-5-public-readme-simulation-audit.md` | Acceptance audit artifact |

## Required Proof Matrix

| ID | Required proof | Evidence | Result |
| --- | --- | --- | --- |
| G5-01 | README one-line definition matches protocol docs. | `README.md`, `docs/protocol/14-protocol-lock.md`, `docs/protocol/16-positioning-adoption-lock.md` | pass |
| G5-02 | README positions Jarvis beside MCP, A2A, and AG-UI without replacing them. | `README.md` | pass |
| G5-03 | README states that hosts own UI, storage, auth, execution, models, tools, memory engines, deployment, monitoring, and workflow. | `README.md` | pass |
| G5-04 | Simulation is treated as public explanation only. | `README.md`, `demo/index.html` | pass |
| G5-05 | Simulation remains static public explanation, not host UI implementation. | `README.md`, `demo/index.html`, `demo/assets/app.js`, `demo/assets/styles.css` | pass |
| G5-06 | Simulation does not define additional protocol objects, operations, or conformance rules. | `demo/index.html`, `demo/assets/app.js`, `docs/openapi/jarvis-openapi.yaml` | pass |

## Source Findings

| Finding ID | Blocker ID | Severity | Source | Gate proof affected | Finding | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G5-F1 | G5-B1 | blocker | `docs/planning/v0.1-acceptance-review/` | G5-04, G5-05, G5-06 | Gate 5 had no dedicated audit artifact. The acceptance review requires a gate-level evidence record before a gate is accepted. | Added this Gate 5 audit artifact with source coverage, proof matrix, blocker ledger, reviewer evidence, command evidence, changed-file coverage, and decision. | resolved |
| G5-F2 | G5-B2 | blocker | `demo/assets/app.js` | G5-06 | The demo used `work_session.create`, which looked like an added operation name and did not match the OpenAPI `createWorkSession` operation id. | Replaced the phrase with `createWorkSession`. | resolved |
| G5-F3 | G5-B3 | blocker | `demo/index.html` | G5-04, G5-05 | The public demo page lacked a visible non-normative boundary even though README carried one. A direct page visitor had no page-level boundary separating the walkthrough from protocol proof or host UI. | Added a visible boundary statement: non-normative walkthrough, not protocol proof, not a host UI implementation. | resolved |
| G5-F4 | G5-B4 | blocker | `demo/index.html`, `demo/assets/app.js` | G5-04, G5-05 | Demo labels used `Launch WorkSession`, `Live mission state`, `operating simulation`, `Operating surface`, `State rails`, `Proof plane`, `Evidence ledger`, and `WorkSession is the surface`, which made the public page read closer to host UI or conformance evidence. | Replaced those labels with walkthrough, record, EvidenceManifest, and protocol-record wording. | resolved |
| G5-F5 | G5-B5 | blocker | `README.md`, `demo/index.html`, `demo/assets/app.js` | G5-03, G5-05 | Public wording described agent execution and tool use without immediately preserving the host-owned execution boundary. | Tightened README and demo wording so AgentWorker contribution is expressed through protocol records and host-owned execution/tool use remains explicit. | resolved |
| G5-F6 | G5-B6 | blocker | `demo/assets/app.js` | G5-05 | The demo used `Authorization: Bearer host-auth-ref`, which implied a credential format that Jarvis does not define. | Replaced it with `Authorization: HostAuth fixture`. | resolved |
| G5-F7 | G5-B7 | blocker | `demo/assets/app.js` | G5-05 | OutcomeReport wording implied post-session feedback directly creates or mutates learning state. | Reworded OutcomeReport as feedback linked to governed LearningRecord state without rewriting sealed WorkSession or EvidenceManifest records. | resolved |

## Blocker List

No blocker remains.

| Blocker ID | Source | Gate proof failed | Resolution evidence | Status |
| --- | --- | --- | --- | --- |
| G5-B1 | Missing Gate 5 audit artifact | G5-04, G5-05, G5-06 | `docs/planning/v0.1-acceptance-review/gate-5-public-readme-simulation-audit.md` | resolved |
| G5-B2 | Noncanonical operation-shaped demo wording | G5-06 | `demo/assets/app.js` | resolved |
| G5-B3 | Missing visible demo boundary | G5-04, G5-05 | `demo/index.html` | resolved |
| G5-B4 | Demo labels read like host UI or proof surface | G5-04, G5-05 | `demo/index.html`, `demo/assets/app.js` | resolved |
| G5-B5 | README and demo execution wording needed sharper host boundary | G5-03, G5-05 | `README.md`, `demo/index.html`, `demo/assets/app.js` | resolved |
| G5-B6 | Demo auth wording implied a credential format | G5-05 | `demo/assets/app.js` | resolved |
| G5-B7 | OutcomeReport demo wording implied learning mutation | G5-05 | `demo/assets/app.js` | resolved |

## Reviewer Evidence

| Reviewer | Focus | Initial finding | Resolution | Final status |
| --- | --- | --- | --- | --- |
| Chandrasekhar | acceptance artifact and demo proof boundary | missing Gate 5 artifact; demo proof terminology needed explicit review | added Gate 5 artifact and replaced demo proof/ledger labels with EvidenceManifest and evidence-record wording | no findings |
| Socrates | README/simulation boundary and canonical operation naming | missing Gate 5 artifact; demo used noncanonical `work_session.create`; visible demo boundary missing | added Gate 5 artifact, changed operation text to `createWorkSession`, and added visible demo boundary | no findings |
| Mencius | public README and protocol-boundary drift | README plain-English section and demo proof terms were clarity risks | tightened README host-owned execution language and replaced demo proof terms | no findings |
| Boole | demo object accuracy and non-normative boundary | auth fixture implied bearer credential format; `Context plane` sounded like a new layer | changed auth wording to `HostAuth fixture` and changed label to `Record context` | no findings |

## Command Evidence

Commands run after Gate 5 fixes:

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
 M README.md
 M demo/assets/app.js
 M demo/assets/styles.css
 M demo/index.html
?? docs/planning/v0.1-acceptance-review/gate-5-public-readme-simulation-audit.md
```

Final branch diff stat against `main`:

```txt
 README.md                                          |   8 +-
 demo/assets/app.js                                 |  10 +-
 demo/assets/styles.css                             |  10 ++
 demo/index.html                                    |  32 ++--
 .../gate-5-public-readme-simulation-audit.md       | 176 +++++++++++++++++++++
 5 files changed, 214 insertions(+), 22 deletions(-)
```

Final branch diff name-only against `main`:

```txt
README.md
demo/assets/app.js
demo/assets/styles.css
demo/index.html
docs/planning/v0.1-acceptance-review/gate-5-public-readme-simulation-audit.md
```

## Gate 5 Decision

Gate 5 status: pass.

Accepted proof rows: G5-01 through G5-06.

Resolved blockers: G5-B1, G5-B2, G5-B3, G5-B4, G5-B5, G5-B6, G5-B7.

Remaining blockers: none.

Decision rationale:

```txt
Jarvis v0.1 public README and non-normative demo now preserve the protocol
boundary. README defines Jarvis as the human-agent collaboration and
learning-loop protocol, positions Jarvis beside MCP, A2A, and AG-UI without
replacing them, and states that hosts own implementation. The demo is a static
public walkthrough of protocol records. It does not define host UI behavior,
runtime behavior, model execution, tool execution, adapter behavior,
additional protocol operations, additional protocol objects, or conformance
proof.
```
