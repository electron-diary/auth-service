from typing import Self, Protocol
from abc import abstractmethod

from src.app.domain.user.value_objects import UserUUID


class IdentityProvider(Protocol):
    @abstractmethod
    async def get_user_id(self: Self) -> UserUUID:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    