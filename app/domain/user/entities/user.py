from typing import Self

from app.domain.user.value_objects.id import Id
from app.domain.user.value_objects.contacts import Contacts
from app.domain.user.value_objects.status import Status
from app.domain.user.entities.profile import Profile
from app.domain.user.value_objects.fullname import Fullname
from app.domain.user.value_objects.profile_pictures import ProfilePictures
from app.domain.user.value_objects.address import Address
from app.domain.user.value_objects.gender import Gender
from app.domain.user.value_objects.age import Age
from app.domain.user.enums.statuses import StatusTypes
from app.domain.domain_event import DomainEvent
from app.domain.user.events.address_changed import AddressChanged
from app.domain.user.events.age_changed import AgeChanged
from app.domain.user.events.contacts_changed import ContactsChanged
from app.domain.user.events.fullname_changed import FullnameChanged
from app.domain.user.events.gender_changed import GenderChanged
from app.domain.user.events.pictures_changed import ProfilePicturesChanged
from app.domain.user.events.status_changed import StatusChanged
from app.domain.uowed import UowedEntity
from app.domain.unit_of_work import UnitOfWork


class User(UowedEntity[Id]):
    def __init__(
        self: Self,
        id: Id,
        uow: UnitOfWork,
        contacts: Contacts,
        status: Status,
        profile: Profile
    ) -> None:
        super().__init__(uow=uow)

        self.id: Id = id
        self.contacts: Contacts = contacts
        self.status: Status = status
        self.profile: Profile = profile
        self._events: list[DomainEvent] = []

    def edit_contacts(self: Self, contacts: Contacts) -> None:
        if self.status.status == StatusTypes.INACTIVE:
            raise ...
        
        self.contacts = contacts
        event: ContactsChanged = ContactsChanged(
            aggregate_id=self.id.id,
            user_id=self.id.id,
            email=self.contacts.email,
            phone_number=self.contacts.phone_number,
            event_type='ContactsChanged',
            agregate_name='User'
        )
        self.add_event(event=event)
        self.mark_dirty()

    def edit_age(self: Self, age: Age) -> None:
        if self.status.status == StatusTypes.INACTIVE:
            raise ...
        
        self.profile.edit_age(age=age)
        event: AgeChanged = AgeChanged(
            aggregate_id=self.id.id,
            user_id=self.id.id,
            age=self.profile.age.age,
            event_type='AgeChanged',
            agregate_name='User'
        )
        self.add_event(event=event)

    def edit_gender(self: Self, gender: Gender) -> None:
        if self.status.status == StatusTypes.INACTIVE:
            raise ...
        
        self.profile.edit_gender(gender=gender)
        event: GenderChanged = GenderChanged(
            aggregate_id=self.id.id,
            user_id=self.id.id,
            gender=self.profile.gender.gender.value,
            event_type='GenderChanged',
            agregate_name='User'
        )
        self.add_event(event=event)

    def edit_address(self: Self, address: Address) -> None:
        if self.status.status == StatusTypes.INACTIVE:
            raise ...
        
        self.profile.edit_address(address=address)
        event: AddressChanged = AddressChanged(
            aggregate_id=self.id.id,
            user_id=self.id.id,
            country=self.profile.address.country,
            city=self.profile.address.city,
            street=self.profile.address.street,
            house_location=self.profile.address.house_location,
            event_type='AddressChanged',
            agregate_name='User'
        )
        self.add_event(event=event)

    def edit_fullname(self: Self, fullname: Fullname) -> None:
        if self.status.status == StatusTypes.INACTIVE:
            raise ...
        
        self.profile.edit_fullname(fullname=fullname)
        event: FullnameChanged = FullnameChanged(
            aggregate_id=self.id.id,
            user_id=self.id.id,
            first_name=self.profile.fullname.first_name,
            last_name=self.profile.fullname.last_name,
            middle_name=self.profile.fullname.middle_name,
            event_type='FullnameChanged',
            agregate_name='User'
        )
        self.add_event(event=event)

    def edit_pictures(self: Self, pictures: ProfilePictures) -> None:
        if self.status.status == StatusTypes.INACTIVE:
            raise ...
        
        self.profile.edit_pictures(pictures=pictures)
        event: ProfilePicturesChanged = ProfilePicturesChanged(
            aggregate_id=self.id.id,
            user_id=self.id.id,
            profile_pictures=self.profile.pictures.profile_pictures,
            event_type='ProfilePicturesChanged',
            agregate_name='User'
        )
        self.add_event(event=event)

    def edit_status(self: Self, status: Status) -> None:
        if self.status.status == StatusTypes.INACTIVE:
            raise ...
        
        self.status = status
        event: StatusChanged = StatusChanged(
            aggregate_id=self.id.id,
            user_id=self.id.id,
            status=self.status.status.value,
            event_type='StatusChanged',
            agregate_name='User'
        )
        self.add_event(event=event)
        self.mark_dirty()

    def add_event(self: Self, event: DomainEvent) -> None:
        self._events.append(event)

    def raise_events(self: Self) -> list[DomainEvent]:
        events: list[DomainEvent] = self._events.copy()
        self._events.clear()
        
        return events