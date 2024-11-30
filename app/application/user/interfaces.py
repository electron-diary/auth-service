from abc import abstractmethod
from typing import Protocol, Self
from uuid import UUID

from app.application.user.dtos import UserDTO
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, UserId
from app.domain.user.actions import UserCreated, UsernameUpdated, UserDeleted, UserRestored, ContactsUpdated


class UserWriterGatewayInterface(Protocol):
    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UserId) -> User | None:
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def create_user(self: Self, user: User) -> None:
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def update_user(self: Self, user: User) -> None:
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def check_phone_exist(self: Self, phone_number: Contacts) -> User | None:
        raise NotImplementedError("method must be implemented by subclasses")


class UserReaderGatewayInterface(Protocol):
    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UUID) -> UserDTO | None:
        raise NotImplementedError("method must be implemented by subclasses")


class UserProjectionsGatewayInterface(Protocol):
    @abstractmethod
    async def add_user(self: Self, event: UserCreated) -> None:
        raise NotImplementedError("method must be implemented by subclasses")
    
    @abstractmethod
    async def update_username(self: Self, event: UsernameUpdated) -> None:
        raise NotImplementedError("method must be implemented by subclasses")
    
    @abstractmethod
    async def delete_user(self: Self, event: UserDeleted) -> None:
        raise NotImplementedError("method must be implemented by subclasses")
    
    @abstractmethod
    async def restore_user(self: Self, event: UserRestored) -> None:
        raise NotImplementedError("method must be implemented by subclasses")
    
    @abstractmethod
    async def update_contacts(self: Self, event: ContactsUpdated) -> None:
        raise NotImplementedError("method must be implemented by subclasses")


