from os import environ
from dotenv import load_dotenv

from src.app.main.config import ConfigFactory
from src.app.infrastructure.database.postgres.config import PostgresConfig
from src.app.infrastructure.brokers.config import NatsConfig
from src.app.infrastructure.database.elastic.config import ElasticConfig

load_dotenv()



def load_config() -> ConfigFactory:
    return ConfigFactory(
        postgres_config=PostgresConfig(
            host=environ.get("POSTGRES_HOST"),
            port=environ.get("POSTGRES_PORT"),
            user=environ.get("POSTGRES_USER"),
            password=environ.get("POSTGRES_PASSWORD"),
            database=environ.get("POSTGRES_DATABASE"),
        ),
        nats_config=NatsConfig(
            host=environ.get("NATS_HOST"),
            port=environ.get("NATS_PORT"),
        ),
        elastic_config=ElasticConfig(
            host=environ.get("ELASTIC_HOST"),
            api_key=environ.get("ELASTIC_API_KEY"),
        ),
    )
