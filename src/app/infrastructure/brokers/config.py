from dataclasses import dataclass

@dataclass(frozen=True)
class NatsConfig:
    host: str = 'localhost'
    port: int = 4222
    user: str = None
    password: str = None

    @staticmethod
    def nats_uri() -> str:
        return f"nats://{NatsConfig.host}:{NatsConfig.port}"