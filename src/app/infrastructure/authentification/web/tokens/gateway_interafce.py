from typing import Self, Protocol
from abc import abstractmethod


class JwtGatewayInterface(Protocol):
    @abstractmethod
    async def get_token(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def save_token(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_token(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def update_token(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )