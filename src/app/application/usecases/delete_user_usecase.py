from typing import Self

from src.app.domain.user.repositories import UserInterface
from src.app.domain.user.value_objects import UserUUID
from src.app.application.dto.request_dto import DeleteUserRequest
from src.app.application.interfaces.interactor import Interactor


class DeleteUserUseCase(Interactor[DeleteUserRequest, None]):
    def __init__(self: Self, user_interface: UserInterface) -> None:
        self.user_interface: UserInterface = user_interface

    async def __call__(self: Self, request: DeleteUserRequest) -> None:
        await self.user_interface.delete_user(
            user_uuid=UserUUID(request.user_uuid)
        )
