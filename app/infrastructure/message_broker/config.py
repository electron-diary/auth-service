from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class RabbitConfig:
    host: str = "localhost"
    port: int = 5672
    username: str = "admin"
    password: str = "admin"
    virtual_host: str = "/"

    @property
    def get_connection_uri(self: Self) -> str:
        return f"amqp://{self.username}:{self.password}@{self.host}:{self.port}/"

@dataclass(frozen=True)
class KafkaConfig:
    host: str = "localhost"
    port: int = 9092
    topic: str = "events"

    @property
    def get_connection_uri(self: Self) -> str:
        return f"{self.host}:{self.port}"