from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class UserDTO:
    id: UUID
    username: str
    email: str | None
    phone: str | None
    created_at: datetime
    delete_date: datetime | None