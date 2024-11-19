from abc import ABC
from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class BaseDomainEvent(ABC):
    uuid: UUID
