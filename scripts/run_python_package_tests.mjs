#!/usr/bin/env node

import { spawnSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const candidates = process.platform === "win32"
  ? [
      ["py", ["-3"]],
      ["python", []],
      ["python3", []],
    ]
  : [
      ["python3", []],
      ["python", []],
    ];

function run(command, args, options = {}) {
  return spawnSync(command, args, {
    cwd: root,
    stdio: "inherit",
    shell: false,
    ...options,
  });
}

function findPython() {
  const versionCheck = "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)";
  for (const [command, prefixArgs] of candidates) {
    const args = [...prefixArgs, "-c", versionCheck];
    const result = spawnSync(command, args, {
      cwd: root,
      stdio: "ignore",
      shell: false,
    });
    if (result.status === 0) {
      return [command, prefixArgs];
    }
  }
  throw new Error("Python 3.10 or newer executable not found.");
}

const [pythonCommand, pythonArgs] = findPython();
const result = run(
  pythonCommand,
  [...pythonArgs, "scripts/run_python_package_tests.py"],
);

process.exit(result.status ?? 1);
