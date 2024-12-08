from typing import Protocol, Self
from abc import abstractmethod

from app.domain.unit_of_work import UowTracker


class UowTransactionManager(Protocol):
    @abstractmethod
    async def commit(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
    

class UnitOfWork(UowTracker, UowTransactionManager):
    ...