# src/infrastructure/events/in_memory_event_dispatcher.py

class InMemoryEventDispatcher:

    def __init__(self):
        self.events = []

    async def publish(self, event) -> None:
        self.events.append(event)