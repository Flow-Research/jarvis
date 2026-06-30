# Gate 1 Protocol Contract Audit

Status: pass.

Review date: 2026-06-27.

Branch: `codex/v0.1-gate-1-protocol-contract-audit`.

Base commit audited: `34db97a`.

Working-tree audit state: Gate 1 diff on top of `34db97a`.

Decision: Gate 1 passes. Every required proof row passes and no blocker remains.

## Scope

Audited sources:

- [README.md](../../../README.md)
- [AGENTS.md](../../../AGENTS.md)
- [protocol docs](../../protocol/)
- [v0.1 acceptance review spec](./acceptance-spec.md)
- [planning roadmap](../12-30-day-roadmap.md)
- [examples](../../examples/)
- [conformance docs](../../conformance/)
- [OpenAPI contract](../../openapi/jarvis-openapi.yaml)

## Source Coverage

| Source group | Covered paths | Gate 1 check | Result |
| --- | --- | --- | --- |
| Repository source of truth | `README.md`, `AGENTS.md` | Thesis, boundary, object list, SDK boundary, zero-trust rules, direct wording | pass |
| Protocol semantics | `docs/protocol/00-principles.md`, `docs/protocol/01-architecture.md`, `docs/protocol/02-memory.md`, `docs/protocol/03-autonomy-policy.md`, `docs/protocol/04-work-sessions.md`, `docs/protocol/05-skills-tools.md`, `docs/protocol/06-integration-boundaries.md`, `docs/protocol/07-protocol-decisions.md`, `docs/protocol/08-package-contracts.md`, `docs/protocol/09-host-integration.md`, `docs/protocol/10-protocol-mvp.md`, `docs/protocol/11-core-protocol-objects.md`, `docs/protocol/12-request-protocol.md`, `docs/protocol/13-contribution-evidence-learning.md`, `docs/protocol/14-protocol-lock.md`, `docs/protocol/15-openapi-communication-binding.md`, `docs/protocol/16-positioning-adoption-lock.md` | Object vocabulary, lifecycle rules, mutation headers, export boundary, OutcomeReport boundary, host-neutral language | pass |
| Machine contract | `docs/openapi/jarvis-openapi.yaml` | Operation paths, component schemas, security schemes, protocol headers, error model | pass |
| Conformance surface | `docs/conformance/README.md`, `docs/conformance/checklist.md`, `docs/conformance/compatibility-mapping.md`, `docs/conformance/existing-agent-proof-plan.md`, `docs/conformance/failure-modes.md`, `docs/conformance/fixtures/README.md`, `docs/conformance/fixtures/valid/*.json`, `docs/conformance/fixtures/invalid/*.json` | Golden path, failure fixtures, error ids, existing-agent compatibility proof, OutcomeReport rejection rule | pass |
| Public examples | `docs/examples/compatible-host-mapping.md`, `docs/examples/existing-agent-compatibility.md`, `docs/examples/protocol-records.md` | Protocol-only examples, existing-agent record mapping, OutcomeReport example, EvidenceManifest export shape | pass |
| Planning and acceptance | `docs/planning/12-30-day-roadmap.md`, `docs/planning/ROADMAP.md`, `docs/planning/sheets/jarvis_roadmap.*`, `docs/planning/v0.1-acceptance-review/*.md`, `docs/planning/week-1/`, `docs/planning/week-2/`, `docs/planning/week-3/`, `docs/planning/week-4/` | Public roadmap alignment, v0.1 acceptance scope, historical planning drift, stale OutcomeReport wording | pass |
| Review criteria | `docs/reviews/acceptance-criteria.md`, `docs/reviews/13-protocol-readiness-review.md` | Acceptance criteria alignment, direct protocol boundary, non-WorkSession mutation header carve-outs | pass |

Every changed file belongs to a coverage row:

