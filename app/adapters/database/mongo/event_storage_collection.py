from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase

from app.adapters.database.mongo.config import MongoConfig


def get_collection(database: AsyncIOMotorDatabase, config: MongoConfig) -> AsyncIOMotorCollection:
    collection: AsyncIOMotorCollection = AsyncIOMotorCollection(database=database, name=config.collection)
    return collection