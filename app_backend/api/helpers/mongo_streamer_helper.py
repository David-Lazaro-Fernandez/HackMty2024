"""
This is a helper class for MongoDB operations and vectorization.
"""
import os
import logging
import certifi
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

logger = logging.getLogger(__name__)
load_dotenv()

class MongoStreamer():
    def __init__(self, db_name: str):
        self.client = AsyncIOMotorClient(
            os.getenv("MONGO_URI"),
            server_api=ServerApi('1'),
            tlsCAFile=certifi.where()
        )
        self.db = self.client[db_name]
    
    async def stream_insert(self, collection_name: str, document: dict):
        collection = self.db[collection_name]
        await collection.insert_one(document)

        logger.info("Document inserted successfully.")