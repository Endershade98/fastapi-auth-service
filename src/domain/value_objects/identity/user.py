# src/domain/value_objects/identity/user.py

import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    value: str

    def __post_init__(self):
        uuid.UUID(self.value)
    
    @staticmethod
    def new():
        return UserId(str(uuid.uuid4()))