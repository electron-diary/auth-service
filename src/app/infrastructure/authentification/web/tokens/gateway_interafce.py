from typing import Self, Protocol
from abc import abstractmethod

from src.app.infrastructure.authentification.web.tokens.constants import TokenData
from src.app.domain.value_objects.user_uuid_value_object import UserUUID

class JwtGatewayInterface(Protocol):
    @abstractmethod
    async def get_tokens(self: Self, user_uuid: UserUUID) -> list[TokenData]:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def save_token(self: Self, token_data: TokenData) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_token(self: Self, user_uuid: UserUUID) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def update_token(self: Self, token_data: TokenData) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )