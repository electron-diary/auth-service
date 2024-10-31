from typing import Self, Protocol
from abc import abstractmethod

from app.domain.value_objects.user_uuid_value_object import UserUUID


class IdentityProvider(Protocol):
    @abstractmethod
    async def get_user_id(self: Self) -> UserUUID:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )


