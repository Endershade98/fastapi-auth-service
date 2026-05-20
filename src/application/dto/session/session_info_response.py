# src/application/dto/session/session_info_response.py

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SessionInfoResponse:
    session_id: str
    user_id: str
    status: str
    ip_address: str
    user_agent: str
    created_at: datetime
    expires_at: datetime