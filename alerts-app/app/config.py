import yaml

class Config:
    def __init__(self):
            config = yaml.safe_load(open("./app/config.yml"))
            self.url_symbols_names = config['url_symbols_names']
            self.symbols_watched = config['symbols_watched']
            self.symbols_thresholds = config['thresholds']

    def get_url_symbols_names(self):
        return self.url_symbols_names

    def get_symbols_watched(self):
        return self.symbols_watched

    def get_symbols_thresholds(self):
        return self.symbols_thresholds