from repository import *
from alertsmonitor import *
import requests
import time
import json  

DB = 'http://host.docker.internal:8000/update-data/'
TIME_INTERVAL = 2.0

repository = Repository()
alerts = AlertsMonitor()


while True:
    # symbols_price = data_fetcher.get_symbols_price()
    # res = requests.post(API, json = symbols_price).json()
    # print(res)
    db_data = repository.fetch_db()
    alerts.process(db_data)
    time.sleep(TIME_INTERVAL)