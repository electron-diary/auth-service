from typing import Self
import logging
from logging import Logger

from src.app.application.dto.request_dto import DeleteUserRequest
from src.app.domain.value_objects.user_uuid_value_object import UserUUID
from src.app.application.interfaces.interactor import Interactor
from src.app.domain.repositories.user_repository import UserRepositoryInterface


logger: Logger = logging.getLogger(__name__)


class DeleteUserUseCase(Interactor[DeleteUserRequest, None]):
    def __init__(self: Self, user_interface: UserRepositoryInterface) -> None:
        self.user_interface: UserRepositoryInterface = user_interface

    async def __call__(self: Self, request: DeleteUserRequest) -> None:
        await self.user_interface.delete_user(
            user_uuid=UserUUID(request.user_uuid)
        )
        logger.info(f"User {request.user_uuid} deleted")
