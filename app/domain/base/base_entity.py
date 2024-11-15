from dataclasses import dataclass

from app.domain.base.base_value_object import CommonDomainValueObject


@dataclass
class BaseDomainEntity[EntityUUID: CommonDomainValueObject]:
    user_uuid: EntityUUID
