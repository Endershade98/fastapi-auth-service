# Domain Model (EPIC 1)

This module defines the core identity system.

## Core Concepts

### User
Represents a system user with lifecycle states:
- ACTIVE
- LOCKED
- DISABLED

### OAuthClient
Represents an OAuth application with:
- redirect URI validation
- scope restrictions
- client lifecycle

### TokenSession
Represents authentication sessions:
- supports rotation
- supports revocation
- supports compromise detection

### AuthorizationCode
Implements OAuth authorization code flow with:
- PKCE support
- single-use enforcement