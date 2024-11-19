from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class PostgresConfig:
    port: int = 5432
    host: str = "localhost"
    password: str = "postgres"
    user: str = "postgres"
    database: str = "postgres"

    @property
    def get_connection_uri(self: Self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
