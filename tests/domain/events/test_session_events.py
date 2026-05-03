# tests/domain/events/test_session_events.py

from src.domain.events.session_events import SessionRevoked, SessionCompromised
from src.domain.value_objects.identity.session import SessionId


def test_session_revoked_event():
    event = SessionRevoked(
        session_id=SessionId.new(),
        reason="logout"
    )

    assert event.reason == "logout"
    assert event.event_type == "SessionRevoked"


def test_session_compromised_event():
    event = SessionCompromised(
        session_id=SessionId.new()
    )

    assert event.event_type == "SessionCompromised"