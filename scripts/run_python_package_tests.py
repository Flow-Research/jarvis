#!/usr/bin/env python3
"""Run Python helper package tests with a local source import path."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PYTHON_SRC = ROOT / "packages/python/src"


def run(command: list[str], env: dict[str, str]) -> None:
    subprocess.run(command, cwd=ROOT, env=env, check=True)


def main() -> int:
    env = os.environ.copy()
    existing_pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = (
        str(PYTHON_SRC)
        if not existing_pythonpath
        else str(PYTHON_SRC) + os.pathsep + existing_pythonpath
    )
    run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(ROOT / "packages/python/tests"),
        ],
        env,
    )
    run([sys.executable, str(ROOT / "scripts/check_python_package_artifacts.py")], env)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
