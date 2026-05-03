# tests/domain/rules/test_password_rules.py

import pytest

from src.domain.rules.password_rules import PasswordRules
from src.domain.value_objects.security.plain_password import PlainPassword
from src.domain.value_objects.security.password_hash import PasswordHash


class FakeHasher:
    def verify(self, plain, hashed):
        return plain == "secret123" and hashed == "HASH"


def test_password_verification_success():
    plain = PlainPassword("secret123")

    result = PasswordRules.verify(
        plain,
        PasswordHash("HASH"),
        FakeHasher()
    )

    assert result is True


def test_password_verification_failure():
    plain = PlainPassword("wrongpass")

    result = PasswordRules.verify(
        plain,
        PasswordHash("HASH"),
        FakeHasher()
    )

    assert result is False