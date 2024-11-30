from dataclasses import dataclass


@dataclass(frozen=True)
class RabbitConfig:
    host: str = "localhost"
    port: int = 5672
    username: str = "admin"
    password: str = "admin"
    queue: str = "events"

    @property
    def get_connection_string(self) -> str:
        return f"amqp://{self.username}:{self.password}@{self.host}:{self.port}/"
