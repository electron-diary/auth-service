from typing import Self
from dishka import Provider, Scope, provide

from app.application.usecases.delete_user_usecase import DeleteUserUseCase
from app.domain.repositories.user_repository import UserRepositoryInterface


class DeleteUserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_delete_user_usecase(
        self: Self, user_interface: UserRepositoryInterface
    ) -> DeleteUserUseCase:
        return DeleteUserUseCase(user_interface=user_interface)