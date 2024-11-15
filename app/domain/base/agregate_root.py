from dataclasses import dataclass, field
from typing import Self

from app.domain.base.base_event import CommonDomainEvent
from app.domain.exceptions.events_exception import EventsNotFoundError, EventValidationError


@dataclass
class AgregateRoot:
    events: list[CommonDomainEvent] = field(default_factory=list, init=False)

    def add_event(self: Self, event: CommonDomainEvent) -> None:
        if not isinstance(event, CommonDomainEvent):
            raise EventValidationError("Invalid event type")
        self.events.append(event)

    def send_events(self: Self) -> list[CommonDomainEvent]:
        if len(self.events) == 0:
            raise EventsNotFoundError("No events to send")
        events: list[CommonDomainEvent] = self.events.copy()
        self.events.clear()
        return events
