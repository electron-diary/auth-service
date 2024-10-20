from typing import Self
from dishka import Provider, Scope, provide

from src.app.application.interfaces.user_name_generator import UserNameGeneratorInterface
from src.app.main.config import ConfigFactory
from src.app.infrastructure.user_name_generator.config import UserNameGeneratorConfig
from src.app.infrastructure.user_name_generator.repositories import UserNameGeneratorRepository


class UserNameGeneratorProvider(Provider):
    @provide(scope=Scope.APP)
    def get_config(self: Self, config: ConfigFactory) -> UserNameGeneratorConfig:
        return config.user_name_generator_config

    @provide(scope=Scope.APP)
    def provide_user_name_generator_repository(self: Self, config: UserNameGeneratorConfig) -> UserNameGeneratorInterface:
        return UserNameGeneratorRepository(config = config)