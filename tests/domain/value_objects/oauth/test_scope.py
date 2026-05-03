# tests/domain/value_objects/oauth/test_scope.py

import pytest
from src.domain.value_objects.oauth.scope import Scope


def test_valid_scope():
    s = Scope("openid")
    assert s.value == "openid"


def test_invalid_scope():
    with pytest.raises(Exception):
        Scope("admin.super.root")