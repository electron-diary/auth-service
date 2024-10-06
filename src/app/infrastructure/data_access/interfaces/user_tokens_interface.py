from typing import Self, Protocol
from abc import abstractmethod


class UserTokensInterface(Protocol):
    @abstractmethod
    async def get_user_tokens(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_all_user_tokens(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def add_token_to_user_list_tokens(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_user_token(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )