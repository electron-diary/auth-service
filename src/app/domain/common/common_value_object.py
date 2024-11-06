from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class CommonDomainValueObject[ObjectType]:
    object: ObjectType

    def to_raw(self: Self) -> ObjectType:
        return self.object

    def validate(self: Self) -> None:
        ...

    def __post_init__(self: Self) -> None:
        self.validate()
