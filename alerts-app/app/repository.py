from pymongo import MongoClient
from bson.json_util import dumps
import json

DOMAIN = 'localhost'
PORT = 27017

class Repository:

    def __init__(self):
        client = MongoClient(DOMAIN, PORT)
        self.db = client['currencies_db']
        self.collection = self.db['currencies']

    def drop_old_collection(self):
        self.collection.drop()

    def fetch_db(self):
        print('fetch_db')
        # currencies = [{"symbol": item["id"], "name": item["name"]} for item in self.collection.find()]
        return dumps(self.collection.find())