| Changed file | Coverage row |
| --- | --- |
| `AGENTS.md` | Repository source of truth |
| `README.md` | Repository source of truth |
| `docs/conformance/checklist.md` | Conformance surface |
| `docs/conformance/compatibility-mapping.md` | Conformance surface |
| `docs/conformance/fixtures/invalid/outcome-report-without-learning-record.json` | Conformance surface |
| `docs/examples/existing-agent-compatibility.md` | Public examples |
| `docs/examples/protocol-records.md` | Public examples |
| `docs/openapi/jarvis-openapi.yaml` | Machine contract |
| `docs/planning/sheets/jarvis_roadmap.csv` | Planning and acceptance |
| `docs/planning/sheets/jarvis_roadmap.xlsx` | Planning and acceptance |
| `docs/planning/v0.1-acceptance-review/acceptance-spec.md` | Planning and acceptance |
| `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md` | Planning and acceptance |
| `docs/planning/week-1/chunk-4-evidence-learning-lock.md` | Planning and acceptance |
| `docs/protocol/00-principles.md` | Protocol semantics |
| `docs/protocol/01-architecture.md` | Protocol semantics |
| `docs/protocol/02-memory.md` | Protocol semantics |
| `docs/protocol/03-autonomy-policy.md` | Protocol semantics |
| `docs/protocol/04-work-sessions.md` | Protocol semantics |
| `docs/protocol/05-skills-tools.md` | Protocol semantics |
| `docs/protocol/06-integration-boundaries.md` | Protocol semantics |
| `docs/protocol/08-package-contracts.md` | Protocol semantics |
| `docs/protocol/09-host-integration.md` | Protocol semantics |
| `docs/protocol/10-protocol-mvp.md` | Protocol semantics |
| `docs/protocol/11-core-protocol-objects.md` | Protocol semantics |
| `docs/protocol/13-contribution-evidence-learning.md` | Protocol semantics |
| `docs/protocol/14-protocol-lock.md` | Protocol semantics |
| `docs/protocol/15-openapi-communication-binding.md` | Protocol semantics |
| `docs/protocol/16-positioning-adoption-lock.md` | Protocol semantics |
| `docs/reviews/acceptance-criteria.md` | Review criteria |

Out of scope:

```txt
host execution
host UI
auth backend
storage backend
model calls
tool execution
billing
deployment
runtime behavior
adapter implementation
wrapper implementation
```

## Required Proof Matrix

| ID | Required proof | Evidence | Result |
| --- | --- | --- | --- |
| G1-01 | Core object names match across public docs. | `README.md:59-62`, `AGENTS.md:31-57`, `docs/protocol/01-architecture.md:44-64`, `docs/protocol/10-protocol-mvp.md:64-84`, `docs/openapi/jarvis-openapi.yaml:714-742`, `docs/planning/sheets/jarvis_roadmap.csv:2` | pass |
| G1-02 | WorkSession remains the central record. | `README.md:227-239`, `docs/protocol/00-principles.md:120-145`, `docs/protocol/14-protocol-lock.md:187-228` | pass |
| G1-03 | HumanWorker and AgentWorker remain first-class workers and actors. | `AGENTS.md:31-49`, `docs/protocol/00-principles.md:54-61`, `docs/conformance/checklist.md:57-61` | pass |
| G1-04 | PolicyDecision exists before accepted AgentWorker protocol state. | `AGENTS.md:200-205`, `docs/protocol/12-request-protocol.md:98-118`, `docs/conformance/checklist.md:69-70` | pass |
| G1-05 | Request remains scoped deferral, not chat, notification, or authority. | `docs/protocol/12-request-protocol.md:3-20`, `docs/protocol/12-request-protocol.md:44-68`, `docs/conformance/compatibility-mapping.md:81-85` | pass |
| G1-06 | Review and Takeover remain the only human-resolution paths for Request. | `docs/protocol/11-core-protocol-objects.md:45-50`, `docs/protocol/12-request-protocol.md:318-321`, `docs/protocol/12-request-protocol.md:457-486`, `docs/conformance/checklist.md:70-72` | pass |
| G1-07 | Contribution records who did what. | `README.md:79-80`, `docs/protocol/13-contribution-evidence-learning.md:11-79`, `docs/conformance/compatibility-mapping.md:88-89` | pass |
| G1-08 | EvidenceManifest exports portable proof without host-private fields. | `README.md:80-81`, `AGENTS.md:207-209`, `docs/protocol/13-contribution-evidence-learning.md:88-183`, `docs/protocol/14-protocol-lock.md:412-422` | pass |
| G1-09 | LearningRecord, MemoryProposal, and SkillProposal preserve governed learning. | `README.md:81-84`, `docs/protocol/13-contribution-evidence-learning.md:185-286`, `docs/conformance/checklist.md:301-347` | pass |
| G1-10 | OutcomeReport carries post-session feedback without sealed-record mutation. | `README.md:83-84`, `docs/protocol/06-integration-boundaries.md:104-141`, `docs/protocol/13-contribution-evidence-learning.md:288-339`, `docs/openapi/jarvis-openapi.yaml:326-344`, `docs/openapi/jarvis-openapi.yaml:2341-2400` | pass |
| G1-11 | Protocol event envelope remains append-only and attributable. | `docs/protocol/11-core-protocol-objects.md:1197-1240`, `docs/protocol/14-protocol-lock.md:207-228`, `docs/protocol/15-openapi-communication-binding.md:273-282` | pass |
| G1-12 | Portable export format excludes forbidden host-private fields. | `AGENTS.md:207-209`, `docs/protocol/11-core-protocol-objects.md:1661-1692`, `docs/protocol/14-protocol-lock.md:506-532`, `docs/protocol/15-openapi-communication-binding.md:284-304` | pass |
| G1-13 | Version negotiation and capability negotiation remain protocol-owned. | `AGENTS.md:31-57`, `docs/protocol/14-protocol-lock.md:28-33`, `docs/protocol/15-openapi-communication-binding.md:160-202`, `docs/conformance/checklist.md:370-379` | pass |
| G1-14 | Extension rules require namespaced extensions and reject core-field override. | `docs/protocol/11-core-protocol-objects.md:77-89`, `docs/protocol/11-core-protocol-objects.md:106-111`, `docs/protocol/15-openapi-communication-binding.md:450-452`, `docs/conformance/checklist.md:370-379` | pass |
| G1-15 | Protocol error ids and error envelope remain public and portable. | `docs/protocol/15-openapi-communication-binding.md:450-477`, `docs/conformance/checklist.md:463-477`, `docs/openapi/jarvis-openapi.yaml:2401-2477` | pass |
| G1-16 | Conformance expectations remain protocol-owned and host-neutral. | `docs/conformance/checklist.md:1-11`, `docs/conformance/checklist.md:34-47`, `docs/conformance/checklist.md:479-505`, `docs/conformance/compatibility-mapping.md:1-20` | pass |

