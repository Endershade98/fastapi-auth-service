# src/domain/aggregates/oauth_client.py

from dataclasses import dataclass, field
from enum import Enum

from src.domain.value_objects.identity.client import ClientId
from src.domain.value_objects.oauth.redirect_uri import RedirectUri
from src.domain.value_objects.oauth.scope_set import ScopeSet
from src.domain.value_objects.security.password_hash import PasswordHash
from src.domain.value_objects.shared.timestamp import Timestamp


class ClientStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"


@dataclass
class OAuthClientAggregate:
    id: ClientId
    secret_hash: PasswordHash
    redirect_uris: set[RedirectUri]
    allowed_scopes: ScopeSet
    created_at: Timestamp
    status: ClientStatus = ClientStatus.ACTIVE

    def disable(self):
        self.status = ClientStatus.DISABLED

    def activate(self):
        self.status = ClientStatus.ACTIVE

    def is_active(self) -> bool:
        return self.status == ClientStatus.ACTIVE

    def allows_redirect_uri(self, uri: RedirectUri) -> bool:
        return uri in self.redirect_uris

    def allows_scope(self, scope: str) -> bool:
        return self.allowed_scopes.contains(scope)

    def rotate_secret(self, new_hash: PasswordHash):
        self.secret_hash = new_hash