# tests/domain/value_objects/security/test_plain_password.py

import pytest
from src.domain.value_objects.security.plain_password import PlainPassword


def test_valid_password():
    pwd = PlainPassword("StrongPass123")
    assert pwd.value == "StrongPass123"


def test_short_password():
    with pytest.raises(Exception):
        PlainPassword("123")