## Source Findings

| Finding ID | Blocker ID | Severity | Source | Gate proof affected | Finding | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G1-F1 | G1-B2 | blocker | `README.md`, `docs/protocol/16-positioning-adoption-lock.md`, `docs/planning/sheets/jarvis_roadmap.*` | G1-01 | Some definition and roadmap lines named collaboration without shared learning or omitted v0.1 contract objects. | Updated definitions and roadmap sheet object list to include governed shared learning and full v0.1 contract objects. | resolved |
| G1-F2 | G1-B1 | blocker | `docs/protocol/06-integration-boundaries.md`, `docs/protocol/11-core-protocol-objects.md`, `docs/protocol/13-contribution-evidence-learning.md`, `docs/protocol/14-protocol-lock.md`, `docs/protocol/09-host-integration.md`, `docs/examples/protocol-records.md` | G1-10, G1-11, G1-12 | OutcomeReport classification, acceptance-event wording, and export boundary were ambiguous. | Locked OutcomeReport as a v0.1 extension protocol object, outside sealed WorkSession export, submitted through non-WorkSession mutation, with OutcomeReport-backed learning linked through `learning_record_refs`, `outcome_report_refs`, and WorkSession source events. OutcomeReport references governed LearningRecord records and does not create them by side effect. | resolved |
| G1-F3 | G1-B2 | blocker | `docs/protocol/01-architecture.md`, `docs/protocol/10-protocol-mvp.md`, `AGENTS.md`, `docs/protocol/15-openapi-communication-binding.md` | G1-01 | Several full object lists omitted `OutcomeReport`, `PolicyDecision`, `JarvisEvent`, Worker, Actor, HumanWorker, or AgentWorker. | Updated object lists to match the v0.1 protocol contract. | resolved |
| G1-F4 | G1-B4 | blocker | `docs/conformance/checklist.md` | G1-09 | SkillProposal conformance used stale `expired` state. | Replaced with locked `archived` state. | resolved |
| G1-F5 | G1-B5 | blocker | `README.md`, `AGENTS.md`, `docs/protocol/00-principles.md`, `docs/protocol/02-memory.md`, `docs/protocol/03-autonomy-policy.md`, `docs/protocol/04-work-sessions.md`, `docs/protocol/05-skills-tools.md`, `docs/protocol/08-package-contracts.md`, `docs/protocol/10-protocol-mvp.md`, `docs/protocol/15-openapi-communication-binding.md`, `docs/protocol/16-positioning-adoption-lock.md`, `docs/examples/existing-agent-compatibility.md`, `docs/planning/v0.1-acceptance-review/acceptance-spec.md` | G1-01, G1-06, G1-16 | Several lines used advisory, colloquial, product-facing, or host-workflow phrasing. | Replaced with direct protocol ownership, compatibility, and acceptance language. | resolved |
| G1-F6 | none | non-blocker | `docs/protocol/03-autonomy-policy.md`, `docs/protocol/04-work-sessions.md` | G1-01 | Headings used spaced display names for object concepts. | Renamed headings to `WorkSession`, `EvidenceManifest`, and `PolicyDecision`. | resolved |
| G1-F7 | G1-B3 | blocker | `docs/protocol/09-host-integration.md`, `docs/protocol/11-core-protocol-objects.md`, `docs/protocol/14-protocol-lock.md` | G1-12 | Portable export lists used stale names or inconsistent ordering. | Aligned export lists to `protocol_version`, `WorkSession`, `Workers`, `Actors`, `JarvisEvents`, `PolicyDecisions`, `Requests`, `Reviews`, `Takeovers`, `Contributions`, `EvidenceManifest`, `LearningRecords`, `MemoryProposals`, `SkillProposals`, and `limitations`. | resolved |
| G1-F8 | G1-B1 | blocker | `docs/conformance/compatibility-mapping.md`, `docs/conformance/fixtures/invalid/outcome-report-without-learning-record.json`, `docs/reviews/acceptance-criteria.md`, `docs/planning/week-1/chunk-4-evidence-learning-lock.md` | G1-10, G1-16 | Conformance and review sources still said OutcomeReport creates or references LearningRecord. | Replaced with the locked rule: OutcomeReport references at least one LearningRecord and rejects missing `learning_record_refs`. | resolved |
| G1-F9 | G1-B6 | blocker | `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md` | G1-16 | The audit artifact needed explicit changed-file coverage, command exit-status evidence, working-tree provenance, reviewer evidence, and one blocker ledger. | Added changed-file coverage, command table, working-tree status, diff stat, diff name-only evidence, reviewer evidence table, and one blocker ledger. | resolved |
| G1-F10 | G1-B5 | blocker | `docs/protocol/01-architecture.md` | G1-01, G1-16 | The architecture summary used soft phrasing for human judgment and future WorkSession improvement. | Replaced it with direct protocol architecture language: Jarvis defines the collaboration architecture, Policy bounds AgentWorker autonomy, and protocol records carry governed learning. | resolved |
| G1-F11 | G1-B1 | blocker | `docs/protocol/02-memory.md`, `docs/examples/protocol-records.md` | G1-10, G1-16 | Memory and example text implied OutcomeReport produced learning records by side effect, and the example referenced a future LearningRecord from OutcomeReport. | Locked OutcomeReport to existing governed LearningRecord refs, moved later post-session LearningRecord creation into its own governed operation, and fixed example record order. | resolved |

