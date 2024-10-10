from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, kw_only=True)
class Message:
    id: UUID 
    data: dict[str]