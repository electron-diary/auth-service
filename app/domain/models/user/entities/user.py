from typing import Self
from uuid import UUID

from app.domain.agregate_root import AgregateRoot
from app.domain.models.user.enums.statuses import Statuses
from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity
from app.domain.models.user.vos.contacts import Contacts


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
        phone_number: int | None
    ) -> Self:
        user = cls(
            uow=uow,
            user_id=user_id,
            status=Statuses.INACTIVE,
            contacts=Contacts(phone_number=phone_number, email=email)
        )
        user.mark_new()

        return user

    def change_username(self: Self, username: str) -> None:
        if self.status == Statuses.INACTIVE:
            raise Exception("User is inactive")

        self.username = username
        self.mark_dirty()

    def change_contacts(self: Self, email: str | None, phone_number: str | None) -> None:
        if self.status == Statuses.INACTIVE:
            raise Exception("User is inactive")

        self.contacts = Contacts(phone_number=phone_number, email=email)
        self.mark_dirty()

    def activate(self: Self) -> None:
        if self.status == Statuses.ACTIVE:
            raise Exception("User is already active")

        self.status = Statuses.ACTIVE
        self.mark_dirty()

    def delete_user(self: Self) -> None:
        self.mark_deleted()
