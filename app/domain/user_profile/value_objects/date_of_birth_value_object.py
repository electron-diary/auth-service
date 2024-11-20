from typing import Self
from dataclasses import dataclass
from datetime import date

from app.domain.common.common_domain_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class DateOfBirthValueObject(CommonDomainValueObject[date]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), date):
                raise ...
            if self.to_raw() > ...:
                raise ...
            
            if self.to_raw() < ...:
                raise ...