from typing import Self
from uuid import UUID

from app.domain.uowed import UowedEntity
from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.user.vos.user.id import Id
from app.domain.user.vos.address.city import City
from app.domain.user.vos.address.house_location import HouseLocation
from app.domain.user.vos.address.region import Region
from app.domain.user.vos.address.street import Street


class Address(UowedEntity[Id]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: Id,
        city: City,
        region: Region,
        street: Street,
        house_location: HouseLocation
    ) -> None:
        super().__init__(uow=uow, id=id)

        self.city: City = city
        self.region: Region = region
        self.address: Street = street
        self.house_location: HouseLocation = house_location

    @classmethod
    def create(
        cls: type[Self], 
        uow: UnitOfWorkInterface,
        id: UUID,
        city: str,
        region: str,
        street: str,
        house_location: str
    ) -> Self:
        address = cls(
            uow=uow, 
            id=Id(id),
            city=City(city),
            region=Region(region),
            street=Street(street),
            house_location=HouseLocation(house_location)
        )
        address.mark_new()

        return address
    
    def edit_city(self: Self, city: str) -> None:
        self.city = City(city)
        self.mark_dirty()

    def edit_region(self: Self, region: str) -> None:
        self.region = Region(region)
        self.mark_dirty()

    def edit_street(self: Self, street: str) -> None:
        self.street = Street(street)
        self.mark_dirty()

    def edit_house_location(self: Self, house_location: str) -> None:
        self.house_location = HouseLocation(house_location)
        self.mark_dirty()

    def delete(self: Self) -> None:
        self.mark_deleted()