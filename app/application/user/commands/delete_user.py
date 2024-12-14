from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class DeleteUserCommand:
    user_id: UUID