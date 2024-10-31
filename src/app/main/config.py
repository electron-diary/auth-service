from dataclasses import dataclass, field

from app.infrastructure.database.postgres.config import PostgresConfig
from app.infrastructure.brokers.config import NatsConfig
from app.infrastructure.database.elastic.config import ElasticConfig
from app.infrastructure.user_name_generator.config import UserNameGeneratorConfig
from app.infrastructure.database.mongo.config import MongoConfig
from app.infrastructure.database.redis.config import RedisConfig


@dataclass
class ConfigFactory:
    postgres_config: PostgresConfig = field(default_factory=PostgresConfig)
    nats_config: NatsConfig = field(default_factory=NatsConfig)
    elastic_config: ElasticConfig = field(default_factory=ElasticConfig)
    user_name_generator_config: UserNameGeneratorConfig = field(default_factory=UserNameGeneratorConfig)
    mongo_config: MongoConfig = field(default_factory=MongoConfig)
    redis_config: RedisConfig = field(default_factory=RedisConfig)
