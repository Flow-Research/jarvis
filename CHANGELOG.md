# Changelog

All notable Jarvis protocol changes are recorded here.

## v0.1.0 - Protocol Alpha

Status: planned tag.

Jarvis v0.1 is accepted as Protocol Alpha by the v0.1 acceptance decision.
This changelog entry prepares the public tag. It does not release, tag,
certify, designate an official host, claim production adoption, establish
foundation governance, or create long-term support.

### Added

- Human-agent collaboration and shared-learning thesis.
- Core protocol object model:
  `Worker`, `Actor`, `HumanWorker`, `AgentWorker`, `WorkSession`,
  `JarvisEvent`, `Policy`, `PolicyDecision`, `Request`, `Review`, `Takeover`,
  `Contribution`, `EvidenceManifest`, `LearningRecord`, `MemoryProposal`,
  `SkillProposal`, and `OutcomeReport`.
- Request, Review, ApprovalScope, and Takeover lifecycle rules.
- Contribution, evidence, governed learning, memory proposal, skill proposal,
  and outcome report contracts.
- OpenAPI 3.1 communication binding.
- Zero-trust mutation headers and protocol error envelope.
- Conformance checklist, golden-path fixture, invalid fixtures, and fixture
  validator.
- Existing-agent compatibility mapping and protocol-record examples.
- Public non-normative simulation.
- v0.1 acceptance review with Gates 1 through 8 accepted and Gate 9 decision
  recorded.

### Boundary

- Hosts own UI, auth, storage, queues, execution, isolation, models, tools,
  billing, monitoring, deployment, and host workflow.
- Jarvis does not include SDK implementation, adapters, wrappers, runtime
  behavior, host UI, model orchestration, tool execution, storage behavior,
  auth behavior, billing behavior, scoring behavior, payment behavior, or
  deployment behavior.

### Validation

- `python3 scripts/check_conformance_fixtures.py`
- `python3 scripts/check_openapi_contract.py`
- `python3 scripts/check_markdown_links.py`
- `python3 scripts/check_protocol_wording.py`
- `git diff --check`
