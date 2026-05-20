# src/application/dto/auth/logout_response.py

from dataclasses import dataclass


@dataclass(frozen=True)
class LogoutResponse:
    success: bool