from typing import Self
from uuid import UUID
from datetime import date

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity
from app.domain.user.entities.address import Address
from app.domain.user.entities.avatar import Avatar
from app.domain.user.entities.social_network import SocialNetwork
from app.domain.user.vos.user.id import Id
from app.domain.user.vos.profile.bio import Bio
from app.domain.user.vos.profile.birth_date import BirthDate
from app.domain.user.vos.profile.fullname import Fullname
from app.domain.user.vos.profile.gender import Gender
from app.domain.user.vos.profile.peofile_type import ProfileType
from app.domain.user.vos.profile.profile_status import ProfileStatus
from app.domain.user.enums.genders import Genders
from app.domain.user.enums.statuses import ProfileStatus


class Profile(UowedEntity[Id]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: Id,
        bio: Bio,
        birth_date: BirthDate,
        fullname: Fullname,
        gender: Gender,
        profile_type: ProfileType,
        profile_status: ProfileStatus,
        avatars: list[Avatar],
        social_networks: list[SocialNetwork],
        addresses: list[Address],
    ) -> None:
        super().__init__(uow=uow, id=id)

        self.avatars: list[Avatar] = avatars
        self.social_networks: list[SocialNetwork] = social_networks
        self.addresses: list[Address] = addresses
        self.bio: Bio = bio
        self.birth_date: BirthDate = birth_date
        self.fullname: Fullname = fullname
        self.gender: Gender = gender
        self.profile_type: ProfileType = profile_type
        self.profile_status: ProfileStatus = profile_status

    @classmethod
    def create(
        cls: type[Self], 
        uow: UnitOfWorkInterface,
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
    ) -> Self:
        profile = cls(
            uow=uow,
            id=Id(profile_id),
            bio=Bio(bio),
            birth_date=BirthDate(birth_date),
            fullname=Fullname(fullname),
            gender=Gender(gender),
            profile_type=ProfileType(profile_type),
            profile_status=ProfileStatus(profile_status),
            avatars=avatars,
            social_networks=social_networks,
            addresses=addresses,
        )
        profile.mark_new()

        return profile

    def add_address(
        self: Self,
        address_id: UUID,
        city: str,
        region: str,
        street: str,
        house_location: str,
    ) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        address: Address = Address.create(
            uow=self.uow,
            id=address_id,
            city=city,
            region=region,
            street=street,
            house_location=house_location,
        )
        self.addresses.append(address)

    def add_social_network(
        self: Self,
        social_network_id: UUID,
        social_network_link: str,
        social_network_type: str,
    ) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        social_network: SocialNetwork = SocialNetwork.create(
            uow=self.uow,
            social_network_id=social_network_id,
            social_network_link=social_network_link,
            social_network_type=social_network_type,
        )
        self.social_networks.append(social_network)

    def add_avatar(
        self: Self,
        file_id: UUID,
        file_name: str,
        file_size: int,
        file_extension: str,
    ) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        avatar: Avatar = Avatar.create(
            uow=self.uow,
            file_id=file_id,
            file_name=file_name,
            file_size=file_size,
            file_extension=file_extension,
        )
        self.avatars.append(avatar)

    def edit_city(self: Self, address_id: UUID, city: str) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        for address in self.addresses:
            if address.id.value == address_id:
                address.edit_city(city=city)

    def edit_region(self: Self, address_id: UUID, region: str) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        for address in self.addresses:
            if address.id.value == address_id:
                address.edit_region(region=region)

    def edit_street(self: Self, address_id: UUID, street: str) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        for address in self.addresses:
            if address.id.value == address_id:
                address.edit_street(street=street)

    def edit_house_location(self: Self, address_id: UUID, house_location: str) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        for address in self.addresses:
            if address.id.value == address_id:
                address.edit_house_location(house_location=house_location)

    def delete_avatar(self: Self, file_id: UUID) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        for avatar in self.avatars:
            if avatar.id.value == file_id:
                avatar.delete()

    def delete_social_network(self: Self, social_network_id: UUID) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        for social_network in self.social_networks:
            if social_network.id.value == social_network_id:
                social_network.delete()

    def delete_address(self: Self, address_id: UUID) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")
        
        for address in self.addresses:
            if address.id.value == address_id:
                address.delete()

    def edit_bio(self: Self, bio: str | None) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")

        self.bio = Bio(bio)
        self.mark_dirty()

    def edit_birth_date(self: Self, birth_date: date | None) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")

        self.birth_date = BirthDate(birth_date)
        self.mark_dirty()

    def edit_fullname(
        self: Self, firstname: str, lastname: str, middlename: str | None = None
    ) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")

        self.fullname = Fullname(firstname=firstname, lastname=lastname, middlename=middlename)
        self.mark_dirty()
    
    def edit_gender(self: Self, gender: Genders | None) -> None:
        if self.profile_status.value != ProfileStatus.ACTIVE:
            raise Exception("Profile is not active")

        self.gender = Gender(gender)
        self.mark_dirty()

    def edit_status(self: Self, status: ProfileStatus) -> None:
        self.profile_status = ProfileStatus(status)
        self.mark_dirty()
    
    def delete(self: Self) -> None:
        for avatar in self.avatars:
            avatar.delete()

        for social_network in self.social_networks:
            social_network.delete()

        for address in self.addresses:
            address.delete()

        self.mark_deleted()
