from typing import Self
from dataclasses import dataclass


@dataclass(frozen=True)
class RabbitConfig:
    host: str = 'localhost'
    port: int = 5672
    username: str = 'admin'
    password: str = 'admin'
    virtual_host: str = '/'
    queue: str = 'events'

    @property
    def get_connection_uri(self: Self) -> str:
        return f'amqp://{self.username}:{self.password}@{self.host}:{self.port}/'