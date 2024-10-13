from dataclasses import dataclass, field

from src.app.infrastructure.database.postgres.config import PostgresConfig
from src.app.infrastructure.brokers.config import NatsConfig
from src.app.infrastructure.database.elastic.config import ElasticConfig


@dataclass
class ConfigFactory:
    postgres_config: PostgresConfig = field(default_factory=PostgresConfig)
    nats_config: NatsConfig = field(default_factory=NatsConfig)
    elastic_config: ElasticConfig = field(default_factory=ElasticConfig)
