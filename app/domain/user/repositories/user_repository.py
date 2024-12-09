from abc import abstractmethod
from typing import Protocol, Self

from app.domain.user.entities.user import User


class UserRepository(Protocol):
    @abstractmethod
    def add(self: Self, user: User) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def load(self: Self) -> User | None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def delete(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
