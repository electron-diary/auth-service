from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class DomainEvent:
    aggregate_id: UUID
    occurred_at: datetime = field(default_factory=datetime.now, init=False)
    event_type: str
    agregate_name: str