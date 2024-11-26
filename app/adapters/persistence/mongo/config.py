from dataclasses import dataclass


@dataclass(frozen=True)
class MongoConfig:
    host: str
    port: int
    database: str
    collection: str
    username: str
    password: str

    @property
    def get_connection_uri(self) -> str:
        return f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/"