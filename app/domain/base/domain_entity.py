from typing import Self
from dataclasses import dataclass

from app.domain.base.domain_event import DomainEvent


@dataclass
class DomainEntity[EntityId]:
    id: EntityId

