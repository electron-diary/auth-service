from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.enums.middle_name_enums import MiddleNameEnums
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidMiddleNameException


@dataclass(frozen=True)
class MiddleNameValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise InvalidMiddleNameException(
                    message=f"Middle name must be a string, not {type(self.to_raw())}",
                )
            if len(self.to_raw()) > MiddleNameEnums.max_middle_name_characters:
                raise InvalidMiddleNameException(
                    message=f"Middle name must be less than {MiddleNameEnums.max_middle_name_characters} characters",
                )
            if len(self.to_raw()) < MiddleNameEnums.min_middle_name_characters:
                raise InvalidMiddleNameException(
                    message=f"Middle name must be more than {MiddleNameEnums.min_middle_name_characters} characters",
                )
