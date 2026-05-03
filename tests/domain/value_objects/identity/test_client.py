# tests/domain/value_objects/test_client.py

import pytest
from src.domain.value_objects.identity.client import ClientId


def test_client_valid():
    cid = ClientId("web_app_1")
    assert cid.value == "web_app_1"


def test_client_invalid():
    with pytest.raises(Exception):
        ClientId("")


def test_client_equality():
    assert ClientId("abc") == ClientId("abc")