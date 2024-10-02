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
from app.application.interfaces.interactor import Interactor
from src.app.domain.user.repositories import UserInterface


class LoginUserUseCase(Interactor[None, None]):
    def __init__(self: Self, user_interface: UserInterface) -> None:
        self.user_interface: UserInterface = user_interface

    async def __call__(self: Self, request: ...) -> ...:
        ...


class RegisterUserUseCase(Interactor[None, None]):
    def __init__(self: Self, user_interface: UserInterface) -> None:
        self.user_interface: UserInterface = user_interface

    async def __call__(self: Self, request: ...) -> ...:
        ...

