from typing import Self
from dataclasses import dataclass


@dataclass(frozen=True)
class CommonDomainValueObject[Object]:
    _object: Object

    def to_raw(self: Self) -> Object:
        return self._object
    
    def __post_init__(self: Self) -> None:
        ...