from typing import Self, Protocol
from abc import abstractmethod
from uuid import UUID

from app.domain.user.user import User
from app.domain.user.value_objects import UserId
from app.application.user.dtos import UserDTO


class UserWriterGatewayInterface(Protocol):
    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UserId) -> User | None:
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def create_user(self: Self, user: User) -> bool:
        raise NotImplementedError("method must be implemented by subclasses")
    
    @abstractmethod
    async def update_user(self: Self, user: User) -> bool:
        raise NotImplementedError("method must be implemented by subclasses")
    

class UserReaderGatewayInterface(Protocol):
    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UUID) -> UserDTO | None:
        raise NotImplementedError("method must be implemented by subclasses")
