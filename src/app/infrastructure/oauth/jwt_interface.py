from typing import Self, Protocol
from abc import abstractmethod

from src.app.domain.user.value_objects import UserUUID

class JwtTokenInterface(Protocol):
    @abstractmethod
    def decode_token(self: Self, token: str) -> UserUUID:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def encode_token(self: Self, payload: dict[UserUUID]) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def validate_token(self: Self, token: str) -> bool:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )