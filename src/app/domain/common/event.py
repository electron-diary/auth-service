from dataclasses import dataclass
from typing import Protocol
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class DomainEvent(Protocol):
    domain_event_uuid: UUID
    domain_event_date: datetime