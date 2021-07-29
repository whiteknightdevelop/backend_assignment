from pymongo import MongoClient
import json

DOMAIN = 'localhost'
PORT = 27017

class Repository:

    def get_db(self):
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
        db = client['currencies_db']
        collection = db['currencies']
        collection.drop()
        return db

    def fetch_db(self):
        print("fetch_db")
        db = self.get_db()
        collection = db['currencies']

        data = {'id': 'j5555', 'name':'44'}
        collection.insert_one(data)

        ans = [{"id": item["id"], "name": item["name"]} for item in collection.find()]
        print(ans)
        return ans
    

