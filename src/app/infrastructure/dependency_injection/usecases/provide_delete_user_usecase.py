from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.delete_user_usecase import DeleteUserUseCase
from src.app.infrastructure.database.postgres.uow import SqlaUnitOfWork
from src.app.infrastructure.database.postgres.repositories.user_repo import UserRepositoryImpl


class DeleteUserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_delete_user_usecase(
        self: Self, uow: SqlaUnitOfWork, user_interface: UserRepositoryImpl
    ) -> DeleteUserUseCase:
        return DeleteUserUseCase(uow=uow, user_interface=user_interface)