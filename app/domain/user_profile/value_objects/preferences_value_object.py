from typing import Self
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class PreferenciesValueObject(CommonDomainValueObject[list[str] | None]):
    def __post_init__(self: Self) -> None:
        ...