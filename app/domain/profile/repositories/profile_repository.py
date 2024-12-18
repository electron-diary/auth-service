from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from app.domain.profile.entities.profile import Profile


class ProfileRepository(Protocol):
    @abstractmethod
    async def load(self, profile_id: UUID) -> Profile | None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def load_all_user_profiles(self, profile_owner_id: UUID) -> list[Profile]:
        raise NotImplementedError("Method must be implemented by subclasses")
