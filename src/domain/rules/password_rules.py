# src/domain/rules/password_rules.py

from src.domain.value_objects.security.password_hash import PasswordHash
from src.domain.value_objects.security.plain_password import PlainPassword


class PasswordRules:

    @staticmethod
    def verify(
        plain: PlainPassword,
        hashed: PasswordHash,
        hasher
    ) -> bool:
        return hashed.verify(plain.value, hasher)