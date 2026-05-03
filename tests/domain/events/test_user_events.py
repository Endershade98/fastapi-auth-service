# tests/domain/events/test_user_events.py

from src.domain.events.user_events import UserRegistered, UserLoggedIn
from src.domain.value_objects.identity.user import UserId


def test_user_registered_event():
    event = UserRegistered(
        user_id=UserId.new(),
        email="test@test.com"
    )

    assert event.event_type == "UserRegistered"
    assert event.user_id is not None


def test_user_logged_in_event():
    event = UserLoggedIn(
        user_id=UserId.new()
    )

    assert event.event_type == "UserLoggedIn"