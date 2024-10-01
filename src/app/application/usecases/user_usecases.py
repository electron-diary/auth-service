from typing import Self
from uuid import UUID
from datetime import datetime

from src.app.domain.user.entity import UserEntity
from src.app.domain.user.value_objects import UserUUID
from src.app.domain.user.value_objects import UserName
from src.app.domain.user.value_objects import UserContact
from src.app.domain.user.value_objects import UserPassword
from src.app.domain.user.value_objects import UserIp
from src.app.domain.user.value_objects import UserCreatedAt
from src.app.domain.user.value_objects import UserUpdatedAt
from src.app.domain.user.value_objects import UserRefreshToken
from src.app.domain.user.value_objects import UserStatus
from src.app.application.dto.user.request_dto import CreateUserRequest
from src.app.application.dto.user.response_dto import GetUserResponse
from src.app.application.interactor import Interactor
from src.app.domain.user.repositories import UserInterface


class CreateUserUseCase(Interactor[CreateUserRequest, UserUUID]):
    def __init__(self: Self, user_interface: UserInterface) -> None:
        self.user_interface: UserInterface = user_interface

    async def __call__(self: Self, request: CreateUserRequest) -> UserUUID:
        date_time: datetime = datetime.now()
        user_uuid: UUID = await self.user_interface.create_user(
            user_name=UserName(object=request.user_name),
            user_contact=UserContact(object=request.user_contact),
            user_password=UserPassword(object=request.user_password),
            user_ip=UserIp(object=...),
            user_refresh_token=UserRefreshToken(object=...),
            user_status=UserStatus(object=False),
            user_created_at=UserCreatedAt(object=date_time),
            user_updated_at=UserUpdatedAt(object=date_time)
        )
        return UserUUID(object=user_uuid)
    

class GetUserUseCase(Interactor[UserUUID, GetUserResponse]):
    def __init__(self: Self, user_interface: UserInterface) -> None:
        self.user_interface: UserInterface = user_interface

    async def __call__(self: Self, request: UserUUID) -> GetUserResponse:
        user_entity: UserEntity = await self.user_interface.get_user(
            user_uuid=request
        )
        return GetUserResponse.from_entity(user=user_entity)