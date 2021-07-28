from datafetcher import *
import requests
import time
import json  

data_fetcher = DataFetcher()
URL = 'http://host.docker.internal:8000/update-data/'


while True:
    symbols_price = data_fetcher.get_symbols_price()
    x = requests.post(URL, json = symbols_price).json()
    print(x)
    time.sleep(data_fetcher.get_fetch_interval)


