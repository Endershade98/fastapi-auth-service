# src/application/dto/auth/refresh_token_request.py

from dataclasses import dataclass

@dataclass(frozen=True)
class RefreshTokenRequest:
    refresh_token: str
    ip_address: str
    user_agent: str