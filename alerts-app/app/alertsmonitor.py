from bson.json_util import dumps
import requests
import json
import yaml

from pykafka import KafkaClient

class AlertsMonitor:

    def __init__(self, config):
        self.conf = config
        self.db_data = None
        self.alert_list = []

    def process(self, data):
        print('alerts-process')
        print(self.db_data)
        if not self.db_data:
            self.db_data = data
        
        data_json = json.loads(self.db_data)
        data_json[0].pop('_id')
        for symbol in data_json[0]:
            value = data_json[0][symbol]
            if self.check_threshold(symbol, value):
                print('append to list')
                fullname = self.get_symbol_fullname(symbol)
                self.alert_list.append(fullname)
        self.dispatch_alert()


    def check_threshold(self, symbol, value):
        print("({}) = ({})".format(symbol, value))
        if value > self.get_symbol_threshold(symbol):
            return True
        else:
            return False

    def get_symbol_threshold(self, symbol):
        symbols_watched = self.conf.get_symbols_watched()
        symbols_thresholds = self.conf.get_symbols_thresholds()

        for idx, val in enumerate(symbols_watched):
            if symbols_watched[idx] == symbol:
                return symbols_thresholds[idx]

    def get_symbol_fullname(self, symbol):
        url = self.conf.get_url_symbols_names()
        req = requests.get(url).json()
        return req[symbol]

    def dispatch_alert(self):
        #if list not empty dispatch alert
        print('dispatch_alert')
        print(self.alert_list)
        if self.alert_list:
            client = KafkaClient(hosts="kafka:9092")
            print(client)
            topic = client.topics['my.test']
            producer = topic.get_sync_producer()
            producer.produce('test message'.encode('ascii'))

            consumer = topic.get_simple_consumer()
            for message in consumer:
                if message is not None:
                    print(message.value)
