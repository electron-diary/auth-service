from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True)
class BaseDomainEvent:
    event_uuid: UUID = field(default=uuid4(), init=False)
    event_start_execution_time: datetime = field(default=datetime.now(), init=False)
