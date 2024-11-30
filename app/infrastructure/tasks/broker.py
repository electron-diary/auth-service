from faststream.rabbit.broker import RabbitBroker
from faststream.rabbit.annotations import RabbitBroker as RabbitBrokerAnnotation

from app.infrastructure.tasks.config import RabbitConfig


def get_rabbit_broker(config: RabbitConfig) -> RabbitBrokerAnnotation:
    broker: RabbitBrokerAnnotation = RabbitBroker(
        url = config.get_connection_string
    )
    return broker
