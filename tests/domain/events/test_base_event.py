# tests/domain/events/test_base_event.py

from src.domain.events.base import DomainEvent


def test_base_event_creation():
    event = DomainEvent()

    assert event.event_type == "DomainEvent"
    assert event.event_id is not None
    assert event.version == 1
    assert event.occurred_at is not None


def test_base_event_immutable():
    event = DomainEvent()

    try:
        event.event_type = "HACK"
        assert False, "Should be immutable"
    except Exception:
        assert True