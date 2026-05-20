# src/domain/repositories/oauth_client_repository.py

from src.domain.aggregates.oauth_client import OAuthClientAggregate

from src.domain.repositories.base_repository import Repository

from src.domain.value_objects.identity.client import ClientId


class OAuthClientRepository(
    Repository[OAuthClientAggregate, ClientId]
):
    pass