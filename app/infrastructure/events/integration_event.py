from typing import Any
from uuid import UUID
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class IntegrationEvent:
    id: UUID
    timestamp: datetime
    event_name: str
    event: dict[str | Any]