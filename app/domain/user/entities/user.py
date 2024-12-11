from datetime import date
from typing import Self
from uuid import UUID

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity
from app.domain.user.entities.address import Address
from app.domain.user.entities.avatar import Avatar
from app.domain.user.entities.profile import Profile
from app.domain.user.entities.social_network import SocialNetwork
from app.domain.user.enums.genders import Genders
from app.domain.user.enums.statuses import ProfileStatus, UserStatus
from app.domain.user.vos.profile.peofile_type import ProfileType
from app.domain.user.vos.profile.profile_status import ProfileStatus
from app.domain.user.vos.user.contacts import Contacts
from app.domain.user.vos.user.id import Id
from app.domain.user.vos.user.user_status import Status
from app.domain.user.vos.user.username import Username
from app.domain.agregate_root import AgregateRoot


class User(UowedEntity[Id], AgregateRoot):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: Id,
        contacts: Contacts,
        status: Status,
        username: Username,
        profiles: list[Profile],
    ) -> None:
        super().__init__(uow=uow, id=id)

        self.profiles: list[Profile] = profiles
        self.contacts: Contacts = contacts
        self.status: Status = status
        self.username: Username = username

    @classmethod
    def create(
        cls: type[Self],
        uow: UnitOfWorkInterface,
        user_id: UUID,
        contacts: str,
        status: UserStatus,
        username: str,
        profiles: list[Profile],
    ) -> Self:
        user = cls(
            uow=uow,
            id=Id(user_id),
            contacts=Contacts(contacts=contacts),
            status=Status(status=status),
            username=Username(username=username),
            profiles=profiles,
        )
        user.mark_new()

        return user

    def add_profile(
        self: Self,
        profile_id: UUID,
        fullname: str,
        profile_type: ProfileType,
        profile_status: ProfileStatus,
        avatars: list[Avatar],
        social_networks: list[SocialNetwork],
        addresses: list[Address],
        bio: str | None = None,
        birth_date: str | None = None,
        gender: Genders | None = None,
    ) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        profile = Profile.create(
            uow=self.uow,
            profile_id=profile_id,
            fullname=fullname,
            profile_type=profile_type,
            profile_status=profile_status,
            avatars=avatars,
            social_networks=social_networks,
            addresses=addresses,
            bio=bio,
            birth_date=birth_date,
            gender=gender,
        )
        self.profiles.append(profile)

    def add_address(
        self: Self,
        address_id: UUID,
        profile_id: UUID,
        city: str,
        region: str,
        street: str,
        house_location: str,
    ) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.add_address(
                    address_id=address_id,
                    city=city,
                    region=region,
                    street=street,
                    house_location=house_location,
                )

    def add_avatar(
        self: Self,
        file_id: UUID,
        profile_id: UUID,
        file_name: str,
        file_size: int,
        file_extension: str,
    ) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.add_avatar(
                    file_id=file_id,
                    file_name=file_name,
                    file_size=file_size,
                    file_extension=file_extension,
                )

    def add_social_network(
        self: Self,
        social_network_id: UUID,
        profile_id: UUID,
        social_network_link: str,
        social_network_type: str,
    ) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.add_social_network(
                    social_network_id=social_network_id,
                    social_network_link=social_network_link,
                    social_network_type=social_network_type,
                )

    def edit_username(self: Self, username: str) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        self.username = Username(username=username)
        self.mark_dirty()

    def edit_status(self: Self, status: UserStatus) -> None:
        self.status = Status(status=status)
        self.mark_dirty()

    def edit_contacts(self: Self, phone: int | None = None, email: str | None = None) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        self.contacts = Contacts(phone=phone, email=email)
        self.mark_dirty()

    def edit_city(self: Self, address_id: UUID, city: str, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.edit_city(address_id=address_id, city=city)

    def edit_region(self: Self, address_id: UUID, region: str, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.edit_region(address_id=address_id, region=region)

    def edit_street(self: Self, address_id: UUID, street: str, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.edit_street(address_id=address_id, street=street)

    def edit_house_location(self: Self, address_id: UUID, house_location: str, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.edit_house_location(address_id=address_id, house_location=house_location)

    def delete_address(self: Self, address_id: UUID, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.delete_address(address_id=address_id)

    def delete_profile(self: Self, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.delete()

    def delete_avatar(self: Self, file_id: UUID, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.delete_avatar(file_id=file_id)

    def delete_social_network(self: Self, social_network_id: UUID, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.delete_social_network(social_network_id=social_network_id)

    def edit_bio(self: Self, bio: str | None, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.edit_bio(bio=bio)

    def edit_birth_date(self: Self, birth_date: date | None, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.edit_birth_date(birth_date=birth_date)

    def edit_fullname(
        self: Self,  profile_id: UUID, firstname: str, lastname: str, middlename: str | None,
    ) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.edit_fullname(firstname=firstname, lastname=lastname, middlename=middlename)

    def edit_gender(self: Self, gender: Genders | None, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.edit_gender(gender=gender)

    def edit_profile_status(self: Self, status: ProfileStatus, profile_id: UUID) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        for profile in self.profiles:
            if profile.id.value == profile_id:
                profile.edit_status(status=status)

    def delete(self: Self) -> None:
        self.mark_deleted()
        for profile in self.profiles:
            profile.delete()
