# tests/domain/value_objects/security/test_ip_address.py

import pytest
from src.domain.value_objects.security.ip_address import IPAddress


def test_valid_ip():
    ip = IPAddress("127.0.0.1")
    assert ip.value == "127.0.0.1"


def test_invalid_ip():
    with pytest.raises(Exception):
        IPAddress("999.999.999.999")