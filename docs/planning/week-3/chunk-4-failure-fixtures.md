# Chunk 4: Failure Fixtures

Chunk 4 adds invalid fixtures for required rejection paths.

## Scope

This chunk creates protocol fixture files that the protocol MUST reject.

It does not simulate host behavior or execute runtime code.

## Required Fixtures

Chunk 4 adds required failure-mode fixtures with these file names and expected
error ids:

```txt
missing-protocol-version.json                  -> missing_protocol_version
missing-actor.json                             -> missing_actor
unauthorized-actor.json                        -> unauthorized_actor
missing-idempotency-key.json                   -> missing_idempotency_key
missing-request-timestamp.json                 -> missing_request_timestamp
stale-request-timestamp.json                   -> stale_request_timestamp
missing-expected-work-session-revision.json    -> missing_expected_work_session_revision
missing-previous-event-hash.json               -> missing_previous_event_hash
missing-policy.json                            -> missing_policy
missing-policy-decision.json                   -> missing_policy_decision
missing-review-resolution.json                 -> missing_review_resolution
missing-takeover-resolution.json               -> missing_takeover_resolution
invalid-approval-scope.json                    -> invalid_approval_scope
stale-work-session-revision.json               -> stale_work_session_revision
invalid-previous-event-hash.json               -> invalid_previous_event_hash
stale-takeover-continuation.json               -> stale_takeover_epoch
invalid-evidence-export-state.json             -> invalid_evidence_export_state
sealed-work-session-mutation.json              -> sealed_work_session_mutation
sealed-evidence-mutation.json                  -> sealed_evidence_mutation
forbidden-host-private-export-field.json       -> forbidden_host_private_field
silent-memory-mutation.json                    -> silent_memory_mutation
silent-skill-activation.json                   -> silent_skill_activation
outcome-report-without-learning-record.json    -> outcome_report_without_learning_record
```

Chunk 4 also adds this OpenAPI-backed fixture:

```txt
unresolved-request.json                        -> request_unresolved
```

`missing-policy.json` proves that `WorkSession.policy_id` MUST reference a
Policy record. WorkSession creation or AgentWorker state mutation without the
required Policy rejects as `missing_policy`.

## Done Criteria

Chunk 4 is complete when:

- every invalid fixture has one primary expected error id
- every invalid fixture follows the Chunk 1 envelope
- required failure-mode rejection ids are covered
- rejection ids match the OpenAPI ProtocolError model
- local checks pass
