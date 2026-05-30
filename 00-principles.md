# Principles

## Official Definition

Jarvis is the human-agent collaboration protocol. It defines how human workers
and agent workers coordinate under shared goals and human-defined policy, so
they can complete work together, review each other, record contributions,
capture evidence, and learn across WorkSessions.

## One-Line Definition

Jarvis is the open protocol that lets human workers and agent workers
collaborate under shared goals and policy, producing durable WorkSessions,
reviewable Requests, attributable Contributions, governed Learning, and
portable Evidence.

## Simple Definition

Jarvis is how humans and agents work together.

The human does not just prompt. The agent does not just answer. Both participate
in the work.

## Design From Collaboration, Not Chat

Chat is only one interface. Jarvis is the protocol underneath human-agent work.

A real human-agent work loop includes messages, tool calls, files, requests,
reviews, corrections, decisions, artifacts, contributions, evidence, and
learning. Jarvis models the whole loop.

## HumanWorker And AgentWorker Are First-Class

Jarvis does not model `User + Assistant`.

Jarvis models `HumanWorker + AgentWorker`.

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
unit is the human-agent team.

Jarvis exists to formalize the loop where the human improves the agent, the
agent improves the human's leverage, and completed WorkSessions improve the
next WorkSession.

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
- what did the pair learn?
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

## Runtime-Agnostic, Cloudflare-First

Jarvis protocol semantics do not require any cloud, model provider, sandbox,
database, queue, or runtime.

Cloudflare remains a first-class implementation substrate because it provides
strong primitives for durable agents. Cloudflare is an implementation path, not
the public identity of Jarvis.

## Protocol Laws

1. Jarvis is not a product.
2. Jarvis is not a personal agent.
3. Jarvis does not prescribe infrastructure.
4. WorkSession is the source of truth.
5. Policy governs autonomy.
6. Learning is governed.
7. Evidence is captured during work.
8. Contributions are attributable.
9. Human judgment remains central.
10. Every session should improve the next session.

## Non-Goals

Jarvis is not:

- Garden
- Workstream
- Harnessy
- a Cloudflare fork
- a product UI
- a personal agent application
- a chatbot
- a runtime clone
- a model provider
- a sandbox implementation
- a database implementation
- a workflow engine only
- an external identity system
- an external work ownership system

Jarvis integrates with many systems, but it owns the human-agent collaboration
protocol.
