from typing import Protocol, Self
from abc import abstractmethod


class UnitOfWorkInterface(Protocol):
    @abstractmethod
    async def commit(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def rollback(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )