from dataclasses import dataclass
from typing import Self

from app.domain.base.base_value_object import BaseDomainValueObject
from app.domain.enums.user_fullname_enum import UserFullnameEnums
from app.domain.exceptions.value_objects_exceptions import (
    LastNameRequiredError,
    LastNameTypeError,
    MaximalLenghtLastNameError,
)


@dataclass(frozen=True)
class UserLastNameValueObject(BaseDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            msg = "User last name cannot be empty"
            raise LastNameRequiredError(
                msg,
            )
        if not isinstance(self.to_raw(), str):
            msg = f"User last name must be a string, get {type(self.to_raw())}"
            raise LastNameTypeError(
                msg,
            )
        if len(self.to_raw()) < UserFullnameEnums.user_last_name_min_length:
            msg = f"User last name must be at least {UserFullnameEnums.user_last_name_min_length} characters long"
            raise MaximalLenghtLastNameError(
                msg,
            )
        if len(self.to_raw()) > UserFullnameEnums.user_last_name_max_length:
            msg = f"User last name must be less than {UserFullnameEnums.user_last_name_max_length} characters long"
            raise MaximalLenghtLastNameError(
                msg,
            )
