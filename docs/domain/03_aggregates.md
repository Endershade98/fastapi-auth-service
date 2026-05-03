# Aggregates

Aggregates define transactional boundaries.

## User Aggregate
Handles:
- authentication state
- lifecycle transitions
- role assignment

## OAuthClient Aggregate
Handles:
- redirect URIs
- allowed scopes
- client activation/deactivation

## TokenSession Aggregate
Handles:
- session lifecycle
- refresh token rotation
- session revocation

## AuthorizationCode Aggregate
Handles:
- PKCE validation
- single-use enforcement