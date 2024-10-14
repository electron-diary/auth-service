from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.update_user_name_usecase import UpdateUserNameUseCase
from src.app.domain.repositories.user_repository import UserRepositoryInterface


class UpdateUserNameUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_delete_user_usecase(
        self: Self, user_interface: UserRepositoryInterface
    ) -> UpdateUserNameUseCase:
        return UpdateUserNameUseCase(user_interface=user_interface)