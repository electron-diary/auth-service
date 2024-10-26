from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

from src.app.infrastructure.database.mongo.config import MongoConfig


def mongo_client(config: MongoConfig) -> AsyncIOMotorClient:
    client: AsyncIOMotorClient = AsyncIOMotorClient(host=config.host, port=config.port)
    return client


async def mongo_session(client: AsyncIOMotorClient) -> AsyncIOMotorClientSession:
    session: AsyncIOMotorClientSession = await client.start_session()
    return session

