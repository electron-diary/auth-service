from abc import abstractmethod
from typing import Protocol, Self

from app.domain.common.uowed import UowedEntity


class UnitOfWorkTracker(Protocol):
    @abstractmethod
    def register_new(self: Self, entity: UowedEntity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def register_dirty(self: Self, entity: UowedEntity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def register_deleted(self: Self, entity: UowedEntity) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
