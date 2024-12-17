from abc import abstractmethod
from typing import Protocol, Self
from uuid import UUID

from app.application.dto.user_dto import UserDto


class UserReader(Protocol):
    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UUID) -> UserDto | None:
        raise NotImplementedError("Method must be implemented by subclasses")
