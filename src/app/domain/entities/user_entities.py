from dataclasses import dataclass

from src.app.domain.value_objects.user_contact_value_object import UserContact
from src.app.domain.value_objects.user_created_at_value_object import UserCreatedAt
from src.app.domain.value_objects.user_name_value_object import UserName
from src.app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from src.app.domain.value_objects.user_uuid_value_object import UserUUID
from src.app.domain.common.entity import DomainEntity
from src.app.domain.value_objects.user_status_value_object import UserStatus


@dataclass
class UserEntity(DomainEntity[UserUUID]):
    uuid: UserUUID
    user_name: UserName
    user_contact: UserContact
    user_created_at: UserCreatedAt
    user_updated_at: UserUpdatedAt
    is_active: UserStatus

