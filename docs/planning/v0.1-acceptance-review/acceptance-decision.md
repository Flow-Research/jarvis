# v0.1 Acceptance Decision Record

Status: accepted Protocol Alpha.

Decision date: 2026-06-30.

Current decision state: accepted Protocol Alpha.

Jarvis v0.1 is accepted as Protocol Alpha. This decision record did not release
or tag v0.1. The v0.1.0 release status is recorded in
[v0.1.0.md](../../releases/v0.1.0.md).

The release does not certify Jarvis or any implementation, designate an
official host, claim production adoption, establish foundation governance, or
create long-term support.

The final acceptance decision records this result because every acceptance gate
passed, every blocker is resolved, and every accepted gate links evidence.

## Accepted Gates

| Gate | Status | Evidence |
| --- | --- | --- |
| Gate 1: Protocol Contract | accepted | [gate-1-protocol-contract-audit.md](./gate-1-protocol-contract-audit.md) |
| Gate 2: OpenAPI Binding | accepted | [gate-2-openapi-binding-audit.md](./gate-2-openapi-binding-audit.md) |
| Gate 3: Conformance Surface | accepted | [gate-3-conformance-surface-audit.md](./gate-3-conformance-surface-audit.md) |
| Gate 4: Compatibility Examples | accepted | [gate-4-compatibility-examples-audit.md](./gate-4-compatibility-examples-audit.md) |
| Gate 5: Public README And Non-Normative Simulation | accepted | [gate-5-public-readme-simulation-audit.md](./gate-5-public-readme-simulation-audit.md) |
| Gate 6: Boundary And Wording | accepted | [gate-6-boundary-wording-audit.md](./gate-6-boundary-wording-audit.md) |
| Gate 7: Local Validation | accepted | [gate-7-local-validation-audit.md](./gate-7-local-validation-audit.md) |
| Gate 8: Protocol Publication Discipline | accepted | [gate-8-protocol-publication-discipline-audit.md](./gate-8-protocol-publication-discipline-audit.md) |

## Resolved Blockers

| Gate | Resolved blockers |
| --- | --- |
| Gate 1 | G1-B1, G1-B2, G1-B3, G1-B4, G1-B5, G1-B6 |
| Gate 2 | G2-B1, G2-B2, G2-B3 |
| Gate 3 | G3-B1, G3-B2, G3-B3, G3-B4, G3-B5, G3-B6, G3-B7 |
| Gate 4 | G4-B1, G4-B2, G4-B3, G4-B4 |
| Gate 5 | G5-B1, G5-B2, G5-B3, G5-B4, G5-B5, G5-B6, G5-B7 |
| Gate 6 | G6-B1, G6-B2, G6-B3, G6-B4, G6-B5, G6-B6, G6-B7, G6-B8 |
| Gate 7 | none |
| Gate 8 | G8-B1, G8-B2, G8-B3, G8-B4, G8-B5, G8-B6, G8-B7 |

No acceptance-gate blocker remains.

## Release And Next-Phase Items Outside Acceptance Gates

These items stay outside v0.1 acceptance. Completed release-preparation items
support the v0.1.0 release and do not change acceptance semantics. Governance
and next-phase items remain outside v0.1.0.

- `CHANGELOG.md`: complete.
- `CONTRIBUTING.md`: complete.
- `SECURITY.md`: complete.
- citation metadata: complete.
- issue templates: complete.
- PR template: complete.
- validation CI for local protocol checks: complete.
- release notes: complete in [v0.1.0.md](../../releases/v0.1.0.md).
- governance before certification, adopter registry, official-host status,
  foundation-governance, production-adoption, or long-term-support claims:
  outside v0.1.0.
- next-phase protocol specification: future.

## Remaining Risks

No protocol-acceptance risk remains inside the v0.1 acceptance gates.

Remaining risks are outside the acceptance gates:

- Execution creep: Hosts own execution, cloud, isolation, storage, queues, and
  deployment.
- Host implementation creep: Hosts implement Jarvis. Jarvis does not own UI,
  identity, operations, or enterprise controls.
- Task-system creep: Task systems own tasks, rubrics, evaluation, and
  settlement. Jarvis owns the collaboration record that external reviewers and
  systems evaluate.
- Weak evidence: EvidenceManifest entries are captured during the WorkSession.
- Silent learning: learning becomes MemoryProposal or SkillProposal until
  reviewed.
