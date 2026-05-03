# src/domain/aggregates/authorization_code.py

from dataclasses import dataclass
from enum import Enum

from src.domain.value_objects.identity.client import ClientId
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.shared.timestamp import Timestamp


class AuthorizationCodeStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CONSUMED = "CONSUMED"


@dataclass
class AuthorizationCodeAggregate:
    code: str
    user_id: UserId
    client_id: ClientId
    code_challenge: str
    expires_at: Timestamp
    status: AuthorizationCodeStatus = AuthorizationCodeStatus.ACTIVE

    def is_active(self) -> bool:
        return self.status == AuthorizationCodeStatus.ACTIVE

    def is_expired(self, now: Timestamp) -> bool:
        return now.is_after(self.expires_at)

    def consume(self):
        self.status = AuthorizationCodeStatus.CONSUMED

    def verify_pkce(self, verifier: str) -> bool:
        return verifier == self.code_challenge