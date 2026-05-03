# src/domain/events/versioning.py

class EventVersioning:

    CURRENT_VERSION = 1

    @staticmethod
    def upgrade(event: dict) -> dict:
        event = dict(event)  # copy safe

        if "version" not in event:
            event["version"] = 1

        return event