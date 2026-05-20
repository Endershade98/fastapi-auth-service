# src/application/interfaces/token_service.py

from abc import ABC, abstractmethod


class TokenService(ABC):

    @abstractmethod
    async def issue_access_token(
        self,
        *,
        user_id: str,
        session_id: str,
        scopes: list[str],
    ) -> str:
        raise NotImplementedError

    @abstractmethod
    async def generate_refresh_token(self) -> str:
        raise NotImplementedError