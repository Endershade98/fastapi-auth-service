# src/domain/rules/user_rules.py

from src.domain.aggregates.user import UserAggregate, UserStatus
from src.domain.exceptions.domain_error import DomainValidationError


class UserRules:

    @staticmethod
    def ensure_can_login(user: UserAggregate):

        if user.status == UserStatus.DISABLED:
            raise DomainValidationError("User is disabled")

        if user.status == UserStatus.LOCKED:
            raise DomainValidationError("User is locked")

        if user.status != UserStatus.ACTIVE:
            raise DomainValidationError("User not active")