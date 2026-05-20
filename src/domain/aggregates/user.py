# src/domain/aggregates/user.py

from dataclasses import dataclass, field
from enum import Enum

from src.domain.events.domain.user_events import (
    UserActivated,
    UserDisabled,
    UserLocked,
    UserRegistered,
)
from src.domain.exceptions.domain_error import DomainValidationError
from src.domain.shared.aggregate_root import AggregateRoot
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.security.email import Email
from src.domain.value_objects.security.password_hash import PasswordHash
from src.domain.value_objects.shared.timestamp import Timestamp


class UserStatus(str, Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    LOCKED = "LOCKED"
    DISABLED = "DISABLED"


@dataclass(eq=False)
class UserAggregate(AggregateRoot[UserId]):

    id: UserId

    email: Email

    password_hash: PasswordHash

    created_at: Timestamp = field(default_factory=Timestamp.now)

    status: UserStatus = UserStatus.PENDING

    roles: set[str] = field(default_factory=set)

    @staticmethod
    def create(
        user_id: UserId,
        email: Email,
        password_hash: PasswordHash,
    ) -> "UserAggregate":

        user = UserAggregate(
            id=user_id,
            email=email,
            password_hash=password_hash,
        )

        user.record_event(
            UserRegistered(
                aggregate_id=str(user.id),
                email=user.email.value,
            )
        )

        return user

    def activate(self):

        if self.status == UserStatus.DISABLED:
            raise DomainValidationError(
                "Disabled user cannot be activated"
            )

        self.status = UserStatus.ACTIVE

        self.record_event(
            UserActivated(
                aggregate_id=str(self.id),
            )
        )

    def lock(self):

        if self.status == UserStatus.DISABLED:
            raise DomainValidationError(
                "Disabled user cannot be locked"
            )

        self.status = UserStatus.LOCKED

        self.record_event(
            UserLocked(
                aggregate_id=str(self.id),
            )
        )

    def disable(self):

        self.status = UserStatus.DISABLED

        self.record_event(
            UserDisabled(
                aggregate_id=str(self.id),
            )
        )

    def ensure_can_login(self):

        if self.status == UserStatus.DISABLED:
            raise DomainValidationError("User disabled")

        if self.status == UserStatus.LOCKED:
            raise DomainValidationError("User locked")

        if self.status != UserStatus.ACTIVE:
            raise DomainValidationError("User not active")