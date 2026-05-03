# src/domain/value_objects/oauth/redirect_uri.py

from urllib.parse import urlparse
from dataclasses import dataclass
from src.domain.exceptions.domain_error import DomainValidationError


@dataclass(frozen=True)
class RedirectUri:
    value: str

    def __post_init__(self):
        parsed = urlparse(self.value)

        if not parsed.scheme or not parsed.netloc:
            raise DomainValidationError("Invalid redirect URI")