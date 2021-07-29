import yaml
import requests
import json

class DataFetcher:
    def __init__(self, config):
        self.conf = config
        
    def get_fetch_interval(self):
        return self.conf.fetch_interval

    def get_url_symbols_names(self):
        return self.conf.url_symbols_names

    def get_url_symbols_price(self):
        return self.conf.url_symbols_price

    def get_symbols_watched(self):
        return self.conf.symbols_watched
    
    def get_watched_currencies(self):
        return self.conf.watched_currencies

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
        symbols = self.get_symbols_watched().split(',')
        watched_currencies = self.get_watched_currencies()
        for symbol in symbols:
            watched_currencies[symbol] = req['eur'][symbol]

        print(watched_currencies)
        return watched_currencies

