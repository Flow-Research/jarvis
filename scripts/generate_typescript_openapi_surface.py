#!/usr/bin/env python3
"""Generate TypeScript OpenAPI surface files for the Jarvis helper package."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
OPENAPI_PATH = ROOT / "docs/openapi/jarvis-openapi.yaml"
OUT_DIR = ROOT / "packages/typescript/src/generated"


SCALAR_ALIASES = {
    "JarvisId": "string",
    "OpaqueRef": "string",
    "Timestamp": "string",
}


def schema_ref_name(ref: str) -> str:
    return ref.rsplit("/", 1)[-1]


def literal(value: object) -> str:
    return json.dumps(value)


def ts_type(schema: dict[str, Any] | None) -> str:
    if not isinstance(schema, dict):
        return "unknown"
    if "$ref" in schema:
        return schema_ref_name(schema["$ref"])
    if "const" in schema:
        return literal(schema["const"])
    if "enum" in schema and isinstance(schema["enum"], list):
        return " | ".join(literal(value) for value in schema["enum"])
    if "oneOf" in schema and isinstance(schema["oneOf"], list):
        return " | ".join(ts_type(item) for item in schema["oneOf"])
    if "anyOf" in schema and isinstance(schema["anyOf"], list):
        return " | ".join(ts_type(item) for item in schema["anyOf"])

    schema_type = schema.get("type")
    if schema_type == "string":
        return "string"
    if schema_type in {"integer", "number"}:
        return "number"
    if schema_type == "boolean":
        return "boolean"
    if schema_type == "null":
        return "null"
    if schema_type == "array":
        return f"Array<{ts_type(schema.get('items'))}>"
    if schema_type == "object":
        properties = schema.get("properties")
        if isinstance(properties, dict) and properties:
            required = set(schema.get("required", []))
            parts = []
            for prop_name, prop_schema in sorted(properties.items()):
                optional = "" if prop_name in required else "?"
                parts.append(f"{json.dumps(prop_name)}{optional}: {ts_type(prop_schema)}")
            return "{ " + "; ".join(parts) + " }"
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            return f"Record<string, {ts_type(additional)}>"
        return "Record<string, unknown>"
    return "unknown"


def interface_for(name: str, schema: dict[str, Any]) -> str:
    if name in SCALAR_ALIASES:
        return f"export type {name} = {SCALAR_ALIASES[name]};"
    if name == "PortableValue":
        return (
            "export type PortableValue = "
            "null | boolean | number | string | PortableValue[] | "
            "{ [key: string]: PortableValue };"
        )
    if name == "NamespacedExtensions":
        return "export type NamespacedExtensions = Record<string, PortableValue>;"
    if "enum" in schema and isinstance(schema["enum"], list):
        return f"export type {name} = {ts_type(schema)};"

    properties = schema.get("properties", {})
    required = set(schema.get("required", []))
    if not isinstance(properties, dict):
        return f"export type {name} = {ts_type(schema)};"

    lines = [f"export interface {name} {{"]
    for prop_name, prop_schema in sorted(properties.items()):
        optional = "" if prop_name in required else "?"
        lines.append(f"  {prop_name}{optional}: {ts_type(prop_schema)};")
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    spec = yaml.safe_load(OPENAPI_PATH.read_text(encoding="utf-8"))
    schemas = spec["components"]["schemas"]
    protocol_version = spec["x-jarvis-protocol"]["version"]

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    type_blocks = [
        "/* Generated from docs/openapi/jarvis-openapi.yaml. Do not edit by hand. */",
        "",
    ]
    for name, schema in schemas.items():
        type_blocks.append(interface_for(name, schema))
        type_blocks.append("")

    (OUT_DIR / "openapi-types.d.ts").write_text("\n".join(type_blocks), encoding="utf-8")

    metadata = {
        "protocolVersion": protocol_version,
        "schemaNames": list(schemas.keys()),
        "requiredFields": {
            name: schema.get("required", [])
            for name, schema in schemas.items()
            if isinstance(schema, dict)
        },
        "enums": {
            name: schema["enum"]
            for name, schema in schemas.items()
            if isinstance(schema, dict) and isinstance(schema.get("enum"), list)
        },
        "forbiddenFields": {
            name: schema.get("x-jarvis-forbidden-fields", [])
            for name, schema in schemas.items()
            if isinstance(schema, dict) and schema.get("x-jarvis-forbidden-fields")
        },
        "allowedFields": {
            name: list(schema.get("properties", {}).keys())
            for name, schema in schemas.items()
            if isinstance(schema, dict)
            and isinstance(schema.get("properties"), dict)
            and schema.get("additionalProperties") is False
        },
        "closedSchemas": [
            name
            for name, schema in schemas.items()
            if isinstance(schema, dict) and schema.get("additionalProperties") is False
        ],
    }
    metadata_js = (
        "/* Generated from docs/openapi/jarvis-openapi.yaml. Do not edit by hand. */\n"
        f"export const PROTOCOL_VERSION = {json.dumps(metadata['protocolVersion'])};\n"
        f"export const OPENAPI_SCHEMA_NAMES = {json.dumps(metadata['schemaNames'], indent=2)};\n"
        f"export const SCHEMA_REQUIRED_FIELDS = {json.dumps(metadata['requiredFields'], indent=2)};\n"
        f"export const SCHEMA_ENUMS = {json.dumps(metadata['enums'], indent=2)};\n"
        f"export const SCHEMA_FORBIDDEN_FIELDS = {json.dumps(metadata['forbiddenFields'], indent=2)};\n"
        f"export const SCHEMA_ALLOWED_FIELDS = {json.dumps(metadata['allowedFields'], indent=2)};\n"
        f"export const SCHEMA_CLOSED_SCHEMAS = {json.dumps(metadata['closedSchemas'], indent=2)};\n"
    )
    (OUT_DIR / "schema-metadata.js").write_text(metadata_js, encoding="utf-8")
    (OUT_DIR / "schema-metadata.d.ts").write_text(
        "/* Generated from docs/openapi/jarvis-openapi.yaml. Do not edit by hand. */\n"
        "export const PROTOCOL_VERSION: string;\n"
        "export const OPENAPI_SCHEMA_NAMES: string[];\n"
        "export const SCHEMA_REQUIRED_FIELDS: Record<string, string[]>;\n"
        "export const SCHEMA_ENUMS: Record<string, string[]>;\n"
        "export const SCHEMA_FORBIDDEN_FIELDS: Record<string, string[]>;\n"
        "export const SCHEMA_ALLOWED_FIELDS: Record<string, string[]>;\n"
        "export const SCHEMA_CLOSED_SCHEMAS: string[];\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
