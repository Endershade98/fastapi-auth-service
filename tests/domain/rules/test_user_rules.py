# tests/domain/rules/test_user_rules.py


import pytest

from src.domain.rules.user_rules import UserRules
from src.domain.aggregates.user import UserAggregate, UserStatus
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.security.email import Email
from src.domain.value_objects.security.password_hash import PasswordHash
from src.domain.value_objects.shared.timestamp import Timestamp


def build_user(status=UserStatus.ACTIVE):
    user = UserAggregate(
        id=UserId.new(),
        email=Email("test@test.com"),
        password_hash=PasswordHash("HASH"),
        created_at=Timestamp.now(),
        status=status
    )
    return user


def test_user_can_login_active():
    user = build_user(UserStatus.ACTIVE)
    UserRules.ensure_can_login(user)


def test_user_disabled_cannot_login():
    user = build_user(UserStatus.DISABLED)

    with pytest.raises(Exception):
        UserRules.ensure_can_login(user)


def test_user_locked_cannot_login():
    user = build_user(UserStatus.LOCKED)

    with pytest.raises(Exception):
        UserRules.ensure_can_login(user)