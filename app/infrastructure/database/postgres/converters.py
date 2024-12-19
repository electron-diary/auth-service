from app.application.common.unit_of_work import UnitOfWork
from app.application.dto.profile_dto import AddressData, ProfileDto, SocialNetwProfileData
from app.application.dto.user_dto import UserDto
from app.domain.profile.entities.address import Address
from app.domain.profile.entities.profile import Profile
from app.domain.profile.entities.social_netw_profile import SocialNetwProfile
from app.domain.profile.value_objects.fullname import Fullname
from app.domain.user.entities.user import User
from app.domain.user.value_objects.contacts import Contacts


def address_entity_to_dict(address: Address) -> dict[str]:
    return {
        "address_id": address.id,
        "profile_id": address.profile_id,
        "country": address.country,
        "city": address.city,
        "street": address.street,
        "house_number": address.house_number,
        "apartament_number": address.apartament_number,
        "postal_code": address.postal_code,
    }


def profile_entity_to_dict(profile: Profile) -> dict[str]:
    return {
        "profile_id": profile.id,
        "user_id": profile.profile_owner_id,
        "first_name": profile.fullname.first_name,
        "last_name": profile.fullname.last_name,
        "middle_name": profile.fullname.middle_name,
        "bio": profile.bio,
        "status": profile.status,
    }


def social_netw_profile_entity_to_dict(social_netw_profile: SocialNetwProfile) -> dict[str]:
    return {
        "social_netw_profile_id": social_netw_profile.id,
        "profile_id": social_netw_profile.profile_id,
        "social_netw_profile_name": social_netw_profile.social_netw_name,
        "social_netw_profile_link": social_netw_profile.social_profile_link,
    }


def user_entity_to_dict(user: User) -> dict[str]:
    return {
        "user_id": user.id,
        "email": user.contacts.email,
        "phone_number": user.contacts.phone_number,
        "username": user.username,
        "status": user.status,
    }


def result_to_user_entity(user: dict, uow: UnitOfWork) -> User:
    return User(
        user_id=user["user_id"],
        username=user["username"],
        contacts=Contacts(
            email=user["email"],
            phone_number=user["phone_number"],
        ),
        status=user["status"],
        uow=uow,
    )


def result_to_user_dto(user: dict) -> UserDto:
    return UserDto(
        user_id=user["user_id"],
        username=user["username"],
        email=user["email"],
        phone_number=user["phone_number"],
        status=user["status"],
    )


def result_to_profile_entity(
    rows: list[dict], uow: UnitOfWork, get_first: bool = True,
) -> Profile:
    result = [
            Profile(
                profile_id=row["profile_id"],
                profile_owner_id=row["user_id"],
                fullname=Fullname(
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    middle_name=row["middle_name"],
                ),
                bio=row["bio"],
                profile_status=row["status"],
                uow=uow,
                addresses=[
                    Address(
                        address_id=r["address_id"],
                        profile_id=r["profile_id"],
                        country=r["country"],
                        city=r["city"],
                        street=r["street"],
                        house_number=r["house_number"],
                        apartment_number=r["apartament_number"],
                        postal_code=r["postal_code"],
                        uow=uow,
                    )
                    for r in rows
                    if r["profile_id"] == row["profile_id"] and r["address_id"]
                ],
                social_netw_profiles=[
                    SocialNetwProfile(
                        id=r["social_netw_profile_id"],
                        profile_id=r["profile_id"],
                        social_netw_name=r["social_netw_profile_name"],
                        social_profile_link=r["social_netw_profile_link"],
                        uow=uow,
                    )
                    for r in rows
                    if r["profile_id"] == row["profile_id"] and r["social_netw_profile_id"]
                ],
            )
        for row in {r["profile_id"]: r for r in rows}.values()
    ]

    if not get_first:
        return result

    return result[0]


def result_to_profile_dto(
    rows: list[dict], get_first: bool = True,
) -> ProfileDto:
    result = [
            ProfileDto(
                profile_id=row["profile_id"],
                profile_owner_id=row["user_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                middle_name=row["middle_name"],
                bio=row["bio"],
                status=row["status"],
                addresses=[
                    AddressData(
                        address_id=r["address_id"],
                        country=r["country"],
                        city=r["city"],
                        street=r["street"],
                        house_number=r["house_number"],
                        apartment_number=r["apartament_number"],
                        postal_code=r["postal_code"],
                    )
                    for r in rows
                    if r["profile_id"] == row["profile_id"] and r["address_id"]
                ],
                social_netw_profiles=[
                    SocialNetwProfileData(
                        social_netw_profile_id=r["social_netw_profile_id"],
                        social_netw_profile_name=r["social_netw_profile_name"],
                        social_netw_profile_link=r["social_netw_profile_link"],
                    )
                    for r in rows
                    if r["profile_id"] == row["profile_id"] and r["social_netw_profile_id"]
                ],
            )
        for row in {r["profile_id"]: r for r in rows}.values()
    ]

    if not get_first:
        return result

    return result[0]
