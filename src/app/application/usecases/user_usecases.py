from typing import Self
from uuid import UUID
from datetime import datetime

from src.app.domain.user.entity import UserEntity
from src.app.domain.user.value_objects import UserUUID
from src.app.application.dto.user.response_dto import GetUserResponse
from app.application.interfaces.interactor import Interactor
from src.app.domain.user.repositories import UserInterface

    

class GetUserUseCase(Interactor[UserUUID, GetUserResponse]):
    def __init__(self: Self, user_interface: UserInterface) -> None:
        self.user_interface: UserInterface = user_interface

    async def __call__(self: Self, request: UserUUID) -> GetUserResponse:
        user_entity: UserEntity = await self.user_interface.get_user_by_uuid(
            user_uuid=request
        )
        return GetUserResponse.from_entity(user=user_entity)