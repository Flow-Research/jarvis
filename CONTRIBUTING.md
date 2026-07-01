# Contributing

Jarvis accepts contributions that strengthen the human-agent collaboration and
learning-loop protocol.

## Contribution Scope

Accepted contribution scope:

- protocol object definitions
- lifecycle rules
- OpenAPI 3.1 communication binding
- protocol error definitions
- conformance fixtures
- conformance validators
- compatible protocol examples
- public protocol documentation
- release-readiness documentation

Rejected contribution scope:

- host runtime implementation
- agent framework implementation
- model orchestration
- tool execution
- storage backend
- auth provider
- billing system
- scoring system
- payment system
- deployment stack
- adapter or wrapper code in this repository

## Required Local Checks

Every protocol PR MUST run:

```txt
python3 scripts/check_conformance_fixtures.py
python3 scripts/check_openapi_contract.py
python3 scripts/check_markdown_links.py
python3 scripts/check_protocol_wording.py
git diff --check
```

Fixture changes MUST run:

```txt
python3 scripts/check_conformance_fixtures.py
```

Demo JavaScript changes MUST run:

```txt
node --check demo/assets/app.js
```

## Pull Request Requirements

Every PR MUST state:

- protocol surface changed
- reason for the change
- compatibility impact
- conformance impact
- validation commands run

Every PR MUST keep Jarvis protocol-only. Hosts own implementation details.

## Wording Requirement

Use direct protocol language:

```txt
Jarvis defines...
Hosts own...
Compatible implementations MUST...
The protocol rejects...
```

Soft protocol wording is a defect. The wording guard enforces this rule.

## Compatibility Requirement

Existing agents remain first-class. A compatible implementation emits Jarvis
protocol records without rewriting the agent as a Jarvis-owned agent.

