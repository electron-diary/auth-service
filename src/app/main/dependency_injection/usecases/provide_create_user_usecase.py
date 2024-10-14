from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.create_user_usecase import CreateUserUseCase
from src.app.domain.user.repositories import UserInterface


class CreateUserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_create_user_use_case(
        self: Self, user_interface: UserInterface
    ) -> CreateUserUseCase:
        return CreateUserUseCase(user_interface=user_interface)