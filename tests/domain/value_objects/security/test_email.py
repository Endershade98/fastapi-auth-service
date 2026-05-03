# tests/domain/value_objects/security/test_email.py

import pytest
from dataclasses import FrozenInstanceError

from src.domain.value_objects.security.email import Email


def test_email_normalized():
    email = Email(" TEST@MAIL.COM ")
    assert email.value == "test@mail.com"


def test_email_invalid():
    with pytest.raises(Exception):
        Email("invalid")


def test_email_equality():
    assert Email("a@test.com") == Email("a@test.com")


def test_email_immutable():
    email = Email("a@test.com")

    with pytest.raises(FrozenInstanceError):
        email.value = "hack@test.com"