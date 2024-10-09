from typing import Protocol, Self
from abc import abstractmethod

from src.app.domain.user.value_objects import UserUUID


class UserIpInterface(Protocol):
    @abstractmethod
    async def set_user_ip(self: Self, user_id: UserUUID, ip: str) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_user_ip(self: Self, user_id: UserUUID, ip: str) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_all_user_ips(self: Self, user_id: str) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def get_all_user_ips(self: Self, user_id: UserUUID) -> list[str]:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )

