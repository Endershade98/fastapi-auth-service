# tests/domain/aggregates/test_oauth_client.py

from src.domain.aggregates.oauth_client import OAuthClientAggregate, ClientStatus
from src.domain.value_objects.identity.client import ClientId
from src.domain.value_objects.oauth.redirect_uri import RedirectUri
from src.domain.value_objects.oauth.scope import Scope
from src.domain.value_objects.oauth.scope_set import ScopeSet
from src.domain.value_objects.security.password_hash import PasswordHash
from src.domain.value_objects.shared.timestamp import Timestamp


def build_client():
    return OAuthClientAggregate(
        id=ClientId("web_app"),
        secret_hash=PasswordHash("HASH"),
        redirect_uris={
            RedirectUri("https://app.test/callback")
        },
        allowed_scopes=ScopeSet(
            frozenset({Scope("openid"), Scope("profile")})
        ),
        created_at=Timestamp.now()
    )


def test_client_active():
    client = build_client()
    assert client.is_active()


def test_disable_client():
    client = build_client()
    client.disable()

    assert client.status == ClientStatus.DISABLED


def test_redirect_allowed():
    client = build_client()

    assert client.allows_redirect_uri(
        RedirectUri("https://app.test/callback")
    )


def test_scope_allowed():
    client = build_client()
    assert client.allows_scope("openid")