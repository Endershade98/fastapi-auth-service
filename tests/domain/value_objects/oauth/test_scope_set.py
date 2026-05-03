# tests/domain/value_objects/oauth/test_scope_set.py

from src.domain.value_objects.oauth.scope import Scope
from src.domain.value_objects.oauth.scope_set import ScopeSet


def test_contains_scope():
    scopes = ScopeSet(frozenset({Scope("openid"), Scope("profile")}))
    assert scopes.contains("openid")


def test_missing_scope():
    scopes = ScopeSet(frozenset({Scope("openid")}))
    assert not scopes.contains("email")