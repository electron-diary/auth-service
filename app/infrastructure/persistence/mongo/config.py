from dataclasses import dataclass


@dataclass(frozen=True)
class MongoConfig:
    host: str = 'localhost'
    port: int = 27017
    database: str = 'event_storage'
    collection: str = 'events'
    username: str = 'admin'
    password: str = 'admin'

    @property
    def get_connection_uri(self) -> str:
        return f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/"
