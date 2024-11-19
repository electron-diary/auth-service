from dataclasses import dataclass, field
from datetime import datetime
from bson import ObjectId
from uuid import UUID
from typing import Optional

@dataclass(frozen=True)
class MongoEvent:
    uuid: str
    event_json: bytes
    timestamp: str = field(default=str(datetime.now().isoformat()), init=False)
    event_name: str
