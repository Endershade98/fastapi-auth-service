# src/domain/events/domain/user_events.py

from dataclasses import dataclass

from src.domain.events.domain.base import DomainEvent


@dataclass(frozen=True, kw_only=True)
class UserRegistered(DomainEvent):

    email: str


@dataclass(frozen=True, kw_only=True)
class UserActivated(DomainEvent):
    pass


@dataclass(frozen=True, kw_only=True)
class UserLocked(DomainEvent):
    pass


@dataclass(frozen=True, kw_only=True)
class UserDisabled(DomainEvent):
    pass