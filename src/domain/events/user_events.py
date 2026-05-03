# src/domain/events/user_events.py

from dataclasses import dataclass
from src.domain.events.base import DomainEvent
from src.domain.value_objects.identity.user import UserId


@dataclass(frozen=True, kw_only=True)
class UserRegistered(DomainEvent):
    user_id: UserId
    email: str


@dataclass(frozen=True, kw_only=True)
class UserLoggedIn(DomainEvent):
    user_id: UserId