# Protocol Record Examples

This file gives concrete Jarvis v0.1 protocol record examples for one
human-agent collaboration loop.

Jarvis records protocol state. Hosts own native execution.

These examples are public protocol examples. They do not define runtime
behavior, host UI, storage, auth, model calls, tool execution, billing,
scoring, payment, deployment, adapters, wrappers, SDK implementation, or host
workflow.

## Conformance Links

These records map to the public conformance checklist:

- [Participant Gate](../conformance/checklist.md#participant-gate)
- [WorkSession Gate](../conformance/checklist.md#worksession-gate)
- [PolicyDecision Gate](../conformance/checklist.md#policydecision-gate)
- [Request Gate](../conformance/checklist.md#request-gate)
- [Review And ApprovalScope Gate](../conformance/checklist.md#review-and-approvalscope-gate)
- [Takeover Gate](../conformance/checklist.md#takeover-gate)
- [Contribution Gate](../conformance/checklist.md#contribution-gate)
- [EvidenceManifest Gate](../conformance/checklist.md#evidencemanifest-gate)
- [Learning Gate](../conformance/checklist.md#learning-gate)
- [MemoryProposal Gate](../conformance/checklist.md#memoryproposal-gate)
- [SkillProposal Gate](../conformance/checklist.md#skillproposal-gate)
- [OutcomeReport Gate](../conformance/checklist.md#outcomereport-gate)

## Example Loop

One HumanWorker and one AgentWorker complete an evidence-backed research task.

The HumanWorker defines the goal and policy. The AgentWorker inspects allowed
local context, reaches a review-required external-source action, creates a
scoped Request, receives a HumanWorker Review with narrowed ApprovalScope,
continues inside that scope, records Contribution and EvidenceManifest records,
records governed LearningRecord, and proposes governed MemoryProposal and
SkillProposal records. A later OutcomeReport carries post-session feedback
into learning.

## Operation Header Examples

Worker and Actor registration are non-WorkSession protocol mutations.

```txt
Authorization: Bearer host-auth-ref
Jarvis-Protocol-Version: v0.1
Jarvis-Actor-Id: actor-host-protocol
Jarvis-Idempotency-Key: idem-register-worker-human-001
Jarvis-Request-Timestamp: 2026-06-24T09:00:00Z
```

WorkSession-scoped mutations require revision and previous event hash.

```txt
Authorization: Bearer host-auth-ref
Jarvis-Protocol-Version: v0.1
Jarvis-Actor-Id: actor-agent-research
Jarvis-Idempotency-Key: idem-policy-decision-source-001
Jarvis-Request-Timestamp: 2026-06-24T09:08:00Z
Jarvis-Expected-WorkSession-Revision: 2
Jarvis-Previous-Event-Hash: hash:event-local-context-read-001
```

OutcomeReport submission is a non-WorkSession protocol mutation.

```txt
Authorization: Bearer host-auth-ref
Jarvis-Protocol-Version: v0.1
Jarvis-Actor-Id: actor-human-reviewer
Jarvis-Idempotency-Key: idem-outcome-report-001
Jarvis-Request-Timestamp: 2026-06-24T10:30:00Z
```

## Worker

Conformance gate:
[Participant Gate](../conformance/checklist.md#participant-gate)

```json
{
  "id": "worker-human-researcher",
  "type": "human",
  "role": "research_reviewer",
  "authority_scope": {
    "grants": [
      "policy.author",
      "request.review",
      "takeover.control",
      "learning.review"
    ]
  },
  "accountability_scope": {
    "accountable_for": [
      "objective",
      "final_judgment",
      "accepted_learning"
    ]
  },
  "display_name": "Human Researcher"
}
```

```json
{
  "id": "worker-agent-research",
  "type": "agent",
  "role": "research_executor",
  "authority_scope": {
    "grants": [
      "policy.bounded_execute",
      "request.create",
      "evidence.capture",
      "learning.propose"
    ]
  },
  "accountability_scope": {
    "accountable_for": [
      "draft_work",
      "evidence_refs",
      "proposal_accuracy"
    ]
  },
  "capabilities": [
    {
      "ref": "capability:local-context-read",
      "capability_type": "context_read",
      "required": true
    }
  ]
}
```

## Actor

Conformance gate:
[Participant Gate](../conformance/checklist.md#participant-gate)

```json
{
  "id": "actor-human-reviewer",
  "worker_id": "worker-human-researcher",
  "type": "human",
  "event_authority": {
    "can_append_events": true,
    "allowed_event_types": [
      "review.recorded",
      "takeover.recorded",
      "learning.reviewed",
      "outcome_report.accepted",
      "work_session.completed"
    ]
  },
  "contribution_scope": {
    "contribution_roles": [
      "human",
      "shared"
    ]
  },
  "created_at": "2026-06-24T09:00:00Z"
}
```

```json
{
  "id": "actor-agent-research",
  "worker_id": "worker-agent-research",
  "type": "agent",
  "event_authority": {
    "can_append_events": true,
    "allowed_event_types": [
      "policy_decision.recorded",
      "agent.action.accepted",
      "request.created",
      "contribution.recorded",
      "evidence.captured",
      "learning.proposed"
    ]
  },
  "contribution_scope": {
    "contribution_roles": [
      "agent",
      "shared"
    ]
  },
  "created_at": "2026-06-24T09:00:00Z"
}
```

## HumanWorker

Conformance gate:
[Participant Gate](../conformance/checklist.md#participant-gate)

```json
{
  "worker_id": "worker-human-researcher",
  "actor_id": "actor-human-reviewer",
  "role": "policy_owner_and_reviewer",
  "policy_authority": {
    "grants": [
      "policy.author",
      "policy.narrow"
    ]
  },
  "review_authority": {
    "grants": [
      "request.approve",
      "request.deny",
      "request.narrow",
      "takeover.start",
      "learning.accept"
    ]
  },
  "domain_context_refs": [
    "ref:research-task-context"
  ],
  "known_patterns": [
    "prefers direct protocol wording",
    "requires evidence-backed claims"
  ]
}
```

## AgentWorker

Conformance gate:
[Participant Gate](../conformance/checklist.md#participant-gate)

```json
{
  "worker_id": "worker-agent-research",
  "actor_id": "actor-agent-research",
  "agent_ref": "agent:existing-research-agent",
  "role": "bounded_research_executor",
  "capability_refs": [
    {
      "ref": "capability:local-context-read",
      "capability_type": "context_read",
      "required": true
    },
    {
      "ref": "capability:evidence-capture",
      "capability_type": "evidence_capture",
      "required": true
    }
  ],
  "autonomy_level": "bounded_execute",
  "operating_constraints": [
    "act only inside Policy",
    "create Request for review-required external source use",
    "propose learning without silently mutating memory"
  ],
  "tool_access_profile": "profile:local-context-only",
  "memory_access_profile": "profile:proposal-only"
}
```

## Policy

Conformance gates:
[WorkSession Gate](../conformance/checklist.md#worksession-gate),
[PolicyDecision Gate](../conformance/checklist.md#policydecision-gate)

```json
{
  "id": "policy-research-001",
  "owner_worker_id": "worker-human-researcher",
  "created_by_actor_id": "actor-human-reviewer",
  "autonomy_level": "bounded_execute",
  "allowed_actions": [
    {
      "action": "inspect_local_context",
      "scope_ref": "scope:local-protocol-docs",
      "grant_refs": [
        "grant:local-read"
      ]
    },
    {
      "action": "draft_artifact",
      "scope_ref": "scope:worksession-draft"
    }
  ],
  "denied_actions": [
    {
      "action": "access_credentials",
      "scope_ref": "scope:any"
    },
    {
      "action": "send_external_message",
      "scope_ref": "scope:any"
    }
  ],
  "review_required_actions": [
    {
      "action": "fetch_external_source",
      "scope_ref": "scope:external-source"
    },
    {
      "action": "final_submission",
      "scope_ref": "scope:final-output"
    }
  ],
  "risk_classes": [
    "low",
    "medium",
    "high"
  ],
  "escalation_rules": [
    {
      "trigger": "high_risk_or_policy_conflict",
      "risk_class": "high",
      "required_action": "create_request",
      "reviewer_ref": "worker-human-researcher",
      "reason": "Human judgment required before high-risk continuation."
    }
  ],
  "created_at": "2026-06-24T09:01:00Z",
  "request_limits": {
    "max_pending_requests": 3,
    "max_repeated_denials": 1,
    "default_expiry_seconds": 1800
  }
}
```

## WorkSession

Conformance gate:
[WorkSession Gate](../conformance/checklist.md#worksession-gate)

```json
{
  "id": "work-session-research-001",
  "protocol_version": "v0.1",
  "created_by_actor_id": "actor-human-reviewer",
  "objective": "Produce an evidence-backed protocol comparison note.",
  "human_worker_id": "worker-human-researcher",
  "agent_worker_id": "worker-agent-research",
  "policy_id": "policy-research-001",
  "status": "active",
  "revision": 0,
  "last_event_hash": "hash:protocol-genesis",
  "event_log_ref": "event-log:work-session-research-001",
  "created_at": "2026-06-24T09:02:00Z",
  "updated_at": "2026-06-24T09:02:00Z",
  "context_manifest_ref": "context:research-note-inputs"
}
```

Terminal WorkSession snapshot before EvidenceManifest export:

```json
{
  "id": "work-session-research-001",
  "protocol_version": "v0.1",
  "created_by_actor_id": "actor-human-reviewer",
  "objective": "Produce an evidence-backed protocol comparison note.",
  "human_worker_id": "worker-human-researcher",
  "agent_worker_id": "worker-agent-research",
  "policy_id": "policy-research-001",
  "status": "completed",
  "revision": 14,
  "last_event_hash": "hash:event-work-session-completed-001",
  "event_log_ref": "event-log:work-session-research-001",
  "created_at": "2026-06-24T09:02:00Z",
  "updated_at": "2026-06-24T09:44:00Z",
  "context_manifest_ref": "context:research-note-inputs",
  "contribution_ledger_ref": "contribution-ledger:work-session-research-001",
  "learning_record_refs": [
    "learning-record-pair-001"
  ]
}
```

## JarvisEvent

Conformance gates:
[WorkSession Gate](../conformance/checklist.md#worksession-gate),
[EvidenceManifest Gate](../conformance/checklist.md#evidencemanifest-gate)

This file expands the first PolicyDecision event and the first accepted
AgentWorker action event. Later event refs identify records in the same
append-only event chain.

```json
{
  "id": "event-policy-decision-local-context-001",
  "sequence": 1,
  "type": "policy_decision.recorded",
  "work_session_id": "work-session-research-001",
  "actor_id": "actor-agent-research",
  "timestamp": "2026-06-24T09:04:00Z",
  "payload": {
    "object_type": "policy_decision",
    "object_id": "policy-decision-local-context-001",
    "action": "record_policy_decision",
    "field_refs": [
      "policy:policy-research-001",
      "work_session:work-session-research-001"
    ],
    "summary": "PolicyDecision recorded allow result for local context inspection."
  },
  "previous_hash": "hash:protocol-genesis",
  "event_hash": "hash:event-policy-decision-local-context-001",
  "canonicalization": {
    "serialization": "json-c14n",
    "hash_method": "sha-256",
    "profile_ref": "canonicalization:jarvis-v01"
  }
}
```

```json
{
  "id": "event-local-context-read-001",
  "sequence": 2,
  "type": "agent.action.accepted",
  "work_session_id": "work-session-research-001",
  "actor_id": "actor-agent-research",
  "timestamp": "2026-06-24T09:05:00Z",
  "payload": {
    "object_type": "jarvis_event",
    "object_id": "event-local-context-read-001",
    "action": "inspect_local_context",
    "field_refs": [
      "policy_decision:policy-decision-local-context-001",
      "work_session.objective",
      "policy.allowed_actions"
    ],
    "evidence_refs": [
      "evidence-item-local-context-001"
    ],
    "summary": "AgentWorker inspected allowed local protocol context."
  },
  "previous_hash": "hash:event-policy-decision-local-context-001",
  "event_hash": "hash:event-local-context-read-001",
  "canonicalization": {
    "serialization": "json-c14n",
    "hash_method": "sha-256",
    "profile_ref": "canonicalization:jarvis-v01"
  }
}
```

Event chain index:

| Sequence | Revision After Event | Event Ref | Previous Hash | Event Hash | Protocol Record |
| --- | ---: | --- | --- | --- | --- |
| 1 | 1 | `event-policy-decision-local-context-001` | `hash:protocol-genesis` | `hash:event-policy-decision-local-context-001` | `policy-decision-local-context-001` |
| 2 | 2 | `event-local-context-read-001` | `hash:event-policy-decision-local-context-001` | `hash:event-local-context-read-001` | `agent.action.accepted` |
| 3 | 3 | `event-policy-decision-external-source-001` | `hash:event-local-context-read-001` | `hash:event-policy-decision-external-source-001` | `policy-decision-external-source-001` |
| 4 | 4 | `event-request-external-source-001` | `hash:event-policy-decision-external-source-001` | `hash:event-request-external-source-001` | `request-external-source-001` |
| 5 | 5 | `event-review-external-source-001` | `hash:event-request-external-source-001` | `hash:event-review-external-source-001` | `review-external-source-001` |
| 6 | 6 | `event-approved-source-fetch-001` | `hash:event-review-external-source-001` | `hash:event-approved-source-fetch-001` | `agent.action.accepted` |
| 7 | 7 | `event-policy-decision-final-submission-001` | `hash:event-approved-source-fetch-001` | `hash:event-policy-decision-final-submission-001` | `policy-decision-final-submission-001` |
| 8 | 8 | `event-request-final-submission-001` | `hash:event-policy-decision-final-submission-001` | `hash:event-request-final-submission-001` | `request-final-submission-001` |
| 9 | 9 | `event-takeover-final-submission-001` | `hash:event-request-final-submission-001` | `hash:event-takeover-final-submission-001` | `takeover-final-submission-001` |
| 10 | 10 | `event-contribution-shared-research-note-001` | `hash:event-takeover-final-submission-001` | `hash:event-contribution-shared-research-note-001` | `contribution-shared-research-note-001` |
| 11 | 11 | `event-learning-record-pair-001` | `hash:event-contribution-shared-research-note-001` | `hash:event-learning-record-pair-001` | `learning-record-pair-001` |
| 12 | 12 | `event-memory-proposal-source-scope-001` | `hash:event-learning-record-pair-001` | `hash:event-memory-proposal-source-scope-001` | `memory-proposal-source-scope-001` |
| 13 | 13 | `event-skill-proposal-protocol-comparison-001` | `hash:event-memory-proposal-source-scope-001` | `hash:event-skill-proposal-protocol-comparison-001` | `skill-proposal-protocol-comparison-001` |
| 14 | 14 | `event-work-session-completed-001` | `hash:event-skill-proposal-protocol-comparison-001` | `hash:event-work-session-completed-001` | `work_session.completed` |

OutcomeReport acceptance uses `event-outcome-report-review-001` after export.
It does not mutate the sealed WorkSession or EvidenceManifest.

## PolicyDecision

Conformance gate:
[PolicyDecision Gate](../conformance/checklist.md#policydecision-gate)

Allowed action:

```json
{
  "id": "policy-decision-local-context-001",
  "work_session_id": "work-session-research-001",
  "actor_id": "actor-agent-research",
  "policy_id": "policy-research-001",
  "requested_action": {
    "action": "inspect_local_context",
    "target_ref": "context:research-note-inputs",
    "scope_ref": "scope:local-protocol-docs"
  },
  "normalized_action_hash": "hash:action-inspect-local-context",
  "risk_class": "low",
  "result": "allow",
  "reason": "Local context inspection is allowed by Policy.",
  "created_at": "2026-06-24T09:04:00Z",
  "selected_grant_refs": [
    "grant:local-read"
  ]
}
```

Review-required action:

```json
{
  "id": "policy-decision-external-source-001",
  "work_session_id": "work-session-research-001",
  "actor_id": "actor-agent-research",
  "policy_id": "policy-research-001",
  "requested_action": {
    "action": "fetch_external_source",
    "target_ref": "source:external-protocol-reference",
    "scope_ref": "scope:external-source"
  },
  "normalized_action_hash": "hash:action-fetch-external-source",
  "risk_class": "medium",
  "result": "review_required",
  "reason": "External source access requires HumanWorker review.",
  "created_at": "2026-06-24T09:08:00Z",
  "request_id": "request-external-source-001"
}
```

Final-submission review-required action:

```json
{
  "id": "policy-decision-final-submission-001",
  "work_session_id": "work-session-research-001",
  "actor_id": "actor-agent-research",
  "policy_id": "policy-research-001",
  "requested_action": {
    "action": "final_submission",
    "target_ref": "artifact:draft-protocol-comparison",
    "scope_ref": "scope:final-output"
  },
  "normalized_action_hash": "hash:action-final-submission",
  "risk_class": "high",
  "result": "review_required",
  "reason": "Final submission requires HumanWorker judgment.",
  "created_at": "2026-06-24T09:24:00Z",
  "request_id": "request-final-submission-001"
}
```

## Request

Conformance gate:
[Request Gate](../conformance/checklist.md#request-gate)

```json
{
  "id": "request-external-source-001",
  "protocol_version": "v0.1",
  "work_session_id": "work-session-research-001",
  "requester_actor_id": "actor-agent-research",
  "requester_worker_id": "worker-agent-research",
  "target_human_worker_id": "worker-human-researcher",
  "policy_decision_id": "policy-decision-external-source-001",
  "type": "permission",
  "blocking_scope": "tool_call",
  "reason_code": "review_required_external_source",
  "reason_summary": "External source access requires HumanWorker review.",
  "requested_action": {
    "action": "fetch_external_source",
    "target_ref": "source:external-protocol-reference",
    "scope_ref": "scope:external-source"
  },
  "requested_outcome": "Approve one external source fetch for this WorkSession.",
  "risk_class": "medium",
  "human_decision_needed": "Choose whether to approve, narrow, deny, or take over the source review.",
  "options": [
    {
      "id": "option-approve-source",
      "label": "Approve one source fetch",
      "effect": "AgentWorker fetches only the referenced source.",
      "risk_class": "medium",
      "scope_ref": "scope:external-source"
    },
    {
      "id": "option-deny-source",
      "label": "Deny external source fetch",
      "effect": "AgentWorker continues with local evidence only.",
      "risk_class": "low",
      "scope_ref": "scope:local-protocol-docs"
    }
  ],
  "default_if_no_response": {
    "action": "continue_with_limited_evidence",
    "reason": "No new authority is granted without HumanWorker review.",
    "limitation_ref": "limitation:no-external-source-review"
  },
  "status": "narrowed",
  "created_at": "2026-06-24T09:08:30Z",
  "expires_at": "2026-06-24T09:38:30Z",
  "recommended_option": "option-approve-source",
  "resolved_at": "2026-06-24T09:12:00Z",
  "resolved_by_review_id": "review-external-source-001"
}
```

Final-submission Request resolved through Takeover:

```json
{
  "id": "request-final-submission-001",
  "protocol_version": "v0.1",
  "work_session_id": "work-session-research-001",
  "requester_actor_id": "actor-agent-research",
  "requester_worker_id": "worker-agent-research",
  "target_human_worker_id": "worker-human-researcher",
  "policy_decision_id": "policy-decision-final-submission-001",
  "type": "takeover",
  "blocking_scope": "final_submission",
  "reason_code": "final_submission_requires_human_judgment",
  "reason_summary": "Final submission requires HumanWorker judgment.",
  "requested_action": {
    "action": "final_submission",
    "target_ref": "artifact:draft-protocol-comparison",
    "scope_ref": "scope:final-output"
  },
  "requested_outcome": "HumanWorker takes direct control of final submission judgment.",
  "risk_class": "high",
  "human_decision_needed": "Take over final submission or return the branch for revision.",
  "options": [
    {
      "id": "option-takeover-final-submission",
      "label": "Take over final submission",
      "effect": "HumanWorker controls final submission scope.",
      "risk_class": "high",
      "scope_ref": "scope:final-output"
    },
    {
      "id": "option-return-for-revision",
      "label": "Return for revision",
      "effect": "AgentWorker keeps final submission blocked and revises draft.",
      "risk_class": "medium",
      "scope_ref": "scope:final-output"
    }
  ],
  "default_if_no_response": {
    "action": "keep_blocked_scope_stopped",
    "reason": "Final submission requires HumanWorker judgment.",
    "limitation_ref": "limitation:final-submission-not-reviewed"
  },
  "status": "takeover",
  "created_at": "2026-06-24T09:24:30Z",
  "expires_at": "2026-06-24T09:54:30Z",
  "resolved_at": "2026-06-24T09:25:00Z",
  "resolved_by_takeover_id": "takeover-final-submission-001"
}
```

## Review And ApprovalScope

Conformance gate:
[Review And ApprovalScope Gate](../conformance/checklist.md#review-and-approvalscope-gate)

```json
{
  "id": "review-external-source-001",
  "work_session_id": "work-session-research-001",
  "reviewer_actor_id": "actor-human-reviewer",
  "reviewer_worker_id": "worker-human-researcher",
  "target_ref": "request:request-external-source-001",
  "decision": "narrow",
  "created_at": "2026-06-24T09:12:00Z",
  "comments": "Approved for the referenced source only.",
  "approval_scope": {
    "request_id": "request-external-source-001",
    "review_id": "review-external-source-001",
    "policy_decision_id": "policy-decision-external-source-001",
    "request_revision": 4,
    "request_event_hash": "hash:event-request-external-source-001",
    "normalized_action_hash": "hash:action-fetch-external-source",
    "approved_action": {
      "action": "fetch_external_source",
      "target_ref": "source:external-protocol-reference",
      "scope_ref": "scope:external-source"
    },
    "allowed_scope": {
      "scope_ref": "scope:single-approved-source",
      "grant_refs": [
        "grant:external-source-single-use"
      ],
      "constraint_refs": [
        "constraint:no-credential-access"
      ]
    },
    "denied_scope": {
      "scope_ref": "scope:all-other-external-sends",
      "grant_refs": [],
      "constraint_refs": [
        "constraint:deny-credentials",
        "constraint:deny-unapproved-domains"
      ]
    },
    "expires_at": "2026-06-24T09:42:00Z",
    "max_uses": 1,
    "applies_to_work_session_id": "work-session-research-001",
    "applies_to_actor_id": "actor-agent-research"
  }
}
```

## Takeover

Conformance gate:
[Takeover Gate](../conformance/checklist.md#takeover-gate)

The Takeover resolves request-final-submission-001.

```json
{
  "id": "takeover-final-submission-001",
  "work_session_id": "work-session-research-001",
  "requested_by_actor_id": "actor-agent-research",
  "controlling_actor_id": "actor-human-reviewer",
  "request_id": "request-final-submission-001",
  "affected_scope": {
    "blocking_scope": "final_submission",
    "scope_ref": "scope:final-output",
    "normalized_action_hash": "hash:action-final-submission",
    "artifact_refs": [
      "artifact:draft-protocol-comparison"
    ]
  },
  "reason": "HumanWorker takes direct control over final submission judgment.",
  "lock_epoch": 2,
  "state": "resumed",
  "created_at": "2026-06-24T09:25:00Z",
  "resumed_by_actor_id": "actor-human-reviewer",
  "reconciliation_notes": "HumanWorker revised final claim and returned formatting to AgentWorker.",
  "reconciliation_refs": [
    "ref:takeover-final-submission-reconciliation"
  ],
  "resolved_at": "2026-06-24T09:32:00Z"
}
```

## Contribution

Conformance gate:
[Contribution Gate](../conformance/checklist.md#contribution-gate)

```json
{
  "id": "contribution-shared-research-note-001",
  "work_session_id": "work-session-research-001",
  "contributor_refs": [
    {
      "worker_id": "worker-human-researcher",
      "actor_id": "actor-human-reviewer",
      "contribution_role": "human"
    },
    {
      "worker_id": "worker-agent-research",
      "actor_id": "actor-agent-research",
      "contribution_role": "agent"
    }
  ],
  "contributor_type": "shared",
  "contribution_type": "artifact",
  "event_refs": [
    "event-policy-decision-local-context-001",
    "event-local-context-read-001",
    "event-policy-decision-external-source-001",
    "event-request-external-source-001",
    "event-review-external-source-001",
    "event-approved-source-fetch-001",
    "event-policy-decision-final-submission-001",
    "event-request-final-submission-001",
    "event-takeover-final-submission-001"
  ],
  "created_at": "2026-06-24T09:40:00Z",
  "artifact_refs": [
    "artifact:protocol-comparison-note"
  ],
  "review_refs": [
    "review-external-source-001"
  ],
  "evidence_refs": [
    "evidence-item-local-context-001",
    "evidence-item-approved-source-001"
  ],
  "confidence": 0.92,
  "limitations": [
    "limitation:no-unapproved-external-sources"
  ]
}
```

## EvidenceManifest

Conformance gate:
[EvidenceManifest Gate](../conformance/checklist.md#evidencemanifest-gate)

EvidenceManifest export happens after terminal WorkSession state.

```json
{
  "id": "evidence-manifest-research-001",
  "work_session_id": "work-session-research-001",
  "generated_by_actor_id": "actor-human-reviewer",
  "objective": "Produce an evidence-backed protocol comparison note.",
  "event_chain_root": "hash:event-chain-root-research-001",
  "evidence_item_refs": [
    {
      "id": "evidence-item-local-context-001",
      "work_session_id": "work-session-research-001",
      "source_event_refs": [
        "event-local-context-read-001"
      ],
      "captured_by_actor_id": "actor-agent-research",
      "evidence_type": "local_context_summary",
      "artifact_ref": "artifact:local-context-summary",
      "content_hash": "hash:evidence-local-context",
      "trust_label": "self_attested_protocol_ref",
      "redaction_state": "redacted",
      "captured_at": "2026-06-24T09:05:30Z",
      "limitation_refs": []
    },
    {
      "id": "evidence-item-approved-source-001",
      "work_session_id": "work-session-research-001",
      "source_event_refs": [
        "event-approved-source-fetch-001"
      ],
      "captured_by_actor_id": "actor-agent-research",
      "evidence_type": "approved_external_source_summary",
      "artifact_ref": "artifact:approved-source-summary",
      "content_hash": "hash:evidence-approved-source",
      "trust_label": "human_reviewed_source",
      "redaction_state": "redacted",
      "captured_at": "2026-06-24T09:16:00Z",
      "limitation_refs": [
        "limitation:single-source-scope"
      ]
    }
  ],
  "policy_decision_refs": [
    "policy-decision-local-context-001",
    "policy-decision-external-source-001",
    "policy-decision-final-submission-001"
  ],
  "request_refs": [
    "request-external-source-001",
    "request-final-submission-001"
  ],
  "review_refs": [
    "review-external-source-001"
  ],
  "takeover_refs": [
    "takeover-final-submission-001"
  ],
  "contribution_refs": [
    "contribution-shared-research-note-001"
  ],
  "export_profile": {
    "profile": "portable-redacted-v01",
    "version": "v0.1",
    "redaction_profile_ref": "redaction:public-safe"
  },
  "generated_at": "2026-06-24T09:45:00Z",
  "artifact_refs": [
    "artifact:protocol-comparison-note"
  ],
  "limitation_refs": [
    "limitation:single-source-scope"
  ],
  "redaction_refs": [
    "redaction:public-safe"
  ]
}
```

## LearningRecord

Conformance gate:
[Learning Gate](../conformance/checklist.md#learning-gate)

```json
{
  "id": "learning-record-pair-001",
  "work_session_id": "work-session-research-001",
  "created_by_actor_id": "actor-human-reviewer",
  "subject_type": "pair",
  "subject_ref": "pair:human-researcher-agent-research",
  "lesson_type": "collaboration_pattern",
  "source_event_refs": [
    "event-review-external-source-001",
    "event-takeover-final-submission-001",
    "event-approved-source-fetch-001"
  ],
  "review_state": "accepted",
  "scope": "scope:future-protocol-comparison-work",
  "created_at": "2026-06-24T09:41:00Z",
  "proposed_change": {
    "summary": "Start future comparison tasks by defining source scope and final-submission review boundaries."
  },
  "memory_proposal_refs": [
    "memory-proposal-source-scope-001"
  ],
  "skill_proposal_refs": [
    "skill-proposal-protocol-comparison-001"
  ]
}
```

OutcomeReport-backed learning:

```json
{
  "id": "learning-record-outcome-001",
  "work_session_id": "work-session-research-001",
  "created_by_actor_id": "actor-human-reviewer",
  "subject_type": "pair",
  "subject_ref": "pair:human-researcher-agent-research",
  "lesson_type": "post_session_feedback",
  "source_event_refs": [
    "event-outcome-report-review-001"
  ],
  "review_state": "accepted",
  "scope": "scope:future-protocol-comparison-work",
  "created_at": "2026-06-24T10:31:00Z",
  "proposed_change": {
    "summary": "Carry post-session feedback into the next comparison WorkSession."
  },
  "outcome_report_refs": [
    "outcome-report-review-001"
  ]
}
```

## MemoryProposal

Conformance gate:
[MemoryProposal Gate](../conformance/checklist.md#memoryproposal-gate)

```json
{
  "id": "memory-proposal-source-scope-001",
  "work_session_id": "work-session-research-001",
  "proposed_by_actor_id": "actor-agent-research",
  "proposed_for": "pair",
  "memory_scope": "scope:future-protocol-comparison-work",
  "memory_type": "human_preference",
  "content": {
    "preference": "Ask for source scope before external-source research."
  },
  "provenance": [
    "event-review-external-source-001",
    "learning-record-pair-001"
  ],
  "confidence": 0.87,
  "review_required": true,
  "status": "pending_review",
  "created_at": "2026-06-24T09:42:00Z",
  "source_event_refs": [
    "event-review-external-source-001"
  ],
  "learning_record_refs": [
    "learning-record-pair-001"
  ]
}
```

## SkillProposal

Conformance gate:
[SkillProposal Gate](../conformance/checklist.md#skillproposal-gate)

```json
{
  "id": "skill-proposal-protocol-comparison-001",
  "work_session_id": "work-session-research-001",
  "proposed_by_actor_id": "actor-agent-research",
  "proposed_for": "pair",
  "skill_scope": "scope:future-protocol-comparison-work",
  "skill_name": "protocol_comparison_workflow",
  "trigger_conditions": [
    "WorkSession objective asks for protocol comparison",
    "HumanWorker requires evidence-backed boundary analysis"
  ],
  "procedure": [
    "List the compared protocol purpose.",
    "Map its objects and operations.",
    "Separate Jarvis-owned records from host-owned behavior.",
    "Create Request before any review-required external-source use.",
    "Record EvidenceManifest and LearningRecord before closure."
  ],
  "review_checks": [
    "No host runtime behavior becomes Jarvis-owned.",
    "Every claim links to evidence refs.",
    "Learning stays governed through proposals."
  ],
  "failure_cases": [
    "Protocol comparison turns into product comparison.",
    "External source use lacks Request and Review.",
    "Skill attempts to expand tool access without policy review."
  ],
  "provenance": [
    "event-review-external-source-001",
    "learning-record-pair-001"
  ],
  "status": "pending_review",
  "created_at": "2026-06-24T09:43:00Z",
  "required_tools": [
    "capability:local-context-read"
  ],
  "source_event_refs": [
    "event-review-external-source-001",
    "event-takeover-final-submission-001"
  ],
  "learning_record_refs": [
    "learning-record-pair-001"
  ]
}
```

## OutcomeReport

Conformance gate:
[OutcomeReport Gate](../conformance/checklist.md#outcomereport-gate)

```json
{
  "id": "outcome-report-review-001",
  "work_session_id": "work-session-research-001",
  "source_ref": "source:post-session-review",
  "reporter_ref": "reporter:human-reviewer",
  "accepted_by_actor_id": "actor-human-reviewer",
  "outcome": "needs_revision",
  "learning_record_refs": [
    "learning-record-outcome-001"
  ],
  "received_at": "2026-06-24T10:30:00Z",
  "external_system_ref": "system:review-channel",
  "reporter_actor_id": "actor-human-reviewer",
  "reason": "Future WorkSessions need source-scope review before external research.",
  "reviewer_feedback_refs": [
    "feedback:source-scope-before-research"
  ]
}
```

OutcomeReport does not mutate the sealed WorkSession or EvidenceManifest. It
creates or references LearningRecord so future WorkSessions inherit governed
learning.

## Required Record Order

Compatible implementations preserve this order:

```txt
1. Worker records exist.
2. Actor records exist.
3. HumanWorker and AgentWorker records bind Worker to Actor.
4. Policy exists before WorkSession starts.
5. WorkSession starts with objective, Policy, revision, and event hash state.
6. AgentWorker action records PolicyDecision before accepted protocol state.
7. Blocked action creates Request.
8. Review or Takeover resolves blocked scope.
9. ApprovalScope bounds narrowed authority.
10. Contribution records who did what.
11. EvidenceManifest exports portable proof.
12. LearningRecord records human, agent, or pair learning.
13. MemoryProposal and SkillProposal remain governed.
14. OutcomeReport carries post-session feedback without sealed record mutation.
```

The examples demonstrate records only. They do not require a specific host,
runtime, agent framework, UI, storage system, model provider, tool runner,
memory engine, or deployment platform.
