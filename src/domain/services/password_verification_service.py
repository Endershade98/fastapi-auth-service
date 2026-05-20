# src/domain/services/password_verification_service.py

class PasswordVerificationService:

    @staticmethod
    def verify(
        plain_password: str,
        password_hash: str,
        hasher
    ) -> bool:
        return hasher.verify(
            plain_password,
            password_hash
        )