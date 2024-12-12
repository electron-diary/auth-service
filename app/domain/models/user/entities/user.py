from typing import Self
from uuid import UUID

from app.domain.agregate_root import AgregateRoot
from app.domain.models.user.enums.statuses import Statuses
from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity


class User(UowedEntity[UUID], AgregateRoot):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        user_id: UUID,
        username: str,
        email: str,
        status: Statuses,
    ) -> None:
        super().__init__(uow=uow, id=user_id)

        self.username = username
        self.email = email
        self.status = status

    @classmethod
    def create_user(
        cls: type[Self],
        uow: UnitOfWorkInterface,
        user_id: UUID,
    ) -> Self:
        user = cls(
            uow=uow,
            user_id=user_id,
            status=Statuses.INACTIVE,
        )
        user.mark_new()

        return user

    def change_username(self: Self, username: str) -> None:
        if self.status == Statuses.INACTIVE:
            raise Exception("User is inactive")

        self.username = username
        self.mark_dirty()

    def change_email(self: Self, email: str) -> None:
        if self.status == Statuses.INACTIVE:
            raise Exception("User is inactive")

        self.email = email
        self.mark_dirty()

    def activate(self: Self) -> None:
        if self.status == Statuses.ACTIVE:
            raise Exception("User is already active")

        self.status = Statuses.ACTIVE
        self.mark_dirty()

    def delete_user(self: Self) -> None:
        self.mark_deleted()
