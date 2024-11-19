from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime


@dataclass(frozen=True)
class BaseDomainEvent:
    uuid: UUID = field(default_factory=uuid4, init=False)
    event_timestamp: datetime = field(default_factory=datetime.now, init=False)