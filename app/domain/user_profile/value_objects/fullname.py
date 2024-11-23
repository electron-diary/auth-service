from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.enums.first_name_enums import FirstNameEnums
from app.domain.user_profile.enums.last_name_enums import LastNameEnums
from app.domain.user_profile.enums.middle_name_enums import MiddleNameEnums
from app.domain.user_profile.exceptions.user_profile_validation_errors import (
    InvalidFirstNameException,
    InvalidLastNameException,
    InvalidMiddleNameException,
)


@dataclass(frozen=True)
class Fullname(CommonDomainValueObject):
    first_name: str
    middle_name: str | None
    last_name: str

    def __post_init__(self: Self) -> None:
        if not self.first_name:
            raise InvalidFirstNameException(
                message="First name must not be empty",
            )
        if not isinstance(self.first_name, str):
            raise InvalidFirstNameException(
                message=f"First name must be a string, not {type(self.first_name)}",
            )
        if len(self.first_name) > FirstNameEnums.max_first_name_characters:
            raise InvalidFirstNameException(
                message=f"First name must be less than {FirstNameEnums.max_first_name_characters} characters",
            )
        if len(self.first_name) < FirstNameEnums.min_first_name_characters:
            raise InvalidFirstNameException(
                message=f"First name must be greater than {FirstNameEnums.min_first_name_characters} characters",
            )

        if not self.last_name:
            raise InvalidLastNameException(
                message="Last name cannot be empty",
            )
        if not isinstance(self.last_name, str):
            raise InvalidLastNameException(
                message=f"Last name must be a string, not {type(self.last_name)}",
            )
        if len(self.last_name) > LastNameEnums.max_last_name_characters:
            raise InvalidLastNameException(
                message=f"Last name must be less than {LastNameEnums.max_last_name_characters} characters",
            )
        if len(self.last_name) < LastNameEnums.min_last_name_characters:
            raise InvalidLastNameException(
                message=f"Last name must be greater than {LastNameEnums.min_last_name_characters} characters",
            )

        if self.middle_name:
            if not isinstance(self.middle_name, str):
                raise InvalidMiddleNameException(
                    message=f"Middle name must be a string, not {type(self.middle_name)}",
                )
            if len(self.middle_name) > MiddleNameEnums.max_middle_name_characters:
                raise InvalidMiddleNameException(
                    message=f"Middle name must be less than {MiddleNameEnums.max_middle_name_characters} characters",
                )
            if len(self.middle_name) < MiddleNameEnums.min_middle_name_characters:
                raise InvalidMiddleNameException(
                    message=f"Middle name must be more than {MiddleNameEnums.min_middle_name_characters} characters",
                )
