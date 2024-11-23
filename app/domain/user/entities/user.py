from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_entity import CommonDomainEntity
from app.domain.user.value_objects.user_contacts import UserContacts
from app.domain.user.value_objects.user_uuid import UserUUID
from app.domain.user.value_objects.username import UserName
from app.domain.user_profile.entities.profile import Profile
from app.domain.user_profile.value_objects.fullname import Fullname


@dataclass
class User(CommonDomainEntity[UserUUID]):
    id: UserUUID
    username: UserName
    contacts: UserContacts
    profile: Profile

    @staticmethod
    def create_user(
        id: UserUUID, 
        contacts: UserContacts, 
        username: UserName, 
        fullname: Fullname
    ) -> "User":
        profile: Profile= Profile.create_profile(id=id, fullname=fullname)
        return User(id=id, username=username, contacts=contacts, profile=profile)
    
    def delete_user(self: Self) -> None:
        self.profile.delete_profile()
        ...