import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

import { runCli } from "../src/index.js";

const packageRoot = dirname(dirname(fileURLToPath(import.meta.url)));
const fixtureRoot = join(packageRoot, "fixtures/v0.1");

function readJson(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

function memoryIo() {
  let stdout = "";
  let stderr = "";
  return {
    io: {
      stdout: {
        write(chunk) {
          stdout += chunk;
        },
      },
      stderr: {
        write(chunk) {
          stderr += chunk;
        },
      },
    },
    output() {
      return JSON.parse(stdout);
    },
    stderr() {
      return stderr;
    },
  };
}

async function run(args) {
  const capture = memoryIo();
  const code = await runCli(args, capture.io);
  return {
    code,
    payload: capture.output(),
    stderr: capture.stderr(),
  };
}

function writeJsonTemp(value) {
  const dir = mkdtempSync(join(tmpdir(), "jarvis-cli-"));
  const file = join(dir, "input.json");
  writeFileSync(file, `${JSON.stringify(value, null, 2)}\n`, "utf8");
  return {
    file,
    cleanup() {
      rmSync(dir, { recursive: true, force: true });
    },
  };
}

test("validate fixture accepts golden-path fixture expectation", async () => {
  const result = await run([
    "validate",
    "fixture",
    join(fixtureRoot, "valid/golden-path.json"),
  ]);
  assert.equal(result.code, 0);
  assert.equal(result.payload.command, "validate fixture");
  assert.equal(result.payload.passed, true);
  assert.equal(result.payload.valid, true);
});

test("validate fixture passes when invalid fixture rejects as expected", async () => {
  const result = await run([
    "validate",
    "fixture",
    join(fixtureRoot, "invalid/missing-actor.json"),
  ]);
  assert.equal(result.code, 0);
  assert.equal(result.payload.passed, true);
  assert.equal(result.payload.valid, false);
  assert.equal(result.payload.expected_error_id, "missing_actor");
  assert.equal(result.payload.errors[0].error_id, "missing_actor");
});

test("validate fixtures runs fixture directory expectations", async () => {
  const result = await run(["validate", "fixtures", fixtureRoot]);
  assert.equal(result.code, 0);
  assert.equal(result.payload.command, "validate fixtures");
  assert.equal(result.payload.passed, true);
  assert.ok(result.payload.fixture_count > 1);
});

test("validate fixtures rejects incomplete fixture directory", async () => {
  const dir = mkdtempSync(join(tmpdir(), "jarvis-cli-fixtures-"));
  const validDir = join(dir, "valid");
  const file = join(validDir, "golden-path.json");
  try {
    symlinkSync(join(fixtureRoot, "valid"), validDir);
    const result = await run(["validate", "fixtures", dir]);
    assert.equal(readJson(file).fixture_id, "valid-golden-path-v01");
    assert.equal(result.code, 1);
    assert.equal(result.payload.passed, false);
    assert.equal(result.payload.errors[0].error_id, "invalid_export");
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});

test("validate fixture rejects non-canonical expected_result aliases", async () => {
  const fixture = readJson(join(fixtureRoot, "invalid/missing-actor.json"));
  fixture.expected_result = "rejected";
  const input = writeJsonTemp(fixture);
  try {
    const result = await run(["validate", "fixture", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.passed, false);
  } finally {
    input.cleanup();
  }
});

test("validate record rejects malformed protocol record", async () => {
  const input = writeJsonTemp({
    object_type: "OutcomeReport",
    record: {
      id: "outcome-test",
      unexpected_host_field: "host",
    },
  });
  try {
    const result = await run(["validate", "record", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.passed, false);
    assert.equal(result.payload.errors[0].error_id, "invalid_export");
  } finally {
    input.cleanup();
  }
});

test("validate record rejects unknown protocol object type", async () => {
  const input = writeJsonTemp({
    object_type: "NotAProtocolObject",
    record: {},
  });
  try {
    const result = await run(["validate", "record", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "invalid_export");
    assert.equal(result.payload.errors[0].field, "object_type");
  } finally {
    input.cleanup();
  }
});

test("validate record rejects nested host-private protocol fields", async () => {
  const golden = readJson(join(fixtureRoot, "valid/golden-path.json"));
  const event = structuredClone(golden.records.jarvis_events.worksession_created);
  event.payload.raw_runtime_state = "host-only";
  const input = writeJsonTemp({
    object_type: "JarvisEvent",
    record: event,
  });
  try {
    const result = await run(["validate", "record", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "forbidden_host_private_field");
    assert.equal(result.payload.errors[0].field, "payload.raw_runtime_state");
  } finally {
    input.cleanup();
  }
});

test("validate evidence-manifest rejects host-private export field", async () => {
  const golden = readJson(join(fixtureRoot, "valid/golden-path.json"));
  const evidenceManifest = structuredClone(golden.records.evidence_manifests.portable_export);
  evidenceManifest.raw_runtime_state = "secret";
  const input = writeJsonTemp({
    evidence_manifest: evidenceManifest,
    work_session: golden.records.work_sessions.completed,
  });
  try {
    const result = await run(["validate", "evidence-manifest", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "forbidden_host_private_field");
  } finally {
    input.cleanup();
  }
});

test("validate evidence-manifest rejects host-private separator variants", async () => {
  const golden = readJson(join(fixtureRoot, "valid/golden-path.json"));
  const evidenceManifest = structuredClone(golden.records.evidence_manifests.portable_export);
  evidenceManifest.evidence_item_refs[0]["private-key"] = "secret";
  const input = writeJsonTemp({
    evidence_manifest: evidenceManifest,
    work_session: golden.records.work_sessions.completed,
  });
  try {
    const result = await run(["validate", "evidence-manifest", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "forbidden_host_private_field");
    assert.equal(result.payload.errors[0].field, "evidence_item_refs[0].private-key");
  } finally {
    input.cleanup();
  }
});

test("validate evidence-manifest rejects missing terminal WorkSession source", async () => {
  const golden = readJson(join(fixtureRoot, "valid/golden-path.json"));
  const input = writeJsonTemp({
    evidence_manifest: golden.records.evidence_manifests.portable_export,
  });
  try {
    const result = await run(["validate", "evidence-manifest", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "invalid_evidence_export_state");
    assert.equal(result.payload.errors[0].field, "work_session.status");
  } finally {
    input.cleanup();
  }
});

test("validate evidence-manifest rejects mismatched WorkSession source", async () => {
  const golden = readJson(join(fixtureRoot, "valid/golden-path.json"));
  const input = writeJsonTemp({
    evidence_manifest: golden.records.evidence_manifests.portable_export,
    work_session: {
      ...golden.records.work_sessions.completed,
      id: "ws-other",
    },
  });
  try {
    const result = await run(["validate", "evidence-manifest", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "invalid_evidence_export_state");
    assert.equal(result.payload.errors[0].field, "work_session_id");
  } finally {
    input.cleanup();
  }
});

test("check headers validates WorkSession genesis mutation headers", async () => {
  const input = writeJsonTemp({
    headers: {
      Authorization: "HostAuth test",
      "Jarvis-Protocol-Version": "v0.1",
      "Jarvis-Actor-Id": "actor-test",
      "Jarvis-Idempotency-Key": "idem-test",
      "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
      "Jarvis-Expected-WorkSession-Revision": 0,
      "Jarvis-Previous-Event-Hash": "hash:protocol-genesis",
    },
  });
  try {
    const result = await run([
      "check",
      "headers",
      input.file,
      "--operation-class",
      "worksession_genesis_mutation",
    ]);
    assert.equal(result.code, 0);
    assert.equal(result.payload.passed, true);
  } finally {
    input.cleanup();
  }
});

test("check headers rejects missing read header", async () => {
  const input = writeJsonTemp({
    headers: {
      Authorization: "HostAuth test",
      "Jarvis-Protocol-Version": "v0.1",
    },
  });
  try {
    const result = await run([
      "check",
      "headers",
      input.file,
      "--operation-id",
      "exportEvidenceManifest",
    ]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "missing_actor");
  } finally {
    input.cleanup();
  }
});

test("check headers rejects operation-id downgrade attempts", async () => {
  const input = writeJsonTemp({
    method: "GET",
    path: "/work-sessions/ws-test/export",
    headers: {
      Authorization: "HostAuth test",
      "Jarvis-Protocol-Version": "v0.1",
      "Jarvis-Actor-Id": "actor-test",
    },
  });
  try {
    const result = await run([
      "check",
      "headers",
      input.file,
      "--operation-id",
      "createRequest",
    ]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "missing_idempotency_key");
  } finally {
    input.cleanup();
  }
});

test("check headers rejects mutation-only headers on read operations", async () => {
  const input = writeJsonTemp({
    headers: {
      Authorization: "HostAuth test",
      "Jarvis-Protocol-Version": "v0.1",
      "Jarvis-Actor-Id": "actor-test",
      "Jarvis-Idempotency-Key": "idem-test",
    },
  });
  try {
    const result = await run([
      "check",
      "headers",
      input.file,
      "--operation-id",
      "exportEvidenceManifest",
    ]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "invalid_export");
    assert.equal(result.payload.errors[0].field, "headers.Jarvis-Idempotency-Key");
  } finally {
    input.cleanup();
  }
});

test("check headers rejects missing mutation header", async () => {
  const input = writeJsonTemp({
    headers: {
      Authorization: "HostAuth test",
      "Jarvis-Protocol-Version": "v0.1",
      "Jarvis-Actor-Id": "actor-test",
      "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
      "Jarvis-Expected-WorkSession-Revision": 0,
      "Jarvis-Previous-Event-Hash": "hash:protocol-genesis",
    },
  });
  try {
    const result = await run([
      "check",
      "headers",
      input.file,
      "--operation-class",
      "worksession_scoped_mutation",
    ]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "missing_idempotency_key");
  } finally {
    input.cleanup();
  }
});

test("check headers rejects unauthorized Actor header", async () => {
  const input = writeJsonTemp({
    headers: {
      Authorization: "",
      "Jarvis-Protocol-Version": "v0.1",
      "Jarvis-Actor-Id": "actor-test",
      "Jarvis-Idempotency-Key": "idem-test",
      "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
      "Jarvis-Expected-WorkSession-Revision": 0,
      "Jarvis-Previous-Event-Hash": "hash:protocol-genesis",
    },
  });
  try {
    const result = await run([
      "check",
      "headers",
      input.file,
      "--operation-class",
      "worksession_scoped_mutation",
    ]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "unauthorized_actor");
  } finally {
    input.cleanup();
  }
});

test("check headers rejects stale WorkSession genesis revision", async () => {
  const input = writeJsonTemp({
    headers: {
      Authorization: "HostAuth test",
      "Jarvis-Protocol-Version": "v0.1",
      "Jarvis-Actor-Id": "actor-test",
      "Jarvis-Idempotency-Key": "idem-test",
      "Jarvis-Request-Timestamp": "2026-06-16T10:00:00Z",
      "Jarvis-Expected-WorkSession-Revision": 1,
      "Jarvis-Previous-Event-Hash": "hash:protocol-genesis",
    },
  });
  try {
    const result = await run([
      "check",
      "headers",
      input.file,
      "--operation-class",
      "worksession_genesis_mutation",
    ]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "stale_work_session_revision");
  } finally {
    input.cleanup();
  }
});

test("check hash-chain rejects previous hash mismatch", async () => {
  const input = writeJsonTemp({
    events: [
      {
        sequence: 1,
        previous_hash: "hash:protocol-genesis",
        event_hash: "hash:first",
      },
      {
        sequence: 2,
        previous_hash: "hash:wrong",
        event_hash: "hash:second",
      },
    ],
  });
  try {
    const result = await run(["check", "hash-chain", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.errors[0].error_id, "invalid_previous_event_hash");
  } finally {
    input.cleanup();
  }
});

test("list rejection-ids emits OpenAPI rejection ids", async () => {
  const result = await run(["list", "rejection-ids"]);
  assert.equal(result.code, 0);
  assert.equal(result.payload.passed, true);
  assert.ok(result.payload.rejection_ids.includes("missing_actor"));
  assert.ok(result.payload.rejection_ids.includes("outcome_report_requires_terminal_source"));
});

test("validate fixture covers sealed WorkSession and EvidenceManifest rejection paths", async () => {
  const sealedWorkSession = await run([
    "validate",
    "fixture",
    join(fixtureRoot, "invalid/sealed-work-session-mutation.json"),
  ]);
  assert.equal(sealedWorkSession.code, 0);
  assert.equal(sealedWorkSession.payload.errors[0].error_id, "sealed_work_session_mutation");

  const sealedEvidence = await run([
    "validate",
    "fixture",
    join(fixtureRoot, "invalid/sealed-evidence-mutation.json"),
  ]);
  assert.equal(sealedEvidence.code, 0);
  assert.equal(sealedEvidence.payload.errors[0].error_id, "sealed_evidence_mutation");
});

test("validate fixture rejects invalid fixture without expected error id", async () => {
  const fixture = readJson(join(fixtureRoot, "invalid/missing-actor.json"));
  delete fixture.expected_error_id;
  const input = writeJsonTemp(fixture);
  try {
    const result = await run(["validate", "fixture", input.file]);
    assert.equal(result.code, 1);
    assert.equal(result.payload.passed, false);
    assert.equal(result.payload.valid, false);
    assert.equal(result.payload.expected_error_id, undefined);
  } finally {
    input.cleanup();
  }
});

test("print compatibility-claim emits non-certification template", async () => {
  const result = await run(["print", "compatibility-claim"]);
  assert.equal(result.code, 0);
  assert.equal(result.payload.passed, true);
  assert.equal(result.payload.compatibility_claim.status, "implementation claim, not certification");
  assert.equal(result.payload.compatibility_claim.verifier, "self-attested");
  assert.ok(result.payload.compatibility_claim.evidence);
  assert.ok(result.payload.compatibility_claim["conformance surface"]);
});

test("unsupported command emits machine-readable protocol error", async () => {
  const result = await run(["run", "agent"]);
  assert.equal(result.code, 1);
  assert.equal(result.payload.valid, false);
  assert.equal(result.payload.errors[0].error_id, "invalid_export");
  assert.equal(result.payload.errors[0].object_type, "CLI");
});

test("installed bin symlink executes CLI", () => {
  const dir = mkdtempSync(join(tmpdir(), "jarvis-cli-bin-"));
  const link = join(dir, "jarvis");
  try {
    symlinkSync(join(packageRoot, "src/index.js"), link);
    const result = spawnSync(process.execPath, [link, "list", "rejection-ids"], {
      cwd: packageRoot,
      encoding: "utf8",
    });
    assert.equal(result.status, 0, result.stderr);
    assert.ok(result.stdout.length > 0);
    const payload = JSON.parse(result.stdout);
    assert.equal(payload.command, "list rejection-ids");
    assert.equal(payload.passed, true);
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});
