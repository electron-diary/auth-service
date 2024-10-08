from typing import Self
from dataclasses import dataclass


@dataclass(frozen=True)
class DomainValueObject[ObjectType]:
    object: ObjectType

    def validate(self: Self) -> None:
        pass

    def to_raw(self: Self) -> ObjectType:
        return self.object

    def __post_init__(self: Self) -> None:
        self.validate()