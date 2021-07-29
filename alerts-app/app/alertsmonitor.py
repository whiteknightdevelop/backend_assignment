from bson.json_util import dumps
import requests
import json
import yaml

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
                # print("({}) = ({})".format(symbol, value))
        self.dispatch_alert()


    def check_threshold(self, symbol, value):
        print("({}) = ({})".format(symbol, value))
        if value > self.get_symbol_threshold(symbol):
            return True
        else:
            return False

    def get_symbol_threshold(self, symbol):
        symbols_watched = self.conf.get_symbols_watched2()
        symbols_thresholds = self.conf.get_symbols_thresholds2()

        for idx, val in enumerate(symbols_watched):
            if symbols_watched[idx] == symbol:
                return symbols_thresholds[idx]

    def dispatch_alert(self):
        #if list not empty dispatch alert
        if self.alert_list:
            print('dispatch_alert')

    def get_symbol_fullname(self, symbol):
        url = self.conf.get_url_symbols_names()
        req = requests.get(url).json()
        return req[symbol]
