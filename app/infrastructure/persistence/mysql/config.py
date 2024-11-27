from dataclasses import dataclass


@dataclass(frozen=True)
class MySqlConfig:
    host: str = 'localhost'
    port: int = 3306
    user: str = 'mysql'
    password: str = 'mysql'
    database: str = 'mysql'

    @property
    def get_connection_url(self) -> str:
        return f"mysql+aiomysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"