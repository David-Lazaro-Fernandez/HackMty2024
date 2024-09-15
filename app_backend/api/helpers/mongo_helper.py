"""
This is a helper class for MongoDB operations and vectorization.
"""
import os
import logging
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

logger = logging.getLogger(__name__)
load_dotenv()

class Mongo():
    def __init__(self, db_name: str):
        self.client = MongoClient(
            os.getenv("MONGO_URI"),
            server_api=ServerApi('1'),
            tlsCAFile=certifi.where()
        )
        self.db = self.client[db_name]
    
    def insert_document(self, collection_name: str, document: dict):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    def find_document(self, collection_name: str, query: dict):
        collection = self.db[collection_name]
        document = collection.find_one(query)
        return document

    def update_document(self, collection_name: str, query: dict, update: dict):
        collection = self.db[collection_name]
        result = collection.update_one(query, {'$set': update})
        return result.modified_count

    def delete_document(self, collection_name: str, query: dict):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count
