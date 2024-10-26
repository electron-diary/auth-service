from typing import AsyncGenerator, Self
from dishka import Provider, provide, Scope
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

from src.app.infrastructure.database.mongo.config import MongoConfig
from src.app.infrastructure.database.mongo.main import mongo_client, mongo_session
from src.app.main.config import ConfigFactory


class MongoProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_mongo_config(self: Self, config: ConfigFactory) -> MongoConfig:
        return config.mongo_config
    
    @provide(scope=Scope.APP)
    def provide_mongo_client(self: Self, config: MongoConfig) -> AsyncIOMotorClient:
        return mongo_client(config)
    
    @provide(scope=Scope.APP)
    async def provide_mongo_session_factory(self: Self, mongo_client: AsyncIOMotorClient) -> AsyncIOMotorClientSession:
        return mongo_session(mongo_client)
    
    @provide(scope=Scope.REQUEST, provides=AsyncIOMotorClientSession)
    async def provide_mongo_session(self: Self, session_factory: AsyncIOMotorClientSession) -> AsyncGenerator[AsyncIOMotorClientSession, None]:
        async with session_factory as session:
            try:
                await session.commit_transaction()
                yield session
            except Exception:
                await session.abort_transaction()
            finally:
                await session.end_session()
           
