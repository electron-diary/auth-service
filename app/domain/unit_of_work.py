from typing import Self, Protocol
from abc import abstractmethod


class UnitOfWork(Protocol):
    @abstractmethod
    async def commit(self: Self) -> None:
        raise NotImplementedError('Method must be implemented by subclasses')
    
    @abstractmethod
    def register_clean(self: Self) -> None:
        raise NotImplementedError('Method must be implemented by subclasses')
    
    @abstractmethod
    def register_dirty(self: Self) -> None:
        raise NotImplementedError('Method must be implemented by subclasses')