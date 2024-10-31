from typing import Self
import logging
from logging import Logger

from app.application.dto.request_dto import EditUserStatusRequest
from app.domain.value_objects.user_uuid_value_object import UserUUID
from app.application.interfaces.interactor import Interactor
from app.domain.repositories.user_repository import UserRepositoryInterface
from app.domain.value_objects.user_status_value_object import UserStatus


logger: Logger = logging.getLogger(__name__)


class EditUserStatusUseCase(Interactor[EditUserStatusRequest, None]):
    def __init__(self: Self, user_interface: UserRepositoryInterface) -> None:
        self.user_interface: UserRepositoryInterface = user_interface

    async def __call__(self: Self, request: EditUserStatusRequest) -> None:
        await self.user_interface.edit_user_status(
            user_uuid=UserUUID(request.user_uuid),
            user_status=UserStatus(request.user_status),
        )
        logger.info(f"User status edited: {request.user_uuid}")
