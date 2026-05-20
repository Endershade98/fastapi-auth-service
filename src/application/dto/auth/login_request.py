# src/application/dto/auth/login_request.py

from dataclasses import dataclass

@dataclass(frozen=True)
class LoginRequest:
    email: str
    password: str
    ip_address: str
    user_agent: str