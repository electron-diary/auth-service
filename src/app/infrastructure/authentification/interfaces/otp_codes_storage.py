from typing import Self, Protocol
from abc import abstractmethod

from src.app.domain.user.value_objects import UserUUID


class UserOTPCodesInterface(Protocol):
    @abstractmethod
    async def get_user_otp_code(self: Self, user_id: UserUUID) -> int:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def add_user_otp_code(self: Self, user_id: UserUUID, code: int) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_user_otp_code(self: Self, user_id: UserUUID) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )