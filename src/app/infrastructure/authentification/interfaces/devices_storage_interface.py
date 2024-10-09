from typing import Self, Protocol
from abc import abstractmethod

from src.app.domain.user.value_objects import UserUUID


class UserDevicesInterface(Protocol):
    @abstractmethod
    async def get_user_devices(self: Self, user_id: UserUUID) -> list[str]:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def add_user_device(self: Self, user_id: UserUUID, device: str) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_all_user_devices(self: Self, user_id: UserUUID) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_user_device(self: Self, user_id: UserUUID, device: str) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )