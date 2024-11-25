from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class DomainVO:
    def __post_init__(self: Self) -> None:
        ...
