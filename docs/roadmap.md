# EPIC 1 – Core Domain Model (Identity Kernel)
Obiettivo: modellare il dominio puro, indipendente da infrastruttura

---

## Feature 1.1 – Value Objects

### Tasks

* Email (validation + normalization)
* PasswordHash (argon2/bcrypt abstraction)
* UserId / ClientId / SessionId (strong typing)
* Scope (OAuth scope parsing + validation)
* TokenId / JTI wrapper
* RedirectUri validation object

---

## Feature 1.2 – Aggregates Core

### Tasks

* User Aggregate (status, credentials, lifecycle)
* OAuthClient Aggregate (client config, secrets, redirect URIs)
* TokenSession Aggregate (session lifecycle + refresh rotation)
* AuthorizationCode Aggregate (PKCE support)

---

## Feature 1.3 – Domain Rules Engine

### Tasks

* Password verification rules (delegated to VO)
* User status lifecycle (ACTIVE / LOCKED / DISABLED)
* Session state machine (ACTIVE / COMPROMISED / REVOKED / EXPIRED)
* Refresh token one-time-use rule
* Authorization code single-use rule

---

## Feature 1.4 – Domain Events (NEW - fondamentale)

### Tasks

* Define base DomainEvent
* UserRegistered / UserLoggedIn
* TokenIssued / TokenRotated
* SessionCompromised / SessionRevoked
* AuthorizationCodeConsumed
* Event versioning strategy

---

# EPIC 2 – Authentication & Session Lifecycle (Application Layer)
Obiettivo: casi d’uso di login e session management

---

## Feature 2.1 – Login Use Case

### Tasks

* Input DTO validation
* Fetch User aggregate
* Verify password (domain rule)
* Create TokenSession
* Emit events (UserLoggedIn, SessionCreated)
* Return access + refresh token DTO

---

## Feature 2.2 – Refresh Token Use Case (CRITICO)

### Tasks

* Parse refresh token (token_id.secret)
* Load TokenSession
* Validate session state
* Verify refresh token hash
* Rotate refresh token
* Detect reuse attack → SessionCompromised event
* Issue new access token (JWT RS256)
* Persist session
* Emit events

---

## Feature 2.3 – Logout Use Case

### Tasks

* Load session from token
* Revoke session aggregate
* Emit SessionRevoked event
* Add token to blacklist (via outbox)
* Persist state

---

## Feature 2.4 – Session Introspection Use Case (NEW)

### Tasks

* Fetch session by token
* Return session status
* Show device + metadata
* Used by admin dashboard

---

# EPIC 3 – OAuth2 Authorization Flow
Obiettivo: Authorization Code + PKCE

---

## Feature 3.1 – Authorization Request

### Tasks

* Validate client_id
* Validate redirect_uri
* Validate scopes
* Generate AuthorizationCode
* Store PKCE challenge
* Emit AuthorizationCodeIssued event

---

## Feature 3.2 – Token Exchange (/oauth/token)

### Tasks

* Validate authorization code
* Verify PKCE
* Mark code as used
* Create TokenSession
* Issue JWT + refresh token
* Emit TokenIssued event

---

# EPIC 4 – Token Management & Security Layer
Obiettivo: sicurezza reale post-issuance

---

## Feature 4.1 – JWT Service (RS256)

### Tasks

* Key management (kid support)
* Token issuance
* Claims standardization (iss, aud, exp, scope)
* Signing strategy

---

## Feature 4.2 – JWKS Endpoint

### Tasks

* Expose /.well-known/jwks.json
* Key rotation support
* Cache strategy

---

## Feature 4.3 – Token Revocation System

### Tasks

* /oauth/revoke endpoint
* Token blacklist (Redis)
* Session revoke propagation
* Event emission

---

## Feature 4.4 – Key Rotation System

### Tasks

* Active/old key management
* Rotate keys without downtime
* Maintain backward compatibility
* Propagate JWKS updates

---

# EPIC 5 – Event-Driven Architecture (Core Infra)
Obiettivo: decoupling e scalabilità

---

## Feature 5.1 – Outbox Pattern

### Tasks

* Outbox table design
* Transactional event saving
* Worker implementation

---

## Feature 5.2 – Redis Streams Event Bus

### Tasks

* Stream definition (auth.events, auth.revoke)
* Consumer groups
* Retry mechanism
* ACK management

---

## Feature 5.3 – Event Consumers

### Tasks

* Audit Consumer
* Security Consumer
* Analytics Consumer
* Blacklist Consumer

---

## Feature 5.4 – Idempotency Layer

### Tasks

* Event deduplication
* Processing tracking
* Replay safety

---

# EPIC 6 – Authorization Layer (RBAC / Policies)
Obiettivo: controllo accessi

---

## Feature 6.1 – RBAC Engine

### Tasks

* Role → Permission mapping
* PolicyEngine implementation
* Admin role override

---

## Feature 6.2 – Middleware Enforcement

### Tasks

* FastAPI RBAC middleware
* require_permission decorator
* Scope validation layer

---

## Feature 6.3 – Advanced Policies (future ABAC-ready)

### Tasks

* Context-aware rules (user, device, IP)
* Policy abstraction layer

---

# EPIC 7 – Observability & Security Operations

🎯 Obiettivo: dashboard + controllo umano

---

## Feature 7.1 – Audit System

### Tasks

* Event persistence
* Audit log schema
* Query API

---

## Feature 7.2 – Security Events System

### Tasks

* TokenReuseDetected tracking
* SessionCompromised alerts
* Incident classification

---

## Feature 7.3 – Admin Dashboard APIs

### Tasks

* session listing endpoint
* revoke session API
* user management APIs
* OAuth client management APIs

---

## Feature 7.4 – Event Stream API (real-time)

### Tasks

* WebSocket endpoint
* Redis Streams → frontend bridge
* live security feed

---

# DIFFERENZA CHIAVE RISPETTO ALLA TUA VERSIONE

## Prima

* login / refresh / logout
* entità isolate
* focus CRUD

---

## ✅ Ora

* sistema event-driven
* session lifecycle completo
* security reactive
* OAuth2 real implementation
* distributed architecture
* control plane + data plane separati

---

# 🧭 MAPPATURA DDD (IMPORTANTE)

| Layer          | Contenuto                   |
| -------------- | --------------------------- |
| Domain         | Aggregates + Rules + Events |
| Application    | Use Cases                   |
| Infrastructure | DB, Redis, JWT, Streams     |
| Interface      | FastAPI + Dashboard         |

---

# 🚀 OUTPUT FINALE

Ora hai:

✔ backlog enterprise-grade
✔ separazione DDD reale
✔ event-driven design integrato
✔ roadmap per Identity Provider completo

---

# 🧠 Se vuoi il prossimo step

Posso aiutarti a:

👉 trasformare queste epics in **Jira-ready backlog (story points + dependency graph)**
👉 oppure costruire **modello C4 architecture completo del sistema**
👉 oppure iniziare il **codice reale strutturato (repo layout completo)**

Dimmi la direzione.
