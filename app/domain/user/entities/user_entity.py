from dataclasses import dataclass

from app.domain.common.agregate_root import AgregateRoot
from app.domain.common.common_domain_entity import CommonDomainEntity
from app.domain.user.value_objects.user_contacts_value_object import UserContactsValueObject
from app.domain.user.value_objects.user_uuid_value_object import UserUUID
from app.domain.user.value_objects.username_value_object import UserNameValueObject
from app.domain.user_profile.entities.profile_entity import ProfileEntity


@dataclass
class UserEntity(CommonDomainEntity[UserUUID], AgregateRoot):
    id: UserUUID
    username: UserNameValueObject
    contacts: UserContactsValueObject
    profiles: list[ProfileEntity]
