from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.update_user_contact_usecase import UpdateUserContactUseCase
from src.app.domain.repositories.user_repository import UserRepositoryInterface


class UpdateUserContactUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_delete_user_usecase(
        self: Self, user_interface: UserRepositoryInterface
    ) -> UpdateUserContactUseCase:
        return UpdateUserContactUseCase(user_interface=user_interface)