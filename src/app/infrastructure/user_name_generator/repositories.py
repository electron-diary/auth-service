from typing import Self
from random import randint

from src.app.domain.value_objects.user_name_value_object import UserName
from src.app.application.interfaces.user_name_generator import UserNameGeneratorInterface
from src.app.infrastructure.user_name_generator.config import UserNameGeneratorConfig


class UserNameGeneratorRepository(UserNameGeneratorInterface):
    def __init__(self: Self, config: UserNameGeneratorConfig) -> None:
        self.config: UserNameGeneratorConfig = config

    def generate_user_name(self: Self) -> UserName:
        random_number: int = randint(0, 500)
        return f"{self.config.prefix}{random_number}"