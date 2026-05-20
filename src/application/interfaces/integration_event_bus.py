# src/application/interfaces/integration_event_bus.py

from abc import ABC, abstractmethod

from src.domain.events.integration.base import IntegrationEvent


class IntegrationEventBus(ABC):

    @abstractmethod
    async def publish(self, event: IntegrationEvent) -> None:
        raise NotImplementedError