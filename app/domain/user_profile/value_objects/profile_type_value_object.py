from typing import Self, Literal
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject

ProfileT = Literal['verified', 'unverified', 'closed', 'opened']


@dataclass(frozen=True)
class ProfileTypeValueObject(CommonDomainValueObject[list[ProfileT]]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise ...
        if not isinstance(self.to_raw(), list):
            raise ...
        for item in self.to_raw():
            if self.to_raw() not in ['verified', 'unverified', 'closed', 'opened']:
                raise ...