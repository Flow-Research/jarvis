#!/usr/bin/env python3
"""Validate the Jarvis v0.1 OpenAPI skeleton."""

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
OPENAPI_PATH = ROOT / "docs" / "openapi" / "jarvis-openapi.yaml"

REQUIRED_TOP_LEVEL = {
    "openapi",
    "jsonSchemaDialect",
    "info",
    "servers",
    "security",
    "tags",
    "paths",
    "components",
    "x-jarvis-protocol",
}

REQUIRED_COMPONENTS = {
    "schemas",
    "parameters",
    "headers",
    "requestBodies",
    "responses",
    "securitySchemes",
    "examples",
}

REQUIRED_PROTOCOL_METADATA = {
    "version",
    "layer",
    "source_of_truth",
    "owns",
    "outside_jarvis",
    "chunk_lock",
}

REQUIRED_SCHEMAS = {
    "JarvisId",
    "OpaqueRef",
    "Timestamp",
    "NamespacedExtensions",
    "PortableValue",
    "WorkerType",
    "ActorType",
    "ContributionRole",
    "AutonomyLevel",
    "WorkSessionStatus",
    "PolicyDecisionResult",
    "RiskClass",
    "DataSensitivity",
    "AuthorityScope",
    "AccountabilityScope",
    "CapabilityRef",
    "EventAuthority",
    "ContributionScope",
    "CanonicalizationProfile",
    "ProtocolTraceContext",
    "JarvisEventPayload",
    "PolicyConstraint",
    "EscalationRule",
    "PolicyActionRule",
    "PolicyRequestLimits",
    "PolicyActionRequest",
    "Worker",
    "Actor",
    "HumanWorker",
    "AgentWorker",
    "WorkSession",
    "JarvisEvent",
    "Policy",
    "PolicyDecision",
}

REQUIRED_SCHEMA_FIELDS = {
    "Worker": {
        "id",
        "type",
        "role",
        "authority_scope",
        "accountability_scope",
    },
    "Actor": {
        "id",
        "worker_id",
        "type",
        "event_authority",
        "contribution_scope",
        "created_at",
    },
    "HumanWorker": {
        "worker_id",
        "actor_id",
        "role",
        "policy_authority",
        "review_authority",
    },
    "AgentWorker": {
        "worker_id",
        "actor_id",
        "agent_ref",
        "role",
        "capability_refs",
        "autonomy_level",
        "operating_constraints",
    },
    "WorkSession": {
        "id",
        "protocol_version",
        "created_by_actor_id",
        "objective",
        "human_worker_id",
        "agent_worker_id",
        "policy_id",
        "status",
        "revision",
        "last_event_hash",
        "event_log_ref",
        "created_at",
        "updated_at",
    },
    "JarvisEvent": {
        "id",
        "sequence",
        "type",
        "work_session_id",
        "actor_id",
        "timestamp",
        "payload",
        "previous_hash",
        "event_hash",
        "canonicalization",
    },
    "Policy": {
        "id",
        "owner_worker_id",
        "created_by_actor_id",
        "autonomy_level",
        "allowed_actions",
        "denied_actions",
        "review_required_actions",
        "risk_classes",
        "escalation_rules",
        "created_at",
    },
    "PolicyDecision": {
        "id",
        "work_session_id",
        "actor_id",
        "policy_id",
        "requested_action",
        "normalized_action_hash",
        "risk_class",
        "result",
        "reason",
        "created_at",
    },
}

OPTIONAL_SCHEMA_FIELDS = {
    "WorkSession": {
        "source_ref",
        "context_manifest_ref",
        "contribution_ledger_ref",
        "evidence_manifest_ref",
        "learning_record_refs",
    },
    "JarvisEvent": {
        "trace_context",
        "actor_signature",
        "signing_key_ref",
    },
    "Policy": {
        "tool_grants",
        "memory_grants",
        "external_send_rules",
        "request_limits",
        "extensions",
    },
    "PolicyDecision": {
        "data_sensitivity",
        "selected_grant_refs",
        "denied_grant_refs",
        "request_id",
        "evidence_refs",
    },
}

