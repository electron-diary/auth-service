from dataclasses import dataclass
from typing import Self

from app.domain.base.base_value_object import BaseDomainValueObject
from app.domain.enums.user_contact_enum import UserContactEnums
from app.domain.exceptions.value_objects_exceptions import (
    MaximalLenghtUserPhoneError,
    MinimalLenghtUserPhoneError,
)


@dataclass(frozen=True)
class UserPhoneValueObject(BaseDomainValueObject[int | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), int):
                raise TypeError(
                    f"User phone must be an integer, get {type(self.to_raw())}",
                )
            if len(str(self.to_raw())) < UserContactEnums.user_phone_min_lenght:
                raise MinimalLenghtUserPhoneError(
                    f"User phone must be more than {UserContactEnums.user_phone_min_lenght} characters long",
                )
            if len(str(self.to_raw())) > UserContactEnums.user_phone_max_lenght:
                raise MaximalLenghtUserPhoneError(
                    f"User phone must be less than {UserContactEnums.user_phone_max_lenght} characters long",
                )

