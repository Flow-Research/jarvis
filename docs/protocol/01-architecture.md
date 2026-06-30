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
Compatible hosts
  UI, auth, storage, execution, deployment, model calls, tool execution

Jarvis protocol
  actors, workers, WorkSessions, policies, requests, reviews, takeover,
  contributions, evidence, learning records, memory proposals,
  skill proposals

External implementation choices
  models, tools, external protocol servers, isolation, storage, queues,
  clouds, local machines, deployment platforms, interfaces
```

Only the middle layer is Jarvis.

Hosts decide how to execute work. Jarvis defines the protocol records and state
transitions that make the work collaborative, governed, reviewable,
attributable, and portable.

Compatibility is the architecture goal. A HumanWorker, AgentWorker, host, or
external system participates without adopting another system's execution stack
or host model.

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
OutcomeReport
```

Jarvis defines this architecture: HumanWorker and AgentWorker collaborate
inside a WorkSession. Policy bounds AgentWorker autonomy. Request, Review, and
Takeover record human judgment and resolution. Contribution records
attributable work. EvidenceManifest records portable evidence. LearningRecord,
MemoryProposal, and SkillProposal carry governed learning into future
WorkSessions. OutcomeReport carries post-session feedback without mutating
sealed WorkSession or EvidenceManifest records.

## Standard Work Flow

```txt
1. HumanWorker defines intent.
2. A compatible host starts or resumes a WorkSession using Jarvis protocol
   records.
3. Policy defines the action boundary.
4. AgentWorker receives context, memory, skills, and available capabilities.
5. AgentWorker plans and executes inside policy.
6. Policy evaluates every meaningful action.
7. Missing permission, context, or judgment becomes a Request.
8. HumanWorker reviews, approves, denies, narrows, corrects, or takes over.
9. AgentWorker resumes when allowed.
10. Events, contributions, and evidence are recorded as protocol records.
11. Memory, skill, and learning updates are proposed for the human, agent, and
    pair.
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

Hosts own:

- user interface
- authentication and accounts
- execution context
- model/provider selection
- tool execution
- isolation
- storage
- queues and scheduling
- deployment
- observability
- billing
- organization controls

## External System Boundary

External systems start WorkSessions, consume EvidenceManifests, route Reviews,
evaluate Contributions, or provide context and skills through Jarvis records.
Jarvis defines the protocol records exchanged with those systems. It does not
define their host architecture.

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
