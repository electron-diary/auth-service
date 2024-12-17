import json
from datetime import datetime
from typing import Any
from uuid import UUID


def exclude_types(obj: object) -> Any:
    if isinstance(obj, UUID):
        return str(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()


def to_json(data: Any) -> bytes | str:
    return json.dumps(obj=data, default=exclude_types)
