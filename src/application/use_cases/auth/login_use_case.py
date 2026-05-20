# src/application/use_cases/auth/login_use_case.py

from src.application.dto.auth.login_request import LoginRequest
from src.application.dto.auth.login_response import LoginResponse

from src.application.exceptions.authentication_error import (
    AuthenticationError,
)

from src.application.interfaces.password_hasher import (
    PasswordHasher,
)

from src.application.interfaces.token_service import (
    TokenService,
)

from src.application.interfaces.unit_of_work import (
    UnitOfWork,
)

from src.application.interfaces.domain_event_dispatcher import (
    DomainEventDispatcher,
)

from src.domain.aggregates.token_session import (
    TokenSessionAggregate,
)

from src.domain.exceptions.domain_error import (
    DomainValidationError,
)

from src.domain.value_objects.identity.session import (
    SessionId,
)

from src.domain.value_objects.security.email import (
    Email,
)

from src.domain.value_objects.security.password_hash import (
    PasswordHash,
)


class LoginUseCase:

    def __init__(
        self,
        *,
        uow: UnitOfWork,
        password_hasher: PasswordHasher,
        token_service: TokenService,
        event_dispatcher: DomainEventDispatcher,
    ):
        self.uow = uow
        self.password_hasher = password_hasher
        self.token_service = token_service
        self.event_dispatcher = event_dispatcher

    async def execute(
        self,
        request: LoginRequest,
    ) -> LoginResponse:

        user = await self.uow.users.get_by_email(
            Email(request.email)
        )

        if user is None:
            raise AuthenticationError(
                "Invalid credentials"
            )

        try:
            user.ensure_can_login()

        except DomainValidationError as exc:
            raise AuthenticationError(str(exc))

        password_valid = self.password_hasher.verify(
            request.password,
            user.password_hash.value,
        )

        if not password_valid:
            raise AuthenticationError(
                "Invalid credentials"
            )

        refresh_token = (
            await self.token_service.generate_refresh_token()
        )

        refresh_token_hash = PasswordHash(
            self.password_hasher.hash(
                refresh_token
            )
        )

        session = TokenSessionAggregate.create(
            session_id=SessionId.new(),
            user_id=user.id,
            refresh_token_hash=refresh_token_hash,
        )

        await self.uow.sessions.save(session)

        access_token = (
            await self.token_service.issue_access_token(
                user_id=str(user.id),
                session_id=str(session.id),
                scopes=[],
            )
        )

        events = session.pull_events()

        await self.uow.commit()

        for event in events:
            await self.event_dispatcher.dispatch(event)

        return LoginResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="Bearer",
            expires_in=3600,
            session_id=str(session.id),
        )