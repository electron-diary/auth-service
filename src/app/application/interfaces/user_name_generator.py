from typing import Self, Protocol
from abc import abstractmethod

from src.app.domain.value_objects.user_name_value_object import UserName


class UserNameGeneratorInterface(Protocol):
    @abstractmethod
    def generate_user_name(self: Self) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )