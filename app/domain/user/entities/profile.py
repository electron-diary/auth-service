from typing import Self

from app.domain.user.value_objects.address import Address
from app.domain.user.value_objects.fullname import Fullname
from app.domain.user.value_objects.gender import Gender
from app.domain.user.value_objects.profile_pictures import ProfilePictures
from app.domain.user.value_objects.age import Age
from app.domain.user.value_objects.id import Id


class Profile:
    def __init__(
        self: Self,
        profile_id: Id,
        age: Age,
        gender: Gender,
        fullname: Fullname,
        address: Address,
        pictures: ProfilePictures
    ) -> None:
        self.profile_id: Id = profile_id
        self.age: Age = age
        self.gender: Gender = gender
        self.fullname: Fullname = fullname
        self.address: Address = address
        self.pictures: ProfilePictures = pictures

    def edit_age(self: Self, age: Age) -> None:
        self.age = age

    def edit_gender(self: Self, gender: Gender) -> None:
        self.gender = gender

    def edit_address(self: Self, address: Address) -> None:
        self.address = address

    def edit_fullname(self: Self, fullname: Fullname) -> None:
        self.fullname = fullname

    def edit_pictures(self: Self, pictures: ProfilePictures) -> None:
        self.pictures = pictures
