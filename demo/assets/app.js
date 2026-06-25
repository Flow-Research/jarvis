const steps = [
  {
    title: "Mutation Headers",
    status: "created",
    mission: "Header gate",
    gate: 10,
    gateColor: "#78f7b4",
    activeNodes: ["human", "kernel"],
    activeBeams: ["beam-human"],
    summary:
      "The WorkSession-scoped mutation enters through the OpenAPI binding with protocol version, actor id, idempotency key, timestamp, expected revision, and previous event hash.",
    events: [
      "Authorization: Bearer host-auth-ref",
      "Jarvis-Protocol-Version: v0.1",
      "Jarvis-Actor-Id: actor-human-reviewer",
      "Jarvis-Idempotency-Key: idem-work-session-create-001",
      "Jarvis-Request-Timestamp: 2026-06-24T09:00:00Z",
      "Jarvis-Expected-WorkSession-Revision: 0",
      "Jarvis-Previous-Event-Hash: hash:protocol-genesis"
    ],
    memory: [
      "Worker ref: worker-human-researcher",
      "Actor ref: actor-human-reviewer",
      "Trace ref: trace-work-session-1042"
    ],
    policy: [
      "Protocol version accepted.",
      "Idempotency key recorded.",
      "Timestamp checked."
    ],
    evidence: ["mutation_headers", "trace_context", "previous_hash"]
  },
  {
    title: "Authority And Revision",
    status: "created",
    mission: "Authority verified",
    gate: 18,
    gateColor: "#78f7b4",
    activeNodes: ["human", "kernel"],
    activeBeams: ["beam-human"],
    summary:
      "Jarvis verifies Actor authority, checks the WorkSession revision, and links the previous event hash before accepting protocol state.",
    events: [
      "Actor authority permits work_session.create.",
      "Expected revision matches current revision.",
      "Previous event hash matches the chain head."
    ],
    memory: [
      "EventAuthority.can_append_events: true",
      "ContributionScope includes human.",
      "No host credential enters the protocol record."
    ],
    policy: [
      "Invalid Actor rejects.",
      "Stale revision rejects.",
      "Previous hash mismatch rejects."
    ],
    evidence: ["actor_authority_check", "revision_check", "hash_link_check"]
  },
  {
    title: "WorkSession And Policy",
    status: "active",
    mission: "WorkSession active",
    gate: 27,
    gateColor: "#78f7b4",
    activeNodes: ["human", "agent", "kernel"],
    activeBeams: ["beam-human", "beam-agent"],
    summary:
      "The WorkSession starts as the durable collaboration record. Policy defines the boundary for autonomous AgentWorker action.",
    events: [
      "WorkSession WS-1042 created.",
      "HumanWorker and AgentWorker refs attached.",
      "Policy policy-research-001 attached."
    ],
    memory: [
      "Objective: produce evidence-backed protocol note.",
      "HumanWorker role: policy owner and reviewer.",
      "AgentWorker role: bounded research executor."
    ],
    policy: [
      "Allowed: inspect local context.",
      "Review required: external source use.",
      "Denied: credentials and unapproved external sends."
    ],
    evidence: ["work_session_created", "policy_attached", "worker_refs"]
  },
  {
    title: "PolicyDecision First",
    status: "active",
    mission: "Action checked",
    gate: 36,
    gateColor: "#78f7b4",
    activeNodes: ["agent", "kernel"],
    activeBeams: ["beam-agent"],
    summary:
      "Every AgentWorker action that affects a WorkSession records a PolicyDecision before the action becomes accepted protocol state.",
    events: [
      "AgentWorker proposes inspect_local_context.",
      "PolicyDecision records result: allow.",
      "Accepted action links to policy-decision-local-context-001."
    ],
    memory: [
      "Requested action hash recorded.",
      "Risk class: low.",
      "Selected grant ref: grant:local-read."
    ],
    policy: [
      "PolicyDecision precedes action event.",
      "Accepted action links to previous hash.",
      "Host execution remains outside Jarvis."
    ],
    evidence: ["policy_decision_allow", "accepted_action_event", "event_hash"]
  },
  {
    title: "Request For Blocked Scope",
    status: "waiting_on_human",
    mission: "Request created",
    gate: 48,
    gateColor: "#ffb86b",
    activeNodes: ["agent", "kernel", "request"],
    activeBeams: ["beam-agent", "beam-request"],
    summary:
      "The AgentWorker reaches a review-required external-source action. Jarvis records a scoped Request instead of treating the message as chat.",
    events: [
      "PolicyDecision records result: review_required.",
      "Request request-external-source-001 created.",
      "Blocking scope: tool_call."
    ],
    memory: [
      "Reason: external source access requires HumanWorker review.",
      "Default fallback: continue with limited evidence.",
      "Request expiry recorded."
    ],
    policy: [
      "Blocked action stays blocked.",
      "Unrelated safe work stays available.",
      "Request is not authority."
    ],
    evidence: ["policy_decision_review_required", "request_created", "safe_fallback"]
  },
  {
    title: "Review And ApprovalScope",
    status: "waiting_on_human",
    mission: "Scope narrowed",
    gate: 58,
    gateColor: "#ffb86b",
    activeNodes: ["human", "request", "kernel"],
    activeBeams: ["beam-request", "beam-human"],
    summary:
      "HumanWorker judgment resolves the Request through Review. ApprovalScope bounds the approved continuation to one action, one actor, and one WorkSession.",
    events: [
      "Review decision: narrow.",
      "ApprovalScope binds request revision 4.",
      "ApprovalScope binds normalized action hash."
    ],
    memory: [
      "Allowed scope: single approved source.",
      "Denied scope: all other external sends.",
      "Max uses: 1."
    ],
    policy: [
      "Unbounded approval rejects.",
      "Stale ApprovalScope use rejects.",
      "Actor mismatch rejects."
    ],
    evidence: ["review_recorded", "approval_scope_created", "request_resolved"]
  },
  {
    title: "Takeover Continuation",
    status: "takeover",
    mission: "Human controls scope",
    gate: 68,
    gateColor: "#6fd9ff",
    activeNodes: ["human", "kernel", "request"],
    activeBeams: ["beam-human", "beam-request"],
    summary:
      "A final-submission Request resolves through Takeover. Lock epoch and reconciliation refs bind the human-controlled continuation.",
    events: [
      "Request request-final-submission-001 records status: takeover.",
      "Takeover lock epoch: 2.",
      "Resumed Takeover records reconciliation refs."
    ],
    memory: [
      "Affected scope: final_submission.",
      "Controlling Actor: actor-human-reviewer.",
      "Resumed by HumanWorker after reconciliation."
    ],
    policy: [
      "Stale agent continuation rejects.",
      "Missing reconciliation refs reject resumed state.",
      "Takeover stays scoped."
    ],
    evidence: ["takeover_recorded", "lock_epoch", "reconciliation_refs"]
  },
  {
    title: "Contribution Recorded",
    status: "active",
    mission: "Attribution recorded",
    gate: 76,
    gateColor: "#78f7b4",
    activeNodes: ["human", "agent", "kernel"],
    activeBeams: ["beam-human", "beam-agent"],
    summary:
      "Contribution records who did what. Shared work preserves individual HumanWorker and AgentWorker contributor refs.",
    events: [
      "Contribution contributor_type: shared.",
      "HumanWorker contribution ref recorded.",
      "AgentWorker contribution ref recorded."
    ],
    memory: [
      "Contribution links to request, review, takeover, and action events.",
      "Artifact refs attach to contribution.",
      "Limitations remain visible."
    ],
    policy: [
      "Missing contribution Actor rejects.",
      "Duplicate contributor refs reject.",
      "Shared contribution requires individual refs."
    ],
    evidence: ["contribution_recorded", "artifact_ref", "review_refs"]
  },
  {
    title: "LearningRecord Created",
    status: "active",
    mission: "Learning recorded",
    gate: 84,
    gateColor: "#78f7b4",
    activeNodes: ["human", "agent", "kernel"],
    activeBeams: ["beam-human", "beam-agent"],
    summary:
      "LearningRecord records what the HumanWorker, AgentWorker, or pair learned from the WorkSession before the WorkSession is sealed.",
    events: [
      "LearningRecord subject_type: pair.",
      "Source event refs point to review, action, and takeover events.",
      "Review state records accepted learning."
    ],
    memory: [
      "The HumanWorker learned review boundaries.",
      "The AgentWorker learned source-scope preference.",
      "The pair learned the next comparison workflow."
    ],
    policy: [
      "Learning is governed.",
      "LearningRecord does not silently mutate memory.",
      "LearningRecord links to proposals."
    ],
    evidence: ["learning_record", "source_event_refs", "pair_learning"]
  },
  {
    title: "Memory And Skill Proposals",
    status: "active",
    mission: "Proposals governed",
    gate: 90,
    gateColor: "#78f7b4",
    activeNodes: ["agent", "kernel", "human"],
    activeBeams: ["beam-agent", "beam-human"],
    summary:
      "MemoryProposal and SkillProposal keep future behavior governed. Proposed memory and reusable workflow changes require review before durable effect.",
    events: [
      "MemoryProposal status: pending_review.",
      "SkillProposal status: pending_review.",
      "Tool access expansion still requires policy review."
    ],
    memory: [
      "Memory scope: future protocol comparison work.",
      "Skill scope: protocol comparison workflow.",
      "Provenance links to learning and source events."
    ],
    policy: [
      "Model self-confirmed memory rejects.",
      "Tool self-confirmed memory rejects.",
      "Unreviewed skill activation rejects."
    ],
    evidence: ["memory_proposal", "skill_proposal", "provenance_refs"]
  },
  {
    title: "EvidenceManifest Export",
    status: "completed",
    mission: "Evidence exported",
    gate: 95,
    gateColor: "#78f7b4",
    activeNodes: ["kernel", "host"],
    activeBeams: ["beam-host"],
    summary:
      "EvidenceManifest exports portable proof after terminal WorkSession state without host-private fields.",
    events: [
      "WorkSession status: completed.",
      "EvidenceManifest includes event chain root.",
      "Export profile redacts host-private fields."
    ],
    memory: [
      "Evidence item refs link to source JarvisEvents.",
      "PolicyDecision refs included.",
      "Request, Review, Takeover, and Contribution refs included."
    ],
    policy: [
      "Sealed EvidenceManifest mutation rejects.",
      "Host-private export fields reject.",
      "After-the-fact evidence rejects."
    ],
    evidence: ["event_chain_root", "portable_export", "redaction_refs"]
  },
  {
    title: "OutcomeReport Feedback",
    status: "closed",
    mission: "Loop improved",
    gate: 100,
    gateColor: "#78f7b4",
    activeNodes: ["human", "agent", "kernel"],
    activeBeams: ["beam-human", "beam-agent"],
    summary:
      "OutcomeReport enters post-session feedback without rewriting the sealed WorkSession or EvidenceManifest. A new LearningRecord carries the feedback forward.",
    events: [
      "OutcomeReport arrives after WorkSession completion.",
      "OutcomeReport references learning-record-outcome-001.",
      "Sealed WorkSession and EvidenceManifest remain unchanged."
    ],
    memory: [
      "Post-session feedback becomes governed learning.",
      "Next WorkSession inherits accepted learning only.",
      "Human-agent pair improves without changing history."
    ],
    policy: [
      "OutcomeReport is not scoring or payment logic.",
      "Sealed WorkSession mutation rejects.",
      "Sealed EvidenceManifest mutation rejects."
    ],
    evidence: ["outcome_report", "outcome_learning_record", "sealed_records"]
  }
];

