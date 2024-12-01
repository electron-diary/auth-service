from dataclasses import dataclass
from uuid import UUID

from app.application.base.base_query import BaseQuery


@dataclass(frozen=True)
class GetUserQuery(BaseQuery):
    user_id: UUID
