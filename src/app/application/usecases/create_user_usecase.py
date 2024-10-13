from typing import Self
from datetime import datetime
import logging

from src.app.application.dto.request_dto import CreateUserRequest
from src.app.application.dto.response_dto import CreateUserResponse
from src.app.domain.user.value_objects import UserContact, UserCreatedAt, UserName, UserUpdatedAt, UserUUID
from src.app.domain.user.repositories import UserInterface
from src.app.application.interfaces.interactor import Interactor
from src.app.application.interfaces.uow import UnitOfWork


class CreateUserUseCase(Interactor[CreateUserRequest, CreateUserResponse]):
    def __init__(self: Self, user_interface: UserInterface, uow: UnitOfWork) -> None:
        self.user_interface: UserInterface = user_interface
        self.uow: UnitOfWork = uow

    async def __call__(self: Self, request: CreateUserRequest) -> CreateUserResponse:
        datetime_now: datetime = datetime.now()
        user_uuid: UserUUID = await self.user_interface.create_user(
            user_name=UserName(request.user_name),
            user_contact=UserContact(request.user_contact),
            user_created_at=UserCreatedAt(datetime_now),
            user_updated_at=UserUpdatedAt(datetime_now)
        )
        await self.uow.commit()
        return CreateUserResponse.from_entity(user_uuid=user_uuid)