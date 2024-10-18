from typing import Protocol, Self
from abc import abstractmethod
from datetime import datetime


class OtpGeneratorInterface(Protocol):
    @abstractmethod
    async def generate_otp(self: Self, length: int, expires_at: datetime) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def validate_otp(self: Self, otp: str) -> str:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
