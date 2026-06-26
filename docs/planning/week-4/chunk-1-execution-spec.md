# Chunk 1: Week 4 Execution Spec

Chunk 1 locks the Week 4 working method before compatibility examples and
public docs start.

## Scope

This chunk defines:

- Week 4 goal
- Week 4 chunk sequence
- artifact ownership
- review lanes
- done gates
- local validation
- CodeRabbit gate

This chunk does not create compatibility examples, public checklist content,
record examples, README edits, simulation edits, adapter code, SDK code, or
runtime behavior.

## Required Artifacts

Chunk 1 creates:

```txt
docs/planning/week-4/README.md
docs/planning/week-4/chunk-1-execution-spec.md
docs/planning/week-4/chunk-2-compatible-host-mapping.md
docs/planning/week-4/chunk-3-existing-agent-example.md
docs/planning/week-4/chunk-4-public-conformance-checklist.md
docs/planning/week-4/chunk-5-protocol-record-examples.md
docs/planning/week-4/chunk-6-public-story-simulation.md
docs/planning/week-4/chunk-7-closeout.md
```

## Review Lanes

Every Week 4 implementation chunk requires these review lanes before PR ready:

```txt
protocol-boundary review
zero-trust security review
conformance and fixture review
existing-agent compatibility review
public-readability review
wording review
```

The protocol-boundary review verifies that Jarvis stays protocol-only.

The zero-trust security review verifies required headers, Actor authority,
WorkSession revision, previous event hash, forbidden export fields, and
host-private exclusion.

The conformance and fixture review verifies that examples match the OpenAPI
contract and the Week 3 fixture gates.

The existing-agent compatibility review verifies that examples preserve native
agent execution and never require a Jarvis-owned agent.

The public-readability review verifies that the public story explains Jarvis
without product-specific or host-specific assumptions.

The wording review verifies direct protocol language.

## Required Checks

Every Week 4 PR runs:

```txt
python3 scripts/check_conformance_fixtures.py
python3 scripts/check_openapi_contract.py
python3 scripts/check_markdown_links.py
python3 scripts/check_protocol_wording.py
git diff --check
```

Fixture or OpenAPI changes also require the relevant targeted validation from
the changed area.

## Week 4 Chunk Order

Week 4 work proceeds in this order:

```txt
1. execution spec
2. compatible host mapping
3. existing-agent example
4. public conformance checklist
5. protocol record examples
6. public story and simulation
7. closeout
```

Later chunks use earlier chunks as inputs. A chunk does not reopen previous
protocol locks unless a concrete contradiction blocks compatibility proof.

## Acceptance Gate

Chunk 1 is complete when:

- Week 4 directory exists
- all Week 4 chunk files exist
- each chunk has scope, output, boundary, review, and done criteria
- local checks pass
- internal reviewer lanes have no valid unresolved findings
- CodeRabbit has no valid unresolved findings
