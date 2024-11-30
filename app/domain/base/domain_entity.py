from dataclasses import dataclass


@dataclass
class DomainEntity[EntityId]:
    id: EntityId

