from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class KafkaConfig:
    host: str = "localhost"
    port: int = 9092
    topic: str = 'kafka'

    @property
    def get_connection_uri(self: Self) -> str:
        return f"kafka://{self.host}:{self.port}/"
