from typing import Self
from dishka import Provider, Scope, provide

from app.application.interfaces.uuid_generator import UUIDGeneratorInterface
from app.infrastructure.uuid_generator.main import UUIDGenerator

class UUIDGeneratorProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_uuid_generator(self: Self) -> UUIDGeneratorInterface:
        return UUIDGenerator()