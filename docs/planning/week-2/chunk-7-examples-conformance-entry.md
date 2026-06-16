# Week 2 Chunk 7: Examples And Conformance Entry

Chunk 7 locks the first protocol examples and conformance entry checks for the
Jarvis v0.1 OpenAPI contract.

This chunk turns the schema and path contract into readable protocol proof
records.

This chunk adds protocol examples and conformance entry checks only. It does
not add behavior outside the Jarvis contract.

## Scope

This chunk adds:

```txt
components.examples.WorkSessionCreateExample
components.examples.PolicyDecisionDeniedExample
components.examples.RequestBlockedActionExample
components.examples.ReviewApproveRequestExample
components.examples.EvidenceManifestExportExample
components.examples.ProtocolErrorExample
docs/conformance/golden-path.md
docs/conformance/failure-modes.md
validator checks for required examples and conformance documents
```

## Example Rules

OpenAPI examples MUST be portable protocol records.

Examples MUST NOT contain:

```txt
host database ids
credentials
secrets
raw auth tokens
session cookies
provider keys
runtime state
container ids
deployment details
billing data
private scores
UI state
model provider internals
tool execution internals
```

Each example MUST demonstrate one protocol fact:

```txt
WorkSessionCreateExample
  HumanWorker and AgentWorker enter a WorkSession under policy.

PolicyDecisionDeniedExample
  AgentWorker action outside policy records PolicyDecision before Request.

RequestBlockedActionExample
  blocked action creates a scoped Request, not chat or notification.

ReviewApproveRequestExample
  HumanWorker judgment resolves Request through Review and bounded approval.

EvidenceManifestExportExample
  completed work exports portable evidence with policy, request, review,
  contribution, evidence item, and limitation refs.

ProtocolErrorExample
  rejection uses the protocol error envelope and a typed error id.
```

## Required Example Fields

The validator checks structural and protocol-specific example requirements. It
does not perform full JSON Schema validation in Chunk 7.

Required fields:

```txt
WorkSessionCreateExample
  id
  protocol_version
  created_by_actor_id
  objective
  human_worker_id
  agent_worker_id
  policy_id
  status
  revision
  last_event_hash
  event_log_ref
  created_at
  updated_at

PolicyDecisionDeniedExample
  id
  work_session_id
  actor_id
  policy_id
  requested_action
  normalized_action_hash
  risk_class
  result
  reason
  created_at

RequestBlockedActionExample
  id
  protocol_version
  work_session_id
  requester_actor_id
  requester_worker_id
  target_human_worker_id
  policy_decision_id
  type
  blocking_scope
  reason_code
  reason_summary
  requested_action
  requested_outcome
  risk_class
  human_decision_needed
  options
  default_if_no_response
  status
  created_at
  expires_at

ReviewApproveRequestExample
  id
  work_session_id
  reviewer_actor_id
  reviewer_worker_id
  target_ref
  decision
  approval_scope
  created_at

EvidenceManifestExportExample
  id
  work_session_id
  generated_by_actor_id
  objective
  event_chain_root
  evidence_item_refs
  policy_decision_refs
  request_refs
  review_refs
  takeover_refs
  contribution_refs
  export_profile
  generated_at

ProtocolErrorExample
  error_id
  protocol_version
  object_type
  field
  reason
  remediation
  trace_id
```

Required semantic checks:

```txt
PolicyDecisionDeniedExample.result == deny
RequestBlockedActionExample.status == pending
RequestBlockedActionExample.blocking_scope is not empty
ReviewApproveRequestExample.decision == approve
ReviewApproveRequestExample.approval_scope exists
EvidenceManifestExportExample.evidence_item_refs is not empty
EvidenceManifestExportExample.policy_decision_refs is not empty
EvidenceManifestExportExample.request_refs is not empty
EvidenceManifestExportExample.review_refs is not empty
EvidenceManifestExportExample.contribution_refs is not empty
ProtocolErrorExample.error_id exists in ProtocolErrorId enum
```

## Conformance Entry Rules

The golden-path conformance entry MUST prove:

```txt
HumanWorker and AgentWorker are represented by Worker and Actor records.
WorkSession is created with objective, policy, revision, and event hash state.
WorkSession-scoped mutations validate Jarvis-Protocol-Version.
WorkSession-scoped mutations validate Jarvis-Actor-Id.
WorkSession-scoped mutations validate Jarvis-Idempotency-Key.
WorkSession-scoped mutations validate Jarvis-Request-Timestamp.
WorkSession-scoped mutations validate Jarvis-Expected-WorkSession-Revision.
WorkSession-scoped mutations validate Jarvis-Previous-Event-Hash.
Every accepted WorkSession-scoped state change records the Actor, verifies
authority, checks Jarvis-Expected-WorkSession-Revision, and links
Jarvis-Previous-Event-Hash.
AgentWorker action records PolicyDecision before accepted protocol state.
Policy-denied action creates scoped Request.
Request is resolved only by Review or Takeover.
Approved Request produces bounded ApprovalScope.
Contribution records attributable work.
EvidenceManifest exports portable proof.
LearningRecord, MemoryProposal, or SkillProposal carries governed learning.
```

The failure-mode conformance entry MUST reject:

```txt
missing protocol version
missing Actor header
invalid Actor authority
missing idempotency key
missing request timestamp
stale request timestamp
missing expected WorkSession revision
missing previous event hash
missing PolicyDecision before AgentWorker state change
Request resolved without Review or Takeover
approval without bounded ApprovalScope
stale WorkSession revision
previous event hash mismatch
stale Takeover continuation
EvidenceManifest export from invalid WorkSession state
sealed WorkSession mutation
sealed EvidenceManifest mutation
host-private export field
silent memory mutation
silent skill activation
OutcomeReport without LearningRecord
```

## Validator Rules

The OpenAPI validator MUST enforce:

```txt
required examples exist in components.examples
each required example uses summary and value
each required example value is an object
required examples contain the expected fields
required examples avoid forbidden host-private keys
golden-path conformance document exists
failure-mode conformance document exists
conformance documents include zero-trust header rejection ids
conformance documents include Actor authority rejection ids
conformance documents include revision and event-hash rejection ids
conformance documents include forbidden host-private export rejection ids
```

The failure-mode conformance document MUST include these rejection ids:

```txt
missing_protocol_version
missing_actor
unauthorized_actor
missing_idempotency_key
missing_request_timestamp
stale_request_timestamp
missing_expected_work_session_revision
missing_previous_event_hash
missing_policy
missing_policy_decision
missing_review_resolution
missing_takeover_resolution
invalid_approval_scope
stale_work_session_revision
invalid_previous_event_hash
stale_takeover_epoch
invalid_evidence_export_state
sealed_work_session_mutation
sealed_evidence_mutation
forbidden_host_private_field
silent_memory_mutation
silent_skill_activation
outcome_report_without_learning_record
```

## Out Of Scope

This chunk does not add executable implementation work.

It locks:

```txt
portable protocol examples
conformance entry documents
validator checks for examples and conformance entry
```

Executable proof work starts after the conformance entry is stable.

## Done State

Chunk 7 is complete when:

```txt
OpenAPI contains the required protocol examples.
The examples are portable protocol records.
The conformance entry documents exist.
The validator rejects missing examples and missing conformance entry docs.
The wording guard passes.
The markdown link checker passes.
The OpenAPI validator passes.
Reviewer agents approve protocol boundary, security, OpenAPI shape, and wording.
```
