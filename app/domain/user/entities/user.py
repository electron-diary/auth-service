from typing import Self
from uuid import UUID

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity
from app.domain.user.entities.profile import Profile
from app.domain.user.enums.statuses import UserStatus
from app.domain.user.vos.user.contacts import Contacts
from app.domain.user.vos.user.id import Id
from app.domain.user.vos.user.user_status import Status
from app.domain.user.vos.user.username import Username


class User(UowedEntity[Id]):
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
        profiles: list[Profile] = [],
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

    def add_profile(self: Self) -> None:
        if self.status.value != UserStatus.ACTIVE:
            raise Exception("User is not active")

        profile = Profile.create(uow=self.uow)
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

    def delete(self: Self) -> None:
        self.mark_deleted()
        for profile in self.profiles:
            profile.delete()
