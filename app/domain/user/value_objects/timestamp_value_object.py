from typing import Self
from dataclasses import dataclass
from datetime import datetime

from app.domain.common.common_domain_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class TimestampValueObject(CommonDomainValueObject[datetime]):
    def __post_init__(self: Self) -> None:
        if not isinstance(self.to_raw(), datetime):
            raise ...
        if self.to_raw() > ...:
            raise ...
        if self.to_raw() < ...:
            raise ...