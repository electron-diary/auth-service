from typing import Self
from dataclasses import dataclass


@dataclass(frozen=True)
class KafkaConfig:
    host: str = 'localhost'
    port: int = 9092

    @property
    def get_connection_uri(self: Self) -> str:
        return f'kafka://{self.host}:{self.port}/'