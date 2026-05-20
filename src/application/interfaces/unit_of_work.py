# src/application/interfaces/unit_of_work.py

from abc import ABC, abstractmethod

from src.domain.repositories.authorization_code_repository import (
    AuthorizationCodeRepository,
)
from src.domain.repositories.token_session_repository import (
    TokenSessionRepository,
)
from src.domain.repositories.user_repository import UserRepository


class UnitOfWork(ABC):

    users: UserRepository

    sessions: TokenSessionRepository

    authorization_codes: AuthorizationCodeRepository

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError