# tests/domain/aggregates/test_token_session.py

from src.domain.aggregates.token_session import TokenSessionAggregate, SessionStatus
from src.domain.value_objects.identity.session import SessionId
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.shared.timestamp import Timestamp


def build_session():
    return TokenSessionAggregate(
        id=SessionId.new(),
        user_id=UserId.new(),
        created_at=Timestamp.now()
    )


def test_rotate():
    s = build_session()
    s.rotate()

    assert s.rotation_counter == 1


def test_revoke():
    s = build_session()
    s.revoke()

    assert s.status == SessionStatus.REVOKED