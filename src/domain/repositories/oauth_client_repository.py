# src/domain/repositories/oauth_client_repository.py

from abc import ABC, abstractmethod

from src.domain.aggregates.oauth_client import OAuthClientAggregate
from src.domain.value_objects.identity.client import ClientId


class OAuthClientRepository(ABC):

    @abstractmethod
    async def get_by_id(
        self,
        client_id: ClientId
    ) -> OAuthClientAggregate | None:
        pass

    @abstractmethod
    async def save(
        self,
        client: OAuthClientAggregate
    ) -> None:
        pass