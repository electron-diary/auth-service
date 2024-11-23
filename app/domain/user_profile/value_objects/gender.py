from dataclasses import dataclass
from typing import Literal, Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidGenderException

GenderT = Literal["male", "female"]

@dataclass(frozen=True)
class Gender(CommonDomainValueObject):
    gender: GenderT | None

    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.gender, str):
                raise InvalidGenderException(
                    message=f"Gender must be a string, not {type(self.gender)}",
                )
            if self.gender not in ["male", "female"]:
                raise InvalidGenderException(
                    message="Gender must be 'male' or 'female'",
                )
