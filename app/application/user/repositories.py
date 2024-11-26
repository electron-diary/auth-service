from abc import abstractmethod
from typing import Protocol, Self
from uuid import UUID

from app.application.user.dto import UserDTO
from app.domain.user.user import User
from app.domain.user.value_objects import UserId


class UserWriterRepository(Protocol):
    @abstractmethod
    async def save_user(self: Self, user: User) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

    @abstractmethod
    async def delete_user(self: Self, user_id: UserId) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

    @abstractmethod
    async def restore_user(self: Self, user_id: UserId) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

    @abstractmethod
    async def update_user(self: Self, user: User) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")


class UserReaderRepository(Protocol):
    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UUID) -> UserDTO:
        raise NotImplementedError("method must be implemnted by subclasses")
