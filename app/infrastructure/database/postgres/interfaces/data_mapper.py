from abc import abstractmethod
from typing import Protocol

from app.domain.common.uowed import UowedEntity


class DataMapper(Protocol):
    @abstractmethod
    async def add(self, entity: UowedEntity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def delete(self, entity: UowedEntity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def update(entity: UowedEntity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
