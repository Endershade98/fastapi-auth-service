# tests/domain/value_objects/security/test_token_id.py

from src.domain.value_objects.security.token_id import TokenId


def test_token_id():
    token = TokenId("abc123")
    assert token.value == "abc123"


def test_token_equality():
    assert TokenId("abc") == TokenId("abc")