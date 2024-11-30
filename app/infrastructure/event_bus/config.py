from typing import Self
from dataclasses import dataclass

@dataclass(frozen=True)
class KafkaConfig:
    host: str = 'localhost'
    port: int = 9092
    topic: str = 'events'

    @property
    def get_connection_string(self: Self) -> str:
        return f'{self.host}:{self.port}'