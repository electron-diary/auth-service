from abc import abstractmethod
from typing import Protocol, Self
from uuid import UUID

from app.application.user.dtos.user_dto import UserDto


class UserReaderInterface(Protocol):
    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UUID) -> UserDto | None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def get_by_email(self: Self, email: str) -> UserDto | None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def get_by_username(self: Self, username: str) -> UserDto | None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def get_by_phone_number(self: Self, phone_number: int) -> UserDto | None:
        raise NotImplementedError("Method must be implemented by subclasses")
