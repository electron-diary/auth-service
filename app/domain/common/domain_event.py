from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True)
class DomainEvent:
    event_uuid: UUID = field(default_factory=uuid4, init=False)
    aggregate_id: UUID
    occurred_at: datetime = field(default_factory=datetime.now, init=False)
    event_type: str
    agregate_name: str
