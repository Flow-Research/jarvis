#!/usr/bin/env python3
"""Validate Python package artifacts for Jarvis protocol helpers."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = ROOT / "packages/python"
CANONICAL_FIXTURE_ROOT = ROOT / "docs/conformance/fixtures"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def run(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        **kwargs,
    )


def canonical_fixture_relatives() -> list[Path]:
    return sorted(path.relative_to(CANONICAL_FIXTURE_ROOT) for path in CANONICAL_FIXTURE_ROOT.rglob("*.json"))


def assert_wheel_contents(wheel_path: Path) -> None:
    expected = {
        "jarvis_protocol/__init__.py",
        "jarvis_protocol/generated/__init__.py",
        "jarvis_protocol/generated/openapi_types.py",
        "jarvis_protocol/generated/schema_metadata.py",
    }
    expected.update(
        f"jarvis_protocol/fixtures/v0.1/{relative.as_posix()}"
        for relative in canonical_fixture_relatives()
    )
    with zipfile.ZipFile(wheel_path) as archive:
        names = set(archive.namelist())
    missing = sorted(expected - names)
    if missing:
        raise AssertionError(f"{rel(wheel_path)}: missing wheel entries: {missing}")


def assert_sdist_contents(sdist_path: Path) -> None:
    with tarfile.open(sdist_path) as archive:
        names = archive.getnames()
    root_prefix = names[0].split("/", 1)[0]
    expected = {
        f"{root_prefix}/src/jarvis_protocol/__init__.py",
        f"{root_prefix}/src/jarvis_protocol/generated/__init__.py",
        f"{root_prefix}/src/jarvis_protocol/generated/openapi_types.py",
        f"{root_prefix}/src/jarvis_protocol/generated/schema_metadata.py",
    }
    expected.update(
        f"{root_prefix}/fixtures/v0.1/{relative.as_posix()}"
        for relative in canonical_fixture_relatives()
    )
    missing = sorted(expected - set(names))
    if missing:
        raise AssertionError(f"{rel(sdist_path)}: missing sdist entries: {missing}")


def assert_installed_package(wheel_path: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="jarvis-python-install-") as target:
        run([
            sys.executable,
            "-m",
            "pip",
            "install",
            "--target",
            target,
            str(wheel_path),
        ])
        script = """
from importlib import resources
import json
import jarvis_protocol as jp
from jarvis_protocol.generated import openapi_types

assert jp.PROTOCOL_VERSION == "v0.1"
assert hasattr(openapi_types, "OutcomeReport")
root = resources.files("jarvis_protocol") / "fixtures/v0.1"
golden = json.loads((root / "valid/golden-path.json").read_text(encoding="utf-8"))
invalid = json.loads((root / "invalid/outcome-report-requires-terminal-source.json").read_text(encoding="utf-8"))
assert golden["fixture_id"] == "valid-golden-path-v01"
assert invalid["expected_error_id"] == "outcome_report_requires_terminal_source"
assert jp.validate_fixture(golden).valid is True
assert jp.validate_fixture(invalid).errors[0]["error_id"] == "outcome_report_requires_terminal_source"
"""
        env = os.environ.copy()
        env["PYTHONPATH"] = target
        run([sys.executable, "-c", script], env=env)


def main() -> int:
    try:
        with tempfile.TemporaryDirectory(prefix="jarvis-python-dist-") as dist:
            dist_path = Path(dist)
            run([
                sys.executable,
                "-m",
                "build",
                "--sdist",
                "--wheel",
                "--no-isolation",
                "--outdir",
                str(dist_path),
                str(PACKAGE_ROOT),
            ])
            wheel_path = next(dist_path.glob("jarvis_protocol-*.whl"))
            sdist_path = next(dist_path.glob("jarvis_protocol-*.tar.gz"))
            assert_wheel_contents(wheel_path)
            assert_sdist_contents(sdist_path)
            assert_installed_package(wheel_path)
    except Exception as exc:
        print(exc)
        return 1
    finally:
        shutil.rmtree(PACKAGE_ROOT / "build", ignore_errors=True)
        shutil.rmtree(PACKAGE_ROOT / "src/jarvis_protocol.egg-info", ignore_errors=True)

    print("python package artifacts ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
