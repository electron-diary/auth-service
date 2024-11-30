from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class UserDTO:
    user_id: UUID
    phone_number: int
    is_deleted: bool
    username: str
