from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ChangeContactsCommand:
    user_id: UUID
    email: str | None
    phone: int | None