let current = 0;
let timer = null;

const els = {
  topbarStatus: document.querySelector("#topbarStatus"),
  missionState: document.querySelector("#missionState"),
  evidenceCount: document.querySelector("#evidenceCount"),
  stepTitle: document.querySelector("#stepTitle"),
  stepCounter: document.querySelector("#stepCounter"),
  stepSummary: document.querySelector("#stepSummary"),
  eventLog: document.querySelector("#eventLog"),
  memoryList: document.querySelector("#memoryList"),
  policyList: document.querySelector("#policyList"),
  evidenceList: document.querySelector("#evidenceList"),
  timeline: document.querySelector("#timeline"),
  gateMeter: document.querySelector("#gateMeter"),
  startBtn: document.querySelector("#startBtn"),
  prevBtn: document.querySelector("#prevBtn"),
  nextBtn: document.querySelector("#nextBtn"),
  autoBtn: document.querySelector("#autoBtn"),
  resetBtn: document.querySelector("#resetBtn"),
  canvas: document.querySelector("#signalCanvas")
};

function pad(value) {
  return String(value).padStart(2, "0");
}

function setItems(target, items, className = "") {
  target.replaceChildren();
  items.forEach((item) => {
    const li = document.createElement("li");
    if (className) li.className = className;
    li.textContent = item;
    target.append(li);
  });
}

