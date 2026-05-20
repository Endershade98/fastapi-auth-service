# src/domain/repositories/user_repository.py

from abc import abstractmethod

from src.domain.aggregates.user import UserAggregate

from src.domain.repositories.base_repository import Repository

from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.security.email import Email


class UserRepository(
    Repository[UserAggregate, UserId]
):

    @abstractmethod
    async def get_by_email(
        self,
        email: Email,
    ) -> UserAggregate | None:
        raise NotImplementedError