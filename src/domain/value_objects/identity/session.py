# src/domain/value_objects/identity/session.py 

import uuid
from dataclasses import dataclass
from src.domain.exceptions.domain_error import DomainValidationError


@dataclass(frozen=True, slots=True)
class SessionId:
    value: str

    def __post_init__(self):
        try:
            uuid.UUID(self.value)
        except Exception:
            raise DomainValidationError("Invalid SessionId UUID")

    @staticmethod
    def new():
        return SessionId(str(uuid.uuid4()))

    def __str__(self):
        return self.value