# src/domain/value_objects/security/email.py

import re
from dataclasses import dataclass
from src.domain.exceptions.domain_error import DomainValidationError


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self):
        normalized = self.value.strip().lower()

        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", normalized):
            raise DomainValidationError("Invalid email")

        object.__setattr__(self, "value", normalized)