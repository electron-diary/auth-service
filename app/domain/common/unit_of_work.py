from abc import abstractmethod
from typing import Protocol


class UnitOfWorkTracker(Protocol):
    @abstractmethod
    def register_new(self, entity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def register_dirty(self, entity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def register_deleted(self, entity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
