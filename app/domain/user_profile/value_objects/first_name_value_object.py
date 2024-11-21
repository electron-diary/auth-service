from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidFirstNameException
from app.domain.user_profile.enums.first_name_enums import FirstNameEnums


@dataclass(frozen=True)
class FirstNameValueObject(CommonDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise InvalidFirstNameException(
                message="First name must not be empty",
            )
        if not isinstance(self.to_raw(), str):
            raise InvalidFirstNameException(
                message=f"First name must be a string, not {type(self.to_raw())}",
            )
        if len(self.to_raw()) > FirstNameEnums.max_first_name_characters:
            raise InvalidFirstNameException(
                message=f"First name must be less than {FirstNameEnums.max_first_name_characters} characters",
            )
        if len(self.to_raw()) < FirstNameEnums.min_first_name_characters:
            raise InvalidFirstNameException(
                message=f"First name must be greater than {FirstNameEnums.min_first_name_characters} characters",
            )
