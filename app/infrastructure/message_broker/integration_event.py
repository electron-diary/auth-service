from dataclasses import dataclass
from typing import Any
from uuid import UUID


@dataclass(frozen=True)
class IntegrationEvent:
    id: UUID
    event_name: str
    event: dict[str, Any]
