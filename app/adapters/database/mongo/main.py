from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

from app.adapters.database.mongo.config import MongoConfig


def mongo_client(config: MongoConfig) -> AsyncIOMotorClient:
    client: AsyncIOMotorClient = AsyncIOMotorClient(config.get_connection_uri)
    return client


async def mongo_session(client: AsyncIOMotorClient) -> AsyncIOMotorClientSession:
    session: AsyncIOMotorClientSession = await client.start_session()
    return session
