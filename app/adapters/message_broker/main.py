from faststream.rabbit import RabbitBroker
from faststream.security import SASLPlaintext
from faststream.rabbit.annotations import RabbitBroker as Broker

from app.adapters.message_broker.config import RabbitConfig


def get_rabbit_broker(config: RabbitConfig) -> Broker:
    broker: Broker = RabbitBroker(
        host=config.host,
        port=config.port,
        security=SASLPlaintext(
            username=config.username,
            password=config.password
        ),
        virtualhost=config.virtual_host
    )
    return broker