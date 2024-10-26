from os import environ
from dotenv import load_dotenv

from src.app.main.config import ConfigFactory
from src.app.infrastructure.database.postgres.config import PostgresConfig
from src.app.infrastructure.brokers.config import NatsConfig
from src.app.infrastructure.database.elastic.config import ElasticConfig
from src.app.infrastructure.database.mongo.config import MongoConfig
from src.app.infrastructure.database.redis.config import RedisConfig
from src.app.infrastructure.user_name_generator.config import UserNameGeneratorConfig

load_dotenv()

def load_nats_config() -> NatsConfig:
    return NatsConfig(
        host=environ.get("NATS_HOST"),
        port=environ.get("NATS_PORT"),
    )

def load_elastic_config() -> ElasticConfig:
    return ElasticConfig(
        host=environ.get("ELASTIC_HOST"),
        api_key=environ.get("ELASTIC_API_KEY"),
    )

def load_postgres_config() -> PostgresConfig:
    return PostgresConfig(
        host=environ.get("POSTGRES_HOST"),
        port=environ.get("POSTGRES_PORT"),
        user=environ.get("POSTGRES_USER"),
        password=environ.get("POSTGRES_PASSWORD"),
        database=environ.get("POSTGRES_DATABASE"),
    )

def load_mongo_config() -> MongoConfig:
    return MongoConfig(
        host=environ.get("MONGO_HOST"),
        port=environ.get("MONGO_PORT")
    )

def load_redis_config() -> RedisConfig:
    return RedisConfig(
        host=environ.get("REDIS_HOST"),
        port=environ.get("REDIS_PORT")
    )

def load_user_name_generator_config() -> UserNameGeneratorConfig:
    return UserNameGeneratorConfig(
        prefix=environ.get("USER_NAME_GENERATOR_PREFIX")
    )

def load_config() -> ConfigFactory:
    return ConfigFactory(
        postgres_config=load_postgres_config(),
        nats_config=load_nats_config(),
        elastic_config=load_elastic_config(),
        redis_config=load_redis_config(),
        mongo_config=load_mongo_config(),
        user_name_generator_config=load_user_name_generator_config()
    )
