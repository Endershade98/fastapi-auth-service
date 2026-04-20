# Identity and Access Control Platform (OAuth2 / OpenID-style System)

## Overview

This project is a production-oriented Identity and Access Control Platform designed to manage authentication, authorization, session lifecycle, and security operations in a distributed microservices environment.

Rather than implementing a simple authentication service, the system is architected as a full Identity Provider, inspired by OAuth2 and OpenID Connect principles, with a strong focus on security, scalability, and event-driven consistency.

The platform addresses real-world challenges such as token revocation in stateless systems, distributed authentication across microservices, session lifecycle management, and secure authorization enforcement.

---

## Problem Statement

Modern microservice architectures require more than basic login functionality. Traditional JWT-based authentication introduces several limitations:

* Tokens are stateless and cannot be revoked easily
* Session management is inconsistent across distributed services
* Authorization logic becomes fragmented across microservices
* Security events (reuse attacks, compromise detection) are difficult to track
* Auditability and operational visibility are often missing

This project was designed to systematically solve these issues by evolving from a minimal authentication service into a fully event-driven identity control platform.

---

## Key Features

### Authentication and Session Management

* Secure login and logout mechanisms
* Password hashing using secure algorithms
* JWT issuance using RS256 asymmetric signing
* Refresh token rotation with reuse detection
* Stateful session management via TokenSession aggregate

### OAuth2 Authorization Flow

* Authorization Code Flow with PKCE support
* Secure client validation and redirect URI enforcement
* Short-lived authorization codes with single-use constraints
* Token exchange endpoint compliant with OAuth2 standards

### Authorization Model

* Role-Based Access Control (RBAC)
* Scope-based authorization aligned with OAuth principles
* Middleware-based enforcement across microservices
* Extensible policy engine for future ABAC integration

### Token Security and Lifecycle Management

* Token revocation system with distributed propagation
* Redis-based blacklist for real-time invalidation
* Key rotation mechanism for JWT signing keys (kid-based)
* JWKS endpoint for secure public key distribution

### Event-Driven Architecture

* Domain events for all security-critical operations
* Outbox pattern for reliable event persistence
* Redis Streams for asynchronous processing
* Consumers for audit logging, security monitoring, and blacklist updates

### Observability and Security Operations

* Full audit trail of authentication and authorization events
* Detection of token reuse and session compromise
* Security event classification and tracking
* Foundation for a real-time security operations dashboard

---

## Architecture

The system follows Clean Architecture and Domain-Driven Design principles:

* Domain Layer: Core business rules, aggregates, and domain events
* Application Layer: Use cases such as login, refresh, revoke, and authorization
* Infrastructure Layer: Database (MySQL), Redis, JWT services, event streaming
* Interface Layer: FastAPI-based REST APIs and future admin dashboard

The architecture is fully event-driven, enabling loose coupling between authentication, security processing, and observability components.

---

## Design Principles

* Stateless authentication enhanced with controlled state where necessary
* Strong separation of concerns using DDD boundaries
* Event-driven consistency for security and auditability
* Zero-trust approach for microservice communication
* Secure-by-design token lifecycle management
* Extensibility for enterprise-grade identity features

---

## Technologies

* Python (FastAPI)
* MySQL (persistent storage)
* Redis (caching, blacklist, event streams)
* JWT (RS256 asymmetric cryptography)
* Clean Architecture + Domain-Driven Design

---

## Architectural Outcome

The final system is not a simple authentication service but a distributed identity control platform capable of:

* Managing secure authentication at scale
* Enforcing authorization policies across services
* Handling token lifecycle and revocation reliably
* Providing real-time security observability
* Supporting event-driven security operations

---

## Purpose

This project was built as a problem-solving exercise focused on addressing real-world distributed system challenges in identity management. It demonstrates how an authentication system evolves into a full identity and security infrastructure when applied to microservice architectures with strict security and scalability requirements.
