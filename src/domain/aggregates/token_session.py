# src/domain/aggregates/token_session.py

from dataclasses import dataclass, field
from enum import Enum

from src.domain.shared.aggregate_root import AggregateRoot

from src.domain.events.domain.session_events import (
    SessionCreated,
    SessionRevoked,
    SessionCompromised,
)

from src.domain.events.domain.token_events import (
    TokenRotated,
)

from src.domain.exceptions.domain_error import DomainValidationError

from src.domain.value_objects.identity.session import SessionId
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.security.password_hash import PasswordHash
from src.domain.value_objects.shared.timestamp import Timestamp


class SessionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    REVOKED = "REVOKED"
    COMPROMISED = "COMPROMISED"


@dataclass(eq=False)
class TokenSessionAggregate(AggregateRoot[SessionId]):

    id: SessionId

    user_id: UserId

    refresh_token_hash: PasswordHash

    created_at: Timestamp

    status: SessionStatus = SessionStatus.ACTIVE

    rotation_counter: int = 0

    compromised_reason: str | None = None

    previous_refresh_token_hashes: list[PasswordHash] = field(
        default_factory=list
    )

    @staticmethod
    def create(
        *,
        session_id: SessionId,
        user_id: UserId,
        refresh_token_hash: PasswordHash,
    ) -> "TokenSessionAggregate":

        session = TokenSessionAggregate(
            id=session_id,
            user_id=user_id,
            refresh_token_hash=refresh_token_hash,
            created_at=Timestamp.now(),
        )

        session.record_event(
            SessionCreated(
                session_id=str(session.id),
                user_id=str(session.user_id),
            )
        )

        return session

    def ensure_active(self):

        if self.status == SessionStatus.REVOKED:
            raise DomainValidationError("Session revoked")

        if self.status == SessionStatus.COMPROMISED:
            raise DomainValidationError("Session compromised")

    def verify_refresh_token(
        self,
        refresh_token: str,
        password_hasher,
    ) -> bool:

        if password_hasher.verify(
            refresh_token,
            self.refresh_token_hash.value,
        ):
            return True

        for previous in self.previous_refresh_token_hashes:

            if password_hasher.verify(
                refresh_token,
                previous.value,
            ):

                self.compromise(
                    "refresh token reuse detected"
                )

                raise DomainValidationError(
                    "Refresh token reuse detected"
                )

        return False

    def rotate_refresh_token(
        self,
        new_refresh_token_hash: PasswordHash,
    ):

        self.ensure_active()

        self.previous_refresh_token_hashes.append(
            self.refresh_token_hash
        )

        self.refresh_token_hash = new_refresh_token_hash

        self.rotation_counter += 1

        self.record_event(
            TokenRotated(
                session_id=self.id,
                rotation_count=self.rotation_counter,
            )
        )

    def revoke(self, reason: str):

        self.ensure_active()

        self.status = SessionStatus.REVOKED

        self.record_event(
            SessionRevoked(
                session_id=str(self.id),
                reason=reason,
            )
        )

    def compromise(self, reason: str):

        self.status = SessionStatus.COMPROMISED

        self.compromised_reason = reason

        self.record_event(
            SessionCompromised(
                session_id=str(self.id),
                reason=reason,
            )
        )