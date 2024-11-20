from typing import Self, Literal
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject


GenderT = Literal['male', 'female']

@dataclass(frozen=True)
class GenderValueObject(CommonDomainValueObject[GenderT | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise ...
            if self.to_raw() not in ['male', 'female']:
                raise ...