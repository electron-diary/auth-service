from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetProfileByIdQuery:
    profile_id: UUID
