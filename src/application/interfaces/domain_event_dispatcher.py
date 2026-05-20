# src/application/interfaces/domain_event_dispatcher.py

from abc import ABC, abstractmethod

from src.domain.events.domain.base import DomainEvent


class DomainEventDispatcher(ABC):

    @abstractmethod
    async def dispatch(self, event: DomainEvent) -> None:
        raise NotImplementedError