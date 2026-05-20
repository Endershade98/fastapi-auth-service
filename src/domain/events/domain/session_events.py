# src/domain/events/domain/session_events.py

from dataclasses import dataclass

from src.domain.events.domain.base import DomainEvent


@dataclass(frozen=True, kw_only=True)
class SessionCreated(DomainEvent):

    session_id: str
    user_id: str


@dataclass(frozen=True, kw_only=True)
class SessionRevoked(DomainEvent):

    session_id: str
    reason: str


@dataclass(frozen=True, kw_only=True)
class SessionCompromised(DomainEvent):

    session_id: str
    reason: str