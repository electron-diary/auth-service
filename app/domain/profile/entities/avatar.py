from typing import Self
from uuid import UUID

from app.domain.unit_of_work import UnitOfWorkTrackerInterface
from app.domain.uowed import UowedEntity


class Avatar(UowedEntity[UUID]):
    def __init__(
        self: Self,
        uow: UnitOfWorkTrackerInterface,
        avatar_id: UUID,
        url: str,
        file_name: str,
        file_extension: str,
        file_size: int,
    ) -> None:
        super().__init__(uow=uow, id=avatar_id)

        self.url = url
        self.file_name = file_name
        self.file_extension = file_extension
        self.file_size = file_size

    @classmethod
    def create_avatar(
        cls: type[Self],
        uow: UnitOfWorkTrackerInterface,
        avatar_id: UUID,
        url: str,
        file_name: str,
        file_extension: str,
        file_size: int,
    ) -> Self:
        avatar = cls(
            uow=uow,
            avatar_id=avatar_id,
            url=url,
            file_name=file_name,
            file_extension=file_extension,
            file_size=file_size,
        )
        avatar.mark_new()

        return avatar

    def delete_avatar(self: Self) -> None:
        self.mark_deleted()
