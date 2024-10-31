from typing import AsyncGenerator, Self
from dishka import Provider, provide, Scope
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession
from pymongo.errors import PyMongoError

from app.infrastructure.database.mongo.config import MongoConfig
from app.infrastructure.database.mongo.main import mongo_client, mongo_session
from app.main.config import ConfigFactory


class MongoProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_mongo_config(self: Self, config: ConfigFactory) -> MongoConfig:
        return config.mongo_config
    
    @provide(scope=Scope.APP)
    def provide_mongo_client(self: Self, config: MongoConfig) -> AsyncIOMotorClient:
        return mongo_client(config)
    
    @provide(scope=Scope.REQUEST, provides=AsyncIOMotorClientSession)
    async def provide_mongo_session(self: Self, mongo_client: AsyncIOMotorClient) -> AsyncGenerator[AsyncIOMotorClientSession, None]:
        async with mongo_session(client=mongo_client) as session:
            try:
                await session.commit_transaction()
                yield session
            except PyMongoError:
                await session.abort_transaction()
            finally:
                await session.end_session()

