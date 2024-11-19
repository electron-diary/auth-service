from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Message:
    message_uuid: UUID = field(default=uuid4(), init=False)
    data: str = ""
