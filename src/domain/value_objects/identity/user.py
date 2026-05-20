# src/domain/value_objects/identity/user.py

import uuid
from dataclasses import dataclass
from src.domain.exceptions.domain_error import DomainValidationError


@dataclass(frozen=True)
class UserId:
    value: str

    def __post_init__(self):
        try:
            uuid.UUID(self.value)
        except Exception:
            raise DomainValidationError("Invalid UserId UUID")
    
    @staticmethod
    def new():
        return UserId(str(uuid.uuid4()))