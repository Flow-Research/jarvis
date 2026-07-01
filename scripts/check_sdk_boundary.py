#!/usr/bin/env python3
"""Validate the Jarvis SDK helper package boundary."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import tomllib


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_FIXTURE_ROOT = ROOT / "docs/conformance/fixtures"
SNAPSHOT_ROOTS = [
    ROOT / "packages/typescript/fixtures/v0.1",
    ROOT / "packages/python/fixtures/v0.1",
    ROOT / "packages/cli/fixtures/v0.1",
]
EXPECTED_JARVIS_METADATA = {
    "packageStatus": "Protocol Alpha helper tooling",
    "protocolVersion": "v0.1",
    "openapiVersion": "0.1.0",
    "fixtureSet": "v0.1",
}

REQUIRED_PATHS = [
    "package.json",
    "packages/README.md",
    "packages/typescript/package.json",
    "packages/typescript/README.md",
    "packages/typescript/src/generated",
    "packages/typescript/src/validators",
    "packages/typescript/src/headers",
    "packages/typescript/src/events",
    "packages/typescript/src/evidence",
    "packages/typescript/tests",
    "packages/typescript/fixtures/v0.1",
    "packages/python/pyproject.toml",
    "packages/python/README.md",
    "packages/python/src/jarvis_protocol/__init__.py",
    "packages/python/src/jarvis_protocol/generated",
    "packages/python/src/jarvis_protocol/validators",
    "packages/python/src/jarvis_protocol/headers",
    "packages/python/src/jarvis_protocol/events",
    "packages/python/src/jarvis_protocol/evidence",
    "packages/python/tests",
    "packages/python/fixtures/v0.1",
    "packages/cli/package.json",
    "packages/cli/README.md",
    "packages/cli/src",
    "packages/cli/tests",
    "packages/cli/fixtures/v0.1",
]

FORBIDDEN_PACKAGE_DIR_NAMES = {
    "runtime",
    "runtimes",
    "adapter",
    "adapters",
    "wrapper",
    "wrappers",
    "ui",
    "auth",
    "storage",
    "queue",
    "queues",
    "sandbox",
    "sandboxes",
    "billing",
    "scoring",
    "payment",
    "payments",
    "deployment",
    "deployments",
    "monitoring",
    "observability",
    "workflow",
    "workflows",
}

FORBIDDEN_TOKEN_GROUPS = [
    {"agent", "runtime"},
    {"agent", "planner"},
    {"model", "router"},
    {"model", "orchestration"},
    {"tool", "executor"},
    {"tool", "execution"},
    {"memory", "engine"},
    {"host", "adapter"},
    {"host", "integration"},
    {"host", "workflow"},
    {"ui", "kit"},
    {"auth", "provider"},
    {"storage", "backend"},
    {"queue", "backend"},
    {"billing", "system"},
    {"scoring", "system"},
    {"payment", "system"},
    {"deployment", "system"},
    {"workflow", "engine"},
]

NPM_DEPENDENCY_FIELDS = [
    "dependencies",
    "devDependencies",
    "peerDependencies",
    "optionalDependencies",
    "bundledDependencies",
    "bundleDependencies",
]

EXPECTED_NPM_PACKAGES = {
    "packages/typescript/package.json": {
        "name": "@jarvis-protocol/sdk",
        "version": "0.1.0-alpha.0",
        "type": "module",
        "fixture_path": "fixtures/v0.1/",
    },
    "packages/cli/package.json": {
        "name": "@jarvis-protocol/cli",
        "version": "0.1.0-alpha.0",
        "type": "module",
        "fixture_path": "fixtures/v0.1/",
    },
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"{rel(path)}: invalid JSON: {exc}") from exc


def boundary_tokens(value: object) -> set[str]:
    return {
        token
        for token in re.split(r"[^a-z0-9]+", str(value).lower())
        if token
    }


def rejected_boundary_surface(value: object) -> bool:
    tokens = boundary_tokens(value)
    if tokens & FORBIDDEN_PACKAGE_DIR_NAMES:
        return True
    return any(group <= tokens for group in FORBIDDEN_TOKEN_GROUPS)


def check_manifest_values(
    relative: str,
    values: list[object],
) -> None:
    for value in values:
        if rejected_boundary_surface(value):
            raise AssertionError(
                f"{relative}: rejected host/runtime surface found in {value!r}"
            )


def collect_npm_manifest_values(relative: str, package: dict[str, object]) -> list[object]:
    manifest_values: list[object] = []
    for field in NPM_DEPENDENCY_FIELDS:
        value = package.get(field)
        if isinstance(value, dict):
            manifest_values.extend(value.keys())
            manifest_values.extend(value.values())
        elif isinstance(value, list):
            manifest_values.extend(value)
        elif value is not None:
            raise AssertionError(f"{relative}: {field} MUST be object or list")
    scripts = package.get("scripts")
    if isinstance(scripts, dict):
        manifest_values.extend(scripts.keys())
        manifest_values.extend(scripts.values())
    elif scripts is not None:
        raise AssertionError(f"{relative}: scripts MUST be an object")
    bin_value = package.get("bin")
    if isinstance(bin_value, dict):
        manifest_values.extend(bin_value.keys())
        manifest_values.extend(bin_value.values())
    elif isinstance(bin_value, str):
        manifest_values.append(bin_value)
    elif bin_value is not None:
        raise AssertionError(f"{relative}: bin MUST be object or string")
    return manifest_values


def collect_python_entry_point_values(relative: str, value: object) -> list[object]:
    if not isinstance(value, dict):
        raise AssertionError(f"{relative}: entry point table MUST be object")
    values: list[object] = []
    for group_name, group_value in value.items():
        values.append(group_name)
        if isinstance(group_value, dict):
            values.extend(group_value.keys())
            values.extend(group_value.values())
        elif isinstance(group_value, list):
            values.extend(group_value)
        else:
            raise AssertionError(f"{relative}: entry point group MUST be object or list")
    return values


def check_required_paths() -> None:
    for relative in REQUIRED_PATHS:
        path = ROOT / relative
        if not path.exists():
            raise AssertionError(f"{relative}: required SDK boundary path missing")


def check_root_package() -> None:
    package = load_json(ROOT / "package.json")
    if not isinstance(package, dict):
        raise AssertionError("package.json: root package MUST be an object")
    if package.get("name") != "jarvis-protocol":
        raise AssertionError("package.json: name MUST be jarvis-protocol")
    if package.get("private") is not True:
        raise AssertionError("package.json: root package MUST remain private")
    if package.get("packageManager") != "npm@11.10.0":
        raise AssertionError("package.json: packageManager MUST be npm@11.10.0")
    workspaces = package.get("workspaces")
    if workspaces != ["packages/typescript", "packages/cli"]:
        raise AssertionError("package.json: workspaces MUST match SDK package plan")
    scripts = package.get("scripts")
    if not isinstance(scripts, dict) or scripts.get("check:sdk-boundary") != (
        "python3 scripts/check_sdk_boundary.py"
    ):
        raise AssertionError("package.json: check:sdk-boundary script missing")
    check_manifest_values("package.json", collect_npm_manifest_values("package.json", package))


def check_npm_packages() -> None:
    for relative, expected in EXPECTED_NPM_PACKAGES.items():
        package = load_json(ROOT / relative)
        if not isinstance(package, dict):
            raise AssertionError(f"{relative}: package MUST be an object")
        for key in ["name", "version", "type"]:
            if package.get(key) != expected[key]:
                raise AssertionError(
                    f"{relative}: {key} MUST be {expected[key]}"
                )
        files = package.get("files")
        if not isinstance(files, list) or expected["fixture_path"] not in files:
            raise AssertionError(
                f"{relative}: files MUST include {expected['fixture_path']}"
            )
        if package.get("jarvis") != EXPECTED_JARVIS_METADATA:
            raise AssertionError(f"{relative}: jarvis metadata mismatch")
        check_manifest_values(relative, collect_npm_manifest_values(relative, package))


def check_python_package() -> None:
    path = ROOT / "packages/python/pyproject.toml"
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    project = data.get("project")
    if not isinstance(project, dict):
        raise AssertionError("packages/python/pyproject.toml: project missing")
    build_system = data.get("build-system")
    if not isinstance(build_system, dict):
        raise AssertionError("packages/python/pyproject.toml: build-system missing")
    build_requires = build_system.get("requires")
    if not isinstance(build_requires, list):
        raise AssertionError(
            "packages/python/pyproject.toml: build-system.requires MUST be list"
        )
    check_manifest_values("packages/python/pyproject.toml", build_requires)
    if project.get("name") != "jarvis-protocol":
        raise AssertionError("packages/python/pyproject.toml: project.name mismatch")
    if project.get("version") != "0.1.0a0":
        raise AssertionError("packages/python/pyproject.toml: project.version mismatch")
    manifest_values: list[object] = []
    dependencies = project.get("dependencies", [])
    if not isinstance(dependencies, list):
        raise AssertionError("packages/python/pyproject.toml: dependencies MUST be list")
    manifest_values.extend(dependencies)
    optional_dependencies = project.get("optional-dependencies", {})
    if not isinstance(optional_dependencies, dict):
        raise AssertionError(
            "packages/python/pyproject.toml: optional-dependencies MUST be object"
        )
    for group_name, group_dependencies in optional_dependencies.items():
        manifest_values.append(group_name)
        if not isinstance(group_dependencies, list):
            raise AssertionError(
                "packages/python/pyproject.toml: optional dependency group MUST be list"
            )
        manifest_values.extend(group_dependencies)
    scripts = project.get("scripts", {})
    if not isinstance(scripts, dict):
        raise AssertionError("packages/python/pyproject.toml: scripts MUST be object")
    manifest_values.extend(scripts.keys())
    manifest_values.extend(scripts.values())
    gui_scripts = project.get("gui-scripts", {})
    if not isinstance(gui_scripts, dict):
        raise AssertionError("packages/python/pyproject.toml: gui-scripts MUST be object")
    manifest_values.extend(gui_scripts.keys())
    manifest_values.extend(gui_scripts.values())
    entry_points = project.get("entry-points", {})
    manifest_values.extend(
        collect_python_entry_point_values(
            "packages/python/pyproject.toml",
            entry_points,
        )
    )
    check_manifest_values("packages/python/pyproject.toml", manifest_values)
    tool = data.get("tool", {}).get("jarvis", {})
    expected = {
        "package-status": "Protocol Alpha helper tooling",
        "protocol-version": "v0.1",
        "openapi-version": "0.1.0",
        "fixture-set": "v0.1",
    }
    if tool != expected:
        raise AssertionError("packages/python/pyproject.toml: tool.jarvis mismatch")
    hatch = data.get("tool", {}).get("hatch", {})
    wheel = (
        hatch.get("build", {})
        .get("targets", {})
        .get("wheel", {})
    )
    force_include = wheel.get("force-include") if isinstance(wheel, dict) else None
    if not isinstance(force_include, dict) or force_include.get("fixtures/v0.1") != (
        "jarvis_protocol/fixtures/v0.1"
    ):
        raise AssertionError(
            "packages/python/pyproject.toml: wheel fixture inclusion missing"
        )


def check_forbidden_package_dirs() -> None:
    packages = ROOT / "packages"
    for path in packages.rglob("*"):
        if not path.is_dir():
            continue
        if rejected_boundary_surface(path.name):
            raise AssertionError(f"{rel(path)}: host/runtime directory is forbidden")


def check_fixture_snapshots() -> None:
    canonical_files = sorted(CANONICAL_FIXTURE_ROOT.rglob("*.json"))
    if not canonical_files:
        raise AssertionError("docs/conformance/fixtures: canonical fixtures missing")
    for snapshot_root in SNAPSHOT_ROOTS:
        for canonical in canonical_files:
            relative = canonical.relative_to(CANONICAL_FIXTURE_ROOT)
            snapshot = snapshot_root / relative
            if not snapshot.exists():
                raise AssertionError(f"{rel(snapshot)}: fixture snapshot missing")
            if snapshot.read_bytes() != canonical.read_bytes():
                raise AssertionError(f"{rel(snapshot)}: fixture snapshot mismatch")


def main() -> int:
    try:
        check_required_paths()
        check_root_package()
        check_npm_packages()
        check_python_package()
        check_forbidden_package_dirs()
        check_fixture_snapshots()
    except AssertionError as exc:
        print(exc)
        return 1

    print("sdk boundary ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
