from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class CommonDomainValueObject:
    def __post_init__(self: Self) -> None:
        ...
