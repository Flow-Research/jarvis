# Architecture

Jarvis is the protocol for policy-governed collaboration and shared learning
between human workers and agent workers.

It defines how a human and an agent become a working team: shared goals,
policy, requests, review, takeover, contribution records, evidence, memory,
learning, and skills.

The architectural center is the HumanWorker + AgentWorker learning loop.
WorkSession is the durable record of that loop.

## Layer Model

```txt
Products and hosts
  product workspaces, task systems, CLI apps, chat apps, custom products

Jarvis protocol
  actors, workers, WorkSessions, policies, requests, reviews, takeover,
  contributions, evidence, learning records, memory proposals,
  skill proposals

External implementation choices
  models, tools, MCP servers, sandboxes, storage, queues, clouds,
  local machines, deployment platforms, product interfaces
```

Only the middle layer is Jarvis.

Products and hosts decide how to execute work. Jarvis defines the protocol
records and state transitions that make the work collaborative, governed,
reviewable, attributable, and portable.

Compatibility is the architecture goal. A HumanWorker, AgentWorker, product,
host, or external system should be able to participate without adopting another
system's execution stack or product model.

## Core Protocol Contracts

The canonical object definitions are in
[11-core-protocol-objects.md](./11-core-protocol-objects.md).

Architecture depends on these objects:

```txt
Worker
Actor
HumanWorker
AgentWorker
WorkSession
JarvisEvent
Policy
PolicyDecision
Request
Review
Takeover
Contribution
EvidenceManifest
LearningRecord
MemoryProposal
SkillProposal
```

The key architectural rule is direct: HumanWorker and AgentWorker collaborate
inside a WorkSession. Policy bounds autonomy. Request and Review keep human
judgment in the loop. Contribution and EvidenceManifest make the work
inspectable. LearningRecord, MemoryProposal, and SkillProposal make the next
WorkSession better.

## Standard Work Flow

```txt
1. HumanWorker defines intent.
2. Jarvis starts or resumes a WorkSession.
3. Policy defines the action boundary.
4. AgentWorker receives context, memory, skills, and available capabilities.
5. AgentWorker plans and executes inside policy.
6. Policy evaluates every meaningful action.
7. Missing permission, context, or judgment becomes a Request.
8. HumanWorker reviews, approves, denies, narrows, corrects, or takes over.
9. AgentWorker resumes when allowed.
10. Jarvis records events, contributions, and evidence.
11. Jarvis proposes memory, skill, and learning updates for the human, agent,
    and pair.
12. HumanWorker confirms or rejects governed learning.
13. EvidenceManifest exports.
14. The HumanWorker, AgentWorker, and next WorkSession start with confirmed
    improvements.
```

## Ownership Boundary

Jarvis owns:

- protocol contracts
- interoperability semantics
- conformance rules
- actor semantics
- worker semantics
- WorkSession lifecycle
- policy-governed autonomy
- request, review, and takeover semantics
- contribution records
- evidence manifests
- learning records
- memory proposal semantics
- skill proposal semantics
- context manifest semantics
- portable export semantics

Products and hosts own:

- user interface
- authentication and accounts
- execution environment
- model/provider selection
- tool execution
- sandboxing
- storage
- queues and scheduling
- deployment
- observability
- billing
- organization controls

## External System Boundary

External systems can start WorkSessions, consume EvidenceManifests, route
Reviews, evaluate Contributions, or provide context and skills. Jarvis defines
the protocol records exchanged with those systems. It does not define their
product architecture.

## Minimum Developer Entry Point

```txt
create HumanWorker
create AgentWorker
start WorkSession
attach Policy
attach tools, skills, and memory
send objective
observe events, requests, contributions, and evidence
review or take over when needed
complete WorkSession
inspect learning proposals
export EvidenceManifest
```

The developer entry point is protocol-first. Execution, hosting, storage, and
UI are implementation choices outside Jarvis.
