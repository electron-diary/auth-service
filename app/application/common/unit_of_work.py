from abc import abstractmethod
from typing import Protocol, Self

from app.domain.common.unit_of_work import UnitOfWorkTracker


class UnitOfWorkCommitter(Protocol):
    @abstractmethod
    async def commit(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def rollback(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def flush(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")


class UnitOfWork(UnitOfWorkCommitter, UnitOfWorkTracker):
    ...
