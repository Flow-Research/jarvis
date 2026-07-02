from __future__ import annotations

from datetime import datetime, timezone
import unittest

from jarvis_protocol import (
    canonicalize_protocol_value,
    find_forbidden_host_private_field,
    hash_protocol_value,
    protocol_error,
    validate_approval_scope,
    validate_event_hash_chain,
    validate_mutation_headers,
    validate_operation_headers,
    validate_outcome_report,
    validate_protocol_record,
    validate_read_headers,
)


class HelperValidationTests(unittest.TestCase):
    def test_mutation_headers_enforce_work_session_zero_trust_headers(self) -> None:
        missing = validate_mutation_headers(
            {
                "Authorization": "HostAuth test",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
                "Jarvis-Idempotency-Key": "idem-test",
                "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
            }
        )
        self.assertFalse(missing.valid)
        self.assertEqual(missing.errors[0]["error_id"], "missing_expected_work_session_revision")

        accepted = validate_mutation_headers(
            {
                "Authorization": "HostAuth test",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
                "Jarvis-Idempotency-Key": "idem-test",
                "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
                "Jarvis-Expected-WorkSession-Revision": 0,
                "Jarvis-Previous-Event-Hash": "hash:protocol-genesis",
            },
            {"now": datetime(2026, 6, 16, 10, 0, 0, tzinfo=timezone.utc)},
        )
        self.assertTrue(accepted.valid, accepted.errors)

    def test_non_work_session_mutation_headers_do_not_require_revision_hash(self) -> None:
        result = validate_mutation_headers(
            {
                "Authorization": "HostAuth test",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
                "Jarvis-Idempotency-Key": "idem-test",
                "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
            },
            {
                "work_session_scoped": False,
                "now": datetime(2026, 6, 16, 10, 0, 0, tzinfo=timezone.utc),
            },
        )
        self.assertTrue(result.valid, result.errors)

    def test_non_work_session_mutations_allow_extra_work_session_headers_without_requiring_them(self) -> None:
        result = validate_mutation_headers(
            {
                "Authorization": "HostAuth test",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
                "Jarvis-Idempotency-Key": "idem-test",
                "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
                "Jarvis-Expected-WorkSession-Revision": 0,
                "Jarvis-Previous-Event-Hash": "hash:protocol-genesis",
            },
            {
                "work_session_scoped": False,
                "now": datetime(2026, 6, 16, 10, 0, 0, tzinfo=timezone.utc),
            },
        )
        self.assertTrue(result.valid, result.errors)

    def test_required_identity_and_replay_headers_reject_empty_values(self) -> None:
        result = validate_mutation_headers(
            {
                "Authorization": " ",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
                "Jarvis-Idempotency-Key": "idem-test",
                "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
                "Jarvis-Expected-WorkSession-Revision": 0,
                "Jarvis-Previous-Event-Hash": "hash:protocol-genesis",
            },
            {"now": datetime(2026, 6, 16, 10, 0, 0, tzinfo=timezone.utc)},
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.errors[0]["field"], "headers.Authorization")

    def test_approval_scope_requires_review_timestamp_when_review_context_exists(self) -> None:
        approval_scope = {
            "id": "approval-test",
            "request_id": "request-test",
            "review_id": "review-test",
            "policy_decision_id": "policy-decision-test",
            "request_revision": 3,
            "request_event_hash": "hash:request",
            "approved_action": {"action": "fetch", "target": "registry.npmjs.org"},
            "allowed_scope": {"scope_ref": "scope:allow"},
            "denied_scope": {"scope_ref": "scope:deny"},
            "expires_at": "2026-06-16T10:30:00Z",
            "max_uses": 3,
            "applies_to_work_session_id": "ws-test",
            "applies_to_actor_id": "actor-agent-test",
            "normalized_action_hash": "hash:approval-test",
        }
        result = validate_approval_scope(
            approval_scope,
            {
                "request": {
                    "id": "request-test",
                    "policy_decision_id": "policy-decision-test",
                    "requester_actor_id": "actor-agent-test",
                },
                "review": {
                    "id": "review-test",
                    "work_session_id": "ws-test",
                },
            },
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.errors[0]["error_id"], "invalid_approval_scope")

    def test_timestamp_skew_rejects_future_requests_beyond_one_minute(self) -> None:
        result = validate_mutation_headers(
            {
                "Authorization": "HostAuth test",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
                "Jarvis-Idempotency-Key": "idem-test",
                "Jarvis-Request-Timestamp": "2026-06-16T10:04:00Z",
                "Jarvis-Expected-WorkSession-Revision": 0,
                "Jarvis-Previous-Event-Hash": "hash:protocol-genesis",
            },
            {"now": datetime(2026, 6, 16, 10, 0, 0, tzinfo=timezone.utc)},
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.errors[0]["error_id"], "stale_request_timestamp")

    def test_timestamp_skew_requires_explicit_now_for_parity(self) -> None:
        result = validate_mutation_headers(
            {
                "Authorization": "HostAuth test",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
                "Jarvis-Idempotency-Key": "idem-test",
                "Jarvis-Request-Timestamp": "2026-06-16T10:04:00Z",
                "Jarvis-Expected-WorkSession-Revision": 0,
                "Jarvis-Previous-Event-Hash": "hash:protocol-genesis",
            }
        )
        self.assertTrue(result.valid, result.errors)

    def test_previous_hash_header_requires_protocol_hash_prefix(self) -> None:
        result = validate_mutation_headers(
            {
                "Authorization": "HostAuth test",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
                "Jarvis-Idempotency-Key": "idem-test",
                "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
                "Jarvis-Expected-WorkSession-Revision": 0,
                "Jarvis-Previous-Event-Hash": "not-a-protocol-hash",
            },
            {"now": datetime(2026, 6, 16, 10, 0, 0, tzinfo=timezone.utc)},
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.errors[0]["error_id"], "invalid_previous_event_hash")

    def test_read_operations_bind_actor_to_header(self) -> None:
        result = validate_operation_headers(
            {
                "operation_id": "exportEvidenceManifest",
                "method": "GET",
                "path": "/work-sessions/ws-test/export",
                "actor_id": "actor-body",
                "expected_status": 200,
                "headers": {
                    "Authorization": "HostAuth test",
                    "Jarvis-Protocol-Version": "v0.1",
                    "Jarvis-Actor-Id": "actor-header",
                },
            }
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.errors[0]["error_id"], "actor_body_id_mismatch")

    def test_read_headers_reject_mutation_only_requirements(self) -> None:
        result = validate_read_headers(
            {
                "Authorization": "HostAuth test",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
            }
        )
        self.assertTrue(result.valid, result.errors)

        extra_headers = validate_read_headers(
            {
                "Authorization": "HostAuth test",
                "Jarvis-Protocol-Version": "v0.1",
                "Jarvis-Actor-Id": "actor-test",
                "Jarvis-Idempotency-Key": "idem-test",
            }
        )
        self.assertTrue(extra_headers.valid, extra_headers.errors)

    def test_outcome_report_requires_terminal_work_session_source(self) -> None:
        report = {
            "id": "outcome-test",
            "work_session_id": "ws-test",
            "source_ref": "source:ws-test",
            "reporter_ref": "reporter:test",
            "accepted_by_actor_id": "actor-human-test",
            "outcome": "accepted",
            "learning_record_refs": ["learning-test"],
            "received_at": "2026-06-16T10:00:00Z",
        }
        missing_source = validate_outcome_report(report)
        self.assertFalse(missing_source.valid)
        self.assertEqual(missing_source.errors[0]["error_id"], "outcome_report_requires_terminal_source")

        active_source = validate_outcome_report(report, {"work_session": {"id": "ws-test", "status": "active"}})
        self.assertFalse(active_source.valid)
        self.assertEqual(active_source.errors[0]["error_id"], "outcome_report_requires_terminal_source")

        completed_source = validate_outcome_report(
            report,
            {"work_session": {"id": "ws-test", "status": "completed"}},
        )
        self.assertTrue(completed_source.valid, completed_source.errors)

        wrong_source = validate_outcome_report(
            report,
            {"work_session": {"id": "ws-other", "status": "completed"}},
        )
        self.assertFalse(wrong_source.valid)
        self.assertEqual(wrong_source.errors[0]["error_id"], "outcome_report_requires_terminal_source")

    def test_protocol_error_helper_emits_openapi_error_envelope(self) -> None:
        error = protocol_error(
            "missing_actor",
            {
                "object_type": "headers",
                "field": "Jarvis-Actor-Id",
                "reason": "actor missing",
                "remediation": "send actor header",
                "trace_id": "trace:test",
            },
        )
        self.assertEqual(
            error,
            {
                "error_id": "missing_actor",
                "protocol_version": "v0.1",
                "object_type": "headers",
                "field": "Jarvis-Actor-Id",
                "reason": "actor missing",
                "remediation": "send actor header",
                "trace_id": "trace:test",
            },
        )

    def test_protocol_error_helper_rejects_ids_outside_openapi_enum(self) -> None:
        error = protocol_error("not_in_openapi")
        self.assertEqual(error["error_id"], "invalid_export")
        self.assertEqual(error["field"], "error_id")

    def test_closed_schema_validation_rejects_unknown_protocol_fields(self) -> None:
        result = validate_protocol_record(
            "OutcomeReport",
            {
                "id": "outcome-test",
                "work_session_id": "ws-test",
                "source_ref": "source:ws-test",
                "reporter_ref": "reporter:test",
                "accepted_by_actor_id": "actor-human-test",
                "outcome": "accepted",
                "learning_record_refs": ["learning-test"],
                "received_at": "2026-06-16T10:00:00Z",
                "unexpected_host_field": "host-only",
            },
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.errors[0]["error_id"], "invalid_export")

    def test_schema_validation_rejects_invalid_protocol_version_and_enum(self) -> None:
        bad_version = validate_protocol_record(
            "WorkSession",
            {
                "id": "ws-test",
                "protocol_version": "v9",
                "objective": "test",
                "human_worker_id": "worker-human",
                "agent_worker_id": "worker-agent",
                "policy_id": "policy-test",
                "created_by_actor_id": "actor-human",
                "status": "active",
                "context_manifest": [],
                "event_log_ref": "events:test",
                "contribution_ledger_ref": "contributions:test",
                "evidence_manifest_ref": "evidence:test",
                "learning_record_refs": [],
                "created_at": "2026-06-16T10:00:00Z",
                "updated_at": "2026-06-16T10:00:00Z",
                "revision": 0,
                "last_event_hash": "hash:protocol-genesis",
            },
        )
        self.assertFalse(bad_version.valid)
        self.assertEqual(bad_version.errors[0]["error_id"], "invalid_export")

        bad_status = validate_protocol_record(
            "WorkSession",
            {
                "id": "ws-test",
                "protocol_version": "v0.1",
                "objective": "test",
                "human_worker_id": "worker-human",
                "agent_worker_id": "worker-agent",
                "policy_id": "policy-test",
                "created_by_actor_id": "actor-human",
                "status": "not_a_state",
                "context_manifest": [],
                "event_log_ref": "events:test",
                "contribution_ledger_ref": "contributions:test",
                "evidence_manifest_ref": "evidence:test",
                "learning_record_refs": [],
                "created_at": "2026-06-16T10:00:00Z",
                "updated_at": "2026-06-16T10:00:00Z",
                "revision": 0,
                "last_event_hash": "hash:protocol-genesis",
            },
        )
        self.assertFalse(bad_status.valid)
        self.assertEqual(bad_status.errors[0]["error_id"], "unknown_state")

    def test_generic_schema_validation_rejects_non_object_records_as_invalid_export(self) -> None:
        result = validate_protocol_record("Request", None)
        self.assertFalse(result.valid)
        self.assertEqual(result.errors[0]["error_id"], "invalid_export")

    def test_canonicalization_and_hashing_are_stable_across_key_order(self) -> None:
        left = {"b": 2, "a": {"y": True, "x": "yes"}}
        right = {"a": {"x": "yes", "y": True}, "b": 2}
        self.assertEqual(canonicalize_protocol_value(left), canonicalize_protocol_value(right))
        self.assertEqual(hash_protocol_value(left), hash_protocol_value(right))

    def test_event_hash_chain_helper_rejects_broken_previous_hashes(self) -> None:
        valid = validate_event_hash_chain(
            [
                {"sequence": 1, "previous_hash": "hash:protocol-genesis", "event_hash": "hash:first"},
                {"sequence": 2, "previous_hash": "hash:first", "event_hash": "hash:second"},
            ]
        )
        self.assertTrue(valid.valid, valid.errors)

        invalid = validate_event_hash_chain(
            [
                {"sequence": 1, "previous_hash": "hash:protocol-genesis", "event_hash": "hash:first"},
                {"sequence": 2, "previous_hash": "hash:wrong", "event_hash": "hash:second"},
            ]
        )
        self.assertFalse(invalid.valid)
        self.assertEqual(invalid.errors[0]["error_id"], "invalid_previous_event_hash")

    def test_host_private_field_scanner_returns_forbidden_path(self) -> None:
        self.assertEqual(
            find_forbidden_host_private_field({"export_profile": {}, "session_cookie": "secret"}),
            "session_cookie",
        )
        self.assertEqual(
            find_forbidden_host_private_field({"export_profile": {}, "private-key": "secret"}),
            "private-key",
        )
        self.assertEqual(
            find_forbidden_host_private_field({"export_profile": {}, "rawPrompt": "secret"}),
            "rawPrompt",
        )


if __name__ == "__main__":
    unittest.main()
