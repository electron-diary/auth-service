from dataclasses import dataclass, field

from src.app.infrastructure.database.postgres.config import PostgresConfig
from src.app.infrastructure.brokers.config import NatsConfig
from src.app.infrastructure.database.elastic.config import ElasticConfig
from src.app.infrastructure.user_name_generator.config import UserNameGeneratorConfig


@dataclass
class ConfigFactory:
    postgres_config: PostgresConfig = field(default_factory=PostgresConfig)
    nats_config: NatsConfig = field(default_factory=NatsConfig)
    elastic_config: ElasticConfig = field(default_factory=ElasticConfig)
    user_name_generator_config: UserNameGeneratorConfig = field(default_factory=UserNameGeneratorConfig)
