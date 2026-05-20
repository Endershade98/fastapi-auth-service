# src/domain/aggregates/authorization_code.py

import base64
import hashlib

from dataclasses import dataclass
from enum import Enum

from src.domain.events.domain.auth_code_events import (
    AuthorizationCodeConsumed,
    AuthorizationCodeIssued,
)
from src.domain.exceptions.domain_error import DomainValidationError
from src.domain.shared.aggregate_root import AggregateRoot
from src.domain.value_objects.identity.client import ClientId
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.shared.timestamp import Timestamp


class AuthorizationCodeStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CONSUMED = "CONSUMED"
    EXPIRED = "EXPIRED"


@dataclass(eq=False)
class AuthorizationCodeAggregate(AggregateRoot[str]):

    id: str

    user_id: UserId

    client_id: ClientId

    code_challenge: str

    code_challenge_method: str

    expires_at: Timestamp

    status: AuthorizationCodeStatus = AuthorizationCodeStatus.ACTIVE

    @staticmethod
    def create(
        code: str,
        user_id: UserId,
        client_id: ClientId,
        code_challenge: str,
        code_challenge_method: str,
        expires_at: Timestamp,
    ) -> "AuthorizationCodeAggregate":

        aggregate = AuthorizationCodeAggregate(
            id=code,
            user_id=user_id,
            client_id=client_id,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            expires_at=expires_at,
        )

        aggregate.record_event(
            AuthorizationCodeIssued(
                aggregate_id=aggregate.id,
                client_id=str(client_id),
            )
        )

        return aggregate

    def ensure_active(self, now: Timestamp):

        if self.status != AuthorizationCodeStatus.ACTIVE:
            raise DomainValidationError(
                "Authorization code inactive"
            )

        if now.is_after(self.expires_at):
            self.status = AuthorizationCodeStatus.EXPIRED

            raise DomainValidationError(
                "Authorization code expired"
            )

    def consume(self):

        if self.status != AuthorizationCodeStatus.ACTIVE:
            raise DomainValidationError(
                "Authorization code already consumed"
            )

        self.status = AuthorizationCodeStatus.CONSUMED

        self.record_event(
            AuthorizationCodeConsumed(
                aggregate_id=self.id,
                client_id=str(self.client_id),
            )
        )

    def verify_pkce(self, verifier: str) -> bool:

        if self.code_challenge_method != "S256":
            raise DomainValidationError(
                "Unsupported PKCE challenge method"
            )

        digest = hashlib.sha256(verifier.encode()).digest()

        encoded = base64.urlsafe_b64encode(digest).rstrip(b'=').decode()

        return encoded == self.code_challenge