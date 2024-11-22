from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True)
class CommonDomainEvent:
    event_uuid: UUID  = field(default_factory=uuid4, init=False)
    event_timestamp: datetime = field(default_factory=datetime.now, init=False)
