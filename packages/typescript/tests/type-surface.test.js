import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

import {
  OPENAPI_SCHEMA_NAMES,
  SCHEMA_ALLOWED_FIELDS,
  SCHEMA_CLOSED_SCHEMAS,
  SCHEMA_ENUMS,
  SCHEMA_REQUIRED_FIELDS,
} from "../src/index.js";

const repoRoot = dirname(dirname(dirname(dirname(fileURLToPath(import.meta.url)))));

function openApiSchemaNames() {
  const text = readFileSync(join(repoRoot, "docs/openapi/jarvis-openapi.yaml"), "utf8");
  const marker = "  schemas:\n";
  const start = text.indexOf(marker);
  assert.notEqual(start, -1, "OpenAPI schemas section exists");
  const tail = text.slice(start + marker.length);
  const end = tail.search(/\n  [a-zA-Z]+:\n/);
  const schemaBlock = end === -1 ? tail : tail.slice(0, end);
  const names = [];
  for (const line of schemaBlock.split("\n")) {
    const match = /^    ([A-Za-z][A-Za-z0-9]*):$/.exec(line);
    if (match) {
      names.push(match[1]);
    }
  }
  return names;
}

test("generated schema metadata covers every OpenAPI component schema", () => {
  assert.deepEqual(OPENAPI_SCHEMA_NAMES, openApiSchemaNames());
});

test("generated metadata exposes required fields and protocol enums", () => {
  assert.deepEqual(SCHEMA_REQUIRED_FIELDS.WorkSession.slice(0, 4), [
    "id",
    "protocol_version",
    "created_by_actor_id",
    "objective",
  ]);
  assert.ok(SCHEMA_REQUIRED_FIELDS.OutcomeReport.includes("learning_record_refs"));
  assert.ok(SCHEMA_ENUMS.ProtocolErrorId.includes("missing_policy_decision"));
  assert.ok(SCHEMA_ENUMS.ProtocolErrorId.includes("outcome_report_requires_terminal_source"));
  assert.ok(SCHEMA_ENUMS.RequestStatus.includes("takeover"));
  assert.ok(SCHEMA_CLOSED_SCHEMAS.includes("OutcomeReport"));
  assert.ok(SCHEMA_ALLOWED_FIELDS.OutcomeReport.includes("learning_record_refs"));
});

test("generated type declarations export every schema name", () => {
  const declarations = readFileSync(
    join(repoRoot, "packages/typescript/src/generated/openapi-types.d.ts"),
    "utf8",
  );
  for (const schemaName of OPENAPI_SCHEMA_NAMES) {
    assert.match(
      declarations,
      new RegExp(`export (type|interface) ${schemaName}\\b`),
      `${schemaName} is exported`,
    );
  }
});

test("public declaration file uses NodeNext-compatible generated imports", () => {
  const declarations = readFileSync(
    join(repoRoot, "packages/typescript/src/index.d.ts"),
    "utf8",
  );
  assert.match(declarations, /from "\.\/generated\/openapi-types\.js"/);
  assert.doesNotMatch(declarations, /from "\.\/generated\/openapi-types";/);
});

test("package exports expose helper root, metadata, and fixture snapshots", () => {
  const packageJson = JSON.parse(
    readFileSync(join(repoRoot, "packages/typescript/package.json"), "utf8"),
  );
  assert.equal(packageJson.exports["."].import, "./src/index.js");
  assert.equal(packageJson.exports["."].types, "./src/index.d.ts");
  assert.equal(packageJson.exports["./package.json"], "./package.json");
  assert.equal(packageJson.exports["./fixtures/v0.1/*"], "./fixtures/v0.1/*");
});
