# src/domain/value_objects/security/password_hash.py

from dataclasses import dataclass


@dataclass(frozen=True)
class PasswordHash:
    value: str

    def verify(self, plain_password: str, hasher):
        return hasher.verify(plain_password, self.value)