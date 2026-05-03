# tests/domain/events/test_auth_code_events.py

from src.domain.events.auth_code_events import AuthorizationCodeConsumed


def test_auth_code_consumed_event():
    event = AuthorizationCodeConsumed(
        code="abc123",
        client_id="web_app"
    )

    assert event.code == "abc123"
    assert event.event_type == "AuthorizationCodeConsumed"