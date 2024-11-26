from abc import abstractmethod
from typing import Protocol, Self
from uuid import UUID

from app.application.user.dto import UserDTO
from app.domain.user.user import User
from app.domain.user.value_objects import UserId, Contacts, Username, DeleteDate


class UserWriterRepository(Protocol):
    @abstractmethod
    async def save_user(self: Self, user: User) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

    @abstractmethod
    async def update_contacts(self: Self, user_id: UserId, contacts: Contacts) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

    @abstractmethod
    async def restore_user(self: Self, user_id: UserId, delete_date: DeleteDate) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

    @abstractmethod
    async def delete_user(self: Self, user_id: UserId, delete_date: DeleteDate) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

    @abstractmethod
    async def update_username(self: Self, user_id: UserId, username: Username) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

class UserReaderRepository(Protocol):
    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UUID) -> UserDTO:
        raise NotImplementedError("method must be implemnted by subclasses")
    
    @abstractmethod
    async def get_users(self: Self) -> list[UserDTO]:
        raise NotImplementedError("method must be implemnted by subclasses")
