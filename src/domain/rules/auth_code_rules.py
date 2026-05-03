# src/domain/rules/auth_code_rules.py

from src.domain.aggregates.authorization_code import AuthorizationCodeAggregate
from src.domain.exceptions.domain_error import DomainValidationError


class AuthorizationCodeRules:

    @staticmethod
    def ensure_single_use(code: AuthorizationCodeAggregate):

        if not code.is_active():
            raise DomainValidationError("Authorization code already used")