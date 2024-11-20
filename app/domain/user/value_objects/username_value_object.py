from typing import Self
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UserNameValueObject(CommonDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not isinstance(self.to_raw(), str):
            raise ...
        if len(self.to_raw()) < ...:
            raise ...
        if len(self.to_raw()) > ...:
            raise ...