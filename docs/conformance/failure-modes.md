# Failure-Mode Conformance Entry

Jarvis v0.1 failure-mode conformance proves that compatible implementations
reject unsafe or incomplete protocol records.

## Required Rejections

A compatible implementation MUST reject:

```txt
missing protocol version
missing Actor header
invalid Actor authority
missing idempotency key
missing request timestamp
stale request timestamp
missing expected WorkSession revision
missing previous event hash
missing Policy
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

## Required Rejection Ids

The failure-mode conformance entry MUST include these protocol error ids:

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

## Required Failure Boundaries

The protocol rejects a record when:

```txt
AgentWorker action changes WorkSession state without PolicyDecision.
WorkSession starts or mutates without required Policy.
Request reaches human-resolved state without Review or Takeover.
Review approval lacks bounded ApprovalScope.
Mutation headers are missing or invalid.
Actor authority is missing or invalid.
WorkSession revision is stale.
Previous event hash does not match current WorkSession state.
Takeover lock epoch is stale.
EvidenceManifest export occurs before a valid export state.
Sealed WorkSession is mutated.
Sealed EvidenceManifest is mutated.
Export contains forbidden host-private fields.
Memory changes without governed proposal and review state.
Skill changes without governed proposal and review state.
OutcomeReport lacks LearningRecord reference.
```

Failure-mode conformance protects the human-agent collaboration and learning
loop from fake compatibility.
