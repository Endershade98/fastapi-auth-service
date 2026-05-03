# tests/domain/aggregates/test_authorization_code.py

from datetime import datetime, timezone

from src.domain.aggregates.authorization_code import (
    AuthorizationCodeAggregate,
    AuthorizationCodeStatus
)

from src.domain.value_objects.identity.client import ClientId
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.shared.timestamp import Timestamp


def build_code():
    return AuthorizationCodeAggregate(
        code="abc123",
        user_id=UserId.new(),
        client_id=ClientId("web"),
        code_challenge="verifier123",
        expires_at=Timestamp(
            datetime(2099,1,1,tzinfo=timezone.utc)
        )
    )


def test_active_code():
    code = build_code()
    assert code.is_active()


def test_consume_code():
    code = build_code()
    code.consume()

    assert code.status == AuthorizationCodeStatus.CONSUMED


def test_verify_pkce():
    code = build_code()
    assert code.verify_pkce("verifier123")


def test_invalid_pkce():
    code = build_code()
    assert not code.verify_pkce("wrong")