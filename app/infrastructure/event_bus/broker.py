from faststream.kafka import KafkaBroker
from faststream.kafka.annotations import KafkaBroker as KafkaBrokerAnnotation

from app.infrastructure.event_bus.config import KafkaConfig


def get_kafka_producer(config: KafkaConfig) -> KafkaBrokerAnnotation:
    producer: KafkaBrokerAnnotation = KafkaBroker(
        bootstrap_servers=config.get_connection_string,
    )
    return producer
