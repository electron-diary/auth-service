from abc import abstractmethod
from typing import Protocol

from app.domain.common.uowed import UowedEntity
from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper


class Registry(Protocol):
    @abstractmethod
    def register_mapper(self, entity: type[UowedEntity], mapper: DataMapper) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    def get_mapper(self, entity: type[UowedEntity]) -> DataMapper:
        raise NotImplementedError("Method must be implemented by subclasses")
