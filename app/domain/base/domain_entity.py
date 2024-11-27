from dataclasses import dataclass

from app.domain.base.domain_vo import DomainVO


@dataclass
class DomainEntity[EntityId: DomainVO]:
    id: EntityId
