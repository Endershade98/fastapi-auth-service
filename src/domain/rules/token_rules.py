# src/domain/rules/token_rules.py

from src.domain.exceptions.domain_error import DomainValidationError


class TokenRules:

    @staticmethod
    def ensure_one_time_use(is_used: bool):

        if is_used:
            raise DomainValidationError("Refresh token already used")