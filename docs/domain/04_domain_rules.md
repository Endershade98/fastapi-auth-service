# Domain Rules Engine

Business rules are isolated from aggregates.

## Password Rules
- verification delegated to PasswordHash VO
- no raw password comparison in domain

## User Rules
- only ACTIVE users can login
- DISABLED users are permanently blocked
- LOCKED users are temporarily blocked

## Session Rules
- ACTIVE sessions are valid
- COMPROMISED sessions are invalid
- REVOKED sessions are invalid

## Token Rules
- refresh tokens are single-use
- reuse is strictly forbidden

## Authorization Code Rules
- codes are single-use
- consumed codes are invalid