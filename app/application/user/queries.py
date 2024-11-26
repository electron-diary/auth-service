from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetUserByIdQuery:
    user_id: UUID
