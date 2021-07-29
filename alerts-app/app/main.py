from config import *
from repository import *
from alertsmonitor import *
import requests
import time
import json  

TIME_INTERVAL = 2.0

config = Config()
repository = Repository()
alerts = AlertsMonitor(config)

while True:
    db_data = repository.fetch_db()
    alerts.process(db_data)
    time.sleep(TIME_INTERVAL)