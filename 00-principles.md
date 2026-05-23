# Principles

## One-Sentence Definition

Jarvis is the open-source harness where a human and an autonomous agent
collaborate, learn, and produce inspectable work through shared memory, tools,
policy, and evidence.

## Design From Collaboration, Not Chat

Chat is an interface. Jarvis is the underlying collaboration system.

A real human-agent work loop includes messages, tool calls, files, requests,
reviews, corrections, decisions, artifacts, and learning. Jarvis must model the
whole loop.

## Human And Agent Are Both First-Class

The human is not just a user. The human is:

- source of goals
- source of judgment
- source of domain knowledge
- reviewer
- teacher
- accountable actor

The agent is not just a chatbot. The agent is:

- autonomous worker
- memory-bearing collaborator
- tool executor
- context retriever
- draft producer
- evidence collector
- learner

Jarvis makes the relationship durable.

## Autonomy Through Policy

The agent does not need the human to approve every small step.

Instead, the human configures policy:

- what the agent can inspect
- what the agent can execute
- what the agent can change
- what the agent can send externally
- when the agent must ask
- when the human must review

Inside those boundaries, the agent proceeds.

## Memory Is Governed

Memory is not a dumping ground for transcripts.

Jarvis memory must be:

- scoped
- typed
- provenance-aware
- revisable
- retrievable
- governed by write policy

The model never mutates durable memory without policy.

## Skills Are Procedural Memory

Skills are reusable ways of working. They are more durable than prompts and
more specific than generic instructions.

A skill captures:

- when to use it
- how to do the work
- required context
- required tools
- examples
- failure cases
- review checks

## Requests Are A Control Plane

When the agent lacks permission, context, or judgment, it creates a request.

Requests are not interruptions only. They are the control plane for safe
autonomy. The human can respond immediately, later through an inbox, or by
taking over the work.

## Evidence Is Captured During Work

Jarvis records evidence as the collaboration happens:

- commands run
- tool outputs
- sources inspected
- files created
- decisions made
- human reviews
- corrections
- final artifacts

Evidence is not reconstructed at the end from memory.

## Runtime-Agnostic, Cloudflare-First

Jarvis kernel concepts do not require Cloudflare types.

The first real implementation uses Cloudflare deeply because it gives
Jarvis the runtime primitives needed for a serious agent harness.

## Non-Goals

Jarvis is not:

- a Cloudflare fork
- a product UI
- an external work ownership system
- an external identity system
- a chat-only assistant
- a runtime clone
- a workflow engine only

Jarvis integrates with many systems, but it owns the human-agent harness layer.