function renderTimeline() {
  els.timeline.replaceChildren();
  steps.forEach((step, stepIndex) => {
    const item = document.createElement("li");
    if (stepIndex === current) item.className = "active";
    const button = document.createElement("button");
    button.type = "button";
    button.className = "timeline-step";
    if (stepIndex === current) {
      button.setAttribute("aria-current", "step");
    }
    button.innerHTML = `
      <span class="step-index">${pad(stepIndex + 1)}</span>
      <span class="step-name">${step.title}</span>
    `;
    button.addEventListener("click", () => {
      setStep(stepIndex);
      stopAuto();
    });
    item.append(button);
    els.timeline.append(item);
  });
}

function renderMap(step) {
  document.querySelectorAll("[data-node]").forEach((node) => {
    node.dataset.active = step.activeNodes.includes(node.dataset.node);
  });

  document.querySelectorAll(".data-beam").forEach((beam) => {
    beam.classList.toggle(
      "active",
      step.activeBeams.some((name) => beam.classList.contains(name))
    );
  });
}

function setStep(nextIndex) {
  current = Math.max(0, Math.min(steps.length - 1, nextIndex));
  const step = steps[current];
  const evidenceTotal = steps.slice(0, current + 1).reduce((sum, item) => {
    return sum + item.evidence.length;
  }, 0);

  els.topbarStatus.textContent = step.status;
  els.missionState.textContent = step.mission;
  els.evidenceCount.textContent = `${pad(evidenceTotal)} items`;
  els.stepTitle.textContent = step.title;
  els.stepCounter.textContent = `${pad(current + 1)} / ${pad(steps.length)}`;
  els.stepSummary.textContent = step.summary;
  els.gateMeter.style.setProperty("--gate", `${step.gate}%`);
  els.gateMeter.style.setProperty("--gate-color", step.gateColor);

  setItems(els.eventLog, step.events);
  setItems(els.memoryList, step.memory);
  setItems(
    els.policyList,
    step.policy,
    step.status === "waiting_on_human" ? "pending" : ""
  );
  setItems(els.evidenceList, step.evidence);

  els.prevBtn.disabled = current === 0;
  els.nextBtn.disabled = current === steps.length - 1;
  renderTimeline();
  renderMap(step);
}

