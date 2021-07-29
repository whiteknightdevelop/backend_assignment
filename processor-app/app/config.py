import yaml

class Config:
    def __init__(self):
            config = yaml.safe_load(open("../../config.yml"))
            # config = yaml.safe_load(open("./app/config.yml"))
            self.fetch_interval = config['fetch_interval']
            self.url_symbols_names = config['url_symbols_names']
            self.url_symbols_price = config['url_symbols_price']
            self.symbols_watched = config['symbols_watched']
            # self.currencies_symbols_names = {}
            self.watched_currencies = {}

    def get_fetch_interval(self):
        return self.fetch_interval

    def get_url_symbols_names(self):
        return self.url_symbols_names

    def get_url_symbols_price(self):
        return self.url_symbols_price

    def get_symbols_watched(self):
        return self.symbols_watched
    
    def get_watched_currencies(self):
        return self.watched_currencies