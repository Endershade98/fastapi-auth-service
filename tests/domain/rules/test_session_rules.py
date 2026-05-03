# tests/domain/rules/test_session_rules.py

import pytest

from src.domain.rules.session_rules import SessionRules
from src.domain.aggregates.token_session import TokenSessionAggregate, SessionStatus
from src.domain.value_objects.identity.session import SessionId
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.shared.timestamp import Timestamp


def build_session(status=SessionStatus.ACTIVE):
    session = TokenSessionAggregate(
        id=SessionId.new(),
        user_id=UserId.new(),
        created_at=Timestamp.now(),
        status=status
    )
    return session


def test_active_session_valid():
    session = build_session(SessionStatus.ACTIVE)
    SessionRules.ensure_valid_session(session)


def test_revoked_session_invalid():
    session = build_session(SessionStatus.REVOKED)

    with pytest.raises(Exception):
        SessionRules.ensure_valid_session(session)


def test_compromised_session_invalid():
    session = build_session(SessionStatus.COMPROMISED)

    with pytest.raises(Exception):
        SessionRules.ensure_valid_session(session)