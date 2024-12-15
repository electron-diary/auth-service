from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class NatsConfig:
    host: str = "localhost"
    port: int = "4222"
    user: str = "admin"
    password: str = "admin"

    @property
    def connection_link(self: Self) -> str:
        return f"nats://{self.user}:{self.password}@{self.host}:{self.port}"
