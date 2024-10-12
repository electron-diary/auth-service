from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.update_user_name_usecase import UpdateUserNameUseCase
from src.app.infrastructure.database.postgres.uow import SqlaUnitOfWork
from src.app.infrastructure.database.postgres.repositories.user_repo import UserRepositoryImpl


class UpdateUserNameUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_delete_user_usecase(
        self: Self, uow: SqlaUnitOfWork, user_interface: UserRepositoryImpl
    ) -> UpdateUserNameUseCase:
        return UpdateUserNameUseCase(uow=uow, user_interface=user_interface)