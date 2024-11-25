from dataclasses import dataclass

from app.domain.base.base_value_object import BaseValueObject


@dataclass
class DomainEntity[EntityId: BaseValueObject]:
    id: EntityId
