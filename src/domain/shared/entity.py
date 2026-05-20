# src/domain/shared/entity.py

from dataclasses import dataclass
from typing import Generic, TypeVar


IdType = TypeVar("IdType")


@dataclass(eq=False)
class Entity(Generic[IdType]):

    id: IdType

    def __eq__(self, other):

        if not isinstance(other, Entity):
            return False

        return self.id == other.id

    def __hash__(self):
        return hash(self.id)