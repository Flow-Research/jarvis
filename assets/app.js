const steps = [
  {
    title: "Start the WorkSession",
    status: "active",
    mission: "WorkSession created",
    gate: 18,
    gateColor: "#78f7b4",
    activeNodes: ["human", "kernel"],
    activeBeams: ["beam-human"],
    summary:
      "The human gives Jarvis a real objective. Jarvis creates the durable collaboration record before the agent starts.",
    events: [
      "Human intent: inspect project and produce an implementation plan.",
      "HumanAgentPair loaded: Abi + Jarvis.",
      "WorkSession WS-1042 created as the public collaboration surface."
    ],
    memory: ["Human preference: direct architecture language.", "Shared rule: ask when permission or judgment is missing."],
    policy: ["Policy profile attached: local_dev_safe.", "Default network posture: denied."],
    evidence: ["work_session_started event", "initial trace context"]
  },
  {
    title: "Context Assembly",
    status: "active",
    mission: "Memory selected",
    gate: 28,
    gateColor: "#78f7b4",
    activeNodes: ["kernel", "agent"],
    activeBeams: ["beam-agent"],
    summary:
      "Jarvis selects the context the agent can use: human memory, project memory, skill inventory, active policy, and tool grants.",
    events: [
      "MemorySelector chooses scoped human, shared, and project memory.",
      "SkillResolver loads research and project-inspection skills.",
      "ContextManifest stores retrieval reasons and hashes."
    ],
    memory: [
      "Project memory: Jarvis owns the harness layer.",
      "Skill memory: inspect repo before proposing implementation.",
      "Context manifest: memory ids, skill ids, policy profile, tool hash."
    ],
    policy: ["Only granted tools become visible.", "Untrusted content is data, not instruction."],
    evidence: ["context_manifest", "skill_inventory_hash", "tool_inventory_hash"]
  },
  {
    title: "Autonomous Execution",
    status: "running",
    mission: "Agent executing",
    gate: 46,
    gateColor: "#78f7b4",
    activeNodes: ["agent", "kernel", "runtime"],
    activeBeams: ["beam-agent", "beam-runtime"],
    summary:
      "The agent works inside the allowed scope. Jarvis wraps each tool call while the runtime supplies session state, files, sandbox, and streaming.",
    events: [
      "Agent proposes plan and starts project inspection.",
      "Policy allows read-only local file inspection.",
      "Runtime opens workspace and sandbox lease."
    ],
    memory: ["Active memory remains scoped to this project.", "No new durable memory yet."],
    policy: [
      "read_private: allowed for project files.",
      "write_local: allowed only inside workspace scratch paths."
    ],
    evidence: ["plan_proposed", "tool_allowed", "sandbox_lease_started"]
  },
  {
    title: "Policy Boundary",
    status: "waiting_on_human",
    mission: "Request generated",
    gate: 62,
    gateColor: "#ffb86b",
    activeNodes: ["agent", "kernel", "request"],
    activeBeams: ["beam-agent", "beam-request"],
    summary:
      "The agent asks for network access. Jarvis denies the action, converts the blocked intent into a structured Request, and pauses that branch of work.",
    events: [
      "Agent requests network_fetch for example.com.",
      "GrantResolver denies uncovered network dimension.",
      "Request created with risk, host, expiry, action hash, and safe alternative."
    ],
    memory: ["Denied action does not mutate memory."],
    policy: [
      "network_fetch: blocked.",
      "Approval required for one host and one WorkSession only."
    ],
    evidence: ["tool_denied", "PolicyDecisionEvent", "request_created"]
  },
  {
    title: "Human Approval",
    status: "waiting_on_human",
    mission: "Human narrows scope",
    gate: 70,
    gateColor: "#ffb86b",
    activeNodes: ["human", "request", "kernel"],
    activeBeams: ["beam-request", "beam-human"],
    summary:
      "The human does not micromanage the task. They approve a narrow capability and hand the work back to the agent.",
    events: [
      "Inbox displays the exact blocked action and risk.",
      "Human approves network_fetch:example.com for this WorkSession.",
      "One-use approval token binds to request version and action hash."
    ],
    memory: ["Human review pattern becomes a learning signal."],
    policy: [
      "Temporary grant created.",
      "Grant expires with WorkSession.",
      "Replay of approval token fails."
    ],
    evidence: ["review_added", "approval_token_issued", "request_resolved"]
  },
  {
    title: "Resume And Produce",
    status: "running",
    mission: "Artifact produced",
    gate: 82,
    gateColor: "#78f7b4",
    activeNodes: ["agent", "kernel", "runtime"],
    activeBeams: ["beam-agent", "beam-runtime"],
    summary:
      "The agent resumes from the WorkSession event log, uses the approved scope, and produces a draft artifact with traceable evidence.",
    events: [
      "WorkSession resumes after request resolution.",
      "Runtime executes approved fetch through policy wrapper.",
      "Agent writes a plan artifact into the workspace."
    ],
    memory: ["ContextManifest updates with approval event.", "Learning remains proposed until review."],
    policy: [
      "Approval is one-use.",
      "Host or payload change invalidates authorization."
    ],
    evidence: ["tool_executed", "artifact_created", "command_trace"]
  },
  {
    title: "Review And Teach",
    status: "review",
    mission: "Review captured",
    gate: 88,
    gateColor: "#6fd9ff",
    activeNodes: ["human", "kernel", "agent"],
    activeBeams: ["beam-human", "beam-agent"],
    summary:
      "The human reviews the artifact. Jarvis records correction as teaching material instead of burying it inside chat history.",
    events: [
      "Human approves the plan structure.",
      "Human corrects tone: direct architecture contract language.",
      "Jarvis creates memory and skill update proposals."
    ],
    memory: [
      "Memory proposal: use direct system-contract wording.",
      "Skill proposal: roadmap review checklist.",
      "State: proposed, not automatically confirmed."
    ],
    policy: ["Model cannot confirm its own learning.", "Memory write requires policy gate."],
    evidence: ["review_added", "memory_suggested", "skill_suggested"]
  },
  {
    title: "Evidence Export",
    status: "completed",
    mission: "Manifest ready",
    gate: 96,
    gateColor: "#78f7b4",
    activeNodes: ["kernel", "runtime"],
    activeBeams: ["beam-runtime"],
    summary:
      "Jarvis exports a manifest showing what happened, what was approved, what context was used, what artifact was produced, and what limits remain.",
    events: [
      "EvidenceManifest generated.",
      "Manifest includes event-chain root, item hashes, reviews, policy decisions, and artifacts.",
      "Redacted exports remain derived from raw immutable evidence."
    ],
    memory: ["Confirmed memory waits for human decision."],
    policy: ["Debug and export surfaces apply redaction.", "Outbox remains closed unless approved."],
    evidence: ["EvidenceManifest JSON", "artifact refs", "known limitations"]
  },
  {
    title: "Learning Carries Forward",
    status: "completed",
    mission: "Future work improved",
    gate: 100,
    gateColor: "#78f7b4",
    activeNodes: ["human", "kernel", "agent"],
    activeBeams: ["beam-human", "beam-agent"],
    summary:
      "The next WorkSession starts smarter because confirmed memory, reviewed skills, and evidence move forward with the human-agent pair.",
    events: [
      "Human confirms useful learning.",
      "Skill update is versioned.",
      "Next WorkSession inherits confirmed memory only."
    ],
    memory: [
      "Confirmed: direct architecture-contract wording.",
      "Confirmed: ask before external network access.",
      "Skill v1: project-roadmap-review."
    ],
    policy: ["Learning is governed.", "Untrusted content remains fenced as data."],
    evidence: ["memory_confirmed", "skill_updated", "work_session_completed"]
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
    item.innerHTML = `
      <span class="step-index">${pad(stepIndex + 1)}</span>
      <span class="step-name">${step.title}</span>
    `;
    item.addEventListener("click", () => {
      setStep(stepIndex);
      stopAuto();
    });
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
  if (els.missionState) els.missionState.textContent = step.mission;
  if (els.evidenceCount) els.evidenceCount.textContent = `${pad(evidenceTotal)} items`;
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
    width = window.innerWidth;
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
