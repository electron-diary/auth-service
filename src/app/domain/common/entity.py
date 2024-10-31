from typing import Self
from dataclasses import dataclass

from app.domain.common.value_objects import DomainValueObject

@dataclass
class DomainEntity[EntityId: DomainValueObject]:
    uuid: EntityId

