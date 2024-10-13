from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.app.domain.common.entity import DomainEntity
from src.app.domain.user.value_objects import UserUUID
from src.app.domain.user.value_objects import UserName
from src.app.domain.user.value_objects import UserContact
from src.app.domain.user.value_objects import UserCreatedAt
from src.app.domain.user.value_objects import UserUpdatedAt


@dataclass
class UserEntity(DomainEntity[UserUUID]):
    uuid: UserUUID
    user_name: UserName
    user_contact: UserContact
    user_created_at: UserCreatedAt
    user_updated_at: UserUpdatedAt

