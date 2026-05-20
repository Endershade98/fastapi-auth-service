# src/domain/repositories/token_session_repository.py

from abc import abstractmethod

from src.domain.aggregates.token_session import TokenSessionAggregate

from src.domain.repositories.base_repository import Repository

from src.domain.value_objects.identity.session import SessionId
from src.domain.value_objects.security.token_id import TokenId


class TokenSessionRepository(
    Repository[TokenSessionAggregate, SessionId]
):

    @abstractmethod
    async def get_by_refresh_token_id(
        self,
        token_id: TokenId,
    ) -> TokenSessionAggregate | None:
        raise NotImplementedError