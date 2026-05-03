# src/domain/aggregates/user.py

from dataclasses import dataclass, field
from enum import Enum

from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.security.email import Email
from src.domain.value_objects.security.password_hash import PasswordHash
from src.domain.value_objects.shared.timestamp import Timestamp


class UserStatus(str, Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    LOCKED = "LOCKED"
    DISABLED = "DISABLED"


@dataclass
class UserAggregate:
    id: UserId
    email: Email
    password_hash: PasswordHash
    created_at: Timestamp
    status: UserStatus = UserStatus.PENDING
    roles: set[str] = field(default_factory=set)

    def activate(self):
        self.status = UserStatus.ACTIVE

    def lock(self):
        self.status = UserStatus.LOCKED

    def disable(self):
        self.status = UserStatus.DISABLED

    def can_login(self) -> bool:
        return self.status == UserStatus.ACTIVE

    def assign_role(self, role: str):
        self.roles.add(role)

    def has_role(self, role: str) -> bool:
        return role in self.roles