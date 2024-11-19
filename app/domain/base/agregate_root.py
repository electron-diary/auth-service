from dataclasses import dataclass, field
from typing import Any, Self

from app.domain.base.base_event import BaseDomainEvent
from app.domain.exceptions.events_exception import EventsNotFoundError, EventValidationError


@dataclass
class AgregateRoot:
    events: list[BaseDomainEvent] = field(default_factory=list, init=False)

    def add_event(self: Self, event: BaseDomainEvent) -> None:
        if not isinstance(event, BaseDomainEvent):
            msg = "Invalid event type"
            raise EventValidationError(msg)
        self.events.append(event)

    def send_events(self: Self) -> list[BaseDomainEvent]:
        if len(self.events) == 0:
            msg = "No events to send"
            raise EventsNotFoundError(msg)
        events: list[BaseDomainEvent] = self.events.copy()
        self.events.clear()
        return events

    def _apply(self: Self, event: BaseDomainEvent) -> None:
        ...

    def replay_events(self: Self, events: list[BaseDomainEvent]) -> Any:
        ...
