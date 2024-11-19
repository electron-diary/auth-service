import aiokafka

from app.adapters.broker.config import KafkaConfig


def get_kafka_consumer(config: KafkaConfig) -> aiokafka.AIOKafkaConsumer:
    consumer: aiokafka.AIOKafkaConsumer = aiokafka.AIOKafkaConsumer(
        'user-service',
        bootstrap_servers=config.get_connection_uri
    )
    return consumer

def get_kafka_producer(config: KafkaConfig) -> aiokafka.AIOKafkaProducer:
    producer: aiokafka.AIOKafkaProducer = aiokafka.AIOKafkaProducer(
        bootstrap_servers=config.get_connection_uri
    )
    return producer