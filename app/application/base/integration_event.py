from dataclasses import dataclass, asdict
from datetime import datetime
from uuid import UUID

from app.domain.base.base_event import BaseDomainEvent


@dataclass(frozen=True)
class IntegrationEvent:
    uuid: UUID
    event_timestamp: datetime
    event_name: str
    event_data: dict[str]

    @staticmethod
    def from_domain_to_integration_event(event: BaseDomainEvent) -> "IntegrationEvent":
        integration_event: IntegrationEvent = IntegrationEvent(
            uuid=event.uuid,
            event_name=event.__class__.__name__,
            event_data=asdict(obj=event),
            event_timestamp=event.event_timestamp
        )
        return integration_event