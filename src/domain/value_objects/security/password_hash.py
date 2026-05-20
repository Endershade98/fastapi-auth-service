# src/domain/value_objects/security/password_hash.py

from dataclasses import dataclass


@dataclass(frozen=True)
class PasswordHash:
    value: str