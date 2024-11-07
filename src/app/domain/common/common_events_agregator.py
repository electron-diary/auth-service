from dataclasses import dataclass
from typing import Self

from app.domain.common.common_event import CommonDomainEvent
from app.domain.common.common_events_strorage import TemporaryEventStorage
from app.domain.exceptions.events_exception import EventsNotFoundError, EventValidationError


@dataclass
class EventsAgregator(TemporaryEventStorage):

    def add_event(self: Self, event: CommonDomainEvent) -> None:
        if not isinstance(event, CommonDomainEvent):
            raise EventValidationError("Invalid event type")
        self.events.append(event)

    def get_events(self: Self) -> list[CommonDomainEvent]:
        if len(self.events) == 0:
            raise EventsNotFoundError("No events to get")
        return self.events

    def remove_events(self: Self) -> None:
        if len(self.events) == 0:
            raise EventsNotFoundError("No events to remove")
        self.events.clear()

    def send_events(self: Self) -> list[CommonDomainEvent]:
        if len(self.events) == 0:
            raise EventsNotFoundError("No events to send")
        events: list[CommonDomainEvent] = self.get_events()
        self.remove_events()
        return events
