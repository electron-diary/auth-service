from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class CommonDomainValueObject[ObjectType]:
    object: ObjectType

    def to_raw(self: Self) -> ObjectType:
        return self.object

