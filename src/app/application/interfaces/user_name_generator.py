from typing import Self, Protocol
from abc import abstractmethod


class UserNameGeneratorInterface(Protocol):
    @abstractmethod
    def generate_user_name(self: Self) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )