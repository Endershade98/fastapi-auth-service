# src/domain/services/token_generator.py

import secrets


class TokenGenerator:

    @staticmethod
    def generate_token_id() -> str:
        return secrets.token_hex(16)

    @staticmethod
    def generate_secret() -> str:
        return secrets.token_urlsafe(48)