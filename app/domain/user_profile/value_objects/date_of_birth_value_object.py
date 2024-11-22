from dataclasses import dataclass
from datetime import date
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidDateOfBirthException


@dataclass(frozen=True)
class DateOfBirthValueObject(CommonDomainValueObject):
    birth_date: date | None

    def __post_init__(self: Self) -> None:
        if self.birth_date:
            if not isinstance(self.birth_date, date):
                raise InvalidDateOfBirthException(
                    message=f"Date of birth must be a date, not {type(self.birth_date)}",
                )
            if self.birth_date > date.today():
                raise InvalidDateOfBirthException(
                    message=f"Date of birth must be less than {date.today()}",
                )