function advance() {
  if (current === steps.length - 1) {
    stopAuto();
    return;
  }
  setStep(current + 1);
}

function stopAuto() {
  if (timer) clearInterval(timer);
  timer = null;
  els.autoBtn.textContent = "Autoplay";
  els.autoBtn.setAttribute("aria-pressed", "false");
}

function startAuto() {
  stopAuto();
  els.autoBtn.textContent = "Pause";
  els.autoBtn.setAttribute("aria-pressed", "true");
  timer = setInterval(advance, 2400);
}

els.startBtn.addEventListener("click", () => {
  setStep(0);
  startAuto();
});

els.prevBtn.addEventListener("click", () => {
  setStep(current - 1);
  stopAuto();
});

els.nextBtn.addEventListener("click", () => {
  advance();
  stopAuto();
});

els.autoBtn.addEventListener("click", () => {
  if (timer) stopAuto();
  else startAuto();
});

els.resetBtn.addEventListener("click", () => {
  stopAuto();
  setStep(0);
});

function runCanvas() {
  const canvas = els.canvas;
  const ctx = canvas.getContext("2d");
  const points = [];
  const count = 62;
  let width = 0;
  let height = 0;

  function resize() {
    const ratio = window.devicePixelRatio || 1;
    width = document.documentElement.clientWidth;
    height = window.innerHeight;
    canvas.width = Math.floor(width * ratio);
    canvas.height = Math.floor(height * ratio);
    canvas.style.width = `${width}px`;
    canvas.style.height = `${height}px`;
    ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  }

  function seed() {
    points.length = 0;
    for (let i = 0; i < count; i += 1) {
      points.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.34,
        vy: (Math.random() - 0.5) * 0.34,
        r: Math.random() * 1.6 + 0.6
      });
    }
  }

  function draw() {
    ctx.clearRect(0, 0, width, height);
    ctx.fillStyle = "rgba(120, 247, 180, 0.45)";
    ctx.strokeStyle = "rgba(120, 247, 180, 0.12)";

    points.forEach((point) => {
      point.x += point.vx;
      point.y += point.vy;
      if (point.x < 0 || point.x > width) point.vx *= -1;
      if (point.y < 0 || point.y > height) point.vy *= -1;

      ctx.beginPath();
      ctx.arc(point.x, point.y, point.r, 0, Math.PI * 2);
      ctx.fill();
    });

    for (let i = 0; i < points.length; i += 1) {
      for (let j = i + 1; j < points.length; j += 1) {
        const a = points[i];
        const b = points[j];
        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const distance = Math.sqrt(dx * dx + dy * dy);
        if (distance < 150) {
          ctx.globalAlpha = (150 - distance) / 150;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
          ctx.globalAlpha = 1;
        }
      }
    }

    requestAnimationFrame(draw);
  }

  window.addEventListener("resize", () => {
    resize();
    seed();
  });

  resize();
  seed();
  draw();
}

setStep(0);
runCanvas();
