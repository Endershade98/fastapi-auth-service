# src/domain/repositories/authorization_code_repository.py

from abc import abstractmethod

from src.domain.aggregates.authorization_code import (
    AuthorizationCodeAggregate,
)

from src.domain.repositories.base_repository import Repository


class AuthorizationCodeRepository(
    Repository[AuthorizationCodeAggregate, str]
):

    @abstractmethod
    async def get_by_code(
        self,
        code: str,
    ) -> AuthorizationCodeAggregate | None:
        raise NotImplementedError