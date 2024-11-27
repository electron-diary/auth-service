from faststream.rabbit import RabbitBroker
from faststream.rabbit.annotations import RabbitBroker as Broker
from faststream.kafka import KafkaBroker
from faststream.kafka.annotations import KafkaBroker as Kafka
from faststream.security import SASLPlaintext

from app.infrastructure.message_broker.config import RabbitConfig
from app.infrastructure.message_broker.config import KafkaConfig


def get_rabbit_broker(config: RabbitConfig) -> Broker:
    broker: Broker = RabbitBroker(
        host=config.host,
        port=config.port,
        security=SASLPlaintext(
            username=config.username,
            password=config.password,
        ),
        virtualhost=config.virtual_host,
    )
    return broker

def get_kafka_broker(config: KafkaConfig) -> Kafka:
    broker: Kafka = KafkaBroker(
        bootstrap_servers=config.get_connection_uri,
    )
    return broker