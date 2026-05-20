# src/domain/events/integration/auth_events.py

from dataclasses import dataclass

from src.domain.events.integration.base import IntegrationEvent


@dataclass(frozen=True, kw_only=True)
class UserLoggedInIntegrationEvent(IntegrationEvent):

    user_id: str

    session_id: str


@dataclass(frozen=True, kw_only=True)
class SessionRevokedIntegrationEvent(IntegrationEvent):

    session_id: str

    reason: str