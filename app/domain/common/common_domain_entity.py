from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject


@dataclass
class CommonDomainEntity[EntityId: CommonDomainValueObject]:
    id: EntityId


