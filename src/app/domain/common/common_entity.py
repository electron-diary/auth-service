from dataclasses import dataclass

from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass
class CommonDomainEntity[EntityUUID: CommonDomainValueObject]:
    user_uuid: EntityUUID
