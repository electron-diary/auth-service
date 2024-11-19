from dataclasses import dataclass

from app.domain.base.base_value_object import BaseDomainValueObject


@dataclass
class BaseDomainEntity[EntityUUID: BaseDomainValueObject]:
    uuid: EntityUUID
