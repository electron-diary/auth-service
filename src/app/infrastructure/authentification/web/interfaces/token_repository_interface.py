from typing import Protocol, Self
from abc import abstractmethod

from app.infrastructure.authentification.web.constants import UserData, TokenData

class JwtRepositoryInterface(Protocol):
    @abstractmethod
    def decode_token(self: Self, token: str | bytes) -> UserData:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )

    @abstractmethod
    def encode_access_token(self: Self, user_data: UserData) -> TokenData:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def encode_refresh_token(self: Self, user_data: UserData) -> TokenData:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def update_access_token(self: Self, refresh_token: TokenData) -> TokenData:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
