from typing import Protocol
from abc import abstractmethod


class UnitOfWork(Protocol):
    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError('method must be implemented by subclasses')

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError('method must be implemented by subclasses')