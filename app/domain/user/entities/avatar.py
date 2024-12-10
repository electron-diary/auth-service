from typing import Self
from uuid import UUID

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity
from app.domain.user.vos.avatars.extension import Extension
from app.domain.user.vos.avatars.name import FileName
from app.domain.user.vos.avatars.size import FileSize
from app.domain.user.vos.user.id import Id


class Avatar(UowedEntity[Id]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: Id,
        file_name: FileName,
        file_size: FileSize,
        file_extension: Extension,
    ) -> None:
        super().__init__(uow=uow, id=id)

        self.file_name: FileName = file_name
        self.file_size: FileSize = file_size
        self.file_extension: Extension = file_extension

    @classmethod
    def create(
        cls: type[Self],
        uow: UnitOfWorkInterface,
        file_id: UUID,
        file_name: str,
        file_size: int,
        file_extension: str,
    ) -> Self:
        avatar = cls(
            uow=uow,
            id=Id(file_id),
            file_name=FileName(file_name),
            file_size=FileSize(file_size),
            file_extension=Extension(file_extension),
        )
        avatar.mark_new()

        return avatar

    def delete(self: Self) -> None:
        self.mark_deleted()