REQUIRED_ENUMS = {
    "WorkerType": {
        "human",
        "agent",
        "service",
        "tool",
    },
    "ActorType": {
        "human",
        "agent",
        "service",
        "tool",
    },
    "ContributionRole": {
        "human",
        "agent",
        "shared",
        "service",
        "tool",
    },
    "AutonomyLevel": {
        "observe_only",
        "propose_only",
        "execute_with_review",
        "bounded_execute",
        "full_execute_in_scope",
    },
    "WorkSessionStatus": {
        "created",
        "active",
        "waiting_on_human",
        "takeover",
        "reconciling",
        "completed",
        "failed",
        "cancelled",
        "closed",
    },
    "PolicyDecisionResult": {
        "allow",
        "deny",
        "narrow",
        "review_required",
    },
    "RiskClass": {
        "low",
        "medium",
        "high",
        "critical",
    },
    "DataSensitivity": {
        "public",
        "private",
        "confidential",
        "restricted",
    },
}

REQUIRED_CLOSED_OBJECT_SCHEMAS = {
    "AuthorityScope",
    "AccountabilityScope",
    "CapabilityRef",
    "EventAuthority",
    "ContributionScope",
    "CanonicalizationProfile",
    "ProtocolTraceContext",
    "JarvisEventPayload",
    "PolicyConstraint",
    "EscalationRule",
    "PolicyActionRule",
    "PolicyRequestLimits",
    "PolicyActionRequest",
    "Worker",
    "Actor",
    "HumanWorker",
    "AgentWorker",
    "WorkSession",
    "JarvisEvent",
    "Policy",
    "PolicyDecision",
}

REQUIRED_FORBIDDEN_METADATA = {
    "Worker": {
        "password",
        "credential",
        "raw_auth_token",
        "billing_account",
        "provider_secret",
        "database_primary_key",
        "deployment_resource_id",
    },
    "Actor": {
        "credential",
        "raw_auth_token",
        "session_cookie",
        "private_key",
        "database_primary_key",
    },
    "HumanWorker": {
        "password",
        "credential",
        "raw_auth_token",
        "private_profile_data",
        "billing_account",
        "host_account_record",
    },
    "AgentWorker": {
        "model_api_key",
        "provider_secret",
        "raw_prompt_store",
        "runtime_process_id",
        "container_id",
        "database_primary_key",
    },
    "WorkSession": {
        "database_primary_key",
        "queue_message_id",
        "runtime_session_id",
        "cloud_resource_id",
        "ui_state",
        "credential",
        "raw_auth_token",
    },
    "JarvisEvent": {
        "raw_auth_token",
        "credential",
        "private_key",
        "database_primary_key",
        "runtime_trace_secret",
        "provider_secret",
    },
    "Policy": {
        "credential",
        "raw_auth_token",
        "provider_secret",
        "billing_rule",
        "cloud_policy_id",
        "database_primary_key",
    },
    "PolicyDecision": {
        "hidden_policy_trace",
        "credential",
        "provider_secret",
        "database_primary_key",
        "runtime_decision_object",
    },
}

FORBIDDEN_SCHEMA_PROPERTIES = {
    "password",
    "credential",
    "raw_auth_token",
    "billing_account",
    "provider_secret",
    "database_primary_key",
    "deployment_resource_id",
    "session_cookie",
    "private_key",
    "private_profile_data",
    "host_account_record",
    "model_api_key",
    "raw_prompt_store",
    "runtime_process_id",
    "container_id",
    "queue_message_id",
    "runtime_session_id",
    "cloud_resource_id",
    "runtime_trace_secret",
    "billing_rule",
    "cloud_policy_id",
    "hidden_policy_trace",
    "runtime_decision_object",
}

REQUIRED_TAGS = {
    "Workers",
    "WorkSessions",
    "ControlPlane",
    "Attribution",
    "Learning",
    "Evidence",
    "Feedback",
    "Conformance",
}

EXPECTED_TITLE = "Jarvis Human-Agent Collaboration Protocol"
EXPECTED_PLACEHOLDER_SERVER = "https://jarvis.example.invalid"
EXPECTED_CHUNK_ID = "week-2-chunk-3-worksession-policy-schemas"
REQUIRED_CHUNK_LOCKS = {
    "OpenAPI 3.1.1 entry point",
    "v0.1 protocol metadata",
    "required top-level buckets",
    "tag taxonomy",
    "host-owned server boundary",
    "shared schema primitives",
    "Worker schema",
    "Actor schema",
    "HumanWorker schema",
    "AgentWorker schema",
    "WorkSession schema",
    "JarvisEvent schema",
    "Policy schema",
    "PolicyDecision schema",
}
PORTABLE_VALUE_REF = {"$ref": "#/components/schemas/PortableValue"}
FORBIDDEN_PORTABLE_KEY_PATTERN = (
    "^(?!.*(password|credential|token|secret|private_key|session_cookie|"
    "cookie|api_key|access_key|auth_header|oauth|database|billing|runtime|"
    "container|deployment|model_api_key|raw_prompt|host_account|ui_state))"
)
NAMESPACED_EXTENSION_PATTERN = (
    FORBIDDEN_PORTABLE_KEY_PATTERN
    + "[a-z0-9][a-z0-9-]*(\\.[a-z0-9_-]+)+$"
)
PORTABLE_PROPERTY_PATTERN = (
    FORBIDDEN_PORTABLE_KEY_PATTERN
    + "[a-z0-9][a-z0-9._:-]*$"
)


def fail(message: str) -> int:
    print(f"openapi skeleton check failed: {message}")
    return 1


def schema_requires_field_when_const(
    schema: dict, property_name: str, const_value: str, required_field: str
) -> bool:
    for branch in schema.get("allOf", []):
        if not isinstance(branch, dict):
            continue
        condition = branch.get("if", {})
        consequence = branch.get("then", {})
        if not isinstance(condition, dict) or not isinstance(consequence, dict):
            continue
        properties = condition.get("properties", {})
        if not isinstance(properties, dict):
            continue
        target = properties.get(property_name, {})
        if not isinstance(target, dict):
            continue
        required = consequence.get("required", [])
        if target.get("const") == const_value and required_field in required:
            return True
    return False


