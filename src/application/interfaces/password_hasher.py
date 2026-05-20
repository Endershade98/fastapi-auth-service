# src/application/interfaces/password_hasher.py

from abc import ABC, abstractmethod


class PasswordHasher(ABC):

    @abstractmethod
    def verify(
        self,
        plain_value: str,
        hashed_value: str,
    ) -> bool:
        raise NotImplementedError

    @abstractmethod
    def hash(
        self,
        plain_value: str,
    ) -> str:
        raise NotImplementedError