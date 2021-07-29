from config import *
from datafetcher import *
from repository import *
import requests
import time
import json  

API = 'http://publicapi:8000/update-data/'

config = Config()
data_fetcher = DataFetcher(config)
repository = Repository()

while True:
    symbols_price = data_fetcher.get_symbols_price()
    res = requests.post(API, json = symbols_price).json()
    print(res)
    repository.update_db(symbols_price)
    time.sleep(config.get_fetch_interval())



