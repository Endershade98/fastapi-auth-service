# tests/domain/events/test_versioning.py

from src.domain.events.versioning import EventVersioning


def test_event_versioning_identity():
    event = {
        "version": 1,
        "data": "test"
    }

    result = EventVersioning.upgrade(event)

    assert result["version"] == 1
    assert result["data"] == "test"


def test_event_versioning_default():
    event = {
        "data": "test"
    }

    result = EventVersioning.upgrade(event)

    assert result["version"] == 1
    assert result["data"] == "test"