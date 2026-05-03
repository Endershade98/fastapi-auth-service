# src/domain/value_objects/security/token_id.py

from dataclasses import dataclass
from src.domain.exceptions.domain_error import DomainValidationError


@dataclass(frozen=True)
class TokenId:
    value: str

    def __post_init__(self):

        if not self.value:
            raise DomainValidationError("TokenId cannot be empty")