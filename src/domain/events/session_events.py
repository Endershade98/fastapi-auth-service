# src/domain/events/session_events.py

from dataclasses import dataclass
from src.domain.events.base import DomainEvent
from src.domain.value_objects.identity.session import SessionId


@dataclass(frozen=True, kw_only=True)
class SessionRevoked(DomainEvent):
    session_id: SessionId
    reason: str


@dataclass(frozen=True, kw_only=True)
class SessionCompromised(DomainEvent):
    session_id: SessionId