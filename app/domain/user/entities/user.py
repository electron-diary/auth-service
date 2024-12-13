from typing import Self
from uuid import UUID

from app.domain.agregate_root import AgregateRoot
from app.domain.user.enums.statuses import Statuses
from app.domain.user.events.contacts_changed import ContactsChanged
from app.domain.user.events.user_created import UserCreated
from app.domain.user.events.user_deleted import UserDeleted
from app.domain.user.events.user_status_changed import UserStatusChanged
from app.domain.user.events.username_changed import UsernameChanged
from app.domain.user.exceptions import UserInactiveError
from app.domain.user.vos.contacts import Contacts
from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity


class User(UowedEntity[UUID], AgregateRoot):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        user_id: UUID,
        username: str,
        contacts: Contacts,
        status: Statuses,
    ) -> None:
        super().__init__(uow=uow, id=user_id)

        self.username = username
        self.contacts = contacts
        self.status = status

    @classmethod
    def create_user(
        cls: type[Self],
        uow: UnitOfWorkInterface,
        user_id: UUID,
        email: str | None,
        phone_number: int | None,
        username: str,
    ) -> Self:
        user = cls(
            uow=uow,
            user_id=user_id,
            status=Statuses.INACTIVE,
            contacts=Contacts(phone_number=phone_number, email=email),
            username=username,
        )
        user.mark_new()
        user.record_event(
            UserCreated(
                aggregate_id=user.id,
                event_type="UserCreated",
                agregate_name="User",
                user_id=user.id,
                username=user.username,
                email=user.contacts.email,
                phone=user.contacts.phone_number,
                status=user.status.value,
            ),
        )
        return user

    def change_username(self: Self, username: str) -> None:
        if self.status == Statuses.INACTIVE:
            raise UserInactiveError("User is inactive")

        self.username = username
        self.record_event(
            UsernameChanged(
                aggregate_id=self.id,
                event_type="UsernameChanged",
                agregate_name="User",
                user_id=self.id,
                username=self.username,
            ),
        )
        self.mark_dirty()

    def change_contacts(self: Self, email: str | None, phone_number: str | None) -> None:
        if self.status == Statuses.INACTIVE:
            raise UserInactiveError("User is inactive")

        self.contacts = Contacts(phone_number=phone_number, email=email)
        self.record_event(
            ContactsChanged(
                aggregate_id=self.id,
                event_type="ContactsChanged",
                agregate_name="User",
                user_id=self.id,
                email=self.contacts.email,
                phone=self.contacts.phone_number,
            ),
        )
        self.mark_dirty()

    def chnage_status(self: Self, status: Statuses) -> None:
        self.status = status
        self.record_event(
            UserStatusChanged(
                aggregate_id=self.id,
                event_type="UserStatusChanged",
                agregate_name="User",
                user_id=self.id,
                status=self.status.value,
            ),
        )
        self.mark_dirty()

    def delete_user(self: Self) -> None:
        self.record_event(
            UserDeleted(
                aggregate_id=self.id,
                event_type="UserDeleted",
                agregate_name="User",
                user_id=self.id,
            ),
        )
        self.mark_deleted()
