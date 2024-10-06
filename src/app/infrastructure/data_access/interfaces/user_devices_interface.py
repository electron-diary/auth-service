from typing import Protocol, Self
from abc import abstractmethod


class UserDevicesInterface(Protocol):
    @abstractmethod
    async def get_user_devices(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def add_device_to_user_devices(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_device_from_user_devices(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_all_user_devices(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )