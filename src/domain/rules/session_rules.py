# src/domain/rules/session_rules.py

from src.domain.aggregates.token_session import TokenSessionAggregate, SessionStatus
from src.domain.exceptions.domain_error import DomainValidationError


class SessionRules:

    @staticmethod
    def ensure_valid_session(session: TokenSessionAggregate):

        if session.status == SessionStatus.REVOKED:
            raise DomainValidationError("Session revoked")

        if session.status == SessionStatus.COMPROMISED:
            raise DomainValidationError("Session compromised")

        if session.status != SessionStatus.ACTIVE:
            raise DomainValidationError("Session not active")