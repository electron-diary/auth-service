from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_entity import CommonDomainEntity
from app.domain.user_profile.value_objects.address import Address
from app.domain.user_profile.value_objects.bio import Bio
from app.domain.user_profile.value_objects.date_of_birth import DateOfBirth
from app.domain.user_profile.value_objects.fullname import Fullname
from app.domain.user_profile.value_objects.gender import Gender
from app.domain.user_profile.value_objects.interests import Interests
from app.domain.user_profile.value_objects.profile_pictures import ProfilePuctures
from app.domain.user_profile.value_objects.profile_uuid import ProfileUUID
from app.domain.user_profile.value_objects.social_profiles import SocialProfiles


@dataclass
class ProfileEntity(CommonDomainEntity[ProfileUUID]):
    id: ProfileUUID
    address: Address
    date_of_birth: DateOfBirth
    bio: Bio
    fullname: Fullname
    gender: Gender
    interests: Interests
    profile_pictures: ProfilePuctures
    social_profiles: SocialProfiles

    @staticmethod
    def create_profile(
        id: ProfileUUID, fullname: Fullname, 
        address: Address | None = None, 
        birth_date: DateOfBirth | None = None,
        bio: Bio| None = None,  
        gender: Gender | None = None,
        interests: Interests | None = None, 
        profile_pictures: ProfilePuctures | None = None,
        social_profiles: SocialProfiles | None = None,
    ) -> "ProfileEntity":
        return ProfileEntity(
            id=id, address=address, date_of_birth=birth_date, bio=bio, fullname=fullname,
            gender=gender, interests=interests, profile_pictures=profile_pictures,
            social_profiles=social_profiles,
        )
