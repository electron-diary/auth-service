from typing import Self
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UserEmailValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise ...
            if len(self.to_raw()) > ...:
                raise ...
            if len(self.to_raw()) < ...:
                raise ...