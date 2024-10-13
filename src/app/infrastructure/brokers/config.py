from dataclasses import dataclass
from typing import Self

@dataclass(frozen=True)
class NatsConfig:
    host: str = 'localhost'
    port: int = 4222
    user: str = None
    password: str = None

    @property
    def nats_uri(self: Self) -> str:
        return f"nats://{self.host}:{self.port}"
