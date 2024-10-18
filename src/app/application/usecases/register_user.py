from typing import Self

from src.app.domain.repositories.user_repository import UserRepositoryInterface
from src.app.application.interfaces.interactor import Interactor
from src.app.application.interfaces.notifications_interface import NotificationsInterface
from src.app.domain.entities.user_entities import UserEntity
from src.app.application.exceptions.auth_exceptions import UserAlreadyExistsError


class RegisterUserUseCase(Interactor[None, None]):
    def __init__(
        self: Self, user_repository: UserRepositoryInterface, 
        notifications_service: NotificationsInterface
    ) -> None:
        self.user_repository: UserRepositoryInterface = user_repository
        self.notifications_service: NotificationsInterface = notifications_service 

    async def __call__(self: Self) -> None:
        user: UserEntity = await self.user_repository.get_user_by_uuid(
            ...
        )
        if user:
            raise UserAlreadyExistsError(
                'user alre'
            )