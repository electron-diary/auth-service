from dataclasses import dataclass
from typing import Self

from app.domain.common.common_exceptions import DomainValidationError
from app.domain.common.common_value_object import CommonDomainValueObject
from app.domain.enums.user_fullname_enum import UserFullnameEnums


@dataclass(frozen=True)
class UserLastNameValueObject(CommonDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "User last name cannot be empty",
            )
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                f"User last name must be a string, get {type(self.to_raw())}",
            )
        if len(self.to_raw()) < UserFullnameEnums.user_last_name_min_length:
            raise DomainValidationError(
                f"User last name must be at least {UserFullnameEnums.user_last_name_min_length} characters long",
            )
        if len(self.to_raw()) > UserFullnameEnums.user_last_name_max_length:
            raise DomainValidationError(
                f"User last name must be less than {UserFullnameEnums.user_last_name_max_length} characters long",
            )
