from abc import abstractmethod
from typing import Protocol, Self

from app.application.data_mapper import DataMapperInterface
from app.domain.uowed import UowedEntity


class RegistryInterface(Protocol):
    @abstractmethod
    def register_mapper(self: Self, entity: type[UowedEntity], mapper: DataMapperInterface) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def get_mapper(self: Self, entity: type[UowedEntity]) -> DataMapperInterface:
        raise NotImplementedError("Method must be implemented by subclasses")
