from dataclasses import dataclass


@dataclass(frozen=True)
class PrometheusConfig:
    host: str
    port: int
    username: str
    password: str