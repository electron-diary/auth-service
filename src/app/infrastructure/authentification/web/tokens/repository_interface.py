from typing import Protocol, Self
from abc import abstractmethod


class JwtRepositoryInterface(Protocol):
    @abstractmethod
    def decode_token(self: Self, token: str | bytes) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )

    @abstractmethod
    def encode_access_token(self: Self) -> str | bytes:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def encode_refresh_token(self: Self) -> str | bytes:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    def update_access_token(self: Self, refresh_token: str | bytes) -> str | bytes:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
