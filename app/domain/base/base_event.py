from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class BaseDomainEvent:
    uuid: UUID
    event_timestamp: datetime = field(default_factory=datetime.now, init=False)
