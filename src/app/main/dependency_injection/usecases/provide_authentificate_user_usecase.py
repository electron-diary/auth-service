from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.usecases.authentificate_user import AuthentificateUserUseCase
from src.app.application.interfaces.user_name_generator import UserNameGeneratorInterface
from src.app.domain.repositories.user_repository import UserRepositoryInterface
from src.app.application.interfaces.uuid_generator import UUIDGeneratorInterface


class AuthentificateeUserUseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_authentificate_user_usecase(
        self: Self, user_interface: UserRepositoryInterface, 
        user_name_generator: UserNameGeneratorInterface,
        uuid_genertor: UUIDGeneratorInterface
    ) -> AuthentificateUserUseCase:
        return AuthentificateUserUseCase(
            user_repository=user_interface, user_name_generator=user_name_generator, uuid_generator=uuid_genertor
        )