# tests/domain/events/test_token_events.py

from src.domain.events.token_events import TokenIssued, TokenRotated
from src.domain.value_objects.identity.session import SessionId


def test_token_issued_event():
    event = TokenIssued(
        session_id=SessionId.new()
    )

    assert event.event_type == "TokenIssued"


def test_token_rotated_event():
    event = TokenRotated(
        session_id=SessionId.new(),
        rotation_count=2
    )

    assert event.rotation_count == 2