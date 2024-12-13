from typing import Self
from uuid import UUID

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity


class Address(UowedEntity[UUID]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        address_id: UUID,
        city: str,
        country: str,
        street: str,
        house_number: str,
        apartment_number: str,
        postal_code: str,
    ) -> None:
        super().__init__(uow=uow, id=address_id)

        self.city = city
        self.country = country
        self.street = street
        self.house_number = house_number
        self.apartament_number = apartment_number
        self.postal_code = postal_code

    @classmethod
    def create_address(
        cls: type[Self],
        uow: UnitOfWorkInterface,
        address_id: UUID,
        city: str,
        country: str,
        street: str,
        house_number: str,
        apartment_number: str,
        postal_code: str,
    ) -> Self:
        address = cls(
            uow=uow,
            address_id=address_id,
            city=city,
            country=country,
            street=street,
            house_number=house_number,
            apartment_number=apartment_number,
            postal_code=postal_code,
        )
        address.mark_new()

        return address

    def change_address(
        self: Self,
        city: str,
        country: str,
        street: str,
        house_number: str,
        apartment_number: str,
        postal_code: str,
    ) -> None:
        self.city = city
        self.country = country
        self.street = street
        self.house_number = house_number
        self.apartament_number = apartment_number
        self.postal_code = postal_code

        self.mark_dirty()

    def delete_address(self: Self) -> None:
        self.mark_deleted()
