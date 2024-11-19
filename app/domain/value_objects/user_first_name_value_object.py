from dataclasses import dataclass
from typing import Self

from app.domain.base.base_value_object import BaseDomainValueObject
from app.domain.enums.user_fullname_enum import UserFullnameEnums
from app.domain.exceptions.value_objects_exceptions import (
    FirstNameRequiredError,
    FirstNameTypeError,
    MaximalLenghtFirstNameError,
    MinimalLenghtFirstNameError,
)


@dataclass(frozen=True)
class UserFirstNameValueObject(BaseDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            msg = "User first name cannot be empty"
            raise FirstNameRequiredError(
                msg,
            )
        if not isinstance(self.to_raw(), str):
            msg = f"User first name must be a string, get {type(self.to_raw())}"
            raise FirstNameTypeError(
                msg,
            )
        if len(self.to_raw()) < UserFullnameEnums.user_first_name_min_length:
            msg = f"User first name must be at least {UserFullnameEnums.user_first_name_min_length} characters long"
            raise MinimalLenghtFirstNameError(
                msg,
            )
        if len(self.to_raw()) > UserFullnameEnums.user_first_name_max_length:
            msg = f"User first name must be less than {UserFullnameEnums.user_first_name_max_length} characters long"
            raise MaximalLenghtFirstNameError(
                msg,
            )
