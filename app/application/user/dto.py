from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class UserDTO:
    id: UUID
    username: str
    email: str | None
    phone: str | None
    is_deleted: bool
