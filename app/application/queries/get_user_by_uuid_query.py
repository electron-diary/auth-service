from dataclasses import dataclass
from uuid import UUID

from app.application.base.base_query import BaseQuery


@dataclass(frozen=True)
class GetUserByUUIDQuery(BaseQuery):
    user_uuid: UUID