## Blocker List

No blocker remains.

| Blocker ID | Source | Gate proof failed | Resolution evidence | Status |
| --- | --- | --- | --- | --- |
| G1-B1 | OutcomeReport docs, examples, conformance, and review criteria | G1-10, G1-11, G1-12, G1-16 | `docs/protocol/06-integration-boundaries.md:128`, `docs/protocol/13-contribution-evidence-learning.md:302`, `docs/protocol/14-protocol-lock.md:449`, `docs/conformance/checklist.md:358`, `docs/conformance/compatibility-mapping.md:93`, `docs/examples/protocol-records.md:1019`, `docs/examples/protocol-records.md:1023` | resolved |
| G1-B2 | Object-list docs | G1-01 | `AGENTS.md:31`, `docs/protocol/01-architecture.md:44`, `docs/protocol/10-protocol-mvp.md:64`, `docs/protocol/15-openapi-communication-binding.md:18` | resolved |
| G1-B3 | Portable export docs | G1-12 | `docs/protocol/09-host-integration.md:117`, `docs/protocol/11-core-protocol-objects.md:1666`, `docs/protocol/14-protocol-lock.md:509` | resolved |
| G1-B4 | SkillProposal conformance docs | G1-09 | `docs/conformance/checklist.md:344` | resolved |
| G1-B5 | Direct protocol wording | G1-01, G1-06, G1-16 | `README.md:16`, `AGENTS.md:170`, `docs/protocol/01-architecture.md:66`, `docs/protocol/02-memory.md:6`, `docs/protocol/04-work-sessions.md:555`, `docs/protocol/15-openapi-communication-binding.md:369` | resolved |
| G1-B6 | Gate 1 audit artifact evidence | G1-16 | `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:28`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:111`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:127`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:140`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:152`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:163`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:197`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:231` | resolved |

## Reviewer Evidence

| Reviewer | Scope | Findings raised | Blocker mapping | Resolution evidence | Remaining blocker status |
| --- | --- | --- | --- | --- | --- |
| Curie | object-name consistency and semantic drift | OutcomeReport missing from integration-boundary contract list; host export list used stale names; pass decision was premature while those blockers remained | G1-B1, G1-B2, G1-B3 | `docs/protocol/06-integration-boundaries.md:30`, `docs/protocol/06-integration-boundaries.md:128`, `docs/protocol/09-host-integration.md:117` | resolved |
| Pauli | protocol boundary drift | no boundary blocker | none | Host-owned execution, UI, auth, storage, model calls, adapters, and runtime remain outside Jarvis | none |
| Maxwell | direct wording | `AGENTS.md` used adoption-test phrasing instead of protocol compatibility phrasing | G1-B5 | `AGENTS.md:170` | resolved |
| Kepler | acceptance artifact evidence structure | OutcomeReport/LearningRecord contradiction; missing source coverage; missing command and working-tree provenance | G1-B1, G1-B6 | `docs/conformance/compatibility-mapping.md:93`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:28`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:152`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:163` | resolved |
| Banach | acceptance artifact evidence structure | one blocker ledger, changed-file coverage, command table, working-tree provenance, reviewer evidence table | G1-B6 | `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:28`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:111`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:127`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:140`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:152`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:163`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:197`, `docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md:231` | resolved |
| Sagan | direct wording | architecture summary used soft phrasing | G1-B5 | `docs/protocol/01-architecture.md:66` | resolved |
| Avicenna | object consistency and OutcomeReport semantics | memory text implied OutcomeReport creates learning records; example referenced a future LearningRecord from OutcomeReport | G1-B1 | `docs/protocol/02-memory.md:368`, `docs/examples/protocol-records.md:1019`, `docs/examples/protocol-records.md:1023` | resolved |

