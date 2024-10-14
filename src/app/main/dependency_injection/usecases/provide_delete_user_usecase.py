from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.delete_user_usecase import DeleteUserUseCase
from src.app.domain.user.repositories import UserInterface


class DeleteUserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_delete_user_usecase(
        self: Self, user_interface: UserInterface
    ) -> DeleteUserUseCase:
        return DeleteUserUseCase(user_interface=user_interface)