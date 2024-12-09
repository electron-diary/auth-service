from abc import abstractmethod
from typing import Protocol, Self


class UnitOfWorkInterface(Protocol):
    @abstractmethod
    def register_new(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def register_dirty(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def register_deleted(self: Self) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
