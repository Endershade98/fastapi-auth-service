# src/domain/repositories/authorization_code_repository.py

from abc import ABC, abstractmethod

from src.domain.aggregates.authorization_code import AuthorizationCodeAggregate


class AuthorizationCodeRepository(ABC):

    @abstractmethod
    async def get_by_code(
        self,
        code: str
    ) -> AuthorizationCodeAggregate | None:
        pass

    @abstractmethod
    async def save(
        self,
        auth_code: AuthorizationCodeAggregate
    ) -> None:
        pass