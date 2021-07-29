from pymongo import MongoClient
from bson.json_util import dumps
import json

# DOMAIN = 'localhost'
DOMAIN = 'mongodb'
PORT = 27017

class Repository:

    def __init__(self):
        # client = MongoClient(DOMAIN, PORT)
        client = MongoClient(
            host = [ str(DOMAIN) + ":" + str(PORT) ],
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = "root",
            password = "1234",
        )
        self.db = client['currencies_db']
        self.collection = self.db['currencies']

    def drop_old_collection(self):
        self.collection.drop()

    def fetch_db(self):
        print('fetch_db')
        # currencies = [{"symbol": item["id"], "name": item["name"]} for item in self.collection.find()]
        return dumps(self.collection.find())
