from typing import Self
from datetime import datetime

from src.app.application.dto.request_dto import UpdateUserNameRequest
from src.app.application.dto.response_dto import UpdateUserNameResponse
from src.app.domain.user.repositories import UserInterface
from src.app.application.interfaces.interactor import Interactor
from src.app.domain.user.value_objects import UserName, UserUpdatedAt, UserUUID


class UpdateUserNameUseCase(Interactor[UpdateUserNameRequest, UpdateUserNameResponse]):
    def __init__(self: Self, user_interface: UserInterface) -> None:
        self.user_interface: UserInterface = user_interface

    async def __call__(self: Self, request: UpdateUserNameRequest) -> UpdateUserNameResponse:
        datetime_now: datetime = datetime.now()
        new_user_name: UserName = await self.user_interface.update_user_name(
            user_uuid=UserUUID(request.user_uuid),
            user_name=UserName(request.user_name),
            user_updated_at=UserUpdatedAt(datetime_now),
        )
        return UpdateUserNameResponse.from_entity(new_user_name=new_user_name)