# tests/domain/value_objects/identity/test_user.py

from src.domain.value_objects.identity.user import UserId


def test_user_generate():
    uid = UserId.new()
    assert uid.value is not None


def test_user_equality():
    uid = UserId.new()
    assert uid == UserId(uid.value)