
from app.application.common.event_bus import EventBus
from app.domain.common.domain_event import DomainEvent
from app.infrastructure.brokers.interfaces import MessagePublisher
from app.infrastructure.event_queue.converters import domain_event_to_integration_event, integration_event_to_message


class EventBusImpl(EventBus):
    def __init__(
        self,
        message_publisher: MessagePublisher,
    ) -> None:
        self.message_publisher = message_publisher

    async def publish(self, events: list[DomainEvent]) -> None:
        for domain_event in events:
            integration_event = domain_event_to_integration_event(domain_event)
            message = integration_event_to_message(integration_event)
            await self.message_publisher.publish(message=message, key=integration_event.event_type)
