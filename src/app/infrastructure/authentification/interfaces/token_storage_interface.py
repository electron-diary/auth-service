from typing import Self, Protocol
from abc import abstractmethod

from src.app.domain.user.value_objects import UserUUID


class UserTokensInterface(Protocol):
    @abstractmethod
    async def add_token(self: Self, user_id: UserUUID, token: str) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def get_tokens(self: Self, user_id: UserUUID) -> list[str]:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def delete_token(self: Self, user_id: UserUUID, token: str) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def delete_all_tokens(self: Self, user_id: UserUUID) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )