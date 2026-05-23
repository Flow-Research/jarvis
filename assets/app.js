const steps = [
  {
    title: "Start the WorkSession",
    status: "active",
    hero: "WorkSession created",
    summary:
      "The human gives Jarvis a real objective. Jarvis creates the collaboration record before the agent starts.",
    activeNodes: ["human", "kernel"],
    activeLines: ["line-human-kernel"],
    events: [
      "Human intent recorded: inspect project and propose a plan.",
      "HumanAgentPair loaded: Abi + Jarvis.",
      "WorkSession WS-1042 started."
    ],
    memory: ["Human preference: be direct and evidence-based."],
    policy: ["local_dev_safe profile attached.", "Network denied by default."],
    evidence: ["work_session_started event recorded."]
  },
  {
    title: "Assemble Context",
    status: "active",
    hero: "Memory and skills selected",
    summary:
      "Jarvis assembles the context the agent is allowed to see: human profile, shared memory, project memory, policy, and active skills.",
    activeNodes: ["kernel", "agent"],
    activeLines: ["line-agent-kernel"],
    events: [
      "MemorySelector loads scoped memory.",
      "SkillResolver loads research and coding-assistant skills.",
      "ContextManifest created with hashes and retrieval reasons."
    ],
    memory: [
      "Human preference: be direct and evidence-based.",
      "Project memory: Jarvis is the harness, not the product UI.",
      "Shared memory: ask when permission or judgment is missing."
    ],
    policy: ["Tool visibility filtered by active grants.", "Only safe local tools exposed."],
    evidence: ["context_manifest created.", "skill inventory hash recorded."]
  },
  {
    title: "Agent Plans And Starts Work",
    status: "running",
    hero: "Agent running inside policy",
    summary:
      "The agent works autonomously inside the allowed scope. It can inspect files and write scratch artifacts without asking every time.",
    activeNodes: ["agent", "kernel", "runtime"],
    activeLines: ["line-agent-kernel", "line-kernel-runtime", "line-runtime-agent"],
    events: [
      "Agent proposes plan.",
      "Policy allows read-only project inspection.",
      "Runtime opens local workspace and starts sandbox lease."
    ],
    memory: [
      "Project memory: Jarvis v0.1 local alpha.",
      "Skill loaded: project inspection."
    ],
    policy: [
      "read_private allowed for project files.",
      "write_local allowed only in workspace scratch paths."
    ],
    evidence: ["plan_proposed event recorded.", "sandbox lease started."]
  },
  {
    title: "Policy Blocks A Boundary",
    status: "waiting_on_human",
    hero: "Request created",
    summary:
      "The agent tries to fetch an external source. Policy denies the action because network access is not granted.",
    activeNodes: ["agent", "kernel", "request"],
    activeLines: ["line-agent-kernel", "line-kernel-request"],
    events: [
      "Agent asks to fetch example.com for external context.",
      "GrantResolver denies network_fetch.",
      "Jarvis creates a structured Request with risk, host, scope, and expiry."
    ],
    memory: ["No durable memory is changed by the denied action."],
    policy: [
      "network_fetch denied.",
      "Request includes narrower safe alternative: allow example.com only."
    ],
    evidence: [
      "tool_denied event recorded.",
      "PolicyDecisionEvent hash-linked.",
      "request_created event recorded."
    ]
  },
  {
    title: "Human Reviews The Request",
    status: "waiting_on_human",
    hero: "Human narrows approval",
    summary:
      "The human does not take over the whole task. They approve a narrow action: fetch one host once, then continue.",
    activeNodes: ["human", "request", "kernel"],
    activeLines: ["line-request-human", "line-kernel-request"],
    events: [
      "Inbox shows exact blocked action and risk.",
      "Human approves with narrower scope.",
      "One-use approval token is bound to request version and action hash."
    ],
    memory: ["Human review pattern captured as a learning signal."],
    policy: [
      "Temporary grant: network_fetch:example.com.",
      "Grant expires after current WorkSession."
    ],
    evidence: ["review_added event recorded.", "approval token receipt recorded."]
  },
  {
    title: "Agent Resumes And Produces Artifact",
    status: "running",
    hero: "Work resumes",
    summary:
      "Jarvis resumes the WorkSession from events and checkpoint. The agent uses the approved scope and creates a draft artifact.",
    activeNodes: ["agent", "runtime", "kernel"],
    activeLines: ["line-runtime-agent", "line-kernel-runtime"],
    events: [
      "WorkSession resumes after approval.",
      "Runtime executes approved fetch through policy wrapper.",
      "Agent writes draft plan into workspace artifact."
    ],
    memory: ["ContextManifest updated with approval event."],
    policy: [
      "Approval cannot be replayed.",
      "Any payload or host change invalidates authorization."
    ],
    evidence: [
      "tool_executed event recorded.",
      "artifact_created event recorded.",
      "command/tool trace stored."
    ]
  },
  {
    title: "Human Reviews Output",
    status: "review",
    hero: "Review becomes teaching signal",
    summary:
      "The human reviews the artifact. Corrections are recorded as review events, not hidden inside a chat transcript.",
    activeNodes: ["human", "kernel", "agent"],
    activeLines: ["line-human-kernel", "line-agent-kernel"],
    events: [
      "Human approves plan structure.",
      "Human corrects wording: design must be direct, not advisory.",
      "Jarvis records correction as authoritative review."
    ],
    memory: [
      "Learning proposal: prefer direct architecture-contract language.",
      "Memory state: proposed, not confirmed automatically."
    ],
    policy: ["Memory write requires policy gate.", "Model cannot confirm its own learning."],
    evidence: ["review_added event recorded.", "memory_suggested event recorded."]
  },
  {
    title: "Evidence Manifest Exports",
    status: "completed",
    hero: "Evidence package ready",
    summary:
      "Jarvis exports a manifest that explains what happened, what was approved, which context was used, what artifacts were produced, and what limits remain.",
    activeNodes: ["kernel", "runtime"],
    activeLines: ["line-kernel-runtime"],
    events: [
      "EvidenceManifest generated.",
      "Manifest includes event-chain root, item hashes, reviews, policy decisions, context manifest, and artifacts.",
      "Redacted export remains derived from raw immutable evidence."
    ],
    memory: ["Confirmed memory waits for human approval."],
    policy: ["Debug/export surfaces apply redaction rules."],
    evidence: [
      "EvidenceManifest exported.",
      "Known limitations captured.",
      "WorkSession completed event recorded."
    ]
  },
  {
    title: "Learning Carries Forward",
    status: "completed",
    hero: "Future work improves",
    summary:
      "The next WorkSession starts better because Jarvis carries governed memory, skill updates, review patterns, and evidence forward.",
    activeNodes: ["human", "agent", "kernel"],
    activeLines: ["line-human-kernel", "line-agent-kernel"],
    events: [
      "Human confirms useful learning.",
      "Skill update remains versioned and reviewable.",
      "Next WorkSession inherits confirmed memory only."
    ],
    memory: [
      "Confirmed: use direct architecture-contract language.",
      "Confirmed: ask before external network access.",
      "Skill update: project-roadmap-review v1."
    ],
    policy: ["Learning remains governed.", "Untrusted content remains fenced as data."],
    evidence: ["memory_confirmed event recorded.", "skill_updated event recorded."]
  }
];

