from typing import Self
import aiokafka

from app.adapters.broker.interfaces import AioKafkaInterface
from app.adapters.broker.config import KafkaConfig
from app.application.base.integration_event import IntegrationEvent


class KafkaRepositoryIml(AioKafkaInterface):
    def __init__(
        self, consumer: aiokafka.AIOKafkaConsumer, producer: aiokafka.AIOKafkaProducer, config: KafkaConfig
    ) -> None:
        self.consumer: aiokafka.AIOKafkaConsumer = consumer
        self.producer: aiokafka.AIOKafkaProducer = producer
        self.config: KafkaConfig = config

    async def send_message(self: Self, message: dict[str]) -> None:
        await self.producer.send_and_wait(topic=self.config.topic, value=message)

    async def recieve_message(self: Self) -> dict[str]:
        async for message in self.consumer:
            return message.value