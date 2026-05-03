# Domain Events

Events represent immutable facts that occurred in the system.

## Base Event

All events include:
- event_type
- version
- timestamp
- aggregate_id

## User Events
- UserRegistered
- UserLoggedIn

## Token Events
- TokenIssued
- TokenRotated

## Session Events
- SessionRevoked
- SessionCompromised

## Authorization Code Events
- AuthorizationCodeConsumed

## Versioning Strategy

Events are versioned to ensure backward compatibility:
- version defaults to 1
- future schema evolution supported
- backward-compatible transformations allowed