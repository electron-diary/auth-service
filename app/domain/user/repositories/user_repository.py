from abc import abstractmethod
from typing import Protocol, Self
from uuid import UUID

from app.domain.user.entities.user import User


class UserRepository(Protocol):
    @abstractmethod
    async def load(self: Self, user_id: UUID) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def add(self: Self, user: User) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def update(self: Self, user: User) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def delete(self: Self, user_id: UUID) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
    
    @abstractmethod
    async def check_phone_number_exists(self: Self, phone_number: int) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")
    
    @abstractmethod
    async def check_email_exists(self: Self, email: str) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")
    
    @abstractmethod
    async def check_username_exists(self: Self, username: str) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")
