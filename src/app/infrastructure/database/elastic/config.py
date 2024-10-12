from dataclasses import dataclass


@dataclass(frozen=True)
class ElasticConfig:
    host: str
    api_key: str | None