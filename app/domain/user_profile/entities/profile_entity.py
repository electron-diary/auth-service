from dataclasses import dataclass

from app.domain.common.common_domain_entity import CommonDomainEntity
from app.domain.user_profile.value_objects.address_value_object import AddressValueObject
from app.domain.user_profile.value_objects.bio_value_object import BioValueObject
from app.domain.user_profile.value_objects.date_of_birth_value_object import DateOfBirthValueObject
from app.domain.user_profile.value_objects.fullname_value_object import FullnameValueObject
from app.domain.user_profile.value_objects.gender_value_object import GenderValueObject
from app.domain.user_profile.value_objects.interests_value_object import InterestsValueObject
from app.domain.user_profile.value_objects.profile_pictures_value_object import ProfilePucturesValueObject
from app.domain.user_profile.value_objects.profile_type_value_object import ProfileTypeValueObject
from app.domain.user_profile.value_objects.profile_uuid_value_object import ProfileUUID
from app.domain.user_profile.value_objects.social_profiles_value_object import SocialProfilesValueObject


@dataclass(frozen=True)
class ProfileEntity(CommonDomainEntity[ProfileUUID]):
    id: ProfileUUID
    address: AddressValueObject
    date_of_birth: DateOfBirthValueObject
    bio: BioValueObject
    fullname: FullnameValueObject
    gender: GenderValueObject
    interests: InterestsValueObject
    profile_pictures: ProfilePucturesValueObject
    profile_type: ProfileTypeValueObject
    social_profiles: SocialProfilesValueObject
