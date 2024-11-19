from collections.abc import Sequence
from dataclasses import asdict
from typing import Self

from app.adapters.broker.interfaces import AioKafkaInterface
from app.application.base.event_bus_interface import EventBusInterface
from app.application.base.integration_event import IntegrationEvent
from app.domain.base.base_event import BaseDomainEvent


class EventBusRepository(EventBusInterface):
    def __init__(self: Self, broker_repository: AioKafkaInterface) -> None:
        self.broker_repository: AioKafkaInterface = broker_repository

    async def send_event(self: Self, event: Sequence[BaseDomainEvent]) -> None:
        for domain_event in event:
            integration_event: IntegrationEvent = IntegrationEvent.from_domain_to_integration_event(event=domain_event)
            await self.broker_repository.send_message(message=asdict(integration_event))

