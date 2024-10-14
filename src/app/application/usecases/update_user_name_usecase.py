from typing import Self
from datetime import datetime

from src.app.application.dto.request_dto import UpdateUserNameRequest
from src.app.application.dto.response_dto import UpdateUserNameResponse
from src.app.domain.repositories.user_repository import UserRepositoryInterface
from src.app.domain.value_objects.user_name_value_object import UserName
from src.app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from src.app.domain.value_objects.user_uuid_value_object import UserUUID
from src.app.application.interfaces.interactor import Interactor


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
        return UpdateUserNameResponse.from_entity(user_name=new_user_name)