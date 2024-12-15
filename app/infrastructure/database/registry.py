from typing import Self

from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapperInterface
from app.domain.uowed import UowedEntity
from app.infrastructure.database.postgres.interfaces.registry import RegistryInterface


class Registry(RegistryInterface):
    def __init__(self: Self) -> None:
        self.data_mappers: dict[type[UowedEntity], DataMapperInterface] = dict()

    def register_mapper(self: Self, entity: type[UowedEntity], mapper: DataMapperInterface) -> None:
        self.data_mappers[entity] = mapper

    def get_mapper(self: Self, entity: type[UowedEntity]) -> DataMapperInterface:
        mapper = self.data_mappers[entity]
        if not mapper:
            raise ValueError(f"Mapper for {entity} not registered")
        
        return mapper