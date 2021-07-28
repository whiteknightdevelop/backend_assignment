import yaml
import requests
import json

class DataFetcher:
    def __init__(self):
        try:
            config = yaml.safe_load(open("./config.yml"))
            self.fetch_interval = config['fetch_interval']
            self.url_symbols_names = config['url_symbols_names']
            self.url_symbols_price = config['url_symbols_price']
            self.symbols_watched = config['symbols_watched']
            # self.currencies_symbols_names = {}
            self.watched_currencies = {}
            
            
            
            # for key, value in config.items():
            #     print (key + " : " + str(value))
        except yaml.YAMLError as exc:
            print(exc)
    @property
    def get_fetch_interval(self):
        return self.fetch_interval

    def get_url_symbols_names(self):
        return self.url_symbols_names

    def get_url_symbols_price(self):
        return self.url_symbols_price

    # def get_symbols_names(self):
    #     url = self.get_url_symbols_names()
    #     req = requests.get(url).json()
    #     symbols = self.symbols_watched.split(',')
    #     for symbol in symbols:
    #         self.currencies_symbols_names[symbol] = req[symbol]

    #     print(self.currencies_symbols_names)
    #     return self.currencies_symbols_names

    def get_symbols_price(self):
        url = self.get_url_symbols_price()
        req = requests.get(url).json()
        symbols = self.symbols_watched.split(',')
        for symbol in symbols:
            self.watched_currencies[symbol] = req['eur'][symbol]

        print(self.watched_currencies)
        return self.watched_currencies

