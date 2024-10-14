from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.get_user_usecase import GetUserUseCase
from src.app.domain.repositories.user_repository import UserRepositoryInterface


class GetUserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_get_user_usecase(self: Self, user_interface: UserRepositoryInterface) -> GetUserUseCase:
        return GetUserUseCase(user_interface=user_interface)