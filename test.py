from uuid import uuid4

from app.domain.user_profile.entities.profile_entity import ProfileEntity
from app.domain.user_profile.value_objects.fullname import FullnameValueObject
from app.domain.user_profile.value_objects.profile_uuid import ProfileUUID


profile = ProfileEntity.create_profile(
    id=ProfileUUID(uuid4()), fullname=FullnameValueObject("John", "Doe", 'Eblan'),
)

@dataclass
class UserEntity(CommonDomainEntity[UserUUID], AgregateRoot):
    id: UserUUID
    username: UserNameValueObject
    contacts: UserContactsValueObject
    profile: ProfileEntity

    @staticmethod
    def create_user(
        id: UserUUID, 
        contacts: UserContactsValueObject, 
        username: UserNameValueObject, 
        fullname: FullnameValueObject
    ) -> "UserEntity":
        profile: ProfileEntity = ProfileEntity.create_profile(id=id, fullname=fullname)
        return UserEntity(id=id, username=username, contacts=contacts, profile=profile)


------------------------


@dataclass
class ProfileEntity(CommonDomainEntity[ProfileUUID]):
    id: ProfileUUID
    address: AddressValueObject
    date_of_birth: DateOfBirthValueObject
    bio: BioValueObject
    fullname: FullnameValueObject
    gender: GenderValueObject
    interests: InterestsValueObject
    profile_pictures: ProfilePucturesValueObject
    social_profiles: SocialProfilesValueObject

    @staticmethod
    def create_profile(
        id: ProfileUUID, fullname: FullnameValueObject, 
        address: AddressValueObject | None = None, 
        birth_date: DateOfBirthValueObject | None = None,
        bio: BioValueObject | None = None,  
        gender: GenderValueObject | None = None,
        interests: InterestsValueObject | None = None, 
        profile_pictures: ProfilePucturesValueObject | None = None,
        social_profiles: SocialProfilesValueObject | None = None,
    ) -> "ProfileEntity":
        return ProfileEntity(
            id=id, address=address, date_of_birth=birth_date, bio=bio, fullname=fullname,
            gender=gender, interests=interests, profile_pictures=profile_pictures,
            social_profiles=social_profiles,
        )