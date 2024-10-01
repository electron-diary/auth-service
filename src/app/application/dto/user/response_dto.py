from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.app.domain.user.entity import UserEntity


@dataclass(frozen=True)
class GetUserResponse:
    uuid: UUID
    user_name: str
    user_contact: str
    user_status: bool
    user_created_at: datetime
    user_updated_at: datetime

    @staticmethod
    def from_entity(user: UserEntity) -> 'GetUserResponse':
        return GetUserResponse(
            uuid=user.uuid,
            user_name=user.user_name,
            user_contact=user.user_contact,
            user_status=user.user_status,
            user_created_at=user.user_created_at,
            user_updated_at=user.user_updated_at
        )