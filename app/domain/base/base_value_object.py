from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class BaseDomainValueObject[ObjectType]:
    object: ObjectType

    def to_raw(self: Self) -> ObjectType:
        return self.object

    def __post_init__(self: Self) -> None:
        ...

