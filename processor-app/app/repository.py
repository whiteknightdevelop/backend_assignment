from pymongo import MongoClient
import json

class Repository:

    def get_db(self):
        client = MongoClient(
            host='test_mongodb',
            port=27017,
            username='root',
            password='password',
            authSource='admin')
        db = client["currencies_db"]
        return db

    def fetch_db(self):
        db = self.get_db()
        data = db.currencies_db.find()
        currencies = [{"id": item["id"], "name": item["name"]} for item in data]
        return json.dumps({"currencies": currencies})

