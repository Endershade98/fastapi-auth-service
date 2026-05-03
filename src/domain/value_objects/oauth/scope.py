# src/domain/value_objects/oauth/scope.py

from dataclasses import dataclass
from src.domain.exceptions.domain_error import DomainValidationError


@dataclass(frozen=True)
class Scope:
    value: str

    def __post_init__(self):
        allowed = {"openid", "profile", "email", "user.read", "user.write"}

        if self.value not in allowed:
            raise DomainValidationError("Invalid scope")