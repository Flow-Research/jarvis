# Protocol Publication Discipline

Status: adopted input.

Review date: 2026-06-30.

This review records Jarvis-owned publication rules for v0.1 acceptance.
Research inputs stay outside this repository.
Jarvis records only the discipline it adopts.

This review does not change Jarvis semantics.
This review does not add host execution, adapters, UI, auth, storage, model
routing, tool execution, runtime behavior, or product workflow.

## Adopted Publication Rules

Jarvis v0.1 acceptance includes these protocol-publication rules:

```txt
public version labels MUST stay consistent
conformance claims MUST use a precise claim format
conformance proof MUST name the tested suite or fixture set
extension rules MUST preserve the rigid core
public release notes MUST record known limits
security disclosure and governance gaps MUST stay visible
machine-readable contracts and prose contracts MUST cross-check each other
public examples MUST stay separate from protocol claims
```

These rules strengthen Jarvis as a protocol.
They do not add host-owned implementation scope to Jarvis.

## v0.1 Acceptance Additions

Jarvis v0.1 acceptance includes a protocol-publication discipline gate.

The gate checks:

- `README.md`, `docs/openapi/jarvis-openapi.yaml`, architecture brief,
  conformance docs, examples, demo text, and roadmap use consistent v0.1
  status language.
- Public conformance wording names exact proof instead of vague compliance.
- Compatibility claims include protocol version, conformance surface, fixture
  or checklist basis, and verification date.
- Public docs reject `certified` language unless a governance process creates
  certification later.
- Extension and capability text preserves namespaced extensions and rejects
  core-field override.
- Release-readiness notes record missing or deferred governance, changelog,
  citation, security, license, issue-template, PR-template, CI, release-note,
  known-limit, website, and conformance-report work.
- Jarvis v0.1 does not claim long-term stable support language before v1.0.
- The non-normative simulation remains public explanation, not conformance
  proof.

## Adopted Shape

Jarvis keeps the current v0.1 protocol contract and adds publication discipline
around it.

```txt
Protocol contract
  -> OpenAPI 3.1 binding
  -> conformance fixtures
  -> compatibility examples
  -> public README and simulation boundary
  -> protocol-publication discipline
  -> acceptance decision
```

## Deferred From v0.1

These repo-shape items remain outside v0.1 acceptance unless they block public
correctness:

- installable SDK packages
- adapter packages
- bridge packages
- public adopter registry
- full governance process
- trademark process
- foundation transition process
- paid or third-party certification
- long-term support commitments
- multi-year standards-body roadmap
- production reference implementation packages

The acceptance decision records these as next-phase work when they remain
missing.
Their absence does not block v0.1 Protocol Alpha unless public docs claim they
exist.

## Conformance Claims

Jarvis compatibility claims MUST use a precise format:

```txt
Implementation: <name> <implementation-version>
Protocol compatibility: Jarvis <protocol-version>
Conformance surface: <conformance-surface>
Verification date: <date>
Verifier: <verifier-or-self-attested-status>
Evidence: <evidence-ref>
```

Example:

```txt
Implementation: ExampleHost 0.1.0
Protocol compatibility: Jarvis v0.1
Conformance surface: v0.1 golden-path and failure-mode fixtures
Verification date: 2026-07-03
Verifier: self-attested
Evidence: artifact:examplehost-fixture-run-20260703
```

Jarvis rejects vague claims:

```txt
Jarvis compliant
Jarvis certified
fully Jarvis ready
official Jarvis host
```

## Version Consistency

Jarvis v0.1 acceptance MUST verify public version consistency.

The check covers:

```txt
README status
OpenAPI info.version
OpenAPI x-jarvis-protocol.version
architecture brief status
conformance fixture protocol_version
roadmap status
demo text
acceptance decision record
release notes when present
citation metadata when present
```

OpenAPI `info.version: 0.1.0` identifies the OpenAPI artifact version.
OpenAPI `x-jarvis-protocol.version: v0.1` identifies the Jarvis protocol line.
Those labels do not conflict when each public document preserves that mapping.

Version drift is an acceptance blocker.

## Rigid Core And Extensions

Jarvis keeps a rigid v0.1 core.

Extensions use namespaced extension fields.
Extensions MUST NOT override core object fields, core lifecycle meanings,
required headers, event-chain rules, conformance gates, or forbidden export
fields.

The protocol rejects extension core-field override through
`extension_core_field_override`.

## Prose And Machine Contract Cross-Check

Jarvis treats prose docs and OpenAPI as one contract with two views.

The acceptance review checks that:

```txt
prose object fields match OpenAPI schema fields
prose operation rules match OpenAPI path requirements
prose security rules match OpenAPI security requirements
prose error ids match OpenAPI error examples
fixtures exercise the same contract
```

When prose and OpenAPI conflict, acceptance fails until the contradiction is
resolved.

## Release-Readiness Gap Log

Jarvis v0.1 acceptance MUST record a release-readiness gap log.

The gap log covers:

```txt
CHANGELOG status
CONTRIBUTING status
SECURITY policy status
CITATION metadata status
license clarity
issue template status
PR template status
CI workflow status
governance process status
public website status
release notes status
known-limit coverage
conformance report format status
```

Missing publication infrastructure becomes either:

```txt
acceptance blocker
next-phase deferral
not applicable for v0.1
```

Each classification MUST record a reason.

## Not Adopted Into Jarvis v0.1

Jarvis does not adopt non-Jarvis:

- domain vocabulary
- producer/subscriber model
- transport-neutral event stream model
- conformance level names
- subscription handshake
- confirmation reply tokens
- reference producer packages
- reference subscriber packages
- bridge packages
- domain extension examples

Jarvis has its own primitive:

```txt
HumanWorker + AgentWorker + WorkSession + Policy + Request + Review +
Contribution + EvidenceManifest + LearningRecord
```

Research inputs inform publication discipline only.
Jarvis remains the human-agent collaboration and learning-loop protocol.

## Acceptance Impact

This review creates Gate 8 in
[acceptance-spec.md](./acceptance-spec.md): Protocol Publication Discipline.

Gate 8 must pass before v0.1 is accepted as Protocol Alpha.
