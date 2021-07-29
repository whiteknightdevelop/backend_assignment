from pymongo import MongoClient
import json

DOMAIN = 'localhost'
PORT = 27017

class Repository:

    def __init__(self):
        self.collection = None
        self.db = None
        self.set_db()
        self.set_collection()

    def set_db(self):
        # db = MongoClient(
        # host = DOMAIN + ":" + str(PORT),
        # serverSelectionTimeoutMS = 3000, # 3 second timeout
        # username = "root",
        # password = "pass")

        # client = MongoClient(
        #     host='test_mongodb',
        #     port=27017,
        #     username='root',
        #     password='password',
        #     authSource='admin')
        # db = client["currencies_db"]

        client = MongoClient(DOMAIN, PORT)
        self.db = client['currencies_db']

    def set_collection(self):
        self.collection = self.db['currencies']

    def drop_old_collection(self):
        self.collection.drop()

    def update_db(self, symbols_price):
        print('update_db')
        print(symbols_price)
        self.drop_old_collection()
        # json_object = json.dumps(symbols_price)
        self.collection.insert_one(symbols_price)
        symbols_price.pop('_id')

    # def fetch_db(self):
    #     currencies = [{"id": item["id"], "name": item["name"]} for item in self.collection.find()]
    #     return currencies
    

