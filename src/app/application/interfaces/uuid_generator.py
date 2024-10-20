from typing import Protocol, Self
from abc import abstractmethod
from uuid import UUID


class UUIDGeneratorInterface(Protocol):
    @abstractmethod
    def generate_uuid(self: Self) -> UUID:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )