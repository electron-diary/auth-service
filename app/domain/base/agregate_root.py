from typing import Self
from dataclasses import dataclass, field

from app.domain.base.domain_event import DomainEvent


@dataclass
class AgregateRoot:
    _events: list[DomainEvent] = field(default_factory=list, init=False)
    
    def _add_event(self: Self, event: DomainEvent) -> None:
        self._events.append(event)

    def get_events(self: Self) -> list[DomainEvent]:
        actions: list[DomainEvent] = self._events.copy()
        self._events.clear()
        return actions
    
    def _apply(self: Self, event: DomainEvent) -> None:
        ...
    
    def replay_events(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            self._apply(event=event)