from abc import abstractmethod
from typing import Protocol, Self

from app.domain.unit_of_work import UnitOfWorkTrackerInterface


class UnitOfWorkCommitterInterace(Protocol):
    @abstractmethod
    async def commit(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def rollback(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def flush(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")


class UnitOfWorkInterface(UnitOfWorkCommitterInterace, UnitOfWorkTrackerInterface):
    ...
