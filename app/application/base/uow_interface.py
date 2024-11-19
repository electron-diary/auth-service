from abc import abstractmethod
from typing import Protocol, Self


class UnitOfWorkInterface(Protocol):
    @abstractmethod
    async def commit(self: Self) -> None:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )

    @abstractmethod
    async def rollback(self: Self) -> None:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )
