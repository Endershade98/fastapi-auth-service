# src/domain/aggregates/token_session.py

from dataclasses import dataclass
from enum import Enum

from src.domain.value_objects.identity.session import SessionId
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.shared.timestamp import Timestamp


class SessionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    REVOKED = "REVOKED"
    COMPROMISED = "COMPROMISED"


@dataclass
class TokenSessionAggregate:
    id: SessionId
    user_id: UserId
    created_at: Timestamp
    status: SessionStatus = SessionStatus.ACTIVE
    rotation_counter: int = 0

    def rotate(self):
        self.rotation_counter += 1

    def revoke(self):
        self.status = SessionStatus.REVOKED

    def compromise(self):
        self.status = SessionStatus.COMPROMISED

    def is_active(self):
        return self.status == SessionStatus.ACTIVE