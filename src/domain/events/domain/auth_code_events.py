# src/domain/events/domain/auth_code_events.py

from dataclasses import dataclass

from src.domain.events.domain.base import DomainEvent


@dataclass(frozen=True, kw_only=True)
class AuthorizationCodeIssued(DomainEvent):

    client_id: str


@dataclass(frozen=True, kw_only=True)
class AuthorizationCodeConsumed(DomainEvent):

    client_id: str


@dataclass(frozen=True, kw_only=True)
class AuthorizationCodeExpired(DomainEvent):
    pass