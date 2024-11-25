from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True)
class DomainEvent:
    event_id: UUID = field(default_factory=uuid4, init=False)
    event_date: datetime = field(default_factory=datetime.now, init=False)
