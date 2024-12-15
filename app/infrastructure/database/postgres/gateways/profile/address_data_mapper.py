from typing import Self

from sqlalchemy.ext.asyncio import AsyncConnection

from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper
from app.domain.profile.entities.address import Address


class AddressDataMapper(DataMapper):
    def __init__(
        self: Self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def add(self: Self, entity: Address) -> None:
        stmt = """
            INSERT INTO addresses
                address_id,
                address_owner_id,
                country,
                city,
                street,
                house_number,
                apartament_number,
                postal_code,
            VALUES
                (?, ?, ?, ?, ?, ?, ?, ?)
        """
        await self.connection.execute(
            stmt,
            (
                entity.id,
                entity.profile_id,
                entity.country,
                entity.city,
                entity.street,
                entity.house_number,
                entity.apartament_number,
                entity.postal_code,
            ),
        )

    async def delete(self: Self, entity: Address) -> None:
        stmt = """
            DELETE FROM addresses
            WHERE address_id = ?
        """
        await self.connection.execute(stmt, (entity.id,))

    async def update(self: Self, entity: Address) -> None:
        ...
