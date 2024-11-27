from dataclasses import asdict

from app.domain.base.domain_event import DomainEvent
from app.infrastructure.persistence.mysql.tables import Events


def event_to_table(event: DomainEvent) -> Events:
    return Events(
        agregate_id=event.agregate_id,
        agregate_type=event.agregate_name,
        event_type=event.event_name,
        event_data=asdict(event),
    )
