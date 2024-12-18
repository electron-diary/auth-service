from app.application.common.unit_of_work import UnitOfWork
from app.application.dto.user_dto import UserDto
from app.domain.profile.entities.address import Address
from app.domain.profile.entities.profile import Profile
from app.domain.profile.entities.social_netw_profile import SocialNetwProfile
from app.domain.user.entities.user import User


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
        "first_name": profile.first_name,
        "last_name": profile.last_name,
        "middle_name": profile.middle_name,
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
        id=user["user_id"],
        username=user["username"],
        contacts=user["contacts"],
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
