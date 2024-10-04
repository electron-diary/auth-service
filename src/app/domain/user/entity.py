from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.app.domain.common.entity import DomainEntity
from src.app.domain.user.value_objects import UserUUID
from src.app.domain.user.value_objects import UserName
from src.app.domain.user.value_objects import UserContact
from src.app.domain.user.value_objects import UserPassword
from src.app.domain.user.value_objects import UserIp
from src.app.domain.user.value_objects import UserCreatedAt
from src.app.domain.user.value_objects import UserUpdatedAt
from src.app.domain.user.value_objects import UserRefreshToken
from src.app.domain.user.value_objects import UserStatus


@dataclass
class UserEntity(DomainEntity[UserUUID]):
    uuid: UserUUID
    user_name: UserName
    user_contact: UserContact
    user_password: UserPassword
    user_status: UserStatus
    user_created_at: UserCreatedAt
    user_updated_at: UserUpdatedAt

    @staticmethod
    def create(
        uuid: UUID, 
        user_name: str,
        user_contact: str | int,
        user_password: str,
        user_status: str,
        user_created_at: datetime,
        user_updated_at: datetime,
    ) -> 'UserEntity':
        return UserEntity(
            uuid=UserUUID(object=uuid),
            user_name=UserName(object=user_name),
            user_contact=UserContact(object=user_contact),
            user_password=UserPassword(object=user_password),
            user_status=user_status,
            user_created_at=UserCreatedAt(user_created_at),
            user_updated_at=UserUpdatedAt(user_updated_at),
        )
