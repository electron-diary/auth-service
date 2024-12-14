from abc import abstractmethod
from typing import Protocol, Self


class UnitOfWorkInterface(Protocol):
    @abstractmethod
    async def commit(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def rollback(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def flush(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
    
    @abstractmethod
    def register_new(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def register_dirty(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def register_deleted(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
