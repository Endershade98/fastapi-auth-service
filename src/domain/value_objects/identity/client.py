# src/domain/value_objects/identity/client.py

import re 
from dataclasses import dataclass
from src.domain.exceptions.domain_error import DomainValidationError



@dataclass(frozen=True, slots=True)
class ClientId:
    value: str

    def __post_init__(self):
        val = self.value.strip()

        if not val:
            raise DomainValidationError("ClientId cannot be empty")

        if len(val) < 3:
            raise DomainValidationError("ClientId too short")

        if not re.match(r"^[a-zA-Z0-9_\-]+$", val):
            raise DomainValidationError("Invalid ClientId format")

        object.__setattr__(self, "value", val)

    def __str__(self):
        return self.value