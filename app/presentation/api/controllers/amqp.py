from faststream.rabbit import RabbitRouter
from faststream import Logger
from dishka.integrations.faststream import FromDishka, inject

from app.infrastructure.events.observable_interface import ObservableInterface
from app.infrastructure.events.integration_event import IntegrationEvent
from app.domain.base.domain_event import DomainEvent
from app.infrastructure.events.converters import integration_event_to_domain


router: RabbitRouter = RabbitRouter()


@router.subscriber(queue='events')
@inject
async def handle_events(event: IntegrationEvent, observable: FromDishka[ObservableInterface]) -> None:
    domain_event: DomainEvent = integration_event_to_domain(event=event)
    await observable.notify_observers(event=domain_event)