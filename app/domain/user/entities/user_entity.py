from dataclasses import dataclass

from app.domain.common.common_domain_entity import CommonDomainEntity
from app.domain.user.value_objects.user_contacts import UserContacts
from app.domain.user.value_objects.user_uuid import UserUUID
from app.domain.user.value_objects.username import UserName
from app.domain.user_profile.entities.profile_entity import ProfileEntity
from app.domain.user_profile.value_objects.fullname import Fullname


@dataclass
class UserEntity(CommonDomainEntity[UserUUID]):
    id: UserUUID
    username: UserName
    contacts: UserContacts
    profile: ProfileEntity

    @staticmethod
    def create_user(
        id: UserUUID, 
        contacts: UserContacts, 
        username: UserName, 
        fullname: Fullname
    ) -> "UserEntity":
        profile: ProfileEntity = ProfileEntity.create_profile(id=id, fullname=fullname)
        return UserEntity(id=id, username=username, contacts=contacts, profile=profile)