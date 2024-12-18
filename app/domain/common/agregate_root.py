
from app.domain.common.domain_event import DomainEvent


class AgregateRoot:
    def __init__(self) -> None:
        self.domain_events: list[DomainEvent] = []

    def record_event(self, event: DomainEvent) -> None:
        self.domain_events.append(event)

    def push_events(self) -> list[DomainEvent]:
        events = self.domain_events.copy()
        self.domain_events.clear()

        return events
