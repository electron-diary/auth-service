from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from app.application.dto.profile_dto import ProfileDto


class ProfileReader(Protocol):
    @abstractmethod
    async def get_profile_by_id(self, profile_id: UUID) -> ProfileDto:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def get_user_profiles(self, user_id: UUID) -> list[ProfileDto]:
        raise NotImplementedError("Method must be implemented by subclasses")
