from dataclasses import dataclass
from typing import Self

from app.domain.base.base_value_object import BaseDomainValueObject
from app.domain.enums.user_fullname_enum import UserFullnameEnums
from app.domain.exceptions.value_objects_exceptions import (
    MaximalLenghtMiddleNameError,
    MiddleNameTypeError,
    MinimalLenghtMiddleNameError,
)


@dataclass(frozen=True)
class UserMiddleNameValueObject(BaseDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                msg = f"User middle name must be a string get {type(self.to_raw())}"
                raise MiddleNameTypeError(
                    msg,
                )
            if len(self.to_raw()) < UserFullnameEnums.user_middle_name_min_length:
                msg = f"User middle name must be at least {UserFullnameEnums.user_middle_name_min_length} characters long"
                raise MinimalLenghtMiddleNameError(
                    msg,
                )
            if len(self.to_raw()) > UserFullnameEnums.user_middle_name_max_lenght:
                msg = f"User middle name must be less than {UserFullnameEnums.user_middle_name_max_lenght} characters long"
                raise MaximalLenghtMiddleNameError(
                    msg,
                )
