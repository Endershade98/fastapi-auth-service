# src/application/services/event_mapper.py

from src.domain.events.domain.session_events import SessionRevoked

from src.domain.events.integration.auth_events import (
    SessionRevokedIntegrationEvent,
)


class EventMapper:

    @staticmethod
    def to_integration_event(domain_event):

        if isinstance(domain_event, SessionRevoked):

            return SessionRevokedIntegrationEvent(
                session_id=str(domain_event.session_id),
                reason=domain_event.reason,
            )

        return None