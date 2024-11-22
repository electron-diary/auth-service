from dataclasses import dataclass, field
from typing import Self

from app.domain.common.common_domain_event import CommonDomainEvent


@dataclass
class AgregateRoot:
    _events: list[CommonDomainEvent] = field(default_factory=list, init=False)

    def add_event(self: Self, event:CommonDomainEvent) -> None:
        self._events.append(event)

    def push_events(self: Self) -> list[CommonDomainEvent]:
        events: list[CommonDomainEvent] = self._events.copy()
        self._events.clear()
        return events
