from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_entity import CommonDomainEntity
from app.domain.user_profile.events.create_profile_event import ProfileCreatedEvent
from app.domain.user_profile.events.delete_profile_event import ProfileDeletedEvent
from app.domain.user_profile.events.update_profile_event import ProfileUpdatedEvent
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

    @staticmethod
    def create_profile(
        id: ProfileUUID, address: AddressValueObject, birth_date: DateOfBirthValueObject,
        bio: BioValueObject, fullname: FullnameValueObject, gender: GenderValueObject,
        interests: InterestsValueObject, profile_pictures: ProfilePucturesValueObject,
        profile_type: ProfileTypeValueObject, social_profiles: SocialProfilesValueObject,
    ) -> "ProfileEntity":
        event: ProfileCreatedEvent = ProfileCreatedEvent(
            id=id, address=address.address, birth_date=birth_date.birth_date,
            bio=bio.bio, first_name=fullname.first_name, last_name=fullname.last_name,
            gender=gender.gender, middle_name=fullname.middle_name,
            interests=interests.interests, profile_pictures=profile_pictures.profile_pictures,
            profile_type=profile_type.profile_type, social_profiles=social_profiles.social_profiles,
        )

    def delete_profile(self: Self) -> None:
        event: ProfileDeletedEvent = ProfileDeletedEvent(id=self.id)

    def update_profile(
        self: Self, address: AddressValueObject, birth_date: DateOfBirthValueObject,
        bio: BioValueObject, fullname: FullnameValueObject, gender: GenderValueObject,
        interests: InterestsValueObject, profile_pictures: ProfilePucturesValueObject,
        profile_type: ProfileTypeValueObject, social_profiles: SocialProfilesValueObject,
    ) -> None:
        event: ProfileUpdatedEvent = ProfileUpdatedEvent(
            id=self.id, address=address.address, birth_date=birth_date.birth_date,
            bio=bio.bio, first_name=fullname.first_name, last_name=fullname.last_name,
            gender=gender.gender, middle_name=fullname.middle_name,
            interests=interests.interests, profile_pictures=profile_pictures.profile_pictures,
            profile_type=profile_type.profile_type, social_profiles=social_profiles.social_profiles,
        )
