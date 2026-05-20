# src/application/dto/auth/login_response.py

from dataclasses import dataclass


@dataclass(frozen=True)
class LoginResponse:
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    session_id: str