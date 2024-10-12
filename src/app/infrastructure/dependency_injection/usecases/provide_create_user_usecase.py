from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.create_user_usecase import CreateUserUseCase
from src.app.infrastructure.database.postgres.uow import SqlaUnitOfWork
from src.app.infrastructure.database.postgres.repositories.user_repo import UserRepositoryImpl


class CreateUserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_create_user_use_case(
        self: Self, uow: SqlaUnitOfWork, user_interface: UserRepositoryImpl
    ) -> CreateUserUseCase:
        return CreateUserUseCase(uow=uow, user_interface=user_interface)