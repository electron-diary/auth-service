from typing import Self

from app.application.base.projector_interface import ProjectorInterface
from app.application.base.event_handler_Interface import EventHandlerInterface
from app.adapters.broker.interfaces import AioKafkaInterface
from app.application.base.integration_event import IntegrationEvent



class EventHandlerRepository(EventHandlerInterface):
    def __init__(self: Self, broker_repository: AioKafkaInterface, projector: ProjectorInterface) -> None:
        self.broker_repository: AioKafkaInterface = broker_repository
        self.projector: ProjectorInterface = projector

    async def __call__(self: Self) -> None:
        async for message in self.broker_repository.recieve_message():
            event: IntegrationEvent = IntegrationEvent(**message)
            await self.projector.project(event=event)
                
