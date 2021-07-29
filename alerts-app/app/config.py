import yaml

class Config:
    def __init__(self):
            config = yaml.safe_load(open("../../config.yml"))
            self.url_symbols_names = config['url_symbols_names']
            self.symbols_watched = config['symbols_watched']
            self.symbols_watched2 = config['symbols_watched2']
            self.symbols_thresholds = config['thresholds']
            self.symbols_thresholds2 = config['thresholds2']

    def get_url_symbols_names(self):
        return self.url_symbols_names

    def get_symbols_watched(self):
        return self.symbols_watched

    def get_symbols_watched2(self):
        return self.symbols_watched2

    def get_symbols_thresholds(self):
        return self.symbols_thresholds

        
    def get_symbols_thresholds2(self):
        return self.symbols_thresholds2