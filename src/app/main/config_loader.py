from os import environ
from dotenv import load_dotenv

from src.app.main.config import ConfigFactory
from src.app.infrastructure.database.postgres.config import PostgresConfig
from src.app.infrastructure.brokers.config import NatsConfig
from src.app.infrastructure.database.elastic.config import ElasticConfig

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

def load_config() -> ConfigFactory:
    return ConfigFactory(
        postgres_config=load_postgres_config(),
        nats_config=load_nats_config(),
        elastic_config=load_elastic_config(),
    )
