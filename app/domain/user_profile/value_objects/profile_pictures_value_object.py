from typing import Self
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class ProfilePucturesValueObject(CommonDomainValueObject[list[str] | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), list):
                raise ...
            if len(self.to_raw()) > ...:
                raise ...
            for item in self.to_raw():
                if not isinstance(item, str):
                    raise ...