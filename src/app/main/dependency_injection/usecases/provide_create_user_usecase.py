from typing import Self
from dishka import Provider, Scope, provide

from app.application.usecases.create_user_usecase import CreateUserUseCase
from app.domain.repositories.user_repository import UserRepositoryInterface
from app.application.interfaces.uuid_generator import UUIDGeneratorInterface


class CreateUserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_create_user_use_case(
        self: Self, user_interface: UserRepositoryInterface, uuid_generator: UUIDGeneratorInterface
    ) -> CreateUserUseCase:
        return CreateUserUseCase(user_interface=user_interface, uuid_generator=uuid_generator)