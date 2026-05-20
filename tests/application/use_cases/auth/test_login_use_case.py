# tests/application/use_cases/auth/test_login_use_case.py

import pytest

from src.application.dto.auth.login_request import LoginRequest
from src.application.use_cases.auth.login_use_case import LoginUseCase

from src.domain.aggregates.user import UserAggregate, UserStatus
from src.domain.value_objects.identity.user import UserId
from src.domain.value_objects.security.email import Email
from src.domain.value_objects.security.password_hash import PasswordHash


# -------------------------
# FAKES
# -------------------------

class FakeUserRepository:

    async def get_by_email(self, email: str):

        return UserAggregate.create(
            user_id=UserId.new(),
            email=Email(email),
            password_hash=PasswordHash("hashed-secret"),
        )


class FakeSessionRepository:

    async def save(self, session):
        self.saved_session = session


class FakeTokenService:

    async def issue_access_token(self, session) -> str:
        return "access-token"

    async def issue_refresh_token(self, session) -> str:
        return "refresh-token"


class FakePasswordHasher:

    def verify(self, plain: str, hashed: str) -> bool:
        return plain == "secret123"


class FakeEventDispatcher:

    async def dispatch(self, event):
        return None


class FakeUnitOfWork:

    async def commit(self):
        return None


# -------------------------
# TEST
# -------------------------

@pytest.mark.asyncio
async def test_login_success():

    use_case = LoginUseCase(
        user_repository=FakeUserRepository(),
        session_repository=FakeSessionRepository(),
        token_service=FakeTokenService(),
        password_hasher=FakePasswordHasher(),
        event_dispatcher=FakeEventDispatcher(),
        unit_of_work=FakeUnitOfWork(),
    )

    request = LoginRequest(
        email="test@example.com",
        password="secret123",
        ip_address="127.0.0.1",
        user_agent="pytest",
    )

    result = await use_case.execute(request)

    # -------------------------
    # ASSERT RESPONSE
    # -------------------------
    assert result.access_token == "access-token"
    assert result.refresh_token == "refresh-token"
    assert result.token_type == "Bearer"

    # -------------------------
    # ASSERT SESSION CREATED
    # -------------------------
    session = use_case.session_repository.saved_session
    assert session is not None
    assert session.user_id.value is not None
    assert session.status.value == "ACTIVE"