from typing import Self
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UserPhoneValueObject(CommonDomainValueObject[int | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), int):
                raise ...
            if len(str(self.to_raw())) < ...:
                raise ...
            if len(str(self.to_raw())) > ...:
                raise ...