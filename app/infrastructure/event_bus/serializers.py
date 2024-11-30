from dataclasses import asdict
from datetime import datetime
from json import dumps
from typing import Any
from uuid import UUID

from app.infrastructure.event_bus.events import IntegrationEvent


def exclude_invalid_types(obj: object) -> Any:
    if isinstance(obj, UUID):
        return str(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()

def integration_event_to_json(event: IntegrationEvent) -> str:
    return dumps(obj=asdict(event), default=exclude_invalid_types)
