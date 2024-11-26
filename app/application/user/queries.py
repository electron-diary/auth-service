from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetUserByIdQuery:
    user_id: UUID

@dataclass(frozen=True)
class GetUserActionsQuery:
    user_id: UUID

@dataclass(frozen=True)
class GetUsersQuery:
    pass