## Command Evidence

| Command | Exit status | Output summary |
| --- | --- | --- |
| `python3 scripts/check_openapi_contract.py` | 0 | `openapi contract ok` |
| `python3 scripts/check_protocol_wording.py` | 0 | `protocol wording ok` |
| `python3 scripts/check_conformance_fixtures.py` | 0 | `conformance fixtures ok` |
| `python3 scripts/check_markdown_links.py` | 0 | `markdown links ok` |
| `git diff --check` | 0 | no output |
| `node --check demo/assets/app.js` | 0 | no output |

Working-tree state at audit time:

```txt
 M AGENTS.md
 M README.md
 M docs/conformance/checklist.md
 M docs/conformance/compatibility-mapping.md
 M docs/conformance/fixtures/invalid/outcome-report-without-learning-record.json
 M docs/examples/existing-agent-compatibility.md
 M docs/examples/protocol-records.md
 M docs/openapi/jarvis-openapi.yaml
 M docs/planning/sheets/jarvis_roadmap.csv
 M docs/planning/sheets/jarvis_roadmap.xlsx
 M docs/planning/v0.1-acceptance-review/acceptance-spec.md
 M docs/planning/week-1/chunk-4-evidence-learning-lock.md
 M docs/protocol/00-principles.md
 M docs/protocol/01-architecture.md
 M docs/protocol/02-memory.md
 M docs/protocol/03-autonomy-policy.md
 M docs/protocol/04-work-sessions.md
 M docs/protocol/05-skills-tools.md
 M docs/protocol/06-integration-boundaries.md
 M docs/protocol/08-package-contracts.md
 M docs/protocol/09-host-integration.md
 M docs/protocol/10-protocol-mvp.md
 M docs/protocol/11-core-protocol-objects.md
 M docs/protocol/13-contribution-evidence-learning.md
 M docs/protocol/14-protocol-lock.md
 M docs/protocol/15-openapi-communication-binding.md
 M docs/protocol/16-positioning-adoption-lock.md
 M docs/reviews/acceptance-criteria.md
?? docs/planning/v0.1-acceptance-review/gate-1-protocol-contract-audit.md
```

