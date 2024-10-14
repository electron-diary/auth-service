from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.update_user_contact_usecase import UpdateUserContactUseCase
from src.app.domain.user.repositories import UserInterface


class UpdateUserContactUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_delete_user_usecase(
        self: Self, user_interface: UserInterface
    ) -> UpdateUserContactUseCase:
        return UpdateUserContactUseCase(user_interface=user_interface)