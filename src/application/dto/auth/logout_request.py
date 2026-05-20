# src/application/dto/auth/logout_request.py

from dataclasses import dataclass


@dataclass(frozen=True)
class LogoutRequest:
    refresh_token: str