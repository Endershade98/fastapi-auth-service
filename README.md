# Identity and Access Control Platform

## Overview

This project implements a domain-driven Identity and Access Control Platform inspired by OAuth2 and OpenID Connect.

It is designed as a **stateless-first authentication system**, where state is introduced only when strictly necessary for security guarantees (sessions, refresh tokens, revocation).

The system addresses core challenges in distributed identity management:

- token revocation in stateless architectures
- refresh token rotation with reuse detection
- session lifecycle consistency across services
- secure authorization code flows (PKCE)
- event-driven security auditing

---

## Problem Statement

Modern microservice architectures require identity systems that go beyond simple JWT authentication.

Pure stateless JWT approaches introduce several limitations:

- no native token revocation mechanism
- inconsistent session tracking across services
- fragmented authorization logic
- limited observability on security-critical events
- weak support for attack detection (replay, reuse, compromise)

This system was designed to explicitly address these constraints by combining:
- controlled state (sessions, refresh tokens)
- event-driven security modeling
- strict domain boundaries (DDD)

---

## Architecture Overview

The system follows Clean Architecture and Domain-Driven Design principles:

### Layers

- **Domain Layer**
  - Aggregates, Value Objects, Domain Rules, Domain Events
  - No framework or infrastructure dependency

- **Application Layer**
  - Use cases (login, refresh, revoke, authorize)
  - Orchestration of domain logic

- **Infrastructure Layer**
  - MySQL persistence
  - Redis (caching, streams, blacklist)
  - JWT signing/verification (RS256)

- **Interface Layer**
  - FastAPI REST APIs

---

## Domain Model Highlights

The domain is structured around explicit consistency boundaries:

- **Strongly typed Value Objects**
  - eliminate primitive obsession
  - enforce validation at construction time

- **Aggregates**
  - User
  - OAuthClient
  - TokenSession
  - AuthorizationCode

Each aggregate enforces its own invariants and lifecycle rules.

- **Domain Rules Engine**
  - isolates business logic from state mutation
  - improves testability and clarity

- **Domain Events**
  - represent immutable facts
  - used for auditability and future event-driven workflows

---

## Design Decisions

### Why event-driven architecture?

Security-critical operations (authentication, token rotation, session revocation) are modeled as domain events to ensure:

- full auditability of identity actions
- decoupled security processing
- extensibility toward real-time security analytics
- future integration with monitoring and SIEM systems

---

### Why Redis Streams instead of Kafka?

Redis Streams were chosen to:
- reduce operational complexity
- support low-latency event processing
- enable replayable event consumption
- fit a single-region deployment model

Kafka is a valid future evolution path for multi-region scaling.

---

### Why RS256 JWT?

Asymmetric signing allows:

- independent verification by downstream services
- secure key rotation without service downtime
- separation between token issuer and consumers
- support for JWKS-based public key distribution

---

### Why refresh token rotation?

Refresh token rotation is used to mitigate replay attacks in stateless systems:

- each refresh token is single-use
- reuse detection triggers session invalidation
- prevents credential stuffing via stolen refresh tokens

---

## Security Model

The system follows a **zero-trust identity model**:

- Tokens are treated as untrusted until verified
- Refresh tokens are strictly single-use
- Sessions are explicitly stateful and revocable
- Authorization codes are single-use (PKCE enforced)

### Threats addressed:

- token replay attacks
- refresh token reuse
- session hijacking
- authorization code interception
- compromised session propagation

---

## Event-Driven Design

All security-critical actions emit domain events:

- UserRegistered
- UserLoggedIn
- TokenIssued
- TokenRotated
- SessionRevoked
- SessionCompromised
- AuthorizationCodeConsumed

### Event properties

- immutable
- versioned
- timestamped
- tied to aggregate identity

### Versioning strategy

Events are versioned to ensure backward compatibility:

- default version = 1
- backward-compatible evolution supported
- transformation layer enables schema upgrades

---

## Technologies

- Python 3.14
- FastAPI
- MySQL (persistent storage)
- Redis (caching + streams + blacklist)
- JWT (RS256 asymmetric cryptography)
- Pytest (domain-first testing strategy)

---

## Architectural Outcome

The system is not a simple authentication service.

It is an identity control platform capable of:

- enforcing secure authentication at scale
- managing distributed session consistency
- handling token lifecycle and revocation reliably
- providing full auditability of identity events
- supporting future event-driven security analytics systems

---

## Engineering Principles

- Domain-driven design with strict bounded contexts
- Strong typing via Value Objects
- Explicit invariants in aggregates
- Event-driven consistency for security operations
- Zero-trust authentication model
- Framework-independent domain layer

---

## Purpose

This project was built as a systems design exercise focused on real-world identity challenges in distributed architectures.

It demonstrates:

- how authentication evolves into identity infrastructure
- how state must be carefully reintroduced into stateless systems
- how domain modeling improves security correctness
- how event-driven design improves observability and auditability

---

## Notes for Reviewers

The design intentionally separates:
- authentication (identity verification)
- authorization (policy enforcement)
- session management (state tracking)
- security auditing (event-driven layer)

This separation is critical for scalability, security correctness, and long-term maintainability in distributed systems.