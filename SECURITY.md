# Security

Jarvis defines protocol security requirements. Hosts own implementation
security.

## Protocol Security Boundary

Jarvis owns:

- required protocol headers
- Actor identity references
- Actor authority checks
- WorkSession revision checks
- previous event hash checks
- idempotency requirements
- request timestamp requirements
- host-private export exclusions
- protocol error envelope

Hosts own:

- identity provider
- authentication backend
- authorization backend
- credential storage
- network security
- runtime isolation
- model execution
- tool execution
- storage security
- deployment security
- monitoring and incident response

## Reporting Security Issues

Report protocol security issues through a private maintainer channel until a
public security advisory process exists.

Do not open a public issue for a vulnerability that exposes credentials,
private keys, private records, or exploitable security details.

## Supported Security Scope

Current security support covers Jarvis v0.1 protocol text, OpenAPI binding,
conformance fixtures, validators, and public examples.

Jarvis v0.1 does not provide long-term support, implementation security
certification, host certification, or production-adoption guarantees.

## Required Security Checks

Every WorkSession-scoped mutating operation requires:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
Jarvis-Expected-WorkSession-Revision
Jarvis-Previous-Event-Hash
```

Every non-WorkSession protocol mutation requires:

```txt
Jarvis-Protocol-Version
Jarvis-Actor-Id
Jarvis-Idempotency-Key
Jarvis-Request-Timestamp
```

Every EvidenceManifest export excludes host-private fields, credentials,
secrets, raw runtime state, host-only database ids, deployment details, billing
data, private scores, UI state, raw auth tokens, provider secrets, session
cookies, and private keys.