let index = 0;
let timer = null;

const elements = {
  heroState: document.querySelector("#hero-state"),
  sessionStatus: document.querySelector("#session-status"),
  stepTitle: document.querySelector("#step-title"),
  stepCounter: document.querySelector("#step-counter"),
  stepSummary: document.querySelector("#step-summary"),
  stepEvents: document.querySelector("#step-events"),
  memoryList: document.querySelector("#memory-list"),
  policyList: document.querySelector("#policy-list"),
  evidenceList: document.querySelector("#evidence-list"),
  timeline: document.querySelector("#timeline"),
  startBtn: document.querySelector("#startBtn"),
  prevBtn: document.querySelector("#prevBtn"),
  nextBtn: document.querySelector("#nextBtn"),
  autoBtn: document.querySelector("#autoBtn"),
  resetBtn: document.querySelector("#resetBtn")
};

function createList(items, target, className = "") {
  target.replaceChildren();
  items.forEach((item) => {
    const li = document.createElement("li");
    if (className) li.className = className;
    li.textContent = item;
    target.append(li);
  });
}

function renderTimeline() {
  elements.timeline.replaceChildren();
  steps.forEach((step, stepIndex) => {
    const li = document.createElement("li");
    if (stepIndex === index) li.className = "active";
    const number = document.createElement("span");
    number.className = "index";
    number.textContent = String(stepIndex + 1);
    const label = document.createElement("span");
    label.textContent = step.title;
    li.append(number, label);
    li.addEventListener("click", () => {
      setStep(stepIndex);
      stopAuto();
    });
    elements.timeline.append(li);
  });
}

function renderMap(step) {
  document.querySelectorAll("[data-node]").forEach((node) => {
    node.dataset.active = step.activeNodes.includes(node.dataset.node);
  });

  document.querySelectorAll(".flow-lines path").forEach((path) => {
    path.classList.toggle("active", step.activeLines.includes(path.id));
  });
}

function setStep(nextIndex) {
  index = Math.max(0, Math.min(steps.length - 1, nextIndex));
  const step = steps[index];

  elements.heroState.textContent = step.hero;
  elements.sessionStatus.textContent = step.status;
  elements.stepTitle.textContent = step.title;
  elements.stepCounter.textContent = `${index + 1} / ${steps.length}`;
  elements.stepSummary.textContent = step.summary;

  createList(step.events, elements.stepEvents);
  createList(step.memory, elements.memoryList);
  createList(step.policy, elements.policyList, step.status === "waiting_on_human" ? "pending" : "");
  createList(step.evidence, elements.evidenceList);

  elements.prevBtn.disabled = index === 0;
  elements.nextBtn.disabled = index === steps.length - 1;
  renderTimeline();
  renderMap(step);
}

function next() {
  if (index >= steps.length - 1) {
    stopAuto();
    return;
  }
  setStep(index + 1);
}

function stopAuto() {
  if (timer) {
    clearInterval(timer);
    timer = null;
  }
  elements.autoBtn.setAttribute("aria-pressed", "false");
  elements.autoBtn.textContent = "Auto play";
}

function startAuto() {
  stopAuto();
  elements.autoBtn.setAttribute("aria-pressed", "true");
  elements.autoBtn.textContent = "Pause";
  timer = setInterval(next, 2200);
}

elements.startBtn.addEventListener("click", () => {
  setStep(0);
  startAuto();
});

elements.prevBtn.addEventListener("click", () => {
  setStep(index - 1);
  stopAuto();
});

elements.nextBtn.addEventListener("click", () => {
  next();
  stopAuto();
});

elements.autoBtn.addEventListener("click", () => {
  if (timer) {
    stopAuto();
  } else {
    startAuto();
  }
});

elements.resetBtn.addEventListener("click", () => {
  stopAuto();
  setStep(0);
});

setStep(0);
