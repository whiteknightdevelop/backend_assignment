from pymongo import MongoClient
import json

# DOMAIN = 'localhost'
DOMAIN = 'mongodb'
PORT = 27017

class Repository:

    def __init__(self):
        self.collection = None
        self.db = None
        self.set_db()
        self.set_collection()

    def set_db(self):
        client = MongoClient(
            host = [ str(DOMAIN) + ":" + str(PORT) ],
            serverSelectionTimeoutMS = 3000,
            username = "root",
            password = "1234",
        )
        self.db = client['currencies_db']

    def set_collection(self):
        self.collection = self.db['currencies']

    def drop_old_collection(self):
        self.collection.drop()

    def update_db(self, symbols_price):
        self.drop_old_collection()
        self.collection.insert_one(symbols_price)
        symbols_price.pop('_id')
    

