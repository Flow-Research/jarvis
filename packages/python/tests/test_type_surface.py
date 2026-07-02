from __future__ import annotations

from pathlib import Path
import re
import unittest

import yaml

import jarvis_protocol
from jarvis_protocol import (
    OPENAPI_SCHEMA_NAMES,
    PROTOCOL_VERSION,
    SCHEMA_ENUMS,
    SCHEMA_FIELD_CONSTS,
    SCHEMA_FIELD_ENUMS,
    SCHEMA_REQUIRED_FIELDS,
)
from jarvis_protocol.generated import openapi_types

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - exercised on Python 3.10
    tomllib = None


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parents[1]
OPENAPI_PATH = REPO_ROOT / "docs/openapi/jarvis-openapi.yaml"
CANONICAL_FIXTURE_ROOT = REPO_ROOT / "docs/conformance/fixtures"


class TypeSurfaceTests(unittest.TestCase):
    def test_generated_schema_metadata_covers_openapi_components(self) -> None:
        spec = yaml.safe_load(OPENAPI_PATH.read_text(encoding="utf-8"))
        schemas = spec["components"]["schemas"]
        expected_schema_names = list(schemas.keys())
        expected_required_fields = {
            name: schema.get("required", [])
            for name, schema in schemas.items()
            if isinstance(schema, dict)
        }
        expected_enums = {
            name: schema["enum"]
            for name, schema in schemas.items()
            if isinstance(schema, dict) and isinstance(schema.get("enum"), list)
        }
        expected_field_consts = {
            name: {
                prop_name: prop_schema["const"]
                for prop_name, prop_schema in schema.get("properties", {}).items()
                if isinstance(prop_schema, dict)
                and prop_name == "protocol_version"
                and "const" in prop_schema
            }
            for name, schema in schemas.items()
            if isinstance(schema, dict) and isinstance(schema.get("properties"), dict)
        }
        expected_field_enums = {}
        for name, schema in schemas.items():
            if not isinstance(schema, dict) or not isinstance(schema.get("properties"), dict):
                continue
            fields = {}
            for prop_name, prop_schema in schema["properties"].items():
                if not isinstance(prop_schema, dict):
                    continue
                if isinstance(prop_schema.get("enum"), list):
                    fields[prop_name] = prop_schema["enum"]
                    continue
                ref = prop_schema.get("$ref")
                if isinstance(ref, str):
                    ref_name = ref.rsplit("/", 1)[-1]
                    ref_schema = schemas.get(ref_name)
                    if isinstance(ref_schema, dict) and isinstance(ref_schema.get("enum"), list):
                        fields[prop_name] = ref_schema["enum"]
            expected_field_enums[name] = fields
        self.assertEqual(OPENAPI_SCHEMA_NAMES, expected_schema_names)
        self.assertEqual(SCHEMA_REQUIRED_FIELDS, expected_required_fields)
        self.assertEqual(SCHEMA_ENUMS, expected_enums)
        self.assertEqual(SCHEMA_FIELD_CONSTS, expected_field_consts)
        self.assertEqual(SCHEMA_FIELD_ENUMS, expected_field_enums)
        self.assertEqual(PROTOCOL_VERSION, "v0.1")

    def test_generated_type_module_exports_every_schema_name(self) -> None:
        exported = set(openapi_types.__all__)
        self.assertEqual(exported, set(OPENAPI_SCHEMA_NAMES))
        for name in OPENAPI_SCHEMA_NAMES:
            self.assertTrue(hasattr(openapi_types, name), name)
            self.assertTrue(hasattr(jarvis_protocol, name), name)
            self.assertIn(name, jarvis_protocol.__all__)

    def test_package_metadata_marks_protocol_alpha(self) -> None:
        data = load_pyproject_data(PACKAGE_ROOT / "pyproject.toml")
        self.assertEqual(data["project"]["name"], "jarvis-protocol")
        self.assertEqual(data["project"]["version"], "0.1.0a0")
        self.assertEqual(data["tool"]["jarvis"]["protocol-version"], "v0.1")
        self.assertEqual(data["tool"]["jarvis"]["fixture-set"], "v0.1")
        self.assertEqual(
            data["tool"]["hatch"]["build"]["targets"]["wheel"]["force-include"]["fixtures/v0.1"],
            "jarvis_protocol/fixtures/v0.1",
        )

    def test_fixture_snapshots_are_present_in_python_package_source(self) -> None:
        snapshot_root = PACKAGE_ROOT / "fixtures/v0.1"
        canonical_files = sorted(CANONICAL_FIXTURE_ROOT.rglob("*.json"))
        snapshot_files = sorted(snapshot_root.rglob("*.json"))
        self.assertEqual(
            [path.relative_to(CANONICAL_FIXTURE_ROOT) for path in canonical_files],
            [path.relative_to(snapshot_root) for path in snapshot_files],
        )
        for canonical_path in canonical_files:
            relative = canonical_path.relative_to(CANONICAL_FIXTURE_ROOT)
            snapshot_path = snapshot_root / relative
            self.assertEqual(
                json_for_compare(snapshot_path),
                json_for_compare(canonical_path),
                str(relative),
            )


def json_for_compare(path: Path) -> object:
    import json

    return json.loads(path.read_text(encoding="utf-8"))


def load_pyproject_data(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if tomllib is not None:
        return tomllib.loads(text)

    return {
        "project": {
            "name": toml_string(text, "project", "name"),
            "version": toml_string(text, "project", "version"),
        },
        "tool": {
            "jarvis": {
                "protocol-version": toml_string(text, "tool.jarvis", "protocol-version"),
                "fixture-set": toml_string(text, "tool.jarvis", "fixture-set"),
            },
            "hatch": {
                "build": {
                    "targets": {
                        "wheel": {
                            "force-include": {
                                "fixtures/v0.1": toml_force_include_fixture(text),
                            },
                        },
                    },
                },
            },
        },
    }


def toml_section(text: str, name: str) -> str:
    match = re.search(
        rf"(?ms)^\[{re.escape(name)}\]\s*$\n(?P<body>.*?)(?=^\[|\Z)",
        text,
    )
    if match is None:
        raise AssertionError(f"pyproject missing [{name}]")
    return match.group("body")


def toml_string(text: str, section: str, key: str) -> str:
    body = toml_section(text, section)
    match = re.search(rf'(?m)^{re.escape(key)}\s*=\s*"([^"]+)"\s*$', body)
    if match is None:
        raise AssertionError(f"pyproject missing {section}.{key}")
    return match.group(1)


def toml_force_include_fixture(text: str) -> str:
    body = toml_section(text, "tool.hatch.build.targets.wheel")
    match = re.search(
        r'(?m)^force-include\s*=\s*\{\s*"fixtures/v0\.1"\s*=\s*"([^"]+)"\s*\}\s*$',
        body,
    )
    if match is None:
        raise AssertionError("pyproject missing wheel fixture force-include")
    return match.group(1)


if __name__ == "__main__":
    unittest.main()
