from abc import abstractmethod
from typing import Protocol, Self

from app.domain.user.entities.user import User
from app.domain.user.value_objects.id import Id


class UserRepository(Protocol):
    @abstractmethod
    async def add(self: Self, user: User) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def update(self: Self, user: User) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def load(self: Self, user_id: Id) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")
