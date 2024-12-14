from abc import abstractmethod
from typing import Protocol, Self
from uuid import UUID

from app.application.profile.dtos.profile_dto import ProfileDto


class ProfileReaderInterface(Protocol):
    @abstractmethod
    async def get_profile_by_id(self: Self, profile_id: UUID) -> ProfileDto:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def get_user_profiles(self: Self, user_id: UUID) -> list[ProfileDto]:
        raise NotImplementedError("Method must be implemented by subclasses")
