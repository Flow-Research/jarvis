# Principles

## Official Definition

Jarvis is the human-agent collaboration and learning-loop protocol. It defines
how human workers and agent workers coordinate under shared goals and
human-defined policy, so they can complete work together, review each other,
record contributions, capture evidence, and both improve across WorkSessions.

## One-Line Definition

Jarvis is the open protocol that lets HumanWorkers and AgentWorkers collaborate
under shared goals and policy, producing durable WorkSessions, reviewable
Requests, attributable Contributions, governed shared Learning, and portable
Evidence.

## Simple Definition

Jarvis is how humans and agents work together.

The human does not just prompt. The agent does not just answer. Both participate
in the work.

Jarvis is a compatibility protocol, not one user's workflow. Any product,
host, human worker, agent worker, or external system can implement the
contracts and participate in the same collaboration loop.

## Design From Collaboration, Not Chat

Chat is only one interface. Jarvis is the protocol underneath human-agent work.

A real human-agent work loop includes messages, tool calls, files, requests,
reviews, corrections, decisions, artifacts, contributions, evidence, and
learning. Jarvis models the whole loop.

## HumanWorker And AgentWorker Are First-Class

Jarvis does not model `User + Assistant`.

Jarvis models `HumanWorker + AgentWorker`.

Both are workers. Both are actors. Both contribute to the WorkSession. Both can
learn from the loop.

The human is:

- goal setter
- domain expert
- reviewer
- teacher
- quality judge
- policy owner
- accountable actor
- source of taste
- source of world context

The agent is:

- autonomous worker
- executor
- researcher
- context retriever
- tool user
- draft producer
- evidence collector
- learning participant

Jarvis makes the working relationship durable, governed, reviewable, and able
to improve over time.

## The Winning Unit Is The Team

The winning unit is not the human alone and not the agent alone. The winning
unit is the human-agent team that learns together.

Jarvis exists to formalize the loop where the human improves, the agent
improves, the relationship improves, and completed WorkSessions improve the
next WorkSession.

The protocol makes the loop portable across agents, products, hosts, and task
systems.

## Jarvis Is About The Shared Learning Loop

The industry usually starts with agent-centric questions:

- how do agents get smarter?
- how do agents become autonomous?
- how do agents use tools?
- how do agents execute tasks?

Jarvis starts from a different loop:

```txt
HumanWorker and AgentWorker collaborate.
HumanWorker reviews, corrects, approves, or takes over.
AgentWorker executes, proposes, adapts, and records evidence.
Both workers learn.
The next WorkSession improves.
```

The WorkSession is central because it is the protocol record of that
collaboration and learning loop.

## WorkSession Is The Source Of Truth

A WorkSession is not chat history.

A WorkSession is the durable record of real collaboration:

- objective
- human worker
- agent worker
- policy
- available capabilities
- context
- events
- requests
- reviews
- tool actions
- artifacts
- contributions
- evidence
- learning proposals
- final outcome

Every meaningful collaboration happens inside a WorkSession.

## Autonomy Through Policy

The agent does not need the human to approve every small step.

The human defines policy:

- what the agent can inspect
- what the agent can execute
- what the agent can change
- what the agent can send externally
- when the agent must ask
- when the human must review

Inside policy, the agent proceeds. Outside policy, it creates a Request.

## Requests Are The Control Plane

When the agent lacks permission, context, or judgment, it creates a Request.

Requests are structured protocol objects, not vague interruptions. A human can
approve, deny, narrow, correct, answer, or take over.

## Reviews Teach The System

Human review is not only quality control. Human review is teaching material.

Jarvis records reviews as protocol events that can become memory proposals,
skill proposals, policy improvements, and better future behavior.

## Contributions Are Attributable

Jarvis records who did what.

Human, agent, service, tool, and shared contributions must remain
distinguishable. The record must not collapse the work into "the agent did it"
or "the human did it."

## Accountability Remains Attributable

Execution can be delegated. Accountability cannot disappear.

The agent may execute, research, draft, automate, and collect evidence. The
human remains an accountable actor for judgment, policy, review, and final
tradeoffs. Jarvis records enough contribution and evidence for accountability
to remain inspectable.

## Evidence Is Captured During Work

Evidence is produced as collaboration happens:

- commands run
- tool outputs
- sources inspected
- files created
- decisions made
- policy decisions
- requests
- human reviews
- corrections
- final artifacts

Evidence is not reconstructed at the end from memory.

## Learning Is Governed

Jarvis does not silently mutate durable memory.

Learning must be proposed, reviewed, scoped, and accepted. Jarvis asks:

- what did the human learn?
- what did the agent learn?
- what did the human-agent pair learn?
- what should improve next time?

## Skills Are Procedural Memory

Skills are reusable ways of working. They are more durable than prompts and
more specific than generic instructions.

A SkillProposal captures:

- when to use it
- how to do the work
- required tools
- review checks
- failure cases
- provenance
- review state

## Infrastructure Is Outside Jarvis

Jarvis protocol semantics do not require any cloud, model provider, sandbox,
database, queue, deployment platform, or execution stack.

Products decide how to run agents, where to store data, which sandbox to use,
which model to call, and which infrastructure to deploy on. Jarvis defines the
collaboration and learning-loop protocol those systems implement.

## Protocol Laws

1. Jarvis defines human-agent collaboration and shared learning.
2. Jarvis is a compatibility protocol.
3. WorkSession is the source of truth.
4. Jarvis does not prescribe infrastructure or execution.
5. Policy governs autonomy.
6. Learning is governed.
7. Evidence is captured during work.
8. Contributions are attributable.
9. Human judgment remains central.
10. Execution may be delegated; accountability remains attributable.
11. HumanWorker and AgentWorker both learn.
12. Every session should improve the next session.

## Non-Goals

Jarvis is not:

- a product UI
- a model provider
- a sandbox implementation
- a database implementation
- a workflow engine only
- an external identity system
- an external work ownership system

Jarvis integrates with many systems, but it owns the human-agent collaboration
and learning-loop protocol.
