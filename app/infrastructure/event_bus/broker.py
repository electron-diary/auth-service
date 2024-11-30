from aiokafka import AIOKafkaProducer

from app.infrastructure.event_bus.config import KafkaConfig


def get_kafka_producer(config: KafkaConfig) -> AIOKafkaProducer:
    producer: AIOKafkaProducer = AIOKafkaProducer(
        bootstrap_servers=config.get_connection_string,
    )
    return producer

async def get_kafka_connection(producer: AIOKafkaProducer) -> None:
    await producer.start()
