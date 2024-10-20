from typing import Protocol, Self
from abc import abstractmethod


class JwtInterface(Protocol):
    @abstractmethod
    def decode_token(self: Self, token: str) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )

    @abstractmethod
    def encode_token(self: Self, user_id: str) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def get_user_id_from_token(self: Self, token: str) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    
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
    

class JwtIdentityProviderInterface(Protocol):
    @abstractmethod
    def get_current_user_id(self: Self) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )


class AuthentificatorInterface(Protocol):
    @abstractmethod
    async def authentificate(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def activate_contact(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
