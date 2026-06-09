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
EXPECTED_CHUNK_ID = "week-2-chunk-1-openapi-skeleton"


def fail(message: str) -> int:
    print(f"openapi skeleton check failed: {message}")
    return 1


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
