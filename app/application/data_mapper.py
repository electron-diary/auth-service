from typing import Self, Protocol
from abc import abstractmethod

from app.domain.uowed import UowedEntity


class DataMapperInterface[T: UowedEntity](Protocol):
    @abstractmethod
    async def add(self: Self, entity: T) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
    
    @abstractmethod
    async def delete(self: Self, entity: T) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
    
    @abstractmethod
    async def update(self: Self, entity: T) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")