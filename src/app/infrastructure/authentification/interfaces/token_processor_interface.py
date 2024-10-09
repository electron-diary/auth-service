from typing import Protocol, Self
from abc import abstractmethod

from src.app.domain.user.value_objects import UserUUID


class TokenProcessorInterface(Protocol):
    @abstractmethod
    async def generate_access_token(self: Self, user_id: UserUUID) -> str:
        raise NotImplementedError(
            "Method generate_token is not implemented"
        )
    
    @abstractmethod
    async def generate_refresh_token(self: Self, user_id: UserUUID) -> str:
        raise NotImplementedError(
            "Method generate_refresh_token is not implemented"
        )
    
    @abstractmethod
    async def get_user_id_from_token(self: Self, token: str) -> UserUUID:
        raise NotImplementedError(
            "Method get_user_id_from_token is not implemented"
        )
    
    @abstractmethod
    async def update_access_token(self: Self, user_id: UserUUID, refresh_token: str) -> str:
        raise NotImplementedError(
            "Method update_access_token is not implemented"
        )