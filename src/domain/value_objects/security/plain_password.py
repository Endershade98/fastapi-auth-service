# src/domain/value_objects/security/plain_password.py

from dataclasses import dataclass
from src.domain.exceptions.domain_error import DomainValidationError


@dataclass(frozen=True)
class PlainPassword:
    value: str

    def __post_init__(self):

        if len(self.value) < 8:
            raise DomainValidationError("Password too short")