from typing import Self
import logging
from logging import Logger

from src.app.application.dto.request_dto import GetUserRequest
from src.app.application.dto.response_dto import GetUserResponse
from src.app.application.interfaces.interactor import Interactor
from src.app.domain.value_objects.user_uuid_value_object import UserUUID
from src.app.application.interfaces.interactor import Interactor
from src.app.domain.repositories.user_repository import UserRepositoryInterface
from src.app.domain.entities.user_entities import UserEntity

logger: Logger = logging.getLogger(__name__)


class GetUserUseCase(Interactor[GetUserRequest, GetUserResponse]):
    def __init__(self: Self, user_interface: UserRepositoryInterface) -> None:
        self.user_interface: UserRepositoryInterface = user_interface

    async def __call__(self: Self, request: GetUserRequest) -> GetUserResponse:
        user_entity: UserEntity = await self.user_interface.get_user_by_uuid(
            user_uuid=UserUUID(request.user_uuid)
        )
        logger.info(f'get user by uuid {user_entity.uuid.to_raw()}')
        return GetUserResponse.from_entity(user=user_entity)