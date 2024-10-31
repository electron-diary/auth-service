from typing import Self
from datetime import datetime
import logging
from logging import Logger

from app.application.dto.request_dto import UpdateUserNameRequest
from app.application.dto.response_dto import UpdateUserNameResponse
from app.domain.repositories.user_repository import UserRepositoryInterface
from app.domain.value_objects.user_name_value_object import UserName
from app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from app.domain.value_objects.user_uuid_value_object import UserUUID
from app.application.interfaces.interactor import Interactor


logger: Logger = logging.getLogger(__name__)


class UpdateUserNameUseCase(Interactor[UpdateUserNameRequest, UpdateUserNameResponse]):
    def __init__(self: Self, user_interface: UserRepositoryInterface) -> None:
        self.user_interface: UserRepositoryInterface = user_interface

    async def __call__(self: Self, request: UpdateUserNameRequest) -> UpdateUserNameResponse:
        datetime_now: datetime = datetime.now()
        new_user_name: UserName = await self.user_interface.update_user_name(
            user_uuid=UserUUID(request.user_uuid),
            user_name=UserName(request.user_name),
            user_updated_at=UserUpdatedAt(datetime_now),
        )
        logger.info(f"Updated user name: {request.user_name} for user {request.user_uuid}")
        return UpdateUserNameResponse.from_entity(user_name=new_user_name)