def iter_refs(value, path: str = "$"):
    if isinstance(value, dict):
        ref = value.get("$ref")
        if isinstance(ref, str):
            yield path, ref
        for key, child in value.items():
            yield from iter_refs(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_refs(child, f"{path}[{index}]")


def local_ref_exists(document: dict, ref: str) -> bool:
    if not ref.startswith("#/"):
        return True
    current = document
    for raw_part in ref[2:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or part not in current:
            return False
        current = current[part]
    return True


def main() -> int:
    if not OPENAPI_PATH.exists():
        return fail(f"missing {OPENAPI_PATH.relative_to(ROOT)}")

    data = yaml.safe_load(OPENAPI_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return fail("root document is not an object")

    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        return fail(f"missing top-level keys: {', '.join(sorted(missing))}")

    if data["openapi"] != "3.1.1":
        return fail("openapi must be 3.1.1")

    info = data["info"]
    if not isinstance(info, dict):
        return fail("info must be an object")
    if info.get("version") != "0.1.0":
        return fail("info.version must be 0.1.0")
    if info.get("title") != EXPECTED_TITLE:
        return fail(f"info.title must be {EXPECTED_TITLE!r}")

    protocol = data["x-jarvis-protocol"]
    if not isinstance(protocol, dict):
        return fail("x-jarvis-protocol must be an object")
    if protocol.get("version") != "v0.1":
        return fail("x-jarvis-protocol.version must be v0.1")
    missing_protocol = REQUIRED_PROTOCOL_METADATA - set(protocol)
    if missing_protocol:
        return fail(
            "missing x-jarvis-protocol keys: "
            + ", ".join(sorted(missing_protocol))
        )

    chunk_lock = protocol["chunk_lock"]
    if not isinstance(chunk_lock, dict):
        return fail("x-jarvis-protocol.chunk_lock must be an object")
    if chunk_lock.get("id") != EXPECTED_CHUNK_ID:
        return fail(f"x-jarvis-protocol.chunk_lock.id must be {EXPECTED_CHUNK_ID}")
    declared_locks = set(chunk_lock.get("locks", []))
    missing_locks = REQUIRED_CHUNK_LOCKS - declared_locks
    if missing_locks:
        return fail(
            "x-jarvis-protocol.chunk_lock.locks missing: "
            + ", ".join(sorted(missing_locks))
        )
    declared_excludes = set(chunk_lock.get("excludes", []))
    if "control-plane schemas" in declared_excludes:
        return fail("chunk_lock.excludes must name out-of-scope schemas directly")

    components = data["components"]
    if not isinstance(components, dict):
        return fail("components must be an object")
    missing_components = REQUIRED_COMPONENTS - set(components)
    if missing_components:
        return fail(
            "missing component buckets: " + ", ".join(sorted(missing_components))
        )
    for bucket in REQUIRED_COMPONENTS:
        if not isinstance(components[bucket], dict):
            return fail(f"components.{bucket} must be an object")

    schemas = components["schemas"]
    missing_schemas = REQUIRED_SCHEMAS - set(schemas)
    if missing_schemas:
        return fail("missing schemas: " + ", ".join(sorted(missing_schemas)))

    for schema_name, expected_values in REQUIRED_ENUMS.items():
        schema = schemas[schema_name]
        actual_values = set(schema.get("enum", []))
        if actual_values != expected_values:
            return fail(
                f"{schema_name} enum mismatch. expected "
                + ", ".join(sorted(expected_values))
                + "; got "
                + ", ".join(sorted(actual_values))
            )

    for schema_name in REQUIRED_CLOSED_OBJECT_SCHEMAS:
        schema = schemas[schema_name]
        if not isinstance(schema, dict):
            return fail(f"components.schemas.{schema_name} must be an object")
        if schema.get("type") != "object":
            return fail(f"{schema_name} must be an object schema")
        if schema.get("additionalProperties") is not False:
            return fail(f"{schema_name} must set additionalProperties: false")

    extensions_schema = schemas["NamespacedExtensions"]
    if extensions_schema.get("additionalProperties") != PORTABLE_VALUE_REF:
        return fail("NamespacedExtensions additionalProperties must use PortableValue")
    extension_pattern = (
        extensions_schema.get("propertyNames", {}).get("pattern", "")
    )
    if extension_pattern != NAMESPACED_EXTENSION_PATTERN:
        return fail("NamespacedExtensions must use the canonical property pattern")

    portable_value = schemas["PortableValue"]
    object_branch = None
    for branch in portable_value.get("anyOf", []):
        if isinstance(branch, dict) and branch.get("type") == "object":
            object_branch = branch
            break
    if object_branch is None:
        return fail("PortableValue must include a bounded object branch")
    portable_key_pattern = object_branch.get("propertyNames", {}).get("pattern", "")
    if portable_key_pattern != PORTABLE_PROPERTY_PATTERN:
        return fail("PortableValue object keys must use the canonical property pattern")
    if object_branch.get("additionalProperties") != PORTABLE_VALUE_REF:
        return fail("PortableValue object additionalProperties must use PortableValue")

    for schema_name, required_fields in REQUIRED_SCHEMA_FIELDS.items():
        schema = schemas[schema_name]
        declared_required = set(schema.get("required", []))
        missing_fields = required_fields - declared_required
        if missing_fields:
            return fail(
                f"{schema_name} missing required fields: "
                + ", ".join(sorted(missing_fields))
            )

        properties = schema.get("properties")
        if not isinstance(properties, dict):
            return fail(f"{schema_name}.properties must be an object")
        missing_properties = required_fields - set(properties)
        if missing_properties:
            return fail(
                f"{schema_name} missing properties for required fields: "
                + ", ".join(sorted(missing_properties))
            )

        forbidden_properties = FORBIDDEN_SCHEMA_PROPERTIES & set(properties)
        if forbidden_properties:
            return fail(
                f"{schema_name} exposes forbidden properties: "
                + ", ".join(sorted(forbidden_properties))
            )

        forbidden_metadata = set(schema.get("x-jarvis-forbidden-fields", []))
        expected_metadata = REQUIRED_FORBIDDEN_METADATA[schema_name]
        if forbidden_metadata != expected_metadata:
            return fail(
                f"{schema_name} x-jarvis-forbidden-fields mismatch. expected "
                + ", ".join(sorted(expected_metadata))
                + "; got "
                + ", ".join(sorted(forbidden_metadata))
            )

    for schema_name, optional_fields in OPTIONAL_SCHEMA_FIELDS.items():
        properties = schemas[schema_name].get("properties", {})
        missing_optional = optional_fields - set(properties)
        if missing_optional:
            return fail(
                f"{schema_name} missing locked optional fields: "
                + ", ".join(sorted(missing_optional))
            )

    policy_decision = schemas["PolicyDecision"]
    for result_value in ("deny", "review_required"):
        if not schema_requires_field_when_const(
            policy_decision, "result", result_value, "request_id"
        ):
            return fail(
                "PolicyDecision must require request_id when result is "
                + result_value
            )

    event_payload_properties = schemas["JarvisEventPayload"].get("properties", {})
    if "extensions" in event_payload_properties:
        return fail("JarvisEventPayload must not expose extensions")

    broken_refs = [
        f"{path} -> {ref}"
        for path, ref in iter_refs(data)
        if not local_ref_exists(data, ref)
    ]
    if broken_refs:
        return fail("unresolved local refs: " + "; ".join(broken_refs))

    preferences = schemas["HumanWorker"]["properties"]["preferences"]
    if preferences.get("additionalProperties") != PORTABLE_VALUE_REF:
        return fail("HumanWorker.preferences additionalProperties must use PortableValue")
    preference_pattern = preferences.get("propertyNames", {}).get("pattern", "")
    if preference_pattern != PORTABLE_PROPERTY_PATTERN:
        return fail("HumanWorker.preferences must use the canonical property pattern")

    security_schemes = components["securitySchemes"]
    host_auth = security_schemes.get("HostAuth")
    if not isinstance(host_auth, dict):
        return fail("components.securitySchemes.HostAuth is required")
    if host_auth.get("type") != "http" or host_auth.get("scheme") != "bearer":
        return fail("HostAuth must be an HTTP bearer security scheme")

    security = data.get("security")
    if security == []:
        return fail("root security must not be an empty no-auth array")
    if security != [{"HostAuth": []}]:
        return fail("root security must require HostAuth")

    tags = data["tags"]
    if not isinstance(tags, list):
        return fail("tags must be a list")
    tag_names = {tag.get("name") for tag in tags if isinstance(tag, dict)}
    missing_tags = REQUIRED_TAGS - tag_names
    if missing_tags:
        return fail(f"missing tags: {', '.join(sorted(missing_tags))}")

    if not isinstance(data["paths"], dict):
        return fail("paths must be an object")

    servers = data.get("servers")
    if not servers:
        return fail("servers must state the host-owned server boundary")
    if not isinstance(servers, list) or not isinstance(servers[0], dict):
        return fail("servers must be a list of server objects")
    if servers[0].get("url") != EXPECTED_PLACEHOLDER_SERVER:
        return fail("server URL must be the Jarvis placeholder URL")
    description = servers[0].get("description", "")
    if "Jarvis does not operate this server" not in description:
        return fail("server description must state that Jarvis does not operate it")

    print("openapi skeleton ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
