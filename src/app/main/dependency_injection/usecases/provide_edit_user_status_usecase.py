from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.edit_user_status import EditUserStatusUseCase
from src.app.domain.repositories.user_repository import UserRepositoryInterface


class EditUserStatusUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_eidt_user_status_usecase(
        self: Self, user_interface: UserRepositoryInterface
    ) -> EditUserStatusUseCase:
        return EditUserStatusUseCase(user_interface=user_interface)