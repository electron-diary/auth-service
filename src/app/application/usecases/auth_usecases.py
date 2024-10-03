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
from src.app.application.dto.auth.request_dto import UserLoginRequest, RegisterUserRequest
from app.application.interfaces.interactor import Interactor
from src.app.domain.user.repositories import UserInterface
from src.app.application.interfaces.notifications_interface import NotificationsInterface
from src.app.domain.common.exceptions import AuthentificationError


class LoginUserUseCase(Interactor[UserLoginRequest, UserUUID]):
    def __init__(
        self: Self, user_interface: UserInterface, 
        notifications_interface: NotificationsInterface
    ) -> None:
        self.user_interface: UserInterface = user_interface
        self.notifications_interface: NotificationsInterface = notifications_interface

    async def __call__(self: Self, request: UserLoginRequest) -> UserUUID:
        user: UserEntity = await self.user_interface.get_user_by_contact(
            user_contact=UserContact(object=request.user_contact)
        )
        if not user:
            raise AuthentificationError('email or password are incorrect')
        if user.user_password != request.user_password:
            raise AuthentificationError('email or password are incorrect')
        # await self.notifications_interface.send_email_notification()
        return UserUUID(object=user.user_uuid)
        
            
class RegisterUserUseCase(Interactor[RegisterUserRequest, UserUUID]):
    def __init__(
        self: Self, user_interface: UserInterface,
        notifications_interface: NotificationsInterface

    ) -> None:
        self.user_interface: UserInterface = user_interface
        self.notifications_interface: NotificationsInterface = notifications_interface

    async def __call__(self: Self, request: RegisterUserRequest) -> UserUUID:
        if await self.user_interface.get_user_by_contact(
            user_contact=UserContact(object=request.user_contact)
        ):
            raise AuthentificationError('user already exists')
        date_time: datetime = datetime.now()
        user_uuid: UUID = await self.user_interface.create_user(
            user_name=UserName(object=request.user_name),
            user_contact=UserContact(object=request.user_contact),
            user_password=UserPassword(object=request.user_password),
            user_ip=UserIp(object=request.user_ip),
            user_refresh_token=UserRefreshToken(object=request.user_refresh_token),
            user_status=UserStatus(object=False),
            user_created_at=UserCreatedAt(object=date_time),
            user_updated_at=UserUpdatedAt(object=date_time)
        )
        # await self.notifications_interface.send_email_notification()
        return UserUUID(object=user_uuid)
        

