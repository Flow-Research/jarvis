#!/usr/bin/env python3
"""Generate Python OpenAPI surface files for the Jarvis helper package."""

from __future__ import annotations

import json
from pathlib import Path
import pprint
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
OPENAPI_PATH = ROOT / "docs/openapi/jarvis-openapi.yaml"
OUT_DIR = ROOT / "packages/python/src/jarvis_protocol/generated"


SCALAR_ALIASES = {
    "JarvisId": "str",
    "OpaqueRef": "str",
    "Timestamp": "str",
}


def schema_ref_name(ref: str) -> str:
    return ref.rsplit("/", 1)[-1]


def py_literal(value: object) -> str:
    return repr(value)


def py_type(schema: dict[str, Any] | None) -> str:
    if not isinstance(schema, dict):
        return "Any"
    if "$ref" in schema:
        return schema_ref_name(schema["$ref"])
    if "const" in schema:
        return f"Literal[{py_literal(schema['const'])}]"
    if "enum" in schema and isinstance(schema["enum"], list):
        return "Literal[" + ", ".join(py_literal(value) for value in schema["enum"]) + "]"
    if "oneOf" in schema and isinstance(schema["oneOf"], list):
        return " | ".join(py_type(item) for item in schema["oneOf"])
    if "anyOf" in schema and isinstance(schema["anyOf"], list):
        return " | ".join(py_type(item) for item in schema["anyOf"])

    schema_type = schema.get("type")
    if schema_type == "string":
        return "str"
    if schema_type == "integer":
        return "int"
    if schema_type == "number":
        return "int | float"
    if schema_type == "boolean":
        return "bool"
    if schema_type == "null":
        return "None"
    if schema_type == "array":
        return f"list[{py_type(schema.get('items'))}]"
    if schema_type == "object":
        properties = schema.get("properties")
        if isinstance(properties, dict) and properties:
            return "dict[str, Any]"
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            return f"dict[str, {py_type(additional)}]"
        return "dict[str, Any]"
    return "Any"


def type_block_for(name: str, schema: dict[str, Any]) -> str:
    if name in SCALAR_ALIASES:
        return f"{name}: TypeAlias = {SCALAR_ALIASES[name]}"
    if name == "PortableValue":
        return (
            "PortableValue: TypeAlias = "
            "None | bool | int | float | str | list['PortableValue'] | "
            "dict[str, 'PortableValue']"
        )
    if name == "NamespacedExtensions":
        return "NamespacedExtensions: TypeAlias = dict[str, Any]"
    if "enum" in schema and isinstance(schema["enum"], list):
        return f"{name}: TypeAlias = {py_type(schema)}"

    properties = schema.get("properties", {})
    required = set(schema.get("required", []))
    if not isinstance(properties, dict):
        return f"{name}: TypeAlias = {py_type(schema)}"

    lines = [f"class {name}(TypedDict, total=False):"]
    if not properties:
        lines.append("    pass")
        return "\n".join(lines)

    for prop_name, prop_schema in sorted(properties.items()):
        marker = "Required" if prop_name in required else "NotRequired"
        lines.append(f"    {prop_name}: {marker}[{py_type(prop_schema)}]")
    return "\n".join(lines)


def python_value(value: object) -> str:
    return pprint.pformat(value, sort_dicts=False, width=100)


def main() -> None:
    spec = yaml.safe_load(OPENAPI_PATH.read_text(encoding="utf-8"))
    schemas = spec["components"]["schemas"]
    protocol_version = spec["x-jarvis-protocol"]["version"]

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    type_blocks = [
        '"""Generated from docs/openapi/jarvis-openapi.yaml. Do not edit by hand."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, Literal, TypeAlias, TypedDict",
        "from typing_extensions import NotRequired, Required",
        "",
    ]
    all_names = list(schemas.keys())
    type_blocks.append(f"__all__ = {python_value(all_names)}")
    type_blocks.append("")
    for name, schema in schemas.items():
        type_blocks.append(type_block_for(name, schema))
        type_blocks.append("")

    (OUT_DIR / "openapi_types.py").write_text("\n".join(type_blocks), encoding="utf-8")

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
        "fieldConsts": {
            name: {
                prop_name: prop_schema["const"]
                for prop_name, prop_schema in schema.get("properties", {}).items()
                if isinstance(prop_schema, dict)
                and prop_name == "protocol_version"
                and "const" in prop_schema
            }
            for name, schema in schemas.items()
            if isinstance(schema, dict) and isinstance(schema.get("properties"), dict)
        },
        "fieldEnums": {
            name: {
                prop_name: (
                    prop_schema["enum"]
                    if "enum" in prop_schema
                    else schemas[schema_ref_name(prop_schema["$ref"])]["enum"]
                )
                for prop_name, prop_schema in schema.get("properties", {}).items()
                if isinstance(prop_schema, dict)
                and (
                    isinstance(prop_schema.get("enum"), list)
                    or (
                        "$ref" in prop_schema
                        and isinstance(schemas.get(schema_ref_name(prop_schema["$ref"])), dict)
                        and isinstance(schemas[schema_ref_name(prop_schema["$ref"])].get("enum"), list)
                    )
                )
            }
            for name, schema in schemas.items()
            if isinstance(schema, dict) and isinstance(schema.get("properties"), dict)
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
    metadata_py = (
        '"""Generated from docs/openapi/jarvis-openapi.yaml. Do not edit by hand."""\n'
        "\n"
        f"PROTOCOL_VERSION = {metadata['protocolVersion']!r}\n"
        f"OPENAPI_SCHEMA_NAMES = {python_value(metadata['schemaNames'])}\n"
        f"SCHEMA_REQUIRED_FIELDS = {python_value(metadata['requiredFields'])}\n"
        f"SCHEMA_ENUMS = {python_value(metadata['enums'])}\n"
        f"SCHEMA_FIELD_CONSTS = {python_value(metadata['fieldConsts'])}\n"
        f"SCHEMA_FIELD_ENUMS = {python_value(metadata['fieldEnums'])}\n"
        f"SCHEMA_FORBIDDEN_FIELDS = {python_value(metadata['forbiddenFields'])}\n"
        f"SCHEMA_ALLOWED_FIELDS = {python_value(metadata['allowedFields'])}\n"
        f"SCHEMA_CLOSED_SCHEMAS = {python_value(metadata['closedSchemas'])}\n"
    )
    (OUT_DIR / "schema_metadata.py").write_text(metadata_py, encoding="utf-8")
    (OUT_DIR / "__init__.py").write_text(
        '"""Generated Jarvis OpenAPI types and metadata."""\n'
        "\n"
        "from .openapi_types import *\n"
        "from .schema_metadata import (\n"
        "    OPENAPI_SCHEMA_NAMES,\n"
        "    PROTOCOL_VERSION,\n"
        "    SCHEMA_ALLOWED_FIELDS,\n"
        "    SCHEMA_CLOSED_SCHEMAS,\n"
        "    SCHEMA_ENUMS,\n"
        "    SCHEMA_FIELD_CONSTS,\n"
        "    SCHEMA_FIELD_ENUMS,\n"
        "    SCHEMA_FORBIDDEN_FIELDS,\n"
        "    SCHEMA_REQUIRED_FIELDS,\n"
        ")\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
