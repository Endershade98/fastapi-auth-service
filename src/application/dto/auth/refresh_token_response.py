# src/application/dto/auth/refresh_token_response.py

from dataclasses import dataclass

@dataclass(frozen=True)
class RefreshTokenResponse:
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int