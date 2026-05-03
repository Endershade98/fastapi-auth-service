# Architecture Overview

This project implements a **Domain-Driven Design (DDD)** architecture for an OAuth2 / Identity system.

## Key Principles

- Pure domain model (no framework dependency)
- Strong typing via Value Objects
- Aggregates enforce consistency boundaries
- Business rules isolated from state
- Domain Events for future event-driven evolution

## Layers

- Domain (core business logic)
- Application (use cases)
- Infrastructure (external systems)
- Interfaces (API layer)

## Design Goals

- Zero primitive obsession
- Fully testable domain layer
- Framework-agnostic core