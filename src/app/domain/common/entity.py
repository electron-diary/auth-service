from typing import Self
from dataclasses import dataclass

from src.app.domain.common.value_objects import DomainValueObject

@dataclass
class DomainEntity[EntityId: DomainValueObject]:
    id: EntityId

