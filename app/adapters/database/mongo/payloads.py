from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class MongoEvent:
    uuid: str
    event_json: bytes
    timestamp: str = field(default=str(datetime.now().isoformat()), init=False)
    event_name: str
