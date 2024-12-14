from typing import Self

from app.domain.domain_event import DomainEvent


class AgregateRoot:
    def __init__(self: Self) -> None:
        self.domain_events: list[DomainEvent] = []

    def record_event(self: Self, event: DomainEvent) -> None:
        self.domain_events.append(event)

    def push_events(self: Self) -> list[DomainEvent]:
        events = self.domain_events.copy()
        self.domain_events.clear()

        return events
