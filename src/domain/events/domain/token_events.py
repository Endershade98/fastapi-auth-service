# src/domain/events/domain/token_events.py

from dataclasses import dataclass

from src.domain.events.domain.base import DomainEvent


@dataclass(frozen=True, kw_only=True)
class AccessTokenIssued(DomainEvent):

    expires_in: int


@dataclass(frozen=True, kw_only=True)
class RefreshTokenIssued(DomainEvent):

    refresh_token_id: str