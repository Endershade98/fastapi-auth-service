# src/domain/repositories/base_repository.py

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


AggregateType = TypeVar("AggregateType")
IdType = TypeVar("IdType")


class Repository(ABC, Generic[AggregateType, IdType]):

    @abstractmethod
    async def get_by_id(
        self,
        entity_id: IdType,
    ) -> AggregateType | None:
        raise NotImplementedError

    @abstractmethod
    async def save(
        self,
        aggregate: AggregateType,
    ) -> None:
        raise NotImplementedError