# Golden-Path Conformance Entry

Jarvis v0.1 golden-path conformance proves that a compatible implementation
records governed human-agent collaboration inside the protocol contract.

## Required Proof

A compatible implementation MUST prove:

```txt
HumanWorker and AgentWorker are represented by Worker records.
HumanWorker and AgentWorker are represented by Actor records.
WorkSession records objective, policy, revision, and event hash state.
Every WorkSession-scoped mutation validates Jarvis-Protocol-Version.
Every WorkSession-scoped mutation validates Jarvis-Actor-Id.
Every WorkSession-scoped mutation validates Jarvis-Idempotency-Key.
Every WorkSession-scoped mutation validates Jarvis-Request-Timestamp.
Every WorkSession-scoped mutation validates Jarvis-Expected-WorkSession-Revision.
Every WorkSession-scoped mutation validates Jarvis-Previous-Event-Hash.
Every accepted WorkSession-scoped state change records the Actor.
Every accepted WorkSession-scoped state change verifies Actor authority.
Every accepted WorkSession-scoped state change checks Jarvis-Expected-WorkSession-Revision.
Every accepted WorkSession-scoped state change links Jarvis-Previous-Event-Hash.
AgentWorker action records PolicyDecision before accepted protocol state.
Policy-denied action creates scoped Request.
Request resolves only through Review or Takeover.
Review approve or narrow produces bounded ApprovalScope.
Stale Takeover rejection is covered by the stale Takeover fixture.
Contribution records attributable human, agent, shared, service, or tool work.
EvidenceManifest exports portable proof.
LearningRecord captures human, agent, or pair learning.
MemoryProposal and SkillProposal keep durable learning governed.
OutcomeReport references LearningRecord without mutating sealed records.
```

## Required Object Path

The golden path includes these protocol records:

```txt
Worker
Actor
HumanWorker
AgentWorker
WorkSession
JarvisEvent
PolicyDecision
Request
Review
ApprovalScope
Contribution
EvidenceManifest
LearningRecord
MemoryProposal
SkillProposal
OutcomeReport
```

## Required Export Boundary

EvidenceManifest export MUST exclude:

```txt
credentials
secrets
raw auth tokens
session cookies
provider keys
raw runtime state
host-only database ids
deployment details
billing data
private scores
UI state
private keys
```

Jarvis conformance records the protocol proof. Hosts own behavior outside the
protocol contract.
