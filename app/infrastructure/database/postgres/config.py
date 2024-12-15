from typing import Self
from dataclasses import dataclass


@dataclass(frozen=True)
class PostgresConfig:
    host: str
    port: int
    user: str
    password: str 
    database: str 
    echo: bool = True

    @property
    def connection_link(self: Self) -> str:
        return f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'