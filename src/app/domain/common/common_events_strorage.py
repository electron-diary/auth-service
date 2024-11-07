from dataclasses import dataclass, field

from app.domain.common.common_event import CommonDomainEvent


@dataclass
class TemporaryEventStorage:
    events: list[CommonDomainEvent] = field(default_factory=list, init=False)