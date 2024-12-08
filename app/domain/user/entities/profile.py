from typing import Self

from app.domain.unit_of_work import UowTracker
from app.domain.uowed import UowedEntity
from app.domain.user.value_objects.address import Address
from app.domain.user.value_objects.age import Age
from app.domain.user.value_objects.fullname import Fullname
from app.domain.user.value_objects.gender import Gender
from app.domain.user.value_objects.id import Id
from app.domain.user.value_objects.profile_pictures import ProfilePictures


class Profile(UowedEntity[Id]):
    def __init__(
        self: Self,
        profile_id: Id,
        age: Age,
        uow: UowTracker,
        gender: Gender,
        fullname: Fullname,
        address: Address,
        pictures: ProfilePictures,
    ) -> None:
        super().__init__(uow=uow, id=profile_id)

        self.profile_id: Id = profile_id
        self.age: Age = age
        self.gender: Gender = gender
        self.fullname: Fullname = fullname
        self.address: Address = address
        self.pictures: ProfilePictures = pictures

    @classmethod
    def create(
        cls: type[Self],
        age: Age,
        profile_id: Id,
        gender: Gender,
        fullname: Fullname,
        address: Address,
        pictures: ProfilePictures,
        uow: UowTracker,
    ) -> Self:
        profile = cls(
            profile_id=profile_id,
            age=age,
            gender=gender,
            fullname=fullname,
            address=address,
            pictures=pictures,
            uow=uow,
        )
        profile.mark_new()

        return profile

    def edit_age(self: Self, age: Age) -> None:
        self.age = age
        self.mark_dirty()

    def edit_gender(self: Self, gender: Gender) -> None:
        self.gender = gender
        self.mark_dirty()

    def edit_address(self: Self, address: Address) -> None:
        self.address = address
        self.mark_dirty()

    def edit_fullname(self: Self, fullname: Fullname) -> None:
        self.fullname = fullname
        self.mark_dirty()

    def edit_pictures(self: Self, pictures: ProfilePictures) -> None:
        self.pictures = pictures
        self.mark_dirty()
