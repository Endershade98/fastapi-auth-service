# tests/domain/rules/test_auth_code_rules.py

import pytest

from src.domain.rules.auth_code_rules import AuthorizationCodeRules
from src.domain.aggregates.authorization_code import AuthorizationCodeAggregate, AuthorizationCodeStatus
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.identity.client import ClientId
from src.domain.value_objects.shared.timestamp import Timestamp


def build_code(status=AuthorizationCodeStatus.ACTIVE):
    code = AuthorizationCodeAggregate(
        code="abc",
        user_id=UserId.new(),
        client_id=ClientId("web"),
        code_challenge="challenge",
        expires_at=Timestamp.now(),
        status=status
    )
    return code


def test_active_code_allowed():
    code = build_code(AuthorizationCodeStatus.ACTIVE)
    AuthorizationCodeRules.ensure_single_use(code)


def test_consumed_code_blocked():
    code = build_code(AuthorizationCodeStatus.CONSUMED)

    with pytest.raises(Exception):
        AuthorizationCodeRules.ensure_single_use(code)