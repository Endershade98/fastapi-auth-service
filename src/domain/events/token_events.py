# src/domain/events/token_events.py

from dataclasses import dataclass
from src.domain.events.base import DomainEvent
from src.domain.value_objects.identity.session import SessionId


@dataclass(frozen=True, kw_only=True)
class TokenIssued(DomainEvent):
    session_id: SessionId


@dataclass(frozen=True, kw_only=True)
class TokenRotated(DomainEvent):
    session_id: SessionId
    rotation_count: int