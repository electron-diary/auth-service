from dataclasses import dataclass


@dataclass(frozen=True)
class MongoConfig:
    host: str
    port: int