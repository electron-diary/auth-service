from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.delete_user_usecase import DeleteUserUseCase
from src.app.domain.user.repositories import UserInterface
from src.app.application.interfaces.uow import UnitOfWork


class DeleteUserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_delete_user_usecase(
        self: Self, uow: UnitOfWork, user_interface: UserInterface
    ) -> DeleteUserUseCase:
        return DeleteUserUseCase(uow=uow, user_interface=user_interface)