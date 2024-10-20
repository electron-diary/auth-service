from uuid import UUID
from uuid import uuid4
from typing import Self

from src.app.application.interfaces.uuid_generator import UUIDGeneratorInterface

class UUIDGenerator(UUIDGeneratorInterface):
    def generate_uuid(self: Self) -> UUID:
        return uuid4()