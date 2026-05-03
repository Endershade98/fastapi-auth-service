## USER STATUS
| Codice  | Stato    | Descrizione            |
| ------- | -------- | ---------------------- |
| USR_001 | ACTIVE   | utente attivo          |
| USR_002 | LOCKED   | bloccato per sicurezza |
| USR_003 | DISABLED | disabilitato           |
| USR_004 | PENDING  | non verificato         |

## CLIENT STATUS
| Codice  | Stato     | Descrizione   |
| ------- | --------- | ------------- |
| CLI_001 | ACTIVE    | client valido |
| CLI_002 | DISABLED  | disabilitato  |
| CLI_003 | SUSPENDED | sospeso       |

## SESSION STATUS
| Codice  | Stato       | Descrizione     |
| ------- | ----------- | --------------- |
| SES_001 | ACTIVE      | sessione valida |
| SES_002 | REVOKED     | revocata        |
| SES_003 | EXPIRED     | scaduta         |
| SES_004 | COMPROMISED | violazione      |

## TOKEN STATUS
| Codice  | Stato   | Descrizione |
| ------- | ------- | ----------- |
| TOK_001 | ACTIVE  | valido      |
| TOK_002 | ROTATED | sostituito  |
| TOK_003 | REVOKED | revocato    |
| TOK_004 | EXPIRED | scaduto     |

## EVENTI (audit + flow)
| Codice  | Evento        |
| ------- | ------------- |
| EVT_001 | LOGIN_SUCCESS |
| EVT_002 | LOGIN_FAILED  |
| EVT_003 | TOKEN_REFRESH |
| EVT_004 | TOKEN_REUSE   |
| EVT_005 | CLIENT_AUTH   |

### Eventi di dominio
UserLoggedIn
TokenIssued
TokenRevoked
ClientAuthenticated

### Eventi di integrazione
AuditLogCreated
SecurityAlertTriggered