- SDK creep: Jarvis SDK work stays limited to protocol implementation helpers.
- Release-status drift: v0.1.0 release notes record known limits and reject
  certification, official host status, production adoption, governance, or
  long-term support claims.
- Foundation-governance drift: governance claims are rejected until governance
  exists.

## Release Notes Recorded For Tag

The v0.1.0 release notes record:

- Jarvis v0.1.0 is Protocol Alpha for governed human-agent collaboration and
  shared learning.
- OpenAPI `info.version: 0.1.0` identifies the OpenAPI artifact.
- OpenAPI `x-jarvis-protocol.version: v0.1` identifies the protocol line.
- Gates 1 through 8 passed and all recorded blockers are resolved.
- compatibility claims require protocol version, conformance surface, fixture
  or checklist basis, and verification date.
- Hosts own UI, auth, storage, queues, execution, isolation, models, tools,
  billing, monitoring, deployment, and host workflow.
- Jarvis v0.1.0 does not include SDK implementation, adapters, wrappers, runtime
  behavior, host UI, model orchestration, tool execution, storage behavior,
  auth behavior, billing behavior, scoring behavior, payment behavior,
  deployment behavior, certification, adopter registry, official host status,
  long-term support, or production adoption claims.
- Release-readiness deferrals remain visible.

## Next-Phase Entry Scope

Next-phase work starts only after preserving the v0.1 protocol boundary.

Allowed next-phase entry:

- public release preparation: release notes, `SECURITY.md`, validation CI, and
  visible release-readiness gap tracking
- repository participation readiness: `CHANGELOG.md`, `CONTRIBUTING.md`,
  citation metadata, issue templates, and PR template
- v0.2 Evidence And Learning Beta: richer Contribution taxonomy, stronger
  EvidenceManifest export profiles, limitation and uncertainty records,
  LearningRecord, MemoryProposal, and SkillProposal review-state rules, memory
  scope compatibility rules, and skill proposal compatibility rules
- governance-gap tracking and no-claim rules before any external governance,
  certification, adopter registry, or official-status claim exists outside
  Jarvis
- protocol implementation helper boundary: SDK work remains limited to
  protocol types, OpenAPI clients, event helpers, hash-chain helpers, header
  helpers, validation helpers, EvidenceManifest helpers, conformance fixture
  runners, protocol error helpers, and example record mappers

Rejected next-phase entry:

- host runtime implementation
- agent framework implementation
- model orchestration
- tool execution
- storage backend
- auth provider
- billing system
- scoring system
- deployment stack
- adapter or wrapper code in this repository

## Decision

Jarvis v0.1 is accepted as Protocol Alpha.

Jarvis remains the human-agent collaboration and learning-loop protocol.
Hosts own implementation.

## Reviewer Evidence

| Reviewer | Focus | Initial finding | Resolution | Final status |
| --- | --- | --- | --- | --- |
| Goodall | gate evidence and blocker status | acceptance-decision record needed final accepted state and required Decision Rule fields | final record now includes accepted gates, resolved blockers, deferrals, risks, recorded release notes, next-phase scope, and evidence links | no findings |
| Harvey | public status consistency | public status surfaces needed direct accepted Protocol Alpha language | final acceptance surfaces separated acceptance from release and tag status; v0.1.0 release status is recorded in release notes | no findings |
| Peirce | release, tag, certification, public-status boundary | no-claim language omitted official host, foundation governance, and long-term support | final acceptance surfaces separated acceptance from release and tag status; release notes reject certification, official host, production adoption, foundation governance, and long-term support claims | no findings |
| Aquinas | future-work deferrals, remaining risks, release notes, next-phase scope | no final acceptance blocker; provided concrete entries | decision record includes deferrals, risks, recorded release notes, and next-phase entry scope | no findings |

## Command Evidence

Commands run for the final acceptance decision:

| Command | Exit status | Output summary |
| --- | --- | --- |
| `python3 scripts/check_conformance_fixtures.py` | 0 | `conformance fixtures ok` |
| `python3 scripts/check_openapi_contract.py` | 0 | `openapi contract ok` |
| `python3 scripts/check_markdown_links.py` | 0 | `markdown links ok` |
| `python3 scripts/check_protocol_wording.py` | 0 | `protocol wording ok` |
| `git diff --check` | 0 | no output |
| `node --check demo/assets/app.js` | 0 | no output |
