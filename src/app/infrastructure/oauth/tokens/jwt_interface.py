from typing import Self, Protocol
from abc import abstractmethod

from src.app.domain.user.value_objects import UserUUID

class JwtTokenInterface(Protocol):
    @abstractmethod
    def encode_access_token(self: Self, user_id: UserUUID) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def encode_refresh_token(self: Self, user_id: UserUUID) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def decode_token(self: Self, token: str) -> dict[str]:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def get_user_uuid_from_token(self: Self, token: str) -> UserUUID:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
   
    @abstractmethod
    def update_refresh_token(self: Self, refresh_token: str) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )