# tests/domain/value_objects/identity/test_session.py

from src.domain.value_objects.identity.session import SessionId


def test_session_generate():
    sid = SessionId.new()
    assert sid.value is not None


def test_session_equality():
    sid = SessionId.new()
    assert sid == SessionId(sid.value)