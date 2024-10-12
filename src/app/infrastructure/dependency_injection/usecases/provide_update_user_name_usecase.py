from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.update_user_name_usecase import UpdateUserNameUseCase
from src.app.domain.user.repositories import UserInterface
from src.app.application.interfaces.uow import UnitOfWork


class UpdateUserNameUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_delete_user_usecase(
        self: Self, uow: UnitOfWork, user_interface: UserInterface
    ) -> UpdateUserNameUseCase:
        return UpdateUserNameUseCase(uow=uow, user_interface=user_interface)