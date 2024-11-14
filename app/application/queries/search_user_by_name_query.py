from dataclasses import dataclass

from app.application.base.base_query import BaseQuery


@dataclass(frozen=True)
class SearchUserByNameQuery(BaseQuery):
    user_name: str