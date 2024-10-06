from typing import Protocol, Self
from abc import abstractmethod


class UserIpInterface(Protocol):
    @abstractmethod
    async def get_user_ip_adreses(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def add_ip_to_user_ip_adreses(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def delete_ip_from_user_ip_adreses(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_all_user_ip_adreses(self: Self) -> ...:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )