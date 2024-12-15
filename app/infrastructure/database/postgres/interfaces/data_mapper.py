from abc import abstractmethod
from typing import Protocol, Self

from app.domain.common.uowed import UowedEntity


class DataMapper(Protocol):
    @abstractmethod
    async def add(self: Self, entity: UowedEntity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def delete(self: Self, entity: UowedEntity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def update(self: Self, entity: UowedEntity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
