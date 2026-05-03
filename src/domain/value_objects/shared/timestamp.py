# src/domain/value_objects/shared/timestamp.py

from dataclasses import dataclass
from datetime import datetime, timezone
from src.domain.exceptions.domain_error import DomainValidationError


@dataclass(frozen=True, slots=True)
class Timestamp:
    value: datetime

    def __post_init__(self):
        if not isinstance(self.value, datetime):
            raise DomainValidationError("Timestamp requires datetime")

        if self.value.tzinfo is None:
            raise DomainValidationError("Timestamp must be timezone aware")

    @staticmethod
    def now():
        return Timestamp(datetime.now(timezone.utc))

    def is_before(self, other: "Timestamp") -> bool:
        return self.value < other.value

    def is_after(self, other: "Timestamp") -> bool:
        return self.value > other.value

    def __str__(self):
        return self.value.isoformat()