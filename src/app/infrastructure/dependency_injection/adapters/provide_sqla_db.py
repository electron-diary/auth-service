from typing import Self
from dishka import Provider, Scope, provide

from src.app.infrastructure.database.postgres.config import PostgresConfig


class SqlaProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_sqla_config(self: Self) -> PostgresConfig:
        return PostgresConfig
    
    