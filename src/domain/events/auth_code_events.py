# src/domain/events/auth_code_events.py

from dataclasses import dataclass
from src.domain.events.base import DomainEvent


@dataclass(frozen=True, kw_only=True)
class AuthorizationCodeConsumed(DomainEvent):
    code: str
    client_id: str