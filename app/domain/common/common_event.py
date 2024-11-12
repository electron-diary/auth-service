from dataclasses import dataclass

from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class CommonDomainEvent[EventUUID: CommonDomainValueObject, EventDate: CommonDomainValueObject]:
    event_uuid: EventUUID
    event_start_execution_time: EventDate
