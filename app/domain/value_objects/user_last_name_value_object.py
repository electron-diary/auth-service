from dataclasses import dataclass
from typing import Self

from app.domain.common.common_value_object import CommonDomainValueObject
from app.domain.enums.user_fullname_enum import UserFullnameEnums
from app.domain.exceptions.value_objects_exceptions import (
    LastNameRequiredError,
    LastNameTypeError,
    MaximalLenghtLastNameError,
)


@dataclass(frozen=True)
class UserLastNameValueObject(CommonDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise LastNameRequiredError(
                "User last name cannot be empty",
            )
        if not isinstance(self.to_raw(), str):
            raise LastNameTypeError(
                f"User last name must be a string, get {type(self.to_raw())}",
            )
        if len(self.to_raw()) < UserFullnameEnums.user_last_name_min_length:
            raise MaximalLenghtLastNameError(
                f"User last name must be at least {UserFullnameEnums.user_last_name_min_length} characters long",
            )
        if len(self.to_raw()) > UserFullnameEnums.user_last_name_max_length:
            raise MaximalLenghtLastNameError(
                f"User last name must be less than {UserFullnameEnums.user_last_name_max_length} characters long",
            )
