# tests/domain/aggregates/test_user.py

from src.domain.aggregates.user import UserAggregate, UserStatus
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.security.email import Email
from src.domain.value_objects.security.password_hash import PasswordHash
from src.domain.value_objects.shared.timestamp import Timestamp


def build_user():
    return UserAggregate(
        id=UserId.new(),
        email=Email("test@test.com"),
        password_hash=PasswordHash("HASH"),
        created_at=Timestamp.now()
    )


def test_activate_user():
    user = build_user()
    user.activate()

    assert user.status == UserStatus.ACTIVE


def test_only_active_can_login():
    user = build_user()

    assert not user.can_login()

    user.activate()

    assert user.can_login()


def test_assign_role():
    user = build_user()
    user.assign_role("admin")

    assert user.has_role("admin")