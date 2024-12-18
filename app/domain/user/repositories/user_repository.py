from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from app.domain.user.entities.user import User


class UserRepository(Protocol):
    @abstractmethod
    async def load(self, user_id: UUID) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def check_phone_number_exists(self, phone_number: int) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def check_email_exists(self, email: str) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def check_username_exists(self, username: str) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")
