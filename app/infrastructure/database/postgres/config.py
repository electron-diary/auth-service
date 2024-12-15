from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class PostgresConfig:
    host: str = "localhost"
    port: int = "5432"
    user: str = "postgres"
    password: str = "postgres"
    database: str = "postgres"
    echo: bool = True

    @property
    def connection_link(self: Self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
