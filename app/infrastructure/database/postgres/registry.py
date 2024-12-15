from typing import Self

from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper
from app.infrastructure.database.postgres.interfaces.registry import Registry
from app.domain.uowed import UowedEntity


class RegistryImpl(Registry):
    def __init__(self: Self) -> None:
        self.data_mappers: dict[type[UowedEntity], DataMapper] = dict()

    def register_mapper(self: Self, entity: type[UowedEntity], mapper: DataMapper) -> None:
        self.data_mappers[entity] = mapper

    def get_mapper(self: Self, entity: type[UowedEntity]) -> DataMapper:
        mapper = self.data_mappers[entity]
        if not mapper:
            raise ValueError(f"Mapper for {entity} not registered")

        return mapper
