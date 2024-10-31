from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession
import logging
from logging import Logger

from app.infrastructure.database.mongo.config import MongoConfig


logger: Logger = logging.getLogger(__name__)


def mongo_client(config: MongoConfig) -> AsyncIOMotorClient:
    client: AsyncIOMotorClient = AsyncIOMotorClient(host=config.host, port=config.port)
    logger.info('connected to mongo')
    return client


async def mongo_session(client: AsyncIOMotorClient) -> AsyncIOMotorClientSession:
    session: AsyncIOMotorClientSession = await client.start_session()
    return session

