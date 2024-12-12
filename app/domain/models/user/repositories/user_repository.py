from typing import Self, Protocol
from abc import abstractmethod
from uuid import UUID

from app.domain.models.user.entities.user import User


class ProfileRepository(Protocol):
    @abstractmethod
    async def load(self: Self, user_id: UUID) -> User:
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