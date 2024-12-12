from typing import Self, Protocol
from abc import abstractmethod
from uuid import UUID

from app.domain.models.user.entities.profile import Profile


class ProfileRepository(Protocol):
    @abstractmethod
    async def load(self: Self, profile_id: UUID) -> Profile:
        raise NotImplementedError("Method must be implemented by subclasses")
    
    @abstractmethod
    async def add(self: Self, profile: Profile) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")

    @abstractmethod
    async def update(self: Self, profile: Profile) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
    
    @abstractmethod
    async def delete(self: Self, profile_id: UUID) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")