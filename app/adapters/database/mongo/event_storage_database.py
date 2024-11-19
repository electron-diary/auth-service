from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.adapters.database.mongo.config import MongoConfig


def get_database(mongo_client: AsyncIOMotorClient, config: MongoConfig) -> AsyncIOMotorDatabase:
    database: AsyncIOMotorDatabase = AsyncIOMotorDatabase(client=mongo_client, name=config.database)
    return database