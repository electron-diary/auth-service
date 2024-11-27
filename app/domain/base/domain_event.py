from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class DomainEvent:
    agregate_id: UUID
    agregate_name: str
    event_name: str
