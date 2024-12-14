from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ChangeUsernameCommand:
    user_id: UUID
    username: str
