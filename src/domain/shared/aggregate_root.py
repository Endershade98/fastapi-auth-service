# src/domain/shared/aggregate_root.py

from dataclasses import dataclass, field
from typing import Generic, TypeVar

from src.domain.events.domain.base import DomainEvent
from src.domain.shared.entity import Entity


IdType = TypeVar("IdType")


@dataclass(eq=False)
class AggregateRoot(Entity[IdType], Generic[IdType]):

    _domain_events: list[DomainEvent] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

    version: int = 0

    def record_event(self, event: DomainEvent):
        self._domain_events.append(event)

    def pull_events(self) -> tuple[DomainEvent, ...]:

        events = tuple(self._domain_events)

        self._domain_events.clear()

        return events