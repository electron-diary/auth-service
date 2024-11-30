from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetUserQuery:
    user_id: UUID