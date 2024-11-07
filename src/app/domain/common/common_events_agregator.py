from typing import Self

from app.domain.common.common_event import CommonDomainEvent
from app.domain.exceptions.events_exception import EventValidationError


class EventsAgregator:
    def __init__(self: Self) -> None:
        self.events: list[CommonDomainEvent] = []

    def add_event(self: Self, event: CommonDomainEvent) -> None:
        if not isinstance(event, CommonDomainEvent):
            raise EventValidationError("Invalid event type")
        self.events.append(event)

    def get_events(self: Self) -> list[CommonDomainEvent]:
        return self.events
    
    def remove_events(self: Self) -> None:
        self.events = []

    def send_events(self: Self) -> list[CommonDomainEvent]:
        events: list[CommonDomainEvent] = self.get_events()
        self.remove_events()
        return events