Diff stat at audit time:

```txt
 AGENTS.md                                          |  12 ++--
 README.md                                          |  28 +++++-----
 docs/conformance/checklist.md                      |   8 +--
 docs/conformance/compatibility-mapping.md          |   2 +-
 .../outcome-report-without-learning-record.json    |   4 +-
 docs/examples/existing-agent-compatibility.md      |   2 +-
 docs/examples/protocol-records.md                  |  62 +++++++++++----------
 docs/openapi/jarvis-openapi.yaml                   |   3 +-
 docs/planning/sheets/jarvis_roadmap.csv            |   2 +-
 docs/planning/sheets/jarvis_roadmap.xlsx           | Bin 8570 -> 8594 bytes
 .../v0.1-acceptance-review/acceptance-spec.md      |   4 +-
 .../week-1/chunk-4-evidence-learning-lock.md       |   2 +-
 docs/protocol/00-principles.md                     |   7 +--
 docs/protocol/01-architecture.md                   |  13 +++--
 docs/protocol/02-memory.md                         |  14 +++--
 docs/protocol/03-autonomy-policy.md                |   4 +-
 docs/protocol/04-work-sessions.md                  |  16 +++---
 docs/protocol/05-skills-tools.md                   |   5 +-
 docs/protocol/06-integration-boundaries.md         |  17 ++++--
 docs/protocol/08-package-contracts.md              |  12 ++--
 docs/protocol/09-host-integration.md               |  11 +++-
 docs/protocol/10-protocol-mvp.md                   |   9 +--
 docs/protocol/11-core-protocol-objects.md          |  22 +++++---
 docs/protocol/13-contribution-evidence-learning.md |  21 ++++---
 docs/protocol/14-protocol-lock.md                  |  10 +++-
 docs/protocol/15-openapi-communication-binding.md  |  16 +++---
 docs/protocol/16-positioning-adoption-lock.md      |  12 ++--
 docs/reviews/acceptance-criteria.md                |   2 +-
 28 files changed, 181 insertions(+), 139 deletions(-)
```

Diff name-only at audit time:

```txt
AGENTS.md
README.md
docs/conformance/checklist.md
docs/conformance/compatibility-mapping.md
docs/conformance/fixtures/invalid/outcome-report-without-learning-record.json
docs/examples/existing-agent-compatibility.md
docs/examples/protocol-records.md
docs/openapi/jarvis-openapi.yaml
docs/planning/sheets/jarvis_roadmap.csv
docs/planning/sheets/jarvis_roadmap.xlsx
docs/planning/v0.1-acceptance-review/acceptance-spec.md
docs/planning/week-1/chunk-4-evidence-learning-lock.md
docs/protocol/00-principles.md
docs/protocol/01-architecture.md
docs/protocol/02-memory.md
docs/protocol/03-autonomy-policy.md
docs/protocol/04-work-sessions.md
docs/protocol/05-skills-tools.md
docs/protocol/06-integration-boundaries.md
docs/protocol/08-package-contracts.md
docs/protocol/09-host-integration.md
docs/protocol/10-protocol-mvp.md
docs/protocol/11-core-protocol-objects.md
docs/protocol/13-contribution-evidence-learning.md
docs/protocol/14-protocol-lock.md
docs/protocol/15-openapi-communication-binding.md
docs/protocol/16-positioning-adoption-lock.md
docs/reviews/acceptance-criteria.md
```

## Gate 1 Decision

Gate 1 status: pass.

Accepted proof rows: G1-01 through G1-16.

Resolved blockers: G1-B1, G1-B2, G1-B3, G1-B4, G1-B5, and G1-B6.

Remaining blockers: none.

Decision rationale:

```txt
Jarvis v0.1 protocol sources now agree on the human-agent collaboration and
learning-loop thesis, object vocabulary, WorkSession centrality, zero-trust
PolicyDecision and mutation rules, scoped Request semantics, Review/Takeover
resolution, Contribution attribution, EvidenceManifest export boundary,
governed learning, OutcomeReport extension boundary, append-only event envelope,
portable error model, extension rules, and host-neutral conformance surface.
```
