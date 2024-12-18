from abc import abstractmethod
from typing import Protocol

from app.domain.common.unit_of_work import UnitOfWorkTracker


class UnitOfWorkCommitter(Protocol):
    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")


class UnitOfWork(UnitOfWorkCommitter, UnitOfWorkTracker):